



import sys
import os
import platform

from db_sources import *

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from db_sources.db_commands import db_commands
from ui_sources import login, signup
from modules import *
from widgets import *


interact = False        

class mvp_app():
    def __init__(self, interactive_mode=interact):
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

        if success:
            self.login_form.show()
            self.signup_form.close()

    def on_click_signup(self, e):
    
        self.signup_form.show()
        self.login_form.close()

    def handle_login(self):
        c_uname = self.login_ui.lineEdit_User.text()
        c_pass = self.login_ui.lineEdit_Password.text()
        user_exists = self.db.authenticate_login(c_uname, c_pass)
        if len(user_exists) != 0:
            self.login_form.hide()
            window.set_customer(user_exists)
            window.show()
            
            
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.customer_info = ()
        self.cart = []
        self.db=db_commands(interactive=interact)


        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Meal Variety Prepping"
        description = "MVP - The next generation of meal prepping"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, False))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
       # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
       #widgets.checkout_.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////


        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.ShoppingCart_button.clicked.connect(self.buttonClick)
        widgets.toggleButton.clicked.connect(self.buttonClick)
        widgets.Button_Addrecipe.clicked.connect(self.buttonClick) #This is for delete
        widgets.Button_Upload.clicked.connect(self.buttonClick)
        widgets.Button_Confirm_Changes.clicked.connect(self.buttonClick)
        widgets.Button_Confirm.clicked.connect(self.buttonClick)
        widgets.Button_UpdateMenu.clicked.connect(self.buttonClick)
        widgets.Button_Addrecipe.clicked.connect(self.buttonClick)
        widgets.Button_ManageSubscriptions.clicked.connect(self.buttonClick)
        widgets.Button_Delete.clicked.connect(self.buttonClick)
        widgets.Subscribe_Button.clicked.connect(self.buttonClick)
        widgets.ShoppingCart_button_3.clicked.connect(self.buttonClick) # cancel order
        widgets.Button_Addtocart.clicked.connect(self.handle_add_to_cart)
        widgets.ShoppingCart_button.clicked.connect(self.handle_shopping_cart)
        

        # EXTRA LEFT BOX
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)

        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # # EXTRA RIGHT BOX
        # def openCloseRightBox():
        #     UIFunctions.toggleRightBox(self, True)
        # widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////


        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home_page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def set_customer(self,customer):
        self.customer_info = customer
        print(*self.customer_info)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home_page)
            self.viewFeatured()
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            pass

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName =="ShoppingCart_button":
            widgets.stackedWidget.setCurrentWidget(widgets.shoppingcart_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            #viewShoppingCart(self)

        #Only manager has access to this. It wont work if they are a customer
        if btnName == "toggleButton":
            widgets.stackedWidget.setCurrentWidget(widgets.managerUI)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "Button_Upload":
            absLocation = r"C:\Users\chris\OneDrive\SJSU\project\pirate\ui_images"
            fname = QFileDialog.getOpenFileName(self,"Open File",absLocation, "All Files (*)")
            print(absLocation)
            self.ui.Textbox_Upload.setText(absLocation)
            

        if btnName == "Button_Addrecipe":
            widgets.stackedWidget.setCurrentWidget(widgets.AddRecipeUI)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))            
            
        if btnName == "Button_Confirm_Changes":
            print("its working")
        
        #We just assume that manager id is 1 for now
        if btnName == "Button_Confirm":
            r_recipe = self.ui.Textbox_Recipename.text()
            r_desc = self.ui.Textbox_RecipeDescription.text()
            r_nutrition = self.ui.Textbox_Nutrition.text()
            r_ethnic = self.ui.Textbox_Ethnictype.text()
            r_price_ = self.ui.Textbox_Setprice.text()
            self.addRecipeToDB()
            self.ui.Textbox_Recipename.clear()
            self.ui.Textbox_RecipeDescription.clear()
            self.ui.Textbox_Nutrition.clear()
            self.ui.Textbox_Ethnictype.clear()
            self.ui.Textbox_Setprice.clear()

        if btnName == "Button_UpdateMenu":   
            self.view_recipes()
            widgets.stackedWidget.setCurrentWidget(widgets.UpdateMenuUI)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName == "Button_ManageSubscriptions":
            widgets.stackedWidget.setCurrentWidget(widgets.ManageSubs)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName == "Button_Delete":
            self.deleteItem()

        if btnName == "Subscribe_Button":
            widgets.stackedWidget.setCurrentWidget(widgets.Thankyou_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))             

        if btnName == "ShoppingCart_button_3":
            widgets.stackedWidget.setCurrentWidget(widgets.home_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))             


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    #Functions
    def addRecipeToDB(self):
        r_recipe = self.ui.Textbox_Recipename.text()
        r_desc = self.ui.Textbox_RecipeDescription.text()
        r_nutrition = self.ui.Textbox_Nutrition.text()
        r_ethnic = self.ui.Textbox_Ethnictype.text()
        r_price_ = self.ui.Textbox_Setprice.text()
        self.db.add_recipe(r_recipe,r_desc,r_nutrition,r_ethnic,r_price_,"1")    


    def viewFeatured(self):
        print("You are seeing featured item")
        f_itemName = "Chicken Curry"
        f_ethnic = "Indian"
        f_desc = "Delicious indian curry"
        f_nutrition = "30g protein, 45g carbs, 10g fat"
        f_price = "12.00"
        self.ui.Featured_Label.setText(f_itemName)
        # self.ui.Ethnic_Label.setText(f_ethnic)
        self.ui.Description_Label.setText(f_desc)
        self.ui.Nutrition_Label.setText(f_nutrition)
        self.ui.Price_Label.setText("$ "+ f_price)

    def deleteItem(self):
        del_recipename = self.ui.DELETE_Textbox_Recipename.text()
        del_rID = self.ui.DELETE_Textbox_RecipeID.text()
        self.db.remove_recipe(del_recipename,del_rID)
        self.ui.DELETE_Textbox_RecipeID.clear()
        self.ui.DELETE_Textbox_Recipename.clear()

    def view_recipes(self):
        helper()
        recipe_data = self.db.get_recipes()
        row = 1
        col_id = 0
        col_rname = 1
        col_desc = 2
        col_nutrition = 3
        col_ethnic = 4
        col_price = 5
        self.ui.menu_.setRowCount(len(recipe_data )+ 1)
        for curr_recipe in recipe_data:
            self.ui.menu_.setItem(row, col_id,QTableWidgetItem(str(curr_recipe[col_id])))
            self.ui.menu_.setItem(row, col_rname,QTableWidgetItem(str(curr_recipe[col_rname])))
            self.ui.menu_.setItem(row, col_desc,QTableWidgetItem(str(curr_recipe[col_desc])))
            self.ui.menu_.setItem(row, col_nutrition,QTableWidgetItem(str(curr_recipe[col_nutrition])))
            self.ui.menu_.setItem(row, col_ethnic,QTableWidgetItem(str(curr_recipe[col_ethnic])))
            self.ui.menu_.setItem(row, col_price,QTableWidgetItem(str(curr_recipe[col_price])))
            row = row + 1

    def handle_add_to_cart(self):
        r_name = widgets.Featured_Label.text()
        r_id = self.db.get_recipe_id(r_name)
        if (r_id != -1):
            self.cart.append(r_id)
        print(self.cart)

    def handle_shopping_cart(self):
        print("hanlding shopping cart btn event.")
        row = 1
        self.ui.shopping_cart_.setRowCount(len(self.cart) + 1)
        for r_id in self.cart:
            data = self.db.get_cart_info(r_id)
            print("data: ", *data)
            self.ui.shopping_cart_.setItem(row, 0, QTableWidgetItem(str(data[0])))
            self.ui.shopping_cart_.setItem(row, 1, QTableWidgetItem(str(data[1])))
            self.ui.shopping_cart_.setItem(row, 3, QTableWidgetItem(str(data[2])))

            row += 1





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = QApplication(sys.argv)
    window = MainWindow()
    mvp_app()

    sys.exit(app.exec_())

def helper():
    print("Do this. Remove me when done daddy") 
