#ifndef GAME_H
#define GAME_H
#include "Player.h"
#include "Computer.h"

class Game{
public:

	void play(); // initialize play

	Game(){}
	unsigned int get_pScore();
	unsigned int get_round();
	unsigned int get_cScore();

	void reset();

private:
	Player player;
	Computer computer;
	unsigned int round = 0; // Keep track of round
	unsigned int pScore = 0; //Player score
	unsigned int cScore = 0; //Computer Score
	unsigned int maxRound = 20;

	void printscore();
	bool chooseWinner(int pChoice, int cChoice);

};


#endif