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

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # OpenME for CK
 $om=$ckr . '/repo/module/web/openme.php';

 # Check if library exists
 if (!file_exists($om)) {
   print '{"return":1, "error":"Internal CK web service error (Can\'t find openme.php)"}';
   exit(1);
 }
 else
   require_once $om;

 # get web environment variables
 $session=$_SESSION;
 $cookie=$_COOKIE;
 $get=openme_web_to_array($_GET, "");
 $post=openme_web_to_array($_POST, "");

 $ii=$get;

 $o="";

 # Process ck_json only in POST
 $ii=array_merge($ii, $post);

 if (array_key_exists("ck_json", $ii))
 {
   try
   {
     $jd=json_decode(urldecode($ii["ck_json"]),TRUE);
   } 
   catch(Exception $e)
   {
     print '{"return":1, "error":"'.$e->getMessage().'"}';
     exit(1);
   }

   unset($ii["ck_json"]);
   $ii=array_merge($ii, $jd);
 }

 # Set output to tmp file
 $ftmpo=tempnam("", "ck-");
 $ii['out']='json_file';
 $ii['out_file']=$ftmpo;

 # Call CK
 $r=openme_ck_access($ii, false);

 if ($r["return"]>0)
 {
  unlink($ftmpo);
  if (array_key_exists("stderr", $r) && $r["stderr"]!="")
    $o=$r["stderr"];
  else
    $o='{"return":'.str($r["return"]).',"error":"'.$r["error"].'"}';
 }
 else
 {
   $o=file_get_contents($ftmpo);
   unlink($ftmpo);
 }

 # Set header with UTF-8 !
 print $o;

?>
