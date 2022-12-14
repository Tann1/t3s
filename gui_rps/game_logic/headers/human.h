#ifndef HUMAN__H
#define HUMAN__H

#include <iostream>

#include "enum/choice.h"
#include "player.h"


class human : public player {
	public:
		human() : player(p_type_e::human_p) {}
		choice_e make_choice();
		choice_e get_choice();
};
#endif
