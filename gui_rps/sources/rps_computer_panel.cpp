#include "rps_computer_panel.h"

void rps_computer_panel::init()
{
	wxSizer *main_panel_sizer = new wxBoxSizer(wxVERTICAL);

	wxPanel *prediction_panel = new wxPanel(this, wxID_ANY);
	wxSizer *prediction_sizer = new wxGridSizer(2, 0, 5);
	
	wxStaticText *prediction_label = new wxStaticText(prediction_panel, wxID_ANY, "computer prediction: ");
	prediction_choice_val = new wxStaticText(prediction_panel, wxID_ANY, "");
	prediction_choice_val->SetFont(prediction_choice_val->GetFont().Larger());

	prediction_sizer->Add(prediction_label, 0, wxALIGN_RIGHT, 0);
	prediction_sizer->Add(prediction_choice_val, 0, 0, 0);

	prediction_panel->SetSizer(prediction_sizer);

	wxPanel *computer_panel = new wxPanel(this, wxID_ANY);
	wxSizer *computer_sizer = new wxGridSizer(2, 0, 5);
	
	wxStaticText *computer_label = new wxStaticText(computer_panel, wxID_ANY, "computer choice: ");
	computer_choice_val = new wxStaticText(computer_panel, wxID_ANY, "");
	computer_choice_val->SetFont(computer_choice_val->GetFont().Larger());

	computer_sizer->Add(computer_label, 0, wxALIGN_RIGHT, 0);
	computer_sizer->Add(computer_choice_val, 0, 0, 0);

	computer_panel->SetSizer(computer_sizer);


	main_panel_sizer->Add(prediction_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);
	main_panel_sizer->Add(computer_panel, 0, wxALIGN_CENTER, 0);
	main_panel_sizer->AddSpacer(20);

	SetSizer(main_panel_sizer);
}

void rps_computer_panel::update()
{
	player* computer = game_logic->get_computer_player();

	prediction_choice_val->SetLabelText(computer->get_prediction());
	computer_choice_val->SetLabelText(computer->get_choice_str());
}
