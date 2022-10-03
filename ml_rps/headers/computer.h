#ifndef COMPUTER__H
#define COMPUTER__H

#include <stdlib.h> /* random function */
#include <time.h>

#include "player.h"

class computer : public player {
	public:
		computer() : player(p_type_e::computer_p) {}
		virtual choice_e make_choice() = 0;
};


class computer_random : public computer {
	public:
		computer_random() {srand(time(0));}
		choice_e make_choice();
};

#endif
