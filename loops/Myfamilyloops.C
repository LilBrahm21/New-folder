//Brahm Brar Family Loops C
#include <stdio.h>

char family[][20] = {"Johann", "Rohann", "Nathaly", "Deagan"};


int main(void){
    int flength = sizeof(family)/sizeof(family[0]);

    int f;
    for(f=0;f<flength;f++){
        printf("Hello %s, Welcome to CSP!\n", family[f]);
    }
    return 0;
}