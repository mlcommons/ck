<?php

/*

 OpenME - Event-driven, plugin-based interactive interface to "open up" 
          any software and connect it to cM or CK

 Developer: Grigori Fursin
 http://cTuning.org/lab/people/gfursin

 (C)opyright 2014 cTuning foundation

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation; either
 version 2.1 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

*/

function openme_web_to_array($web, $prefix, $remove=true)
{
  if ($prefix=="")
    $r=$web;
  else
    $r=array();
    foreach ($web as $key => $value)
      if ($prefix==substr($key, 0, strlen($prefix)))
      {
        if ($remove) $key=substr($key,strlen($prefix));
        $r[$key]=$value;
      }
  return $r; 
}

function openme_ck_access($i, $output=true)
{
 # Convert to json and call CK
 # FGG: in the future we may want to connect through socket

 # Get action
 if (!array_key_exists('action', $i))
   return array("return"=>1,"error"=>"action is not defined");

 $action=$i["action"];
 unset($i["cm_action"]);

 # Decode dict to json and save to temp file
 $str=json_encode($i);
 $ftmp=tempnam("", "ck-");
 $f=fopen($ftmp, "w");
  fwrite($f, $str);
 fclose($f);

 # Prepare call to CK
 $cmd="ck ".$action." @".$ftmp;

 #Add cmd if Windows (FGG:TODO maybe can be done cleaner?)
 if (substr(strtoupper(PHP_OS),0,3)=="WIN")
    $cmd="cmd /c ".$cmd;

 #FGG: important note for Windows: stderr pipe should be "a" not "w"
 #     see http://www.php.net/manual/en/function.proc-open.php   Luceo 28-Mar-2010 07:39
 $tmpfname = tempnam("", "ck-err-");
 $descriptorspec = array(0 => array("pipe", "r"), 1 => array("pipe", "w"), 2 => array("file", $tmpfname, "w"));

 $process = proc_open($cmd, $descriptorspec, $pipes, NULL, NULL);

 $tout='';
 $terr='';
 $rv=0;
 if (is_resource($process)) 
 {
    fclose($pipes[0]);

    $tout=stream_get_contents($pipes[1]);
    fclose($pipes[1]);

    $rv = proc_close($process);
  }

  # Read and delete temporal file with error output
  $terr=file_get_contents($tmpfname);
  unlink($tmpfname);

  if ($output)
  {
    echo $tout;
    echo $terr;
  }

  # Delete temporal input file
  if (file_exists($ftmp)) 
     unlink($ftmp);

  $r=array("return"=>$rv, "stdout"=>$tout, "stderr"=>$terr);

  if ($rv>0)
     $r["error"]="Internal CK web-service error";

  return $r;
}

?>
