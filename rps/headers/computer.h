#ifndef COMPUTER__H
#define COMPUTER__H

#include <stdlib.h> /* random function */
#include <time.h>

#include "player.h"


class computer : public player {
	public:
		computer() : player(p_type_e::computer_p) {srand(time(0));}
		choice_e make_choice();
		choice_e get_choice();
		
};

#endif
