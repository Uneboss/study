/******
LAB5_1
++++++/
#include <stdio.h>

int main(void)
{
    char gender;
    int age;
    double height;
    
    printf("Enter your gender: ");
    scanf("%c", &gender);
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Enter your height: ");
    scanf("%lf", &height);
    
    printf("성별\t나이\t키\n");
    printf("%c\t%d\t%f\n", gender, age, height);
    
    return 0;
}
