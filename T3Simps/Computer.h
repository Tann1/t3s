#ifndef COMPUTER_H
#define COMPUTER_H

class Computer {
public:
	unsigned int getcomputerselection();
	unsigned int get_guess();

protected:
	unsigned int computerselection;
	unsigned int guess = 5;
};

#endif
