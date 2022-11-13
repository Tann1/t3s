/***************************************************************
 * Name:      LoginUIMain.cpp
 * Purpose:   Code for Application Frame
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#include "LoginUIMain.h"
#include <wx/msgdlg.h>
#include "Signup\SingupUPMain.cpp"
#include "Signup\SingupUPMain.h"

//(*InternalHeaders(LoginUIFrame)
#include <wx/font.h>
#include <wx/intl.h>
#include <wx/settings.h>
#include <wx/string.h>
//*)

//helper functions
enum wxbuildinfoformat {
    short_f, long_f };

wxString wxbuildinfo(wxbuildinfoformat format)
{
    wxString wxbuild(wxVERSION_STRING);

    if (format == long_f )
    {
#if defined(__WXMSW__)
        wxbuild << _T("-Windows");
#elif defined(__UNIX__)
        wxbuild << _T("-Linux");
#endif

#if wxUSE_UNICODE
        wxbuild << _T("-Unicode build");
#else
        wxbuild << _T("-ANSI build");
#endif // wxUSE_UNICODE
    }

    return wxbuild;
}

//(*IdInit(LoginUIFrame)
const long LoginUIFrame::Text_Header = wxNewId();
const long LoginUIFrame::TEXTCTRL_USERNAME = wxNewId();
const long LoginUIFrame::TEXTCTRL_PASSWORD = wxNewId();
const long LoginUIFrame::ID_BUTTON1 = wxNewId();
const long LoginUIFrame::BUTTON_SIGNUP = wxNewId();
const long LoginUIFrame::STATICTEXT_Username = wxNewId();
const long LoginUIFrame::STATICTEXT_PASSWORD = wxNewId();
const long LoginUIFrame::PANEL_LOGIN = wxNewId();
const long LoginUIFrame::ID_MENUITEM1 = wxNewId();
const long LoginUIFrame::idMenuAbout = wxNewId();
const long LoginUIFrame::ID_STATUSBAR1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(LoginUIFrame,wxFrame)
    //(*EventTable(LoginUIFrame)
    //*)
END_EVENT_TABLE()

LoginUIFrame::LoginUIFrame(wxWindow* parent,wxWindowID id)
{
    //(*Initialize(LoginUIFrame)
    wxMenu* Menu1;
    wxMenu* Menu2;
    wxMenuBar* MenuBar1;
    wxMenuItem* MenuItem1;
    wxMenuItem* MenuItem2;

    Create(parent, wxID_ANY, _("UIFrame"), wxDefaultPosition, wxDefaultSize, wxDEFAULT_FRAME_STYLE|wxRESIZE_BORDER, _T("wxID_ANY"));
    SetClientSize(wxSize(350,400));
    SetMinSize(wxSize(350,400));
    SetMaxSize(wxSize(350,400));
    LoginUI_Panel = new wxPanel(this, PANEL_LOGIN, wxDefaultPosition, wxSize(350,400), wxTAB_TRAVERSAL, _T("PANEL_LOGIN"));
    LoginUI_Panel->SetMinSize(wxSize(350,400));
    LoginUI_Panel->SetMaxSize(wxSize(350,400));
    LoginUI_Panel->SetBackgroundColour(wxColour(233,75,60));
    ST_Header = new wxStaticText(LoginUI_Panel, Text_Header, _("Meal Variety \nPrepping"), wxPoint(75,24), wxSize(120,16), wxALIGN_CENTRE, _T("Text_Header"));
    ST_Header->SetForegroundColour(wxSystemSettings::GetColour(wxSYS_COLOUR_MENU));
    wxFont ST_HeaderFont(24,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_BOLD,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    ST_Header->SetFont(ST_HeaderFont);
    TC_Username = new wxTextCtrl(LoginUI_Panel, TEXTCTRL_USERNAME, wxEmptyString, wxPoint(128,144), wxSize(100,25), 0, wxDefaultValidator, _T("TEXTCTRL_USERNAME"));
    TC_Password = new wxTextCtrl(LoginUI_Panel, TEXTCTRL_PASSWORD, wxEmptyString, wxPoint(128,176), wxSize(100,25), wxTE_PASSWORD, wxDefaultValidator, _T("TEXTCTRL_PASSWORD"));
    TC_Password->SetMaxSize(wxSize(-1,-1));
    B_Login = new wxButton(LoginUI_Panel, ID_BUTTON1, _("Login"), wxPoint(128,208), wxSize(100,25), wxBU_BOTTOM|wxBORDER_NONE, wxDefaultValidator, _T("ID_BUTTON1"));
    wxFont B_LoginFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_BOLD,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    B_Login->SetFont(B_LoginFont);
    B_Signup = new wxButton(LoginUI_Panel, BUTTON_SIGNUP, _("Sign up"), wxPoint(128,238), wxSize(100,25), wxBU_BOTTOM|wxBORDER_NONE, wxDefaultValidator, _T("BUTTON_SIGNUP"));
    wxFont B_SignupFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_BOLD,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    B_Signup->SetFont(B_SignupFont);
    ST_Username = new wxStaticText(LoginUI_Panel, STATICTEXT_Username, _("Username:"), wxPoint(40,144), wxSize(75,24), 0, _T("STATICTEXT_Username"));
    wxFont ST_UsernameFont(11,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    ST_Username->SetFont(ST_UsernameFont);
    ST_Password = new wxStaticText(LoginUI_Panel, STATICTEXT_PASSWORD, _("Password:"), wxPoint(40,176), wxSize(75,25), 0, _T("STATICTEXT_PASSWORD"));
    wxFont ST_PasswordFont(11,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    ST_Password->SetFont(ST_PasswordFont);
    MenuBar1 = new wxMenuBar();
    Menu1 = new wxMenu();
    MenuItem1 = new wxMenuItem(Menu1, ID_MENUITEM1, _("Quit\tAlt-F4"), _("Quit the application"), wxITEM_NORMAL);
    Menu1->Append(MenuItem1);
    MenuBar1->Append(Menu1, _("&File"));
    Menu2 = new wxMenu();
    MenuItem2 = new wxMenuItem(Menu2, idMenuAbout, _("About\tF1"), _("Show info about this application"), wxITEM_NORMAL);
    Menu2->Append(MenuItem2);
    MenuBar1->Append(Menu2, _("Help"));
    SetMenuBar(MenuBar1);
    StatusBar1 = new wxStatusBar(this, ID_STATUSBAR1, 0, _T("ID_STATUSBAR1"));
    int __wxStatusBarWidths_1[1] = { -1 };
    int __wxStatusBarStyles_1[1] = { wxSB_NORMAL };
    StatusBar1->SetFieldsCount(1,__wxStatusBarWidths_1);
    StatusBar1->SetStatusStyles(1,__wxStatusBarStyles_1);
    SetStatusBar(StatusBar1);
    Center();

    Connect(ID_BUTTON1,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&LoginUIFrame::OnB_LoginClick);
    Connect(BUTTON_SIGNUP,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&LoginUIFrame::OnB_SignupClick);
    Connect(ID_MENUITEM1,wxEVT_COMMAND_MENU_SELECTED,(wxObjectEventFunction)&LoginUIFrame::OnQuit);
    Connect(idMenuAbout,wxEVT_COMMAND_MENU_SELECTED,(wxObjectEventFunction)&LoginUIFrame::OnAbout);
    Connect(wxID_ANY,wxEVT_CLOSE_WINDOW,(wxObjectEventFunction)&LoginUIFrame::OnClose);
    //*)
}

LoginUIFrame::~LoginUIFrame()
{
    //(*Destroy(LoginUIFrame)
    //*)
}

void LoginUIFrame::OnQuit(wxCommandEvent& event)
{
    Close();
}

void LoginUIFrame::OnAbout(wxCommandEvent& event)
{
    wxString msg = wxbuildinfo(long_f);
    wxMessageBox(msg, _("Welcome to..."));
}

void LoginUIFrame::OnClose(wxCloseEvent& event)
{
}


void LoginUIFrame::OnB_SignupClick(wxCommandEvent& event)
{
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	SingupUPFrame* Frame = new SingupUPFrame(0);
    	Frame->Show();
//SetTopWindow(Frame);
    }
    //*)
    //return wxsOK;
}

void LoginUIFrame::OnB_LoginClick(wxCommandEvent& event)
{
}
