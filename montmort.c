/*
Simulation of the de Montmort's matching problem, 
with reference to Blitzstein and Hwang's Introduction to Probability (Second edition).

Example 1.6.4 (pg 25) Problem statement:
	Consider a well-shuffled deck of n cards, labeled 1 through n. You flip over the cards one by one, saying the
	numbers 1 through n as you do so. You win the game if, at some point, the number
	you say aloud is the same as the number on the card being flipped over (for example,
	if the 7th card in the deck has the label 7). What is the probability of winning?

The solution is that as n goes to infinity the probability approaches (1 - e^-1), where e is the Euler's number.
This program simulates the problem using a pseudorandom number generator.  

*/

#include <stdio.h>
#include <stdlib.h>

#define VALUE (1 - (double)1/2.7182818284590452)
#define TRIALS 30

int montmort(int n);
void shuffle(int *array, size_t n);


int main()
{
	int sizes[TRIALS] = {0};
	int total, successful;

	for(int i=0; i<TRIALS; i++)
		sizes[i] += (i+1)*20;

	printf("inverse of e: %lf\n", VALUE);

	for(int i=0; i<TRIALS; i++)
	{
		total = 0;
		successful = 0;
			
		for(int j=0; j<sizes[i]; j++)
		{
			successful += montmort(sizes[i]);
			total++;
		}

		printf("\nSize of the deck (n): %d\nProbability :%lf", sizes[i], (double)successful/(double)total);
		printf("\ndeviation: %lf\n", VALUE-(double)successful/(double)total);
	}
}


int montmort(int n)
{
	int *deck = malloc(n * sizeof(int));

	for(int i=0; i<n; i++)
		deck[i] = i;

	shuffle(deck, n);

	for(int i=0; i<n; i++)
	{
		if(deck[i] == i)
		{
			free(deck);
			return 1;
		}
	}

	free(deck);
	return 0;
}

void shuffle(int *array, size_t n)
{
    if (n > 1) {
        size_t i;
	for (i = 0; i < n - 1; i++) {
	  size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
	  int t = array[j];
	  array[j] = array[i];
	  array[i] = t;
	}
    }
}