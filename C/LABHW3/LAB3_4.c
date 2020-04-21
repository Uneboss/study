/*********************************************************
 LAB3_4
 *********************************************************/
#include <stdio.h>

int main(void)
{
    int base, height;
    int area;
    
    printf("밑변과 높이를 입력하세요: ");
    scanf("%d %d", &base, &height);
    
    area = base * height / 2;
    
    printf("밑변과 높이가 각각 %d와 %d인 삼각형의 넓이는 %d이다\n", base, height, area);
    
    return 0;
}
