#ifndef GUI_RPS_APP__H
#define GUI_RPS_APP__H

#include <wx/wx.h>

#include "gui_rps_frame.h"

class gui_rps_app : public wxApp
{
	public:
		virtual bool OnInit();
};
#endif
