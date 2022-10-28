#include "rps_stats_panel.h"
#include <sstream>


void rps_stats_panel::init()
{
	wxSizer *main_panel_sizer = new wxBoxSizer(wxVERTICAL);

	/* Stats header panel */
	wxPanel *stats_header_panel = new wxPanel(this, wxID_ANY);
	
	wxStaticText *stats_label = new wxStaticText(stats_header_panel, wxID_ANY, "STATS");

	/* human wins panel */
	wxPanel *human_wins_panel = new wxPanel(this, wxID_ANY);
	wxSizer *human_wins_sizer = new wxGridSizer(2, 0, 5);

	wxStaticText *human_wins_label = new wxStaticText(human_wins_panel, wxID_ANY, "human wins: ");
	human_wins_val = new wxStaticText(human_wins_panel, wxID_ANY, "0");
	human_wins_val->SetFont(human_wins_val->GetFont().Larger());

	human_wins_sizer->Add(human_wins_label, 0, wxALIGN_RIGHT, 0);
	human_wins_sizer->Add(human_wins_val, 0, 0, 0);

	human_wins_panel->SetSizer(human_wins_sizer);

	/* computer wins panel */
	wxPanel *computer_wins_panel = new wxPanel(this, wxID_ANY);
	wxSizer *computer_wins_sizer = new wxGridSizer(2, 0, 5);

	wxStaticText *computer_wins_label = new wxStaticText(computer_wins_panel, wxID_ANY, "computer wins: ");
	computer_wins_val = new wxStaticText(computer_wins_panel, wxID_ANY, "0");
	computer_wins_val->SetFont(computer_wins_val->GetFont().Larger());

	computer_wins_sizer->Add(computer_wins_label, 0, wxALIGN_RIGHT, 0);
	computer_wins_sizer->Add(computer_wins_val, 0, 0, 0);

	computer_wins_panel->SetSizer(computer_wins_sizer);

	/* ties wins panel */
	wxPanel *ties_panel = new wxPanel(this, wxID_ANY);
	wxSizer *ties_sizer = new wxGridSizer(2, 0, 5);

	wxStaticText *ties_label = new wxStaticText(ties_panel, wxID_ANY, "ties: ");
	ties_val = new wxStaticText(ties_panel, wxID_ANY, "0");
	ties_val->SetFont(ties_val->GetFont().Larger());

	ties_sizer->Add(ties_label, 0, wxALIGN_RIGHT, 0);
	ties_sizer->Add(ties_val, 0, 0, 0);

	ties_panel->SetSizer(ties_sizer);

	main_panel_sizer->Add(stats_header_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);
	main_panel_sizer->Add(human_wins_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);	
	main_panel_sizer->Add(computer_wins_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);	
	main_panel_sizer->Add(ties_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);	

	SetSizer(main_panel_sizer);
}


void rps_stats_panel::update()
{
	std::stringstream h_wins, c_wins, ties;
	h_wins << game_logic->get_human_wins();
	c_wins << game_logic->get_computer_wins();
	ties << game_logic->get_ties();

	human_wins_val->SetLabelText(h_wins.str());
	computer_wins_val->SetLabelText(c_wins.str());
	ties_val->SetLabelText(ties.str());
}
