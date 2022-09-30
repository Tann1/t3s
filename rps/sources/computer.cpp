#include "computer.h"


choice_e computer::make_choice() {

	int c = rand() % CHOICES + 1;
	choice_e ch = static_cast<choice_e>(c);
	this->choice = ch;
	
	return ch;
}
