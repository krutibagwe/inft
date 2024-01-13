#include <stdio.h>
#include <stdlib.h>

struct node {
    int info;
    struct node* ptr;
};

struct node* top = NULL;

void push(int data) {
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->info = data;
    newNode->ptr = top;
    top = newNode;
}

void pop() {
    if (top == NULL) {
        printf("Stack is empty.\n");
    } else {
        struct node* temp = top;
        top = top->ptr;
        printf("Popped value: %d\n", temp->info);
        free(temp);
    }
}

int peek() {
    if (top == NULL) {
        printf("Stack is empty.\n");
    }
    return top->info;
}

void display() {
    struct node* temp = top;
    if (temp == NULL) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Stack elements: \n");
    while (temp != NULL) {
        printf("%d \n", temp->info);
        temp = temp->ptr;
    }
    printf("\n");
}

int main() {
    int no, ch, e;
    
    while (1) {
    printf("\n 1. Push");
    printf("\n 2. Pop");
    printf("\n 3. Peek");
    printf("\n 4. Display");
    
   
        printf("\nEnter the choice: ");
        scanf("%d", &ch);
        
        switch (ch) {
            case 1:
                printf("Enter data: ");
                scanf("%d", &no);
                push(no);
                break;
            
            case 2:
                pop();
                break;
            
            case 3:
                if (top == NULL) {
                    printf("Stack is Empty.\n");
                } else {
                    e = peek();
                    printf("Top element: %d\n", e);
                }
                break;
                
            case 4:
                display();
                break;
            
            default:
                printf("Wrong choice!\n");
                break;
        }
    }

    return 0;
}
