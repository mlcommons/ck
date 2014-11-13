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

 # Load configuration 
 $pcfg=$ckr . '/repo/module/web/.cm/meta.json';

 $cfg=array();

 if (!file_exists($pcfg)) 
 {
   $er="Internal CK web service error (Can\'t find meta.json)";
   if ($type=='json')
   {
     header("content-type: application/json; charset=UTF-8"); 
     print '{"return":1, "error":"'.$er.'"}';
   }
   else
   {
     header("content-type: text/html; charset=UTF-8"); 
     print $er;
   }
   exit(1);
 }

 try
 {
    $x=file_get_contents($pcfg);
    $cfg=json_decode($x,true);
 } 
 catch(Exception $e)
 {
   $er="Internal CK web service error (".$e->getMessage().")";
   if ($type=='json')
   {
     header("content-type: application/json; charset=UTF-8"); 
     print '{"return":1, "error":"'.$er.'"}';
   }
   else
   {
     header("content-type: text/html; charset=UTF-8"); 
     print $er;
   }
   exit(1);
 }

 # Load OpenME for CK
 $om=$ckr . '/repo/module/web/openme.php';

 # Check if library exists
 if (!file_exists($om)) {
   $er="Internal CK web service error (Can\'t find openme.php)";
   if ($type=='json')
   {
     header("content-type: application/json; charset=UTF-8"); 
     print '{"return":1, "error":"'.$er.'"}';
   }
   else
   {
     header("content-type: text/html; charset=UTF-8"); 
     print $er;
   }
   exit(1);
 }
 else
   require_once $om;

 # Get web environment variables
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
     openme_web_err($cfg, $type, 1, $e->getMessage());
     exit(1);
   }

   unset($ii["ck_json"]);
   $ii=array_merge($ii, $jd);
 }

 # Check action
 $act='';
 if (array_key_exists("action", $ii)) $act=$ii['action'];

 # Set output to tmp file
 $ftmpo=tempnam("", "ck-");
 if ($type!='json' && $act!='pull')
   $ii['web']='yes';
 
 $ii['out']='json_file';
 $ii['out_file']=$ftmpo;

 # Call CK
 $r=openme_ck_access($ii, false);

 # Check errors
 if (array_key_exists("stderr", $r) && $r["stderr"]!="")
 {
   $x=$r["stderr"];
   if ($type=='json')
   {
      $x=str_replace('\\','-',$x); 
      $x=str_replace("\n","\\n",$x);
      $x=str_replace("\r","\\r",$x); 
      $x=str_replace(':','-',$x); 
      $x=str_replace('"','\'',$x); 
   }
   $r["stderr"]=$x;
 }

 # Process output
 if ($r["return"]>0)
 {
   if (file_exists($ftmpo)) unlink($ftmpo);
   if (array_key_exists("stderr", $r) && $r["stderr"]!="")
     $r["error"]=$r['stderr'];
   openme_web_err($cfg, $type, $r['return'], $r['error']);
   exit(1);
 }

 $o=file_get_contents($ftmpo);
 unlink($ftmpo);

 if ($o=='' && array_key_exists("stderr", $r) && $r["stderr"]!="")
 {
   $x=', see error output ('.$r['stderr'].')';
   openme_web_err($cfg, $type, $r['return'], 'returned file is empty'.$x);
   exit(1);
 }

 # Output
 $fx='';

 try
 {
    $rr=json_decode($o,true);
 } 
 catch(Exception $e)
 {
   $er="Internal CK web service error (".$e->getMessage().")";
   openme_web_err($cfg, $type, 1, $er);
   exit(1);
 }

 if ($rr['return']>0)
 {
   openme_web_err($cfg, $type, $rr['return'], $rr['error']);
   exit(1);
 }

 # Check if file was returned
 $fr=false;
 if (array_key_exists("file_content_base64", $rr) &&
     array_key_exists("filename", $rr))
   $fr=true;

 # Check if download
 if (($type=='web' && $fr) || ($act=='pull' && $type!='json'))
 {
   if (array_key_exists("file_content_base64", $rr))
     $x=$rr['file_content_base64'];

   $fx='';

   if (array_key_exists("filename", $rr))
     $fx=$rr['filename'];

   if ($fx=='')
      $fx='ck-archive.zip';

   try
   {
     $o=urlsafe_b64decode($x);
   } 
   catch(Exception $e)
   {
     $er="Internal CK web service error (".$e->getMessage().")";
     openme_web_err($cfg, $type, 1, $er);
     exit(1);
   }

   # Process extension
   $type = pathinfo($fx, PATHINFO_EXTENSION);
 }
 else
 {
   # If html mode and output file is empty, use stdout from module ...
   if (array_key_exists("html", $rr))
      $o=$rr['html'];

   if ($o=='')
   {
     if (array_key_exists("stdout", $r) && $r["stdout"]!="")
     $o=$r['stdout'];
   }
   else
   {
     if (array_key_exists("file_content_base64", $rr))
       $x=$rr['file_content_base64'];
   }
 }

 openme_web_out($cfg, $type, $o, $fx);

?>
