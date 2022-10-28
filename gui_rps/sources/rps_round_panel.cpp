#include "rps_round_panel.h"
#include <sstream>

using namespace std;

void rps_round_panel::init()
{
	wxSizer *main_panel_sizer = new wxBoxSizer(wxVERTICAL);
	wxSizer *round_sizer = new wxGridSizer(2, 0, 5);

	wxPanel *round_pan = new wxPanel(this, wxID_ANY);
	
	wxStaticText *round_text = new wxStaticText(round_pan, wxID_ANY, "Round: ");
	stringstream curr_rt; //rt = round text
	curr_rt << game_logic->get_curr_round();
	curr_round_text = new wxStaticText(round_pan, wxID_ANY, wxString(curr_rt.str()));
	curr_round_text->SetFont(curr_round_text->GetFont().Larger());

	round_sizer->Add(round_text, 0, wxALIGN_RIGHT, 0);
	round_sizer->Add(curr_round_text, 0, 0, 0);
	
	round_pan->SetSizer(round_sizer);
	
	main_panel_sizer->Add(round_pan, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);

	SetSizer(main_panel_sizer);	
}


void rps_round_panel::update()
{
	stringstream curr_rt;
	curr_rt << game_logic->get_curr_round();
	curr_round_text->SetLabelText(wxString(curr_rt.str()));
}
