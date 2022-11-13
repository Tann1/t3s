/***************************************************************
 * Name:      SingupUPMain.h
 * Purpose:   Defines Application Frame
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#ifndef SINGUPUPMAIN_H
#define SINGUPUPMAIN_H

//(*Headers(SingupUPFrame)
#include <wx/button.h>
#include <wx/frame.h>
#include <wx/menu.h>
#include <wx/panel.h>
#include <wx/stattext.h>
#include <wx/statusbr.h>
#include <wx/textctrl.h>
//*)

class SingupUPFrame: public wxFrame
{
    public:

        SingupUPFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~SingupUPFrame();

    private:

        //(*Handlers(SingupUPFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnClose(wxCloseEvent& event);
        void OnPanel1Paint(wxPaintEvent& event);
        void OnSignup_PANELPaint(wxPaintEvent& event);
        void OnTextCtrl1Text(wxCommandEvent& event);
        //*)

        //(*Identifiers(SingupUPFrame)
        static const long STATICTEXT_WELCOME;
        static const long STATICTEXT_FIRSTNAME;
        static const long STATICTEXT_LASTNAME;
        static const long STATICTEXT_STREETADDRESS;
        static const long ID_STATICTEXT5;
        static const long STATICTEXT_CITY;
        static const long STATICTEXT_PHONE;
        static const long ID_STATICTEXT8;
        static const long TEXTCTRL_FIRSTNAME;
        static const long TEXTCTRL_LASTNAME;
        static const long TEXTCTRL_STREETADDRESS;
        static const long TEXTCTRL_STATE;
        static const long TEXTCTRL_CITY;
        static const long TEXTCTRL_PHONE;
        static const long TEXTCTRL_EMAIL;
        static const long ID_BUTTON1;
        static const long STATICTEXT_ZIP;
        static const long TEXTCTRL_ZIP;
        static const long PANEL_SIGNUP;
        static const long idMenuQuit;
        static const long idMenuAbout;
        static const long ID_STATUSBAR1;
        //*)

        //(*Declarations(SingupUPFrame)
        wxButton* B_Signup;
        wxPanel* Signup_PANEL;
        wxStaticText* ST_City;
        wxStaticText* ST_FirstName;
        wxStaticText* ST_LastName;
        wxStaticText* ST_Phone;
        wxStaticText* ST_StreetAddress;
        wxStaticText* ST_Welcome;
        wxStaticText* ST_ZIP;
        wxStaticText* StaticText5;
        wxStaticText* StaticText8;
        wxStatusBar* StatusBar1;
        wxTextCtrl* TC_City;
        wxTextCtrl* TC_Email;
        wxTextCtrl* TC_FirstName;
        wxTextCtrl* TC_LastName;
        wxTextCtrl* TC_Phone;
        wxTextCtrl* TC_State;
        wxTextCtrl* TC_StreetAddress;
        wxTextCtrl* TC_Zip;
        //*)

        DECLARE_EVENT_TABLE()
};

#endif // SINGUPUPMAIN_H
