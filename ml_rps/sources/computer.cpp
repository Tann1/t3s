#include "computer.h"
#include <iostream>

choice_e computer_random::make_choice() 
{

	int c = rand() % CHOICES + 1;
	choice_e ch = static_cast<choice_e>(c);
	this->choice = ch;
	
	return ch;
}

/* start of ml computer definition */

computer_ml::computer_ml() : N(DEFAULT_N)
{
	std::string permutation;
	int frequency;

	data_file.open(default_file, std::ios::in | std::ios::out);

	if (data_file.peek() != std::ifstream::traits_type::eof()) {	// only if it's not empty then update permutation_frequency
		while (!data_file.eof()) {
			data_file >> permutation >> frequency;
			this->permutation_frequency[permutation] = frequency;
		}
	}
	data_file.clear();

	this->curr_sequence = ""; 
	this->opp_choice == choice_e::invalid;
}

computer_ml::computer_ml(int n)
{
	computer_ml();
	this->N = n;
}

computer_ml::~computer_ml()
{
	std::unordered_map<std::string, int>::iterator itr;

	this->data_file.seekp(0, std::ios::beg);
	for (itr = permutation_frequency.begin(); itr != permutation_frequency.end(); itr++) 
		data_file << itr->first << " " << itr->second << std::endl;

	data_file.close();
}


void computer_ml::store_opponent_choice(player *p)
{
	this->opp_choice = p->get_choice();
}


choice_e computer_ml::make_choice()
{
	bool exist = false;

	if (this->curr_sequence.size() < this->N  || this->opp_choice == invalid) {
		if (this->opp_choice != invalid) {
			this->curr_sequence += get_str_val(this->opp_choice);
			if (this->curr_sequence.size() % this->N != 0)
				this->curr_sequence += get_str_val(rock);
		}
		this->choice = rock;
		return rock; // default value while our ml algo learns
	}
	std::cout << this->curr_sequence << std::endl;	
	exist = check_permutation_exists(this->curr_sequence);	
	if (exist == false)
		this->permutation_frequency[this->curr_sequence] = 0; // make an entry
	
	this->choice = paper;
	return paper;	
}


/* private methods */

std::string computer_ml::get_str_val(choice_e ch)
{
	if (ch == rock)
		return "R";
	if (ch == paper)
		return "P";
	if (ch == scissors)
		return "S";
	return "I"; // invalid
}

bool computer_ml::check_permutation_exists(std::string c_seq)
{
	if (this->permutation_frequency.find(c_seq) == this->permutation_frequency.end())
		return false;	
	return true;
}
