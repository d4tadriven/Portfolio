#include <stdio.h>

int main() {

    /*
    Use comments ("//") to disable certain lines of code.
    This is useful when you want to test certain parts of your code

    Use comments ("/*" and "*./") to disable multiple lines of code.
    */

    //     EXAMPLE
    int age;
    // double height;

    printf("Enter your age: ");
    scanf("%d", &age);

    // printf("Enter your height (cm): ");
    // scanf("%lf", &height);

    printf("Age = %d", age);
    // printf("\nHeight = %.1lf", height, " cm");

    return 0;
}