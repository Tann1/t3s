#include <iostream>

#include "player.h"
#include "computer.h"


int main() {
	
	player *p1 = new computer(); 
	p1->make_choice();
	std::cout << *p1 << " made choice: " << p1->get_choice() << std::endl;
	delete p1;
	return 0;
}
