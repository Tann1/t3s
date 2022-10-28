#ifndef PLAYER__H
#define PLAYER__H

#include <iostream>
#include <string>
#include "enum/choice.h"
#include "enum/p_type.h"


class player {
	public:
		player(){this->choice = choice_e::invalid;}
		player(p_type_e p_t) : p_type(p_t) {player();}
		virtual ~player() {}

		virtual choice_e make_choice() {return choice_e::invalid;}
		virtual void store_opponent_choice(player *p) {}
		void set_choice(choice_e ch) {this->choice = ch;}
		choice_e get_choice() {return this->choice;}
		
		friend std::ostream& operator<<(std::ostream& os, const player& p);
	protected:
		choice_e choice;
		p_type_e p_type;
};


#endif 
