/****************************************************
LAB5_2 
++++++++++++++++++++++++++++++++++*/

#include <stdio.h>

int main(void)
{
    char ch;
    int value;
    
    printf("Enter an alphabet: ");
    scanf("%c", &ch);
    
    printf("%c %d\n", ch, ch);

    printf("Enter a ascii value: ");
    scanf("%d", &value);
    
    printf("%d %c\n", value, value);
    
    return 0;
}
