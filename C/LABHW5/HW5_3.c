/****************************************************
 HW5_3 
 ++++++++++++++++++++++++++++++++++*/

#include <stdio.h>

int main(void)
{
    double celsius, fahrenheit;
    const int BASE = 32;
    const double CONVERSION_FACTOR 9.0 / 5.0;
    
    printf("Enter a celsius temperature: ");
    scanf("%lf", &celsius);
    
    fahrenheit = celsius * CONVERSION_FACTOR + BASE;
    
    printf("Fahrenheit Equivalent : %f\n", fahrenheit);
    
    return 0;
}
