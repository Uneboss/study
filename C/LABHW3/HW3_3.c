/*********************************************************
 HW3_3 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int hour, minute, second;
    int totalSeconds;
    
    printf("Enter h m s: ");
    scanf("%d %d %d", &hour, &minute, &second);
    
    totalSeconds = hour * 3600 + minute * 60 + second;
    
    printf("---Calculation Result---\n");
    printf("Total %d seconds\n", totalSeconds);
    
    return 0;
}
