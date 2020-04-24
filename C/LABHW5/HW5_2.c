/****************************************************
HW5_2 
++++++++++++++++++++++++++++++++++*/

#include <stdio.h>

int main(void)
{
    const double PI = 3.141592;
    int radius;
    double area;
       
    printf("Enter a radius: ");
    scanf("%d", &radius);
       
    area = radius * radius * PI;
       
    printf("The area of a circle with %d: %f\n", radius, area);
    printf("The circumferenece of a circle with %d: %f\n", radius, radius * 2 * PI);
       
    return 0;
}
