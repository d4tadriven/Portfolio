
/*
int       (4 bytes) | %d for printing
double    (8 bytes) | %lf for printing | RECCOMENDED (preciser)
float     (4 bytes) | %f for printing
char      (1 byte)  | %c for printing
*/

#include <stdio.h>

int main() {
    
    /*
    double num = 12.345678;
    float num1 = 10.9817f;
    printf("%.2lf", num);
    printf("\n%.2f", num1);
    */
    /*
    double num = 5.5e6;
    printf("%lf", num);
    */
    /*
    char chr = 'z';
    printf("%c", chr);
    printf(" %d", chr);
    */

    int age;
    double number;
    float flt;
    char chr;

    printf("int size = %zu", sizeof (age));
    printf("\nnumer size = %zu", sizeof (number));
    printf("\nfloat size = %zu", sizeof (flt));
    printf("\nchar size = %zu", sizeof (chr));

    return 0;
}