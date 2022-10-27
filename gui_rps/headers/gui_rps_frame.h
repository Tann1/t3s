#ifndef GUI_RPS_FRAME__H
#define GUI_RPS_FRAME__H

#include <wx/wx.h>

#include "rps_button_panel.h"

enum
{
	rps_about = wxID_ABOUT,
	rps_quit = wxID_EXIT
};

class gui_rps_frame : public wxFrame
{
	public:
		gui_rps_frame(){}
		gui_rps_frame(const wxString& title);
		virtual ~gui_rps_frame() {}
	
		void on_exit(wxCommandEvent& e);
		void on_about(wxCommandEvent& e);
	private:
		rps_button_panel *rps_panel;
	
		void init();
		void init_sizer();
		void init_menu_bar();

		wxDECLARE_EVENT_TABLE();
};
#endif
