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
	std::unordered_map<std::string, int>::iterator itr;

	data_file.open(default_file, std::ios::in | std::ios::out);

	if (data_file.peek() != std::ifstream::traits_type::eof()) {	// only if it's not empty then update permutation_frequency
		while (!data_file.eof()) {
			data_file >> permutation >> frequency;
			this->permutation_frequency[permutation] = frequency;
		}
	}
	data_file.clear();

	for (itr = permutation_frequency.begin(); itr != permutation_frequency.end(); itr++)
		std::cout << itr->first << " " << itr->second << std::endl;

		
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
