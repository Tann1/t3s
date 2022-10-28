#ifndef RPS_COMPUTER_PANEL__H
#define RPS_COMPUTER_PANEL__H

#include <wx/wx.h>
#include "game_logic.h"

class rps_computer_panel : public wxPanel
{
	public:
		rps_computer_panel(wxFrame *parent) : wxPanel(parent, wxID_ANY) { init(); }
	
	void update();

	private:
		wxStaticText *prediction_choice_val;
		wxStaticText *computer_choice_val;
		
		void init();
};

#endif
