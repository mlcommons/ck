def define_env(env):

   @env.macro
   def dummy(spaces):
     pre_space = ""
     for i in range(1,spaces):
       pre_space  = pre_space + " "
     f_pre_space = pre_space
     pre_space += " "

     content=""

     return content
   
   @env.macro
   def print_str(my_str):

     content="{{"+my_str+"}}"

     return content
