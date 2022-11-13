/***************************************************************
 * Name:      SingupUPApp.cpp
 * Purpose:   Code for Application Class
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#include "SingupUPApp.h"

//(*AppHeaders
#include "SingupUPMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(SingupUPApp);

bool SingupUPApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	SingupUPFrame* Frame = new SingupUPFrame(0);
    	Frame->Show();
    	SetTopWindow(Frame);
    }
    //*)
    return wxsOK;

}
