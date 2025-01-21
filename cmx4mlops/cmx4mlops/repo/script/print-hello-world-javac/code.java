/*
 Developer: Grigori Fursin
*/

//Import libraries...
import java.io.*;

public class code
{
  static int N=16;
  static double[][] A=new double [N][N];
  static double[][] B=new double [N][N];
  static double[][] C=new double [N][N];

  // *******************************************************************
  public static void main(String args[]) 
  {
    System.out.println("Hello world!");
    System.out.println("");

    String env=System.getenv("CM_VAR1");
    System.out.println("CM_VAR1="+env);

    env=System.getenv("CM_VAR2");
    System.out.println("CM_VAR2="+env);
  }
}
