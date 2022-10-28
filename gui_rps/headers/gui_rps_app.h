#ifndef GUI_RPS_APP__H
#define GUI_RPS_APP__H

#include <wx/wx.h>

#include "gui_rps_frame.h"
#include "game_logic.h"

#define ROUNDS 20
#define COMP_TYPE 'm'

class gui_rps_app : public wxApp
{
	public:
		virtual bool OnInit();
		~gui_rps_app() {delete game_logic;}

};
#endif
