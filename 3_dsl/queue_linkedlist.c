#include<stdlib.h>
#include<stdio.h>

struct node{
    int info;
    struct node*ptr;
};
struct node *front, *rear, *temp, *front1;

void enqueue(int data);
void dequeue();
void display();



void enqueue(int data){
    if(rear==NULL){
        rear = (struct node*)malloc(sizeof(struct node));
        rear->ptr = NULL;
        rear->info = data;
        front=rear;
    }
    else{
        temp= (struct node* )malloc(sizeof(struct node));
        rear->ptr = temp;
        temp->info= data;
        temp->ptr = NULL;
        
        rear= temp;
    }
}


void dequeue() {
    if (front == NULL) {
        printf("Queue is empty.\n");
        return;
    }
    
    struct node* temp = front;
    printf("Dequeued %d\n", temp->info);
    front = front->ptr;
    free(temp);

    if (front == NULL) {
        rear = NULL;
    }
}


void display() {
    struct node* temp = front;
    
    if (temp == NULL) {
        printf("Queue is empty.\n");
        return;
    }
    
    while (temp != NULL) {
        printf("%d \n", temp->info);
        temp = temp->ptr;
    }
    printf("\n");
}


int main(){
    int num, choice, element;
    
    while(1){
        printf("\n1. Enqueue \n2. Dequeue \n3. Display\n");
        printf("Enter the choice: \n");
        scanf("%d", &choice);
        
        switch(choice){
            case 1:
            printf("Enter the element to be enqueued: \n");
            scanf("%d", &num);
            enqueue(num);
            break;
            
            case 2: 
            dequeue();
            break;
            
            case 3:
            display();
            break;
            
            default:
            printf("Wrong choice!\n");
            break;
        }
    }
    return 0;
}
