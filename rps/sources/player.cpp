#include "player.h"


std::ostream& operator<<(std::ostream& os, const player& p)
{
	std::string p_type_str = "hello";
	p_type_e p_type = p.p_type;

	switch(p_type) {
		case human_p:
			p_type_str = "your";
			break;
		case computer_p:
			p_type_str = "computer";
			break;
	}
	os << p_type_str;
	
	return os;
}
