#include "rps_button_panel.h"
#include <string>

void rps_button_panel::init()
{
	wxSizer *main_panel_sizer = new wxBoxSizer(wxVERTICAL);
	
	wxPanel *button_panel = new wxPanel(this, wxID_ANY);
	wxSizer *button_sizer = new wxBoxSizer(wxHORIZONTAL);

	wxStaticText *choose_text = new wxStaticText(button_panel, wxID_ANY, "Choose: ");
	wxButton *rock_button = new wxButton(button_panel, wxID_ANY, wxString("rock"));
	wxButton *paper_button = new wxButton(button_panel, wxID_ANY, wxString("paper"));
	wxButton *scissors_button = new wxButton(button_panel, wxID_ANY, wxString("scissors"));

	/* event handler for each button */
	rock_button->Bind(wxEVT_BUTTON, &rps_button_panel::on_rock, this);
	paper_button->Bind(wxEVT_BUTTON, &rps_button_panel::on_paper, this);
	scissors_button->Bind(wxEVT_BUTTON, &rps_button_panel::on_scissors, this);

	/* arrange the layout */
	button_sizer->Add(choose_text, 0, 0, 0);
	button_sizer->AddSpacer(5);
	button_sizer->Add(rock_button, 0, 0, 0);
	button_sizer->AddSpacer(5);
	button_sizer->Add(paper_button, 0, 0, 0);
	button_sizer->AddSpacer(5);
	button_sizer->Add(scissors_button, 0, 0, 0);

	button_panel->SetSizer(button_sizer);

	/* show player choice panel */
	wxPanel *choice_panel = new wxPanel(this, wxID_ANY);
	wxSizer *choice_sizer = new wxGridSizer(2, 0, 5);

	wxStaticText *choice_label = new wxStaticText(choice_panel, wxID_ANY, "Choice made: ");
	choice_button_name = new wxStaticText(choice_panel, wxID_ANY, "");
	choice_button_name->SetFont(choice_button_name->GetFont().Larger());

	choice_sizer->Add(choice_label, 0, wxALIGN_RIGHT, 0);
	choice_sizer->Add(choice_button_name, 0, 0, 0);

	choice_panel->SetSizer(choice_sizer);

	/* add both rps buttons and player choice panels to the main panel */
	main_panel_sizer->Add(button_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);
	main_panel_sizer->Add(choice_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);
	
	SetSizer(main_panel_sizer);
}


void rps_button_panel::on_rock(wxCommandEvent& e)
{
	std::string r = "rock";
	update_button_choice_text(wxString(r));

	/* execute internal logic after player had made their choice */
	game_logic->get_human_player()->set_choice(choice_e::rock);
	game_logic->get_computer_player()->store_opponent_choice(game_logic->get_human_player());
	game_logic->get_computer_player()->make_choice();
	choice_e human = game_logic->get_human_player()->get_choice();
	choice_e computer = game_logic->get_computer_player()->get_choice();
	std::cout << game_logic->determine_winner() << human << computer << std::endl;
}

void rps_button_panel::on_paper(wxCommandEvent& e)
{
	std::string p = "paper";
	update_button_choice_text(wxString(p));

	/* execute internal logic after player had made their choice */
	game_logic->get_human_player()->set_choice(choice_e::paper);
	game_logic->get_computer_player()->store_opponent_choice(game_logic->get_human_player());
	game_logic->get_computer_player()->make_choice();
	choice_e human = game_logic->get_human_player()->get_choice();
	choice_e computer = game_logic->get_computer_player()->get_choice();
	std::cout << game_logic->determine_winner() << human << computer << std::endl;
}


void rps_button_panel::on_scissors(wxCommandEvent& e)
{
	std::string s = "scissors";
	update_button_choice_text(wxString(s));

	/* execute internal logic after player had made their choice */
	game_logic->get_human_player()->set_choice(choice_e::scissors);
	game_logic->get_computer_player()->store_opponent_choice(game_logic->get_human_player());
	game_logic->get_computer_player()->make_choice();
	choice_e human = game_logic->get_human_player()->get_choice();
	choice_e computer = game_logic->get_computer_player()->get_choice();
	std::cout << game_logic->determine_winner() << human << computer << std::endl;
}

void rps_button_panel::update_button_choice_text(const wxString &choice)
{
	choice_button_name->SetLabelText(choice);
}
