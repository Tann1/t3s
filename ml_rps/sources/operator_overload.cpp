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
		case _exit:
			choice = "exit";
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
	if (!(ch >= rock && ch <= choice_e::_exit))
		ch = invalid;

	return in;
}
