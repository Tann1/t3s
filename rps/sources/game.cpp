#include "game.h"


game_rps::game_rps(unsigned int rounds) : rounds(rounds) 
{
	p1 = new human();
	p2 = new computer();
}

game_rps::~game_rps()
{
	delete p1;
	delete p2;
}

void game_rps::display_choices()
{
	std::cout << static_cast<int>(choice_e::rock) << ". " << choice_e::rock << std::endl;
	std::cout << static_cast<int>(choice_e::paper) << ". " << choice_e::paper << std::endl;
	std::cout << static_cast<int>(choice_e::scissors) << ". " << choice_e::scissors << std::endl;
	std::cout << static_cast<int>(choice_e::_exit) << ". " << choice_e::_exit << std::endl;
	std::cout << "Pick your choice: ";
}

int game_rps::determine_winner()
{
	choice_e p1_choice = p1->get_choice();
	choice_e p2_choice = p2->get_choice();
	if (p1_choice == p2_choice)
		return 0;
	if (p1_choice == rock && p2_choice == scissors)
		return 1;
	if (p1_choice == paper && p2_choice == rock)
		return 1;
	if (p1_choice == scissors && p2_choice == paper)
		return 1;
	return -1; 
}

void game_rps::print_winner()
{
	std::string winner_str = "";
	int winner; 

	winner = determine_winner();
	if (winner == 0) {
		std::cout << "It's a tie!" << std::endl;
	} else {	
		winner_str = winner > 0 ? "You" : "Computer"; 
		std::cout << winner_str << " won!" << std::endl;
	}
}

void game_rps::play_rps()
{

	std::cout << "number of rounds: " << this->rounds << std::endl;
	for (unsigned int curr_round = 0; curr_round < this->rounds; ++curr_round)
	{
		display_choices();
		p1->make_choice();
		if (p1->get_choice() == choice_e::_exit)
			break;
		p2->make_choice();
		std::cout << *p1 << " choice made: " << p1->get_choice() << std::endl;
		std::cout << *p2 << " choice made: " << p2->get_choice() << std::endl;
		print_winner();	
		std::cout << std::endl << std::endl;
	}
}

