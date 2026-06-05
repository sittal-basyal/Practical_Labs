// Write a program to simulate the concept of DIning-Philosophers probelm.
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int tph, philname[20], status[20], howhung, hu[20], cho;
int i, j;

void one();
void two();

void main()
{
    printf("\n\n Dining Philosopher Problem");
    printf("\nEnter the total no. of philosophers: ");
    scanf("%d", &tph);
    
    for(i = 0; i < tph; i++)
    {
        philname[i] = (i + 1);
        status[i] = 1;
    }
    
    printf("How many are hungry: ");
    scanf("%d", &howhung);
    
    if(howhung == tph)
    {
        printf("\n All are hungry.\n Deadlock stage will occur");
        printf("\nExiting\n");
    }
    else
    {
        for(i = 0; i < howhung; i++)
        {
            printf("Enter philosopher %d position: ", (i + 1));
            scanf("%d", &hu[i]);
            status[hu[i]] = 2;
        }
        
        do
        {
            printf("\n1. One can eat at a time\t2. Two can eat at a time\t3. Exit");
            printf("\nEnter your choice: ");
            scanf("%d", &cho);
            
            switch(cho)
            {
                case 1:
                    one();
                    break;
                case 2:
                    two();
                    break;
                case 3:
                    exit(0);
                default:
                    printf("\nInvalid option.");
            }
        } while(1);
    }
}

void one()
{
    int pos = 0, x;
    printf("\n Allow one philosopher to eat at any time\n");
    
    for(i = 0; i < howhung; i++, pos++)
    {
        printf("\n P %d is granted to eat", philname[hu[pos]]);
        
        for(x = pos + 1; x < howhung; x++)
            printf("\n P %d is waiting", philname[hu[x]]);
    }
}

void two()
{
    int s = 0, t, r, x;
    printf("\n Allow two philosophers to eat at same time\n");
    
    for(i = 0; i < howhung; i++)
    {
        for(j = i + 1; j < howhung; j++)
        {
            if(abs(hu[i] - hu[j]) >= 1 && abs(hu[i] - hu[j]) != 4)
            {
                printf("\n Combination %d", (s + 1));
                t = hu[i];
                r = hu[j];
                s++;
                printf("\n P %d and P %d are granted to eat", philname[t], philname[r]);
                
                for(x = 0; x < howhung; x++)
                {
                    if((hu[x] != t) && (hu[x] != r))
                        printf("\n P %d is waiting", philname[hu[x]]);
                }
                printf("\n");
            }
        }
    }
}