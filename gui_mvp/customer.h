#ifndef CUSTOMER_H
#define CUSTOMER_H


#include <QString>
#include <QFile>
#include <QByteArray>
#include <QFileInfo>
#include <QList>

#define STR_EQUAL 0

typedef struct {
    QByteArray username;
    QByteArray email;
    QByteArray password;
    QByteArray address;
} customer_s;

class Customer
{
public:
    Customer();
    ~Customer();

    void add_customers(customer_s new_customer);
    bool validate_new_customer(customer_s new_customer, QByteArray cpy_pass);
    bool login_authenticate(QString username, QString inputted_password);
    const QList<customer_s> *get_customers();

private:
    QFile *customer_file;
    QList<customer_s> *customers;
    QString file_path;
    customer_s* curr_customer;

    customer_s* find_user(QString username);
};

#endif // CUSTOMER_H
