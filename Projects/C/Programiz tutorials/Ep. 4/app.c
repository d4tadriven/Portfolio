
#include <stdio.h>

int main() {
    
    /*     INT INPUT
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Age = %d", age);
    */
    /*     DOUBLE AND CHAR INPUT
    double number;
    char alphabet;

    printf("Enter double input: ");
    scanf("%lf", &number);

    printf("Enter a single character: ");
    scanf("\n%c", &alphabet);

    printf("Number: %lf", number);
    printf("\nCharacter: %c", alphabet);
    */
    /*     MULTIPLE INPUT
    double num;
    char chr;

    printf("Enter input values: ");
    scanf("%lf %c", &num, &chr);

    printf("Number: %lf", num);
    printf("\nCharacter: %c", chr);
    */

    // CHALLENGE
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if (age >= 18) {
        printf("You're an adult because you're %d", age, " years old");
    }
    else {
        printf("You're not an adult because you're %d", age, " years old");
    }
    
    return 0;
}