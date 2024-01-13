#include<stdio.h>
#define size 10

void insert(int hashTable[], int key){
    int index = key% size;
    
    while(hashTable[index]!=-1){
        index= (index+1) % size;
    }
    hashTable[index]= key;
}

void display(int hashTable[]){
    printf("Hash Table: \n");
    for(int i=0; i< size; i++){
        printf("%d: %d \n", i, hashTable[i]);
    }
}

int main(){
    int hashTable[size];
    for(int i=0; i<size; i++){
        hashTable[i]=-1;
    }
    
    int n,key;
    printf("Enter the number of elements to be inserted: \n");
    scanf("%d", &n);
    
    printf("Enter the elements to be inserted: \n");
    for(int i=0; i<n; i++){
        scanf("%d", &key);
        insert(hashTable, key);
    }
    
    display(hashTable);
    
    return 0;
}
