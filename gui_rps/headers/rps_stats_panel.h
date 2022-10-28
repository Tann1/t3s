#ifndef RPS_STATS_PANEL__H
#define RPS_STATS_PANEL__H

#include <wx/wx.h>
#include "game_logic.h"

class rps_stats_panel : public wxPanel
{
	public:
		rps_stats_panel(wxFrame *parent) : wxPanel(parent, wxID_ANY) { init(); }
		
		void update();

	private:
		wxStaticText *human_wins_val, *computer_wins_val, *ties_val;

		void init();
};

#endif
