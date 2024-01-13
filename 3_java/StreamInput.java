import java.io.FileInputStream; 
public class StreamInput { 
  public static void main(String args[]){ 
    try{ 
      StreamInput fin=new StreamInput("D:\\testout.txt");
      int i=fin.read(); 
      System.out.print((char)i); 
      fin.close();
       } catch(Exception e){
          System.out.println(e);
          }   
  } 
