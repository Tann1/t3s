#ifndef RPS_BUTTON_PANEL__H
#define RPS_BUTTON_PANEL__H

#include <wx/wx.h>
#include "game_logic.h"

class rps_button_panel : public wxPanel
{
	public:
		rps_button_panel(wxFrame *parent) : wxPanel(parent, wxID_ANY) { init(); }
	
	void on_rock(wxCommandEvent& e);
	void on_paper(wxCommandEvent& e);
	void on_scissors(wxCommandEvent& e);

	private:
		wxStaticText *choice_button_name;

		void init();
		void update_button_choice_text(const wxString &choice);
};

#endif
