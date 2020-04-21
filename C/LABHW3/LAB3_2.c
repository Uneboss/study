/*********************************************************
 LAB3_2 
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int totalMinutes;
    int hour, minute;
    
    printf("Enter the total minutes : ");
    scanf("%d", &totalMinutes);
    
    hour = totalMinutes / 60;
    minute = totalMinutes % 60;
    
    printf("%d minutes\n", totalMinutes);
    printf("%dh %dm\n", hour, minute);
    
    return 0;
}
