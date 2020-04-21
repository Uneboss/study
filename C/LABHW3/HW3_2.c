/*********************************************************
 HW3_2 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int totalSeconds;
    int hour, minute, second;
    
    printf("Enter the total seconds: ");
    scanf("%d", &totalSeconds);
    
    hour = totalSeconds / 3600;
    minute = totalSeconds % 3600 / 60;
    second = totalSeconds % 3600 % 60;
    
    printf("---Calculation Result---\n");
    printf("%d seconds\n", totalSeconds);
    printf("%dh %dm %ds\n", hour, minute, second);
}
