/***************************************************************
 * Name:      LoginUIMain.h
 * Purpose:   Defines Application Frame
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#ifndef LOGINUIMAIN_H
#define LOGINUIMAIN_H

//(*Headers(LoginUIFrame)
#include <wx/button.h>
#include <wx/frame.h>
#include <wx/menu.h>
#include <wx/panel.h>
#include <wx/stattext.h>
#include <wx/statusbr.h>
#include <wx/textctrl.h>
//*)

class LoginUIFrame: public wxFrame
{
    public:

        LoginUIFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~LoginUIFrame();

    private:

        //(*Handlers(LoginUIFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnClose(wxCloseEvent& event);
        void OnB_SignupClick(wxCommandEvent& event);
        void OnB_LoginClick(wxCommandEvent& event);
        //*)

        //(*Identifiers(LoginUIFrame)
        static const long Text_Header;
        static const long TEXTCTRL_USERNAME;
        static const long TEXTCTRL_PASSWORD;
        static const long ID_BUTTON1;
        static const long BUTTON_SIGNUP;
        static const long STATICTEXT_Username;
        static const long STATICTEXT_PASSWORD;
        static const long PANEL_LOGIN;
        static const long ID_MENUITEM1;
        static const long idMenuAbout;
        static const long ID_STATUSBAR1;
        //*)

        //(*Declarations(LoginUIFrame)
        wxButton* B_Login;
        wxButton* B_Signup;
        wxPanel* LoginUI_Panel;
        wxStaticText* ST_Header;
        wxStaticText* ST_Password;
        wxStaticText* ST_Username;
        wxStatusBar* StatusBar1;
        wxTextCtrl* TC_Password;
        wxTextCtrl* TC_Username;
        //*)

        DECLARE_EVENT_TABLE()
};

#endif // LOGINUIMAIN_H
