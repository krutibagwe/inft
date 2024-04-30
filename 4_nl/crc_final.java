import java.util.Scanner;
public class CrcExp4 {
    public static boolean[] rem = new boolean[100];
    public static void XORop(boolean[] temp, boolean[] g, int datawSize, int genSize) {
        int i, j, k;
        for (i = 0; i < datawSize; i++) {
            j = 0;
            k = i;

            // check for divisibility
            if ((temp[k] == true && g[k] == false) || (temp[k] == true && g[k] == true)) {
                for (j = 0, k = i; j < genSize; j++, k++) {
                    if ((temp[k] == true && g[j] == true) || (temp[k] == false && g[j] == false))
                        temp[k] = false;
                    else
                        temp[k] = true;
                }
            }
        }
    }
    // creating the main class
    public static void main(String[] argenSize) {
        int i, j;
        // ask user to enter size of data word and data word (one bit at a time)
        int datawSize;
        System.out.print("\nEnter size of data word: ");
        Scanner scanner1= new Scanner(System.in);
        datawSize = scanner1.nextInt();
        boolean[] f = new boolean[100];
        System.out.print("\nEnter data word bit by bit: \n");
        for (i = 0; i < datawSize; i++) {
            int temp = scanner1.nextInt();
            f[i] = temp == 1;
        }

        //ask user to enter size of generator and generator (one bit at a time)
        System.out.print("\nEnter size of generator: ");
        Scanner scanner2 = new Scanner(System.in);
        int genSize = scanner2.nextInt();
        boolean[] g = new boolean[100];
        System.out.print("\nEnter generator bit by bit: \n");
        for (i = 0; i < genSize; i++) {
            int temp = scanner1.nextInt();
            g[i] = temp == 1;
        }
        
        // display the inputs given by user
        System.out.print("\nAt Sender's Side, ");
        System.out.print("\nData word: ");
        Scanner scanner3 = new Scanner(System.in);
        for (i = 0; i < datawSize; i++) {
            System.out.print(f[i] ? 1 : 0);
        }
        System.out.print("\nGenerator :");
        for (i = 0; i < genSize; i++) {
            System.out.print(g[i] ? 1 : 0);
        }
        // calculate number of zeros to be appended
        // number of 0 is one less than size of generator
        int recWordSize = genSize - 1;
        System.out.print("\nNumber of 0's to be appended to data word: ");
        System.out.print(recWordSize);
        for (i = datawSize; i < datawSize + recWordSize; i++)
            f[i] = false;
        boolean[] temp = new boolean[100];
        for (i = 0; i < 100; i++)
            temp[i] = f[i];

        System.out.print("\nData word after appending 0's :");
        for (i = 0; i < datawSize + recWordSize; i++) {
            System.out.print(temp[i] ? 1 : 0);
        }
        // perform XOR operation for polynomial division
        XORop(temp, g, datawSize, genSize);
        // calculate remainder
        for (i = 0, j = datawSize; i < recWordSize; i++, j++)
            rem[i] = temp[j];

        System.out.print("\nCRC: ");
        for (i = 0; i < recWordSize; i++) {
            System.out.print(rem[i] ? 1 : 0);
        }
        
        // calculate and display word transmitted by sender
        System.out.print("\n");
        System.out.print("\nTransmitted codeword = data word + remainder ");
        System.out.print("\nTransmitted codeword: ");
        boolean[] tf = new boolean[150];
        for (i = 0; i < datawSize; i++)
            tf[i] = f[i];
        for (i = datawSize, j = 0; i < datawSize + recWordSize; i++, j++)
            tf[i] = rem[j];
        for (i = 0; i < datawSize + recWordSize; i++) {
            System.out.print(tf[i] ? 1 : 0);
        }
        // ask user to enter size of word received at receiver's side 
        System.out.print("\n");
        System.out.print("\nAt Receiver's side, ");
        System.out.print("\nEnter size of received word: ");
        Scanner scanner4 = new Scanner(System.in);
        int fr = scanner4.nextInt();
        boolean[] a = new boolean[fr];
        
        // if size of transmitted word and size of received word does not match, display error message
        if (datawSize + recWordSize != fr) {
            System.out.print("Error in Transmission ");
            System.exit(1);
        }
        
        // ask user to enter received data word (one bit at a time)
        System.out.print("Enter data word received bit by bit: \n");
        for (i = 0; i < datawSize + recWordSize; i++) {
            int tem = scanner4.nextInt();
            a[i] = tem == 1;
        }
         // perform polynomial division
        for (i = 0; i < datawSize + recWordSize; i++)
            temp[i] = a[i];
        // perform XOR operation for polynomial division 	
        XORop(temp, g, datawSize, genSize);
        
        // calculate and display remainder
        System.out.print("Remainder: ");
        boolean[] rrem = new boolean[100];
        for (i = datawSize, j = 0; i < datawSize + recWordSize; i++, j++)
            rrem[j] = temp[i];
        for (i = 0; i < recWordSize; i++) {
            System.out.print(rrem[i] ? 1 : 0);
        }
        
        // flag is used to keep track of errors. if bits in remainder are not zero, flag is set to 1. else, if all bits are zero, flag remains 0
        int flag = 0;
        for (i = 0; i < recWordSize; i++) {
            if (rrem[i] != false) {
                flag = 1;
                break;
            }
        }
        
        // error is detected on the basis of flag. if flag is 0, all remainder bits are 0 hence no error
        if (flag == 0)
            System.out.print("\nRemainder is 0, hence transmitted data has no error");        
        // else if flag is 1, all remainder bits are not zero, hence there is error 
        else
            System.out.print("\nRemainder is not 0, hence transmitted data has error");
    }
}
