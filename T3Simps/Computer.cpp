#include <iostream>
#include "Computer.h"
#include <time.h>
using namespace std;

unsigned int Computer::getcomputerselection() {
	// Get the system time.
    unsigned seed = time(0);

    // Seed the random number generator.
    srand(seed);

    computerselection = (rand() % 3) + 1;
	return computerselection;
}

unsigned int Computer:: get_guess() {
	return guess;
}
