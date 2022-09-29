#include <iostream>
#include "Game.h"

using namespace std;

void Game::play(){

	cout <<"-------------------------------------";
	cout <<"\nWelcome to T3S Rock Paper Scissors!\n";
	cout <<"-------------------------------------" << endl;

	int user;


	while(user != 0){
		cout << "\n---------Please choose---------\n";
		cout << "\n1. Rock";
		cout << "\n2. Paper";
		cout << "\n3. Scissor";
		cout << "\n0. Exit";
		cout << "\nInput: ";
		cin >> user;
		switch(user)
		{
			case (1):
			{
				cout << "\nYou chose Rock";
				player.setplayerselection(1);
				computer.getcomputerselection();
				break;
			}
			case (2):
			{

				cout << "\nYou chose Paper";
				player.setplayerselection(2);
				computer.getcomputerselection();
				break;
			}
			case (3):
			{
				cout << "\nYou chose Scissors";
				player.setplayerselection(3);
				computer.getcomputerselection();
				break;
			}
			case 0:
			{
				cout << "\nThanks for playing!";
				break;
			}
		}
	}

}

unsigned int Game::get_pScore(){
	return pScore;
}
unsigned int Game::get_round(){
	return round;
}
unsigned int Game::get_cScore(){
	return cScore;
}

void Game::printscore(){
	cout << "Player score: " << pScore << endl;
	cout << "Computer score: " << cScore << endl;	
}

void Game::reset(){
	pScore = 0;
	cScore = 0;
	round = 0;
}

bool Game::chooseWinner(int pChoice, int cChoice){
	if(pChoice)
}

