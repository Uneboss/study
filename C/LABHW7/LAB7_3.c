//
//  main.c
//  LAB7_3
//
//  Created by 김윤혜 on 2020/04/27.
//  Copyright © 2020 김윤혜. All rights reserved.
//

#include <stdio.h>

int main(void)
{
    int i, n;
    
    printf("Enter a number: ");
    scanf("%d", &n);
    
    i = 1;
    while (i <= n)
    {
        printf("%d\n", i*i*i);
        i++;
    }
    
    return 0;
}
