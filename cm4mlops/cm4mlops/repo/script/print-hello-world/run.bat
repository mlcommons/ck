if not "%CM_PRINT_HELLO_WORLD_SKIP_PRINT_ENV%" == "yes" (
  echo.
  echo CM_ENV_TEST1 = %CM_ENV_TEST1%
  echo CM_ENV_TEST2 = %CM_ENV_TEST2%
  echo CM_ENV_TEST3 = %CM_ENV_TEST3%
)

echo.
echo HELLO WORLD!
if not "%CM_PRINT_HELLO_WORLD_TEXT%" == "" (

  echo.
  echo %CM_PRINT_HELLO_WORLD_TEXT%

)
echo.
