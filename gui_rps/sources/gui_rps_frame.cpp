#include <iostream>
#include <wx/wx.h>
#include "gui_rps_frame.h"

using namespace std;

wxBEGIN_EVENT_TABLE(gui_rps_frame, wxFrame)
	EVT_MENU(wxID_ABOUT, gui_rps_frame::on_about)
	EVT_MENU(wxID_EXIT, gui_rps_frame::on_exit)
	EVT_BUTTON(id_rock, gui_rps_frame::on_rock)
	EVT_BUTTON(id_paper, gui_rps_frame::on_paper)
	EVT_BUTTON(id_scissors, gui_rps_frame::on_scissors)
wxEND_EVENT_TABLE()


gui_rps_frame::gui_rps_frame(const wxString& title) : wxFrame(NULL, wxID_ANY, title)
{
	round_panel = new rps_round_panel(this);
	rps_panel = new rps_button_panel(this);
	computer_panel = new rps_computer_panel(this);
	stats_panel = new rps_stats_panel(this);
	init();
}

void gui_rps_frame::init()
{
	init_menu_bar();
	init_sizer();
	wxSize size = GetBestSize();
	SetMinClientSize(size);
}


void gui_rps_frame::init_sizer()
{
	wxSizer *frame_sizer = new wxBoxSizer(wxVERTICAL);

	frame_sizer->AddSpacer(20);
	frame_sizer->Add(round_panel, 0, wxALIGN_CENTER, 0);
	frame_sizer->AddSpacer(20);
	frame_sizer->Add(rps_panel, 0, wxALIGN_CENTER, 0);
	frame_sizer->AddSpacer(20);
	frame_sizer->Add(computer_panel, 0, wxALIGN_CENTER, 0);
	frame_sizer->AddSpacer(20);
	frame_sizer->Add(stats_panel, 0, wxALIGN_CENTER, 0);
	frame_sizer->AddSpacer(40);

	SetSizerAndFit(frame_sizer);
}

void gui_rps_frame::init_menu_bar()
{
	wxMenu *fileMenu = new wxMenu();
	fileMenu->Append(rps_quit, "E&xit\tAlt-X", "Quit program");
	
	wxMenu *helpMenu = new wxMenu();
	helpMenu->Append(rps_about, "&About\tF1", "Show about dialog");
	
	wxMenuBar *menuBar = new wxMenuBar();
	menuBar->Append(fileMenu, "&File");
	menuBar->Append(helpMenu, "&Help");
	SetMenuBar(menuBar);
}


void gui_rps_frame::on_about(wxCommandEvent& WXUNUSED(e))
{
	wxMessageBox(wxString::Format(
			"This is an Rock-Paper-Scissors game\n"
			"made by the best people in the world\n"),
			"About",
			wxOK | wxICON_INFORMATION,
			this);
}

void gui_rps_frame::on_exit(wxCommandEvent& WXUNUSED(e))
{
	Close(true);
}

void gui_rps_frame::on_rock(wxCommandEvent& WXUNUSED(e))
{
	player* human = game_logic->get_human_player();
	player *computer = game_logic->get_computer_player();
	
	human->set_choice(choice_e::rock);
	rps_panel->update_button_choice_text("rock");
	
	computer->store_opponent_choice(human);
	computer->make_choice();
	game_logic->determine_winner();
	update();
}
void gui_rps_frame::on_paper(wxCommandEvent& WXUNUSED(e))
{
	player* human = game_logic->get_human_player();
	player *computer = game_logic->get_computer_player();
	
	human->set_choice(choice_e::paper);
	rps_panel->update_button_choice_text("paper");
	
	computer->store_opponent_choice(human);
	computer->make_choice();
	game_logic->determine_winner();
	update();
}
void gui_rps_frame::on_scissors(wxCommandEvent& WXUNUSED(e))
{
	player* human = game_logic->get_human_player();
	player *computer = game_logic->get_computer_player();
	
	human->set_choice(choice_e::scissors);
	rps_panel->update_button_choice_text("scissors");
	
	computer->store_opponent_choice(human);
	computer->make_choice();
	game_logic->determine_winner();
	update();
}

void gui_rps_frame::update()
{
	round_panel->update();
	computer_panel->update();
	stats_panel->update();
}
