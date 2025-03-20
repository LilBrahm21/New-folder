
#include<stdio.h>

 char aname[] = "Johann";
 char bname[] = "Brahm";
 char cname[] = "Governor";
 char dname[] = "Nathaly";
 char ename[] = "Kaleb";

void hello(char name[]){
    printf("Hello %s\n", name);
}

   
int main(void){
   hello("Johann");
   hello("Brahm");
   hello("Governor");
   hello("Nathaly");
   hello("Kaleb");
    return 0;

}
