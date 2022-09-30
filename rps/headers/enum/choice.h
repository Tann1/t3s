#ifndef CHOICE__H
#define CHOICE__H

#include <iostream>
#include <string>

#define CHOICES 3

enum choice_e {
	rock=1,
	paper,
	scissors,
	invalid
};


std::ostream& operator<<(std::ostream& os, const choice_e &ch);
std::istream& operator>>(std::istream& in, choice_e &ch);
#endif
