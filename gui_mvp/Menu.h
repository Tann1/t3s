#ifndef MENU_H
#define MENU_H



#include <QString>
#include <QFile>
#include <QByteArray>
#include <QFileInfo>
#include <QList>

typedef struct {
    QByteArray title;
    QByteArray description;
    QByteArray price;
} menu_item_t;

class Menu {
public:
    Menu();
    ~Menu();

    void add_menu(menu_item_t new_item);
    void add_menu_to_file(menu_item_t item);
    menu_item_t get_curr_menu_item();
    menu_item_t get_next_menu_item();
    menu_item_t get_prev_menu_item();

private:
    QFile *recipe_file;
    QList<menu_item_t> *menu_items;
    QString file_path;
    qsizetype curr_menu;
};


#endif // MENU_H
