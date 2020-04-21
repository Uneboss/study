/*********************************************************
 LAB3_3 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int hour, minute;
    int totalMinutes;
    
    printf("Enter hour : ");
    scanf("%d", &hour);
    printf("Enter minute : ");
    scanf("%d", &minute);
    
    totalMinutes = hour * 60 + minute;
    
    printf("Total %d minutes\n", totalMinutes);
    
    return 0;
}
