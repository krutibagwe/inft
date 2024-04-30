//using TCP socket

//server side for chat application
import java.net.*;  
import java.io.*;  
// MyClient class for creating a client socket and communicating with the server
class MyClient {  
    public static void main(String args[]) throws Exception {  
        // Establishing a connection with the server at localhost on port 3333
        Socket s = new Socket("localhost",3333);  
        // Creating input and output streams to communicate with the server
        DataInputStream din = new DataInputStream(s.getInputStream());  
        DataOutputStream dout = new DataOutputStream(s.getOutputStream());  
        // Creating a BufferedReader to read input from the console
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        String str="", str2="";  
        // Loop for continuous communication until the client inputs "stop"
        while(!str.equals("stop")) {  
            // Reading input from the console
            str = br.readLine();  
            // Sending the input string to the server
            dout.writeUTF(str);  
            dout.flush();  
            // Receiving response from the server
            str2 = din.readUTF();  
            // Displaying the response from the server
            System.out.println("Server says: " + str2);  
        }  
        // Closing the streams and socket when communication is finished
        dout.close();  
        s.close();  
    }
}
