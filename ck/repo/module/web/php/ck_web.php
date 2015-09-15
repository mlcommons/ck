<?php
/*

#
# Collective Knowledge (CK web service)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, 2014-2015
#

*/

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # Load configuration 
 $pcfg=$ckr . '/ck/repo/module/web/.cm/meta.json';

 $cfg=array();

 if (!file_exists($pcfg)) 
 {
   $er="Internal CK web service error (Can\'t find meta.json)";
   if ($xt=='json')
   {
     header("content-type: application/json; charset=UTF-8"); 
     print '{"return":1, "error":"'.$er.'"}';
   }
   else
   {
     header("content-type: text/html; charset=UTF-8"); 
     print $er;
   }
   return;
 }

 try
 {
    $x=file_get_contents($pcfg);
    $cfg=json_decode($x,true);
 } 
 catch(Exception $e)
 {
   $er="Internal CK web service error (can't parse web meta.json)";
   if ($xt=='json')
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
 $om=$ckr . '/ck/repo/module/web/php/openme.php';

 # Check if library exists
 if (!file_exists($om)) {
   $er="Internal CK web service error (Can\'t find openme.php)";
   if ($xt=='json')
   {
     header("content-type: application/json; charset=UTF-8"); 
     print '{"return":1, "error":"'.$er.'"}';
   }
   else
   {
     header("content-type: text/html; charset=UTF-8"); 
     print $er;
   }
   return;
 }
 else
   require_once $om;

 # Get web environment variables
 $session=$_SESSION;
 $cookie=$_COOKIE;
 $get=openme_web_to_array($_GET, "");
 $post=openme_web_to_array($_POST, "");
 $files=openme_web_file_to_array($_FILES, "");

 $ii=$get;

 $ii=array_merge($ii, $files);

 $o="";

 # Process ck_json
 $ii=array_merge($ii, $post);

 if (array_key_exists("ck_json", $ii) && $ii['ck_json']!='')
 {
   try
   {
     $jd=json_decode(urldecode($ii["ck_json"]));//,TRUE);
   } 
   catch(Exception $e)
   {
     openme_web_err($cfg, $xt, 1, $e->getMessage());
     exit(1);
   }

   unset($ii["ck_json"]);
   $ii=array_merge($ii, get_object_vars($jd));
 }

 # Check action
 $act='';
 if (array_key_exists("action", $ii)) $act=$ii['action'];

 # Check output type
 if (array_key_exists("out", $ii) && $ii['out']!='') $xt=$ii['out'];

 if ($xt=='') $xt='web';

 if ($xt!='json' && $xt!='con' && $xt!='web')
 {
    header("content-type: text/html; charset=UTF-8"); 
    print 'Unknown CK request ('.$xt.')!';
    return;
 }

 # Set output to tmp file
 $fn=tempnam("", "ck-");
 if ($xt!='json' && $act!='pull')
   $ii['web']='yes';
 
 $ii['out_file']=$fn;
 $ii['web']='yes';
 if ($xt=='json' or $xt=='web')
    $ii['out']='json_file';
 # else output to console (for remote access for example)

 $ii['con_encoding']='utf8';

 # Call CK ***************************************************************************
 if (!array_key_exists('action', $ii))
 {
   if (array_key_exists("if_web_action_not_defined", $cfg) &&
       array_key_exists("if_web_module_not_defined", $cfg))
   {
     $ii["action"]=$cfg["if_web_action_not_defined"];
     $ii["module_uoa"]=$cfg["if_web_module_not_defined"];
   } 
 }

 $r=openme_ck_access($ii, false);

 # Process output
 if ($r["return"]>0)
 {
   if (file_exists($fn)) unlink($fn);
   openme_web_err($cfg, $xt, $r['return'], $r['error']);
   exit(1);
 }

 # If output to console or detached console
 if ($xt=='con')
 {
   if (file_exists($fn)) unlink($fn);
   openme_web_out($cfg, $xt, $r['std'], '');
   return;
 }

 # If json or web
 # Try to load output file
 if (!file_exists($fn))
 {
   openme_web_err($cfg, $xt, 1, 'Output json file was not created, see output ('.$r['std'].')');
   return;
 } 

 $bin=file_get_contents($fn);
 unlink($fn);

 if ($bin=='' && array_key_exists("stderr", $r) && $r["stderr"]!="")
 {
   $x=', see error output ('.$r['stderr'].')';
   openme_web_err($cfg, $xt, $r['return'], 'returned file is empty'.$x);
   exit(1);
 }

 # Output
 $fx='';

 try
 {
    $rr=json_decode($bin,true);
 } 
 catch(Exception $e)
 {
   $er="Can't parse output json file (".$e->getMessage().")";
   openme_web_err($cfg, $xt, 1, $er);
   exit(1);
 }

 if ($rr['return']>0)
 {
   openme_web_err($cfg, $xt, $rr['return'], $rr['error']);
   exit(1);
 }

 # Check if file was returned
 $fr=false;
 if (array_key_exists("file_content_base64", $rr) &&
     array_key_exists("filename", $rr) &&
     $rr['filename']!='')
   $fr=true;

 # Check if download
 if (($xt=='web' && $fr) || ($act=='pull' && $xt!='json'))
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
     $bin=urlsafe_b64decode($x);
   } 
   catch(Exception $e)
   {
     $er="Internal CK web service error (".$e->getMessage().")";
     openme_web_err($cfg, $xt, 1, $er);
     exit(1);
   }

   # Process extension
   $xt = pathinfo($fx, PATHINFO_EXTENSION);
 }
 else
 {
   # If html mode and output file is empty, use stdout from module ...
   if (array_key_exists("html", $rr))
      $bin=$rr['html'];
 }

 openme_web_out($cfg, $xt, $bin, $fx);

?>
