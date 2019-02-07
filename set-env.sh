# Checking python

XPYTHON=""
if command -v python &>/dev/null ; then
   XPYTHON="YES"
fi

XPYTHON3=""
if command -v python3 &>/dev/null ; then
   XPYTHON3="YES"
fi

if ! ( [ "$XPYTHON" == "YES" ] || [ "$XPYTHON3" == "YES" ] ) ; then
  echo "Problem: neither python nor python3 is installed!"
  return 1
fi

XGIT=""
if command -v git &>/dev/null ; then
   XGIT="YES"
fi

if [ "$XGIT" == "" ] ; then
  echo "Problem: git is not installed!"
  return 1
fi

XWGET=""
if command -v wget &>/dev/null ; then
   XWGET="YES"
fi

if [ "$XWGET" == "" ] ; then
  echo "Problem: wget is not installed!"
  return 1
fi

export PATH=$PWD/ck/bin:$PATH

if [ "$PYTHONPATH" == "" ] ; then
   export PYTHONPATH=$PWD/ck
else
   export PYTHONPATH=$PWD/ck:$PYTHONPATH
fi

return 0
