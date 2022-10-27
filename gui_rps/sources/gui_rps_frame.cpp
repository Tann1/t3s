#include <iostream>
#include <wx/wx.h>
#include "gui_rps_frame.h"

using namespace std;

wxBEGIN_EVENT_TABLE(gui_rps_frame, wxFrame)
	EVT_MENU(wxID_ABOUT, gui_rps_frame::on_about)
	EVT_MENU(wxID_EXIT, gui_rps_frame::on_exit)
wxEND_EVENT_TABLE()


gui_rps_frame::gui_rps_frame(const wxString& title) : wxFrame(NULL, wxID_ANY, title)
{
	rps_panel = new rps_button_panel(this);
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
	frame_sizer->Add(rps_panel, 0, wxALIGN_CENTER, 0);

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
