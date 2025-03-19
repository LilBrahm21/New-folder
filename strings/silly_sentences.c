#include <stdio.h>
#include <string.h>

int main(void){
    char name[20], place[20], verb[20], noun[20], sentence[500];
    printf("Type a name: ");
    scanf("%s", name);
    printf("Type a restaurant: ");
    scanf("%s", place);
    printf("Type a verb: ");
    scanf("%s", verb);
    printf("Type a food: ");
    scanf("%s", noun);
    strcat(sentence, name);
    strcat(sentence, " ate at the ");
    strcat(sentence,place);
    strcat(sentence," where they ");
    strcat(sentence,verb);
    strcat(sentence, " and bought ");
    strcat(sentence, noun);
    strcat(sentence, ".\n");
    printf("%s", sentence);
    return 0;
}
