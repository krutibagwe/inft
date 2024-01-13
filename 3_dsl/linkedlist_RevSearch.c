#include<stdio.h>
#include<stdlib.h>

struct node{
    int data; 
    struct node* next;
};

struct node* createNode(int data){
    struct node* newNode= (struct node*)malloc(sizeof(struct node));
    newNode->data= data;
    newNode->next= NULL;
    return newNode;
}

struct node* createList(){
    int data;
    int num;
    struct node *head= NULL;
    struct node *temp= NULL;
    
    printf("Enter the number of nodes: \n");
    scanf("%d", &num);
    
    printf("Enter the elements: \n");
    for(int i=0; i<num; i++){
        scanf("%d", &data);
        struct node *newNode = createNode(data);
        
        if(head == NULL){
            head = newNode;
            temp = head;
        }
        else{
            temp->next= newNode;
            temp = newNode;
        }
    }
    return head;
}

struct node* reverse(struct node* head){
    
     if (head == NULL) {
        printf("Empty List\n");
        
    }
    
    struct node* prev = NULL;
    struct node* current = head;
    struct node* next = NULL;
    
    while(current!=NULL){
        next= current->next;
        current->next= prev;
        prev = current;
        current = next;
    }
    
    head = prev;
    return head;
}

void search(struct node* head, int key){
    struct node* temp = head;
    int pos = 1;
    while(temp!= NULL){
        if(temp->data == key){
        printf("Node with data %d found at position: %d\n",key, pos);
        return;
        }
        temp = temp->next;
        pos++;
    }
    printf("Node with data %d not found in the list.\n", key);
}

void display(struct node* head) {
    if (head == NULL) {
        printf("Empty List\n");
    } else {
        struct node* temp = head;
        printf("Linked List: \n");
        while (temp != NULL) {
            printf("%d\n", temp->data);
            temp = temp->next;
        }
    }
}

int main(){
    struct node *head = NULL;
    int choice, key;
    
    while(1){
        printf("\n\n1. Create\n2.Reverse\n3.Search\n4.Display \n");
        printf("Enter yor choice: \n");
        scanf("%d",&choice);
        
        switch(choice){
            case 1:
            head = createList();
            break;
            
            case 2:
            head = reverse(head);
            break;
          
            case 3:
            if (head == NULL) {
            printf("Empty List\n");
            }
            printf("Enter the key to be searched: \n");
            scanf("%d", & key);
            search(head, key);
            break;
            
            case 4:
            display(head);
            break;
            
            default:
            printf("Wrong choice. \n");
        }
    }
    return 0;
}


