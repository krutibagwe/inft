import java.util.Scanner;
public class Alphabet{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter a wrod: ");
        String w= scanner.nextLine();
        String word=w.toLowerCase();
        
        int vow=0, cons=0;
        for(int i=0; i<word.length(); i++){
            char ch= word.charAt(i);
            if(ch>='a' && ch<='z'){
                if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u'){
                    vow ++;
                }
                else{
                    cons++;
                }
            }
        }
        System.out.println("Number of vowels: "+ vow);
        System.out.println("Number of consonants: "+ cons);
    
    }
}
