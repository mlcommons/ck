<?php
 /*

  Collective Knowledge

  See CK LICENSE.txt for licensing details.
  See CK Copyright.txt for copyright details.

  Developer: Grigori Fursin

 */

 # Add local environment
 # putenv("CK_ROOT=");
 # putenv("CK_LOCAL_REPO=");
 # putenv("CK_REPOS=");

 # Start session
 session_start();

 # Type
 $xt='ck';

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # Call CK web in php
 $ckp=$ckr . '/repo/module/web/php/ck_web.php';

 # Check if library exists
 if (!file_exists($ckp)) {
   header("content-type: application/json; charset=UTF-8"); 
   print '{"return":1, "error":"Internal CK web service error (Can\'t find ck_web.php)"}';
   exit(1);
 }
 else
   require_once $ckp;
?>
