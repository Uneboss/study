//
//  main.c
//  LAB7_5
//
//  Created by 김윤혜 on 2020/04/27.
//  Copyright © 2020 김윤혜. All rights reserved.
//

#include <stdio.h>

int main(void)
{
    int num, i;
    int sum = 0, multi = 1;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    i = 1;
    while (i <= num)
    {
        sum += 3;
        multi *= 3;
        i++;
    }
    
    printf("3을 %d번 더한 값은 %d이다.\n", i,  sum);
    printf("3을 %d번 곱한 값은 %d이다.\n", i, multi);
    
    return 0;
}
