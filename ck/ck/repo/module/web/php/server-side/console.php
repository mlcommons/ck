<?php
 /*

  Collective Knowledge

  See CK LICENSE.txt for licensing details.
  See CK COPYRIGHT.txt for copyright details.

  Developer: Grigori Fursin

 */

 # Load local environment, if needed
 if (file_exists('local_env.php')) require_once 'local_env.php';

 # Start session
 session_start();

 # Type
 $xt='con';

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # Call CK web in php
 $ckp=$ckr . '/ck/repo/module/web/php/ck_web.php';

 # Check if library exists
 if (!file_exists($ckp)) {
   header("content-type: application/json; charset=UTF-8"); 
   print '{"return":1, "error":"Internal CK web service error (Can\'t find ck_web.php)"}';
   exit(1);
 }
 else
   require_once $ckp;
?>
