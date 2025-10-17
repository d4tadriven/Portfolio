/*
OPERATORS IN C
Operators are special symbols that perform specific operations on one, two, or more operands and then return a result.
    +  | Addition
    -  | Subtraction
    *  | Multiplication
    /  | Division
    %  | Remainder / Modulus
    ++ | Increment (by 1)
    -- | Decrement (by 1)
*/
#include <stdio.h>

int main() {
    // Addition (int)
    int x = 12;
    printf("%d", x + 8);
    // Addition (double)
    double x1 = 12.57;
    printf("\n%.2lf", x1 + 8.67);
    // Addition (int & double)
    double x2 = 12.57;
    int y = 8;
    printf("\n%.2lf", x2 + y);
    // Division
    double x3 = 12;
    printf("\n%.2lf", x3/8);
    // Remainder
    int x4 = 12;
    printf("\n%d", x4 % 8);
    // Increment
    int x5 = 12;
    printf("\n%d", ++x5);
    // Decrement
    int x6 = 12;
    printf("\n%d", --x6);
    // Multiple operators
    int x7 = (4/2) + (6*5) - 1;
    printf("%d", x);

    // Answer of the test
    //  C. 8

    return 0;
}