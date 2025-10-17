/*
booleans
    true = 1
    false = 2
Comparison operators
    >  | Greater than
    <  | Less than
    == | Equal to
    >= | Greater of equal to
    >= | Less or equal to
    != | Not equal to
Logical operators
    && | and
    || | or
    !  | not
*/
#include <stdio.h>
#include <stdbool.h>

int main() {

    // bool value1 = true; // Don't use capitals eg.(True).
    // bool value2 = false;
    // printf("%d", value1);
    // printf("\n%d", value2);
    //                 Greater than
    bool value = (12 > 9);
    printf("\n%d", value);
    //                 Less than
    bool value1 = (5 < 9);
    printf("\n%d", value1);
    //                 Equal to
    bool value2 = (5 == 5);
    printf("\n%d", value2);
    //                 Greater of equal to
    bool value3 = (7 >= 7);
    printf("\n%d", value3);
    //                 Less or equal to
    bool value4 = (6 <= 3);
    printf("\n%d", value4);
    //                 Not equal to
    bool value5 = (5 != 2);
    printf("\n%d", value5);
    //                 AND operator
    int age = 18;
    double height = 6.3;
    bool result = (age >= 18) && (height > 6.0);
    printf("\n%d", result);
    //                 OR operator
    int age1 = 16;
    double height1 = 6.3;
    bool result1 = (age1 >= 18) || (height1 > 6.0);
    printf("\n%d", result1);
    //                  NOT operator
    bool result2 = !true;
    printf("\n%d", result2);

    // Answer of the test
    //  B. 9 > 9

    return 0;
}