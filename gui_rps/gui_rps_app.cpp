#include <wx/wx.h>
#include "gui_rps_app.h"

using namespace std;

bool gui_rps_app::OnInit()
{
	if (!wxApp::OnInit())
		return false;

	gui_rps_frame *frame = new gui_rps_frame("rps game");
	frame->Show(true);
	
	return true;
}

wxIMPLEMENT_APP(gui_rps_app);

