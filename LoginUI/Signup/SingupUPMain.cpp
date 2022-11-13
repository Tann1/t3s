/***************************************************************
 * Name:      SingupUPMain.cpp
 * Purpose:   Code for Application Frame
 * Author:    Tanishq,Christian,Kcirde,Alex ()
 * Created:   2022-11-12
 * Copyright: Tanishq,Christian,Kcirde,Alex ()
 * License:
 **************************************************************/

#include "SingupUPMain.h"
#include <wx/msgdlg.h>

//(*InternalHeaders(SingupUPFrame)
#include <wx/font.h>
#include <wx/intl.h>
#include <wx/string.h>
//*)

//helper functions
/*
enum wxbuildinfo1format {
    short_f, long_f };

wxString wxbuildinfo11(wxbuildinfo1format format)
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
*/

//(*IdInit(SingupUPFrame)
const long SingupUPFrame::STATICTEXT_WELCOME = wxNewId();
const long SingupUPFrame::STATICTEXT_FIRSTNAME = wxNewId();
const long SingupUPFrame::STATICTEXT_LASTNAME = wxNewId();
const long SingupUPFrame::STATICTEXT_STREETADDRESS = wxNewId();
const long SingupUPFrame::ID_STATICTEXT5 = wxNewId();
const long SingupUPFrame::STATICTEXT_CITY = wxNewId();
const long SingupUPFrame::STATICTEXT_PHONE = wxNewId();
const long SingupUPFrame::ID_STATICTEXT8 = wxNewId();
const long SingupUPFrame::TEXTCTRL_FIRSTNAME = wxNewId();
const long SingupUPFrame::TEXTCTRL_LASTNAME = wxNewId();
const long SingupUPFrame::TEXTCTRL_STREETADDRESS = wxNewId();
const long SingupUPFrame::TEXTCTRL_STATE = wxNewId();
const long SingupUPFrame::TEXTCTRL_CITY = wxNewId();
const long SingupUPFrame::TEXTCTRL_PHONE = wxNewId();
const long SingupUPFrame::TEXTCTRL_EMAIL = wxNewId();
const long SingupUPFrame::ID_BUTTON1 = wxNewId();
const long SingupUPFrame::STATICTEXT_ZIP = wxNewId();
const long SingupUPFrame::TEXTCTRL_ZIP = wxNewId();
const long SingupUPFrame::PANEL_SIGNUP = wxNewId();
const long SingupUPFrame::idMenuQuit = wxNewId();
const long SingupUPFrame::idMenuAbout = wxNewId();
const long SingupUPFrame::ID_STATUSBAR1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(SingupUPFrame,wxFrame)
    //(*EventTable(SingupUPFrame)
    //*)
END_EVENT_TABLE()

