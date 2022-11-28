#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "Menu.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();



private:
    Ui::MainWindow *ui;
    Menu *menu;

    void define_interaction_handlers();
    void update_recipe_menu(menu_item_t menu_item);

private slots:
    void handle_login();
    void handle_signup();
    void handle_customer_creation();
    void handle_prev_recipe();
    void handle_next_recipe();
};
#endif // MAINWINDOW_H
