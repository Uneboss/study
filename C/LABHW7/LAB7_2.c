
#include <stdio.h>

int main(void)
{
    char operator;
    int num1, num2, result;
    
    printf("Enter an operator: ");
    scanf("%c", &operator);
    printf("Enter the first operand: ");
    scanf("%d", &num1);
    printf("Enter the second operand: ");
    scanf("%d", &num2);
    
    switch(operator)
    {
        case '+':
            result = num1 + num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '/':
            result = num1 / num2;
            break;
    }
    
    printf("%d %c %d = %d\n", num1, operator, num2, result);

    return 0;
}
