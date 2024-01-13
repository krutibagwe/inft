Apublic class AlphaCount{
    public static void main(String[]args){
        String word= "Java Programming";
        word= word.replaceAll("\\s", "").toLowerCase();
        
        for(char ch='a'; ch<='z'; ch++){
            int count=0;
            for(int i=0; i<word.length(); i++){
                if(ch==word.charAt(i)){
                    count++;
                }
            }
            if(count>0){
                System.out.println("'"+ch+"' : "+ count);
            }
        }
    }
}
