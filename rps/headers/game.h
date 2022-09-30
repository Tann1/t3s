#ifndef GAME__H
#define GAME__H

#include <iostream>

#include "player.h"
#include "human.h"
#include "computer.h"


class game_rps {
	public:
		game_rps(){}
		game_rps(unsigned int rounds);
		~game_rps();

		void play_rps();

	private:
		unsigned int rounds;
		player *p1, *p2;

		void display_choices(); 
		int determine_winner(); 
		void print_winner();
};

#endif
