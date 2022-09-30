#include "enum/choice.h"


std::ostream& operator<<(std::ostream& os, const choice_e &ch)
{
	std::string choice = "";

	switch(ch) {
		case rock:
			choice = "rock";
			break;
		case paper:
			choice = "paper";
			break;
		case scissors:
			choice = "scissors";
			break;
		default:
			choice = "invalid";
	}

	os << choice;
	return os;
}

std::istream& operator>>(std::istream& in, choice_e &ch)
{
	unsigned int c;
	in >> c;
	ch = static_cast<choice_e>(c);

	return in;
}
