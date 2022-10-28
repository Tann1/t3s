#ifndef RPS_ROUND_PANEL__H
#define RPS_ROUND_PANEL__H

#include <wx/wx.h>
#include "game_logic.h"

class rps_round_panel : public wxPanel
{
	public:
		rps_round_panel(wxFrame *parent) : wxPanel(parent, wxID_ANY) { init(); }
		void update();

	private:
		wxStaticText *curr_round_text;

		void init();
};

#endif
