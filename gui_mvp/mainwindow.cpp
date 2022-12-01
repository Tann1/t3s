#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QTextStream>
#include <iostream>

#define STR_EQUAL 0

QTextStream out{stdout};
QFileInfo fileinfo {QString("user_loginx.txt")};
QByteArray read_line;
QList<QByteArray> user_fields;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle(QString("MVP"));
    ui->stackedWidget->setCurrentWidget(ui->login);

    define_interaction_handlers();

    menu = new Menu();
    cart = new Cart();
    customer = new Customer();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete menu;
    delete cart;
    delete customer;
}

void MainWindow::define_interaction_handlers()
{
    connect(ui->btn_login, &QPushButton::clicked, this, &MainWindow::handle_login);
    connect(ui->btn_signup, &QPushButton::clicked, this, &MainWindow::handle_signup);
    connect(ui->btn_confirm_signup, &QPushButton::clicked, this, &MainWindow::handle_customer_creation);
    connect(ui->prev_recipe_btn, &QPushButton::clicked, this, &MainWindow::handle_prev_recipe);
    connect(ui->next_recipe_btn, &QPushButton::clicked, this, &MainWindow::handle_next_recipe);
    connect(ui->add_to_cart_btn, &QPushButton::clicked, this, &MainWindow::handle_add_to_cart);
    connect(ui->shoppingcart_btn, &QPushButton::clicked, this, &MainWindow::handle_shopping_cart_press);
    connect(ui->cart_to_home_btn, &QPushButton::clicked, this, &MainWindow::handle_home_press);
    connect(ui->customer_logout, &QPushButton::clicked, this, &MainWindow::handle_logout);

    //admin page
    connect(ui->update_menu_btn, &QPushButton::clicked, this, &MainWindow::handle_update_menu_press);
    connect(ui->admin_page_back_btn, &QPushButton::clicked, this, &MainWindow::admin_page);
    connect(ui->admin_page_back_btn_2, &QPushButton::clicked, this, &MainWindow::admin_page);
    connect(ui->admin_page_back_btn_3, &QPushButton::clicked, this, &MainWindow::admin_page);
    connect(ui->add_recipe_btn,&QPushButton::clicked, this, &MainWindow::handle_add_recipe_press);
    connect(ui->view_customers_btn,&QPushButton::clicked, this, &MainWindow::handle_view_customers_press);
    connect(ui->admin_logout, &QPushButton::clicked, this, &MainWindow::handle_logout);
}

void MainWindow::handle_login()
{
    QString username = ui->input_username->text();
    QString password = ui->input_password->text();

    bool root_login = QString::compare(username, QString("root")) == STR_EQUAL && QString::compare(password, QString("root")) == STR_EQUAL;


    if (root_login) {

        ui->stackedWidget->setCurrentWidget(ui->admin);
    }
    if (customer->login_authenticate(username, password)) {
        menu_item_t menu_item = menu->get_curr_menu_item();
        update_recipe_menu(menu_item);
        ui->stackedWidget->setCurrentWidget((ui->home));
    }

}

void MainWindow::handle_signup()
{
    ui->stackedWidget->setCurrentWidget(ui->signup);
}

void MainWindow::update_recipe_menu(menu_item_t menu_item) {
    ui->recipe_title_label->setText(menu_item.title);
    ui->description_label->setText(menu_item.description);
    ui->price_label->setText(menu_item.price);

}

void MainWindow::handle_customer_creation()
{
    QByteArray username = ui->input_signup_username->text().toUtf8();
    QByteArray email = ui->input_signup_email->text().toUtf8();
    QByteArray password = ui->input_signup_password->text().toUtf8();
    QByteArray password_cpy = ui->input_signup_password_cpy->text().toUtf8();
    QByteArray address = ui->input_signup_address->text().toUtf8();

    customer_s new_customer;
    new_customer.username = username;
    new_customer.email = email;
    new_customer.password = password;
    new_customer.address = address;

       //open file then store

    if (customer->validate_new_customer(new_customer, password_cpy)) {
        customer->add_customers(new_customer);
        ui->stackedWidget->setCurrentWidget(ui->login);
    }
}

void MainWindow::handle_next_recipe()
{
    menu_item_t menu_item = menu->get_next_menu_item();
    update_recipe_menu(menu_item);
}

void MainWindow::handle_prev_recipe()
{
    menu_item_t menu_item = menu->get_prev_menu_item();
    update_recipe_menu(menu_item);
}

void MainWindow::handle_add_to_cart()
{

    menu_item_t menu_item = menu->get_curr_menu_item();
    cart->add_to_cart(menu_item);

}

void MainWindow::handle_shopping_cart_press()
{
    populate_cart_table();
    ui->stackedWidget->setCurrentWidget(ui->checkout);
}

void MainWindow::handle_home_press()
{
    ui->stackedWidget->setCurrentWidget(ui->home);
}

void MainWindow::populate_cart_table()
{
    QList<menu_item_t> *cart_items = cart->get_cart_items();
    ui->cart_table->setRowCount(cart_items->length());
    menu_item_t curr_item;

    for (int i = 0; i < cart_items->length(); ++i) {
        curr_item = cart_items->value(i);
        ui->cart_table->setItem(i, 0, new QTableWidgetItem(QString(curr_item.title)));
        ui->cart_table->setItem(i, 1, new QTableWidgetItem(QString(curr_item.price)));
    }
    delete cart_items;
}

void MainWindow::handle_update_menu_press()
{
    ui->stackedWidget->setCurrentWidget(ui->update_menu);
}

void MainWindow::admin_page()
{
    ui->stackedWidget->setCurrentWidget(ui->admin);
}

void MainWindow::handle_add_recipe_press()
{
    ui->stackedWidget->setCurrentWidget(ui->add_recipe);
}

void MainWindow::handle_view_customers_press()
{
    ui->stackedWidget->setCurrentWidget(ui->view_customers);
}

void MainWindow::handle_logout()
{
    while(ui->cart_table->rowCount() > 0)
        ui->cart_table->removeRow(0);
    ui->input_password->setText(QString(""));
    ui->input_username->setText(QString(""));
    ui->stackedWidget->setCurrentWidget(ui->login);
}



