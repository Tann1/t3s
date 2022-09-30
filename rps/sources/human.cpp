#include "human.h"


choice_e human::make_choice() 
{
	choice_e ch = choice_e::invalid;
	std::cin >> ch;
	this->choice = ch;
	return ch;		
}
