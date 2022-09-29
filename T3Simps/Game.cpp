#include <iostream>
#include "Game.h"
#include <Windows.h>

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

				chooseWinner(player.getplayerselection(),computer.getcomputerselection());
				printscore();
				break;
			}
			case (2):
			{

				cout << "\nYou chose Paper";
				player.setplayerselection(2);
				chooseWinner(player.getplayerselection(),computer.getcomputerselection());
				printscore();
				break;
			}
			case (3):
			{
				cout << "\nYou chose Scissors";
				player.setplayerselection(3);
				chooseWinner(player.getplayerselection(),computer.getcomputerselection());
				printscore();
				break;
			}
			case 0:
			{
				cout << "\nThanks for playing!";
				break;
			}
			default:
			{
				cout <<"\nERROR:Invalid input\n";
				Sleep(2000);
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
	cout << "Player score: " << get_pScore() << endl;
	cout << "Computer score: " << get_cScore() << endl;	
}

void Game::reset(){
	pScore = 0;
	cScore = 0;
	round = 0;
}

bool Game::chooseWinner(int pChoice, int cChoice){
	if(pChoice == 2 && cChoice == 1){// Paper beats Rock
		cout << "\nComputer chose Rock. You win!\n";
		pScore++;
		return true;
	} 
	else if(pChoice == 3 && cChoice == 2){ // Scissors beats paper 
		cout << "\nComputer chose Paper. You win!\n";
		pScore++;
		return true;
	}
	else if(pChoice == 1 && cChoice == 3){ // Rock beats scissors
		cout << "\nComputer chose Scissors. You win!\n";
		pScore++;
		return true;
	}
	else if(pChoice == cChoice) // Tie
	{
		cout << "\nIt was a tie!\n";
		return false;
	}
	else{ // computer beats you
		cout << "\nComputer beat you. You lose!\n";
		cScore ++; 
		return false;
	}
}

