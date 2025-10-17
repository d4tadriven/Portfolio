/*
DATA TYPE HYRARCHY
    1. long double
    2. double
    3. float
    4. long
    5. int
    6. short
    7. char
*/

#include <stdio.h>

int main() {

    // double a = 5.67;
    // int b = a; // Double conferts to int and loses 2 numbers.
    // printf("%d", a);

    // double a = 5.67;
    // int b = 9;
    // printf("%d", (int)a + b); // Conferts double (a) to an int (always down so 5) and adds it to b.

    int a = 9;
    int b = 2;
    printf("%.1lf", (double)a/b); // Conferts a to double so the result will be double.

    // Answer of the test
    //  B. 68

    return 0;
}