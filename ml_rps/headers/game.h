#ifndef GAME__H
#define GAME__H

#include <iostream>
#include <cctype>

#include "player.h"
#include "human.h"
#include "computer.h"


class game_rps {
	public:
		game_rps(){}
		game_rps(unsigned int rounds);
		game_rps(unsigned int rounds, char comp_type);
		~game_rps();

		void play_rps();

	private:
		unsigned int rounds;
		player *p1, *p2;
		char mode;

		void display_choices(); 
		int determine_winner(); 
		void print_winner();
};

#endif
