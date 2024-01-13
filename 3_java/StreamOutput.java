import java.io.FileOutputStream; 
public class StreamOutput {
  public static void main(String args[]){ 
    try{ 
    StreamOutput fout=new StreamOutput("D:\\testout.txt"); 
    fout.write(65); 
    fout.close(); 
    System.out.println("successfully Written..."); 
    }  catch(Exception e){
      System.out.println(e);
        }    
    }    
}