SingupUPFrame::SingupUPFrame(wxWindow* parent,wxWindowID id)
{
    //(*Initialize(SingupUPFrame)
    wxMenu* Menu1;
    wxMenu* Menu2;
    wxMenuBar* MenuBar1;
    wxMenuItem* MenuItem1;
    wxMenuItem* MenuItem2;

    Create(parent, wxID_ANY, _("SignupUI_Frame"), wxDefaultPosition, wxDefaultSize, wxDEFAULT_FRAME_STYLE, _T("wxID_ANY"));
    SetClientSize(wxSize(450,500));
    Move(wxPoint(450,500));
    SetMinSize(wxSize(450,500));
    SetMaxSize(wxSize(450,500));
    Signup_PANEL = new wxPanel(this, PANEL_SIGNUP, wxPoint(450,500), wxSize(395,320), wxTAB_TRAVERSAL, _T("PANEL_SIGNUP"));
    Signup_PANEL->SetMinSize(wxSize(395,320));
    Signup_PANEL->SetMaxSize(wxSize(450,500));
    Signup_PANEL->SetBackgroundColour(wxColour(233,75,60));
    ST_Welcome = new wxStaticText(Signup_PANEL, STATICTEXT_WELCOME, _("Welcome"), wxPoint(120,16), wxDefaultSize, 0, _T("STATICTEXT_WELCOME"));
    ST_Welcome->SetForegroundColour(wxColour(255,255,255));
    wxFont ST_WelcomeFont(36,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_BOLD,false,_T("Ofelia Display"),wxFONTENCODING_DEFAULT);
    ST_Welcome->SetFont(ST_WelcomeFont);
    ST_FirstName = new wxStaticText(Signup_PANEL, STATICTEXT_FIRSTNAME, _("First Name"), wxPoint(45,100), wxDefaultSize, 0, _T("STATICTEXT_FIRSTNAME"));
    ST_FirstName->SetForegroundColour(wxColour(255,255,255));
    wxFont ST_FirstNameFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_FirstName->SetFont(ST_FirstNameFont);
    ST_LastName = new wxStaticText(Signup_PANEL, STATICTEXT_LASTNAME, _("Last Name"), wxPoint(230,100), wxDefaultSize, 0, _T("STATICTEXT_LASTNAME"));
    ST_LastName->SetForegroundColour(wxColour(240,240,240));
    wxFont ST_LastNameFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_LastName->SetFont(ST_LastNameFont);
    ST_StreetAddress = new wxStaticText(Signup_PANEL, STATICTEXT_STREETADDRESS, _("Street Address"), wxPoint(45,150), wxDefaultSize, 0, _T("STATICTEXT_STREETADDRESS"));
    ST_StreetAddress->SetForegroundColour(wxColour(240,240,240));
    wxFont ST_StreetAddressFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_StreetAddress->SetFont(ST_StreetAddressFont);
    StaticText5 = new wxStaticText(Signup_PANEL, ID_STATICTEXT5, _("State"), wxPoint(230,150), wxSize(26,16), 0, _T("ID_STATICTEXT5"));
    StaticText5->SetForegroundColour(wxColour(255,255,255));
    wxFont StaticText5Font(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    StaticText5->SetFont(StaticText5Font);
    ST_City = new wxStaticText(Signup_PANEL, STATICTEXT_CITY, _("City"), wxPoint(45,200), wxDefaultSize, 0, _T("STATICTEXT_CITY"));
    ST_City->SetForegroundColour(wxColour(255,255,255));
    wxFont ST_CityFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_City->SetFont(ST_CityFont);
    ST_Phone = new wxStaticText(Signup_PANEL, STATICTEXT_PHONE, _("Phone Number"), wxPoint(230,200), wxDefaultSize, 0, _T("STATICTEXT_PHONE"));
    ST_Phone->SetForegroundColour(wxColour(255,255,255));
    wxFont ST_PhoneFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_Phone->SetFont(ST_PhoneFont);
    StaticText8 = new wxStaticText(Signup_PANEL, ID_STATICTEXT8, _("Email"), wxPoint(45,250), wxDefaultSize, 0, _T("ID_STATICTEXT8"));
    StaticText8->SetForegroundColour(wxColour(255,255,255));
    wxFont StaticText8Font(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    StaticText8->SetFont(StaticText8Font);
    TC_FirstName = new wxTextCtrl(Signup_PANEL, TEXTCTRL_FIRSTNAME, wxEmptyString, wxPoint(45,120), wxSize(120,25), 0, wxDefaultValidator, _T("TEXTCTRL_FIRSTNAME"));
    wxFont TC_FirstNameFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_FirstName->SetFont(TC_FirstNameFont);
    TC_LastName = new wxTextCtrl(Signup_PANEL, TEXTCTRL_LASTNAME, wxEmptyString, wxPoint(230,120), wxSize(120,25), 0, wxDefaultValidator, _T("TEXTCTRL_LASTNAME"));
    wxFont TC_LastNameFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_LastName->SetFont(TC_LastNameFont);
    TC_StreetAddress = new wxTextCtrl(Signup_PANEL, TEXTCTRL_STREETADDRESS, wxEmptyString, wxPoint(45,170), wxSize(170,25), 0, wxDefaultValidator, _T("TEXTCTRL_STREETADDRESS"));
    wxFont TC_StreetAddressFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_StreetAddress->SetFont(TC_StreetAddressFont);
    TC_State = new wxTextCtrl(Signup_PANEL, TEXTCTRL_STATE, wxEmptyString, wxPoint(230,170), wxSize(50,25), 0, wxDefaultValidator, _T("TEXTCTRL_STATE"));
    TC_State->SetMaxLength(2);
    wxFont TC_StateFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_State->SetFont(TC_StateFont);
    TC_City = new wxTextCtrl(Signup_PANEL, TEXTCTRL_CITY, wxEmptyString, wxPoint(45,220), wxSize(120,25), 0, wxDefaultValidator, _T("TEXTCTRL_CITY"));
    wxFont TC_CityFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_City->SetFont(TC_CityFont);
    TC_Phone = new wxTextCtrl(Signup_PANEL, TEXTCTRL_PHONE, wxEmptyString, wxPoint(230,220), wxSize(120,25), 0, wxDefaultValidator, _T("TEXTCTRL_PHONE"));
    wxFont TC_PhoneFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_Phone->SetFont(TC_PhoneFont);
    TC_Email = new wxTextCtrl(Signup_PANEL, TEXTCTRL_EMAIL, wxEmptyString, wxPoint(45,270), wxSize(170,25), 0, wxDefaultValidator, _T("TEXTCTRL_EMAIL"));
    wxFont TC_EmailFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_Email->SetFont(TC_EmailFont);
    B_Signup = new wxButton(Signup_PANEL, ID_BUTTON1, _("Sign up"), wxPoint(230,270), wxSize(120,25), 0, wxDefaultValidator, _T("ID_BUTTON1"));
    ST_ZIP = new wxStaticText(Signup_PANEL, STATICTEXT_ZIP, _("Zip"), wxPoint(290,150), wxDefaultSize, 0, _T("STATICTEXT_ZIP"));
    ST_ZIP->SetForegroundColour(wxColour(255,255,255));
    wxFont ST_ZIPFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    ST_ZIP->SetFont(ST_ZIPFont);
    TC_Zip = new wxTextCtrl(Signup_PANEL, TEXTCTRL_ZIP, wxEmptyString, wxPoint(288,170), wxSize(60,25), 0, wxDefaultValidator, _T("TEXTCTRL_ZIP"));
    TC_Zip->SetMaxLength(5);
    wxFont TC_ZipFont(10,wxFONTFAMILY_SWISS,wxFONTSTYLE_NORMAL,wxFONTWEIGHT_NORMAL,false,_T("Ofelia Display Medium"),wxFONTENCODING_DEFAULT);
    TC_Zip->SetFont(TC_ZipFont);
    MenuBar1 = new wxMenuBar();
    Menu1 = new wxMenu();
    MenuItem1 = new wxMenuItem(Menu1, idMenuQuit, _("Quit\tAlt-F4"), _("Quit the application"), wxITEM_NORMAL);
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

    Connect(TEXTCTRL_FIRSTNAME,wxEVT_COMMAND_TEXT_UPDATED,(wxObjectEventFunction)&SingupUPFrame::OnTextCtrl1Text);
    Signup_PANEL->Connect(wxEVT_PAINT,(wxObjectEventFunction)&SingupUPFrame::OnSignup_PANELPaint,0,this);
    Connect(idMenuQuit,wxEVT_COMMAND_MENU_SELECTED,(wxObjectEventFunction)&SingupUPFrame::OnQuit);
    Connect(wxID_ANY,wxEVT_CLOSE_WINDOW,(wxObjectEventFunction)&SingupUPFrame::OnClose);
    //*)
}

SingupUPFrame::~SingupUPFrame()
{
    //(*Destroy(SingupUPFrame)
    //*)
}

void SingupUPFrame::OnQuit(wxCommandEvent& event)
{
    Close();
}


void SingupUPFrame::OnClose(wxCloseEvent& event)
{
}

void OnPanel1Paint(wxPaintEvent& event)
{
}

void SingupUPFrame::OnSignup_PANELPaint(wxPaintEvent& event)
{
}

void SingupUPFrame::OnTextCtrl1Text(wxCommandEvent& event)
{
}
