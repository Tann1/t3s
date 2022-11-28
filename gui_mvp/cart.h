#ifndef CART_H
#define CART_H

#include "Menu.h"
#include <QList>

class Cart
{
public:
    Cart();
    ~Cart();
    void add_to_cart(menu_item_t item);
    QList<menu_item_t> *get_cart_items();
    double get_total_price();

private:
    QList<menu_item_t> *curr_cart;
    double total_price;
};

#endif // CART_H
