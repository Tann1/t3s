#include <iostream>
#include <cctype>

#include "game.h"

#define ROUNDS 20

static bool validate_cmd_params(int argc, char *argv[]);
static void show_valid_cmd_params();

int main(int argc, char *argv[]) {
	
	game_rps *game;

	if (!validate_cmd_params(argc, argv))
		return -1;
	game = new game_rps(ROUNDS, argv[1][1]);
	game->play_rps();
	
	delete game;
	return 0;
}

static bool validate_cmd_params(int argc, char *argv[])
{
	char option = '\0';

	if (argc != 2 && sizeof(argv[1]) != 2) {
		show_valid_cmd_params();
		return false;
	}
	if (argv[1][0] != '-') {
		show_valid_cmd_params();
		return false;
	}	
	option = argv[1][1];	
	if (tolower(option) != 'm' && tolower(option) != 'r') {
		show_valid_cmd_params();
		return false;
	}
	return true;
}


static void show_valid_cmd_params()
{
	std::cout << "correct usage: <prog> -[rm]" << std::endl;
}
