#include <iostream>

#include "game.h"

#define ROUNDS 20

int main() {
	
	game_rps *game = new game_rps(ROUNDS);
	game->play_rps();

	delete game;
	return 0;
}
