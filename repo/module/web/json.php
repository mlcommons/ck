<?php
 /*

  Collective Knowledge

  See CK LICENSE.txt for licensing details.
  See CK Copyright.txt for copyright details.

  Developer: Grigori Fursin

 */

 # Start session
 session_start();

 header("content-type: application/json; charset=UTF-8"); 

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # OpenME for CK
 $omc=$ckr . '/repo/module/web/openme_ck_json.php';

 # Check if library exists
 if (!file_exists($omc)) {
   print '{"return":1, "error":"Internal CK web service error (Can\'t find openme_ck_json.php)"}';
   exit(1);
 }
 else
   require_once $omc;
?>
