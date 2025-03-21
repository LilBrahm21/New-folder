// Brahm Brar Old Enough C
#include<stdio.h>
#include <string.h>
int age;

int main(void){
    printf("Hello I will tell you if you are old enough!\n");
    printf("How old are you?\n");
    scanf("%d", &age);

    if (age >= 18){
    printf("You are old enough to vote!\n");
}else if (age >= 16){
    printf("You are old enough to drive!\n");
}else if (age >= 15){
        printf("You are old enough to get a learners permit!\n");
}else if (age >= 5){
        printf("You are old enough to go to school!\n");
}else{
    printf("You're too young to go to school.");
};
    return 0;
}
