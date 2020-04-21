/*********************************************************
 HW3_1 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int score1, score2;
    int average;
    
    printf("Enter two scores: ");
    scanf("%d %d", &score1, &score2);
    
    average = (score1 + score2) / 2;
    
    printf("The average is %d\n", average);
    
    return 0;
}
