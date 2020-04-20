//  HW2_3

#include <stdio.h>
int main(void)
{
    int totalSeconds = 14000;
    int hour = totalSeconds/3600;
    int minute = totalSeconds%3600/60;
    int second = totalSeconds%3600%60;
    
    printf("%d seconds:\n", totalSeconds);
    printf("%dh %dm %ds\n", hour, minute, second);
    
    return 0;
}
