
import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from db_sources.db_commands import db_commands
from ui_sources import login, signup

from main import *        

        

class mvp_app():
    def __init__(self, interactive_mode=True):
        # db property
        self.db = db_commands(interactive=interactive_mode)

        # login ui 
        self.login_form = QtWidgets.QWidget()
        self.login_ui = login.Ui_Form()
        self.login_ui.setupUi(self.login_form)
        self.login_form.show()
    
        #signup ui
        self.signup_form = QtWidgets.QWidget()
        self.signup_ui = signup.signup_ui_form()
        self.signup_ui.setupUi(self.signup_form)

        # bind call back functions for button presses
        self.define_button_actions()

        


    
    def define_button_actions(self):
        self.signup_ui.Button_Signup.clicked.connect(self.handle_sign_up)
        
        self.login_ui.label.mousePressEvent = self.on_click_signup
        self.login_ui.pushButton.clicked.connect(self.handle_login)
    
    def handle_sign_up(self):
        c_fname = self.signup_ui.s_Firstname.text()
        c_lname = self.signup_ui.s_Lastname.text()
        c_uname = self.signup_ui.s_User.text()
        c_email = self.signup_ui.s_Email.text()
        c_pass  = self.signup_ui.s_Pass.text()
        c_addr  = self.signup_ui.s_Address.text() + ' ' + self.signup_ui.s_City.text() + ', ' + self.signup_ui.s_State.text() + ' ' + self.signup_ui.s_ZIP.text()

        success = self.db.insert_new_customer(c_fname, c_lname, c_uname, c_email, c_pass, c_addr)

        if (success):
            self.login_form.show()
            self.signup_form.close()

    def on_click_signup(self, e):
        self.signup_form.show()
        self.login_form.close()

    def handle_login(self):
        c_uname = self.login_ui.lineEdit_User.text()
        c_pass = self.login_ui.lineEdit_Password.text()
        success = self.db.authenticate_login(c_uname, c_pass)
        if (success):
            self.user = MainWindow()
            os.system('python main.py')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mvp_app()
    sys.exit(app.exec_())
    #sys.exit(app.exec_())


    
    
    