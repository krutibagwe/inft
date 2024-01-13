#include <stdio.h>
#include <ctype.h>

char stack[100];
int top = -1;

void push(char x) {
    stack[++top] = x;
}

char pop() {
    return (top == -1) ? -1 : stack[top--];
}

int priority(char x) {
    return (x == '+' || x == '-') ? 1 : ((x == '*' || x == '/') ? 2 : 0);
}

int main() {
    char exp[100];
    printf("Enter the expression: ");
    scanf("%s", exp);
    printf("\n");

    for (int i = 0; exp[i] != '\0'; ++i) {
        if (isalnum(exp[i]))
            printf("%c ", exp[i]);
        else if (exp[i] == '(')
            push(exp[i]);
        else if (exp[i] == ')') {
            char x;
            while ((x = pop()) != '(')
                printf("%c ", x);
        } else {
            while (priority(stack[top]) >= priority(exp[i]))
                printf("%c ", pop());
            push(exp[i]);
        }
    }

    while (top != -1) {
        printf("%c ", pop());
    }

    return 0;
}


