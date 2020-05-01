
#include <stdio.h>

int main(void)
{
    int i, studentNum, score, totalScore = 0;
    
    printf("Enter a sutdent number: ");
    scanf("%d", &studentNum);
    
    i = 1;
    while (i <= studentNum)
    {
        printf("Enter a score: ");
        scanf("%d", &score);
        
        totalScore += score;
        i++;
    }
    
    printf("The total is %d\n", totalScore);
    
    return 0;
}
