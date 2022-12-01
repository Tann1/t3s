#include "Menu.h"
#include <QList>
#include <QTextStream>

Menu::Menu()
{
    QTextStream out{stdout};
    QFileInfo fileinfo {QString("recipes.txt")};
    QByteArray read_line;
    QList<QByteArray> menu_fields;
    menu_item_t curr_menu_item;



    this->file_path = fileinfo.absoluteFilePath();
    this->recipe_file = new QFile(this->file_path);
    this->menu_items = new QList<menu_item_t>();

    if (this->recipe_file->open(QIODevice::ReadOnly)) {
        out << "Recipe file open success\n";
        while (!this->recipe_file->atEnd()) {
            read_line = this->recipe_file->readLine();
            menu_fields = read_line.split('|');
            curr_menu_item.title = menu_fields[0];
            curr_menu_item.description = menu_fields[1];
            curr_menu_item.price = menu_fields[2];
            add_menu(curr_menu_item);
        }
        this->curr_menu = 0;
    }

    this->recipe_file->close();
}

Menu::~Menu()
{
    delete this->recipe_file;
    delete this->menu_items;
}


void Menu::add_menu(menu_item_t new_item)
{
    this->menu_items->push_back(new_item);
}

void Menu::add_menu_to_file(menu_item_t item)
{
    QTextStream out{this->recipe_file};
    QString data{item.title};

    data.append('|');
    data.append(item.description);
    data.append('|');
    data.append(item.price);

    if (this->recipe_file->open(QIODevice::Append)) {
        out << data << "\n";
    }
    this->recipe_file->close();
}

menu_item_t Menu::get_curr_menu_item() {
    return this->menu_items->value(curr_menu);
}

menu_item_t Menu::get_next_menu_item() {
    this->curr_menu++;
    this->curr_menu = this->curr_menu % this->menu_items->length();

    return this->menu_items->value(curr_menu);
}

menu_item_t Menu::get_prev_menu_item() {
    this->curr_menu--;
    if (this->curr_menu < 0)
        this->curr_menu = this->menu_items->length() - 1;
    return this->menu_items->value(curr_menu);
}
