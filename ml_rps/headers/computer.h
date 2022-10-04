#ifndef COMPUTER__H
#define COMPUTER__H

#include <fstream>
#include <unordered_map>
#include <string>

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

#define DEFAULT_N 5
#define default_file "data.txt"

class computer_ml : public computer {
	public:
		computer_ml();   
		computer_ml(int n);
		~computer_ml();
		void store_opponent_choice(player *p);
		choice_e make_choice() {return rock;}

	private:
		int N;
		std::fstream data_file;
		std::unordered_map<std::string, int> permutation_frequency;
		
};

#endif
