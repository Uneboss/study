//
//  main.c
//  LAB7_4
//
//  Created by 김윤혜 on 2020/04/27.
//  Copyright © 2020 김윤혜. All rights reserved.
//

#include <stdio.h>

int main(void)
{
    int num, i;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    i = 1;
    while (i <= num)
    {
        if (i % 3 == 0 || i % 5 == 0)
            printf("%d\n", i);
        i++;
    }
    
    return 0;
}
