#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QTextStream>
#include <iostream>

#define STR_EQUAL 0

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle(QString("MVP"));
    ui->stackedWidget->setCurrentWidget(ui->login);

    define_interaction_handlers();

    menu = new Menu();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete menu;
}

void MainWindow::define_interaction_handlers()
{
    connect(ui->btn_login, &QPushButton::clicked, this, &MainWindow::handle_login);
    connect(ui->btn_signup, &QPushButton::clicked, this, &MainWindow::handle_signup);
    connect(ui->btn_confirm_signup, &QPushButton::clicked, this, &MainWindow::handle_customer_creation);
    connect(ui->prev_recipe_btn, &QPushButton::clicked, this, &MainWindow::handle_prev_recipe);
    connect(ui->next_recipe_btn, &QPushButton::clicked, this, &MainWindow::handle_next_recipe);
}

void MainWindow::handle_login()
{
    QString username = ui->input_username->text();
    QString password = ui->input_password->text();

    bool root_login = QString::compare(username, QString("root")) == STR_EQUAL && QString::compare(password, QString("root")) == STR_EQUAL;

    if (root_login) {
        menu_item_t menu_item = menu->get_curr_menu_item();
        update_recipe_menu(menu_item);
        ui->stackedWidget->setCurrentWidget(ui->home);

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
    QString username = ui->input_signup_username->text();
    QString email = ui->input_signup_email->text();
    QString password = ui->input_signup_password->text();
    QString password_cpy = ui->input_signup_password_cpy->text();
    QString address = ui->input_signup_address->text();

    bool input_there = username.size() != 0 && email.size() != 0 && password.size() != 0 && password_cpy.size() != 0 && password_cpy.size() != 0 && address.size() != 0;
    bool passwords_match = QString::compare(password, password_cpy, Qt::CaseSensitive) == STR_EQUAL;

    if (input_there && passwords_match)
        ui->stackedWidget->setCurrentWidget(ui->login);
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
