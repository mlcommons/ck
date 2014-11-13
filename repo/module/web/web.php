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
 $type='html';

 # initalize path to CK
 $ckr=getenv("CK_ROOT"); 
 if ($ckr=="") $ckr=getcwd();

 # OpenME for CK
 $omc=$ckr . '/repo/module/web/openme_web.php';

 # Check if library exists
 if (!file_exists($omc)) {
   header("content-type: text/html; charset=UTF-8"); 
   print 'Internal CK web service error (Can\'t find openme_web.php)';
   exit(1);
 }
 else
   require_once $omc;
?>
