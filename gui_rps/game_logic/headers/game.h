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
		player *get_human_player() {return p1;}
		player *get_computer_player() {return p2;}
		unsigned int get_rounds() {return rounds;}
		unsigned int get_curr_round() {return curr_round;}
		int determine_winner(); 

		unsigned int get_human_wins();
		unsigned int get_computer_wins();
		unsigned int get_ties();

	private:
		unsigned int rounds, curr_round, computer_wins, ties;
		player *p1, *p2;
		char mode;

		void display_choices(); 
		void print_winner();
};

#endif
