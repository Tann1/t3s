#include "cart.h"

Cart::Cart()
{
    this->curr_cart = new QList<menu_item_t>;
}

Cart::~Cart()
{
    delete this->curr_cart;
}


void Cart::add_to_cart(menu_item_t item)
{
    QTextStream out{stdout};
    if (curr_cart != nullptr) {
        out << item.title << " " << item.description << " " << item.price << "\n";
        curr_cart->push_back(item);
    }
}

QList<menu_item_t> *Cart::get_cart_items()
{
    QList<menu_item_t> *cart_list = new QList<menu_item_t>();

    for (int i = 0; i < this->curr_cart->length(); i++)
        cart_list->push_back(this->curr_cart->value(i));
    return cart_list;
}

double Cart::get_total_price()
{
    double total_price = 0;

    for (int i = 0; i < this->curr_cart->length(); i++)
        total_price += QString(this->curr_cart->value(i).price).toDouble();
    return total_price;
}

