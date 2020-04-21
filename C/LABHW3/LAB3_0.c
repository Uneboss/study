/*******
 LAB3_0  
 *******/
#include <stdio.h>

int main(void)
{
    int x = 10, y = 20;
    int result1, result2, result3;
    
    printf("두 수의 덧셈 : %d\n", x + y);
    
    x += 3;
    y *= 4;
    printf("reult : %d %d\n", x, y);
    
    //단항연산자
    x = -x;
    printf("x = -x 연산 이후 x 는 %d\n", x);
    
    x = 10;
    y = 10;
    printf("선 연산 후 증가 : %d\n", x++);
    printf("다시 한 번 출력 : %d\n\n", x);
    printf("선 증가 후 연산 : %d\n", ++y);
    printf("다시 한 번 출력 : %d\n", y);
    
    x = 10;
    y = (x--) + 2;
    printf("x : %d\n", x);
    printf("y : %d\n", y);
    
    //관계연산자
    x = 10, y = 10; //콤마연산자
    result1 = (x == y);
    result2 = (x <= y);
    result3 = (x > y);
    printf("result1 : %d\n", result1);
    printf("result2 : %d\n", result2);
    printf("result3 : %d\n", result3);
    
    //논리연산자
    x = 10;
    y = 20;
    result1 = (x == 10 && y == 10);
    result2 = (x == 10 || y == 10);
    result3 = ! (x == 10);
    printf("result1 : %d\n", result1);
    printf("result2 : %d\n", result2);
    printf("result3 : %d\n", result3);
    
    return 0;
}
