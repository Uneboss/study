//  LAB2_3

#include <stdio.h>
int main(void)
{
    // 세 개의 변수 totalMinute, hour, minute 을 선언하고 totalMinute 에 값 130을 배정하라.
    int totalMinute = 200;
    int hour, minute;
    // hour 를 계산한다. 이때 totalMinute 을 이용한다.
    hour = totalMinute/60;
    // minute 을 계산한다. 이때 totalMinute 을 이용한다.
    minute = totalMinute%60;
    // 출력한다. 이때 totalMinute, hour, minute 을 이용한다.
    printf("%d분:\n%dh %dm\n", totalMinute, hour, minute);
    
    return 0;
}
