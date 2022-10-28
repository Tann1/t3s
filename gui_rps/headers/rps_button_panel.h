#ifndef RPS_BUTTON_PANEL__H
#define RPS_BUTTON_PANEL__H

#include <wx/wx.h>
#include "game_logic.h"

enum {
	id_rock = 1,
	id_paper = 2,
	id_scissors = 3
};

class rps_button_panel : public wxPanel
{
	public:
		rps_button_panel(wxFrame *parent) : wxPanel(parent, wxID_ANY) { init(); }
	
	void update_button_choice_text(const wxString &choice);

	private:
		wxStaticText *choice_button_name;
		void init();
};

#endif
