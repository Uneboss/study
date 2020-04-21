/*********************************************************
 LAB3_1 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int x, y;
    
    printf("Enter the first number : ");
    scanf("%d", &x);
    printf("Enter the second number : ");
    scanf("%d", &y);
    
    printf("%d + %d = %d\n", x, y, x + y);
    printf("%d - %d = %d\n", x, y, x - y);
    printf("%d * %d = %d\n",x, y, x * y);
    printf("%d / %d = %d\n", x, y, x / y);
    
    return 0;
}
