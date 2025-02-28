//Brahm Brar Fiancial Calculator C
#include <stdio.h>  

char name[1000];
  float income, rent, utilities, groceries, transportation, savings, spending;

int main() {  
 
    printf("What is your income?\n");  
    scanf("%f", &income);  

    printf("What is your rent?\n");
    scanf("%f", &rent);  

    printf("What is your utilities?\n");  
    scanf("%f", &utilities);  

    printf("What is your groceries?\n");  
    scanf("%f", &groceries);  

    printf("What is your transportation?\n");  
    scanf("%f", &transportation);

float total_expenses = rent + utilities + groceries + transportation;  
float rent_percentage = (rent / income) * 100;  
float utilities_percentage = (utilities / income) * 100;  
float groceries_percentage = (groceries / income) * 100;  
float transportation_percentage = (transportation / income) * 100;  
float savings_percentage = (savings / income) * 100;  

    
    savings = income * 0.1;  
    spending = income - rent - utilities - groceries - transportation;  
  
     
    printf("Your savings is \$%.2f\n", savings);  
   
  
    return 0;  
}  