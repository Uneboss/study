#include <stdio.h>

int main(void)
{
    int score;
    char grade;
    
    printf("Enter a score: ");
    scanf("%d", &score);
    
    if (score >= 80)
        grade = 'A';
    else if (score >= 50)
        grade = 'B';
    else if (score >= 30)
        grade = 'C';
    else
        grade = 'F';
    
    printf("The grade is %c!\n", grade);
    
    return 0;
}
