/****************************************************
HW5_1 
++++++++++++++++++++++++++++++++++*/

#include <stdio.h>

int main(void)
{
    char ch;
    
    printf("Enter an upper letter(A-Y): ");
    scanf("%c", &ch);
    
    printf("Character given is %c(%d)\n", ch, ch);
    printf("The next character is %c(%d)\n", ch+1, ch+1);
    printf("The lower case letter is %c(%d)\n", ch+32, ch+32);
    
    return 0;
}
