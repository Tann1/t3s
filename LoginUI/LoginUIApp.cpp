/***************************************************************
 * Name:      LoginUIApp.cpp
 * Purpose:   Code for Application Class
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#include "LoginUIApp.h"

//(*AppHeaders
#include "LoginUIMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(LoginUIApp);

bool LoginUIApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	LoginUIFrame* Frame = new LoginUIFrame(0);
    	Frame->Show();
    	SetTopWindow(Frame);
    }
    //*)
    return wxsOK;

}
