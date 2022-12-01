#include "customer.h"

Customer::Customer()
{
    QTextStream out{stdout};
    QFileInfo fileinfo {QString("user_logins.txt")};
    QByteArray read_line;
    QList<QByteArray> customer_fields;
    customer_s curr_customer;



    this->file_path = fileinfo.absoluteFilePath();
    this->customer_file = new QFile(this->file_path);
    this->customers = new QList<customer_s>();

    if (this->customer_file->open(QIODevice::ReadOnly)) {
        out << "Customer file open success\n";
        while (!this->customer_file->atEnd()) {
            read_line = this->customer_file->readLine();
            customer_fields = read_line.split('|');
            curr_customer.username = customer_fields[0];
            curr_customer.email = customer_fields[1];
            curr_customer.password = customer_fields[2];
            curr_customer.address = customer_fields[3];
            this->customers->push_back(curr_customer);
        }

    }

    this->customer_file->close();
}


Customer::~Customer()
{
    this->customer_file->close();
    delete this->customer_file;
    delete this->customers;
    delete this->curr_customer;
}

void Customer::add_customers(customer_s new_customer)
{
    QTextStream out{this->customer_file};
    QString customer_data;
    if (this->customer_file->open(QIODevice::Append)) {
        customer_data.append(QString(new_customer.username.data()));
        customer_data.append("|");
        customer_data.append(QString(new_customer.email.data()));
        customer_data.append("|");
        customer_data.append(QString(new_customer.password.data()));
        customer_data.append("|");
        customer_data.append(QString(new_customer.address.data()));

        out << customer_data << "\n";
        this->customers->push_back(new_customer);
        this->customer_file->close();
    }

}

bool Customer::validate_new_customer(customer_s new_customer, QByteArray cpy_pass)
{
    bool input_there = new_customer.username.size() != 0 && new_customer.email.size() != 0 && new_customer.password.size() != 0 && new_customer.address.size() != 0;
    bool passwords_match = QString::compare(cpy_pass, new_customer.password) == STR_EQUAL;

    return input_there && passwords_match;
}

bool Customer::login_authenticate(QString username, QString inputted_password)
{
    QTextStream out{stdout};

    this->curr_customer = find_user(username);
    if (this->curr_customer == nullptr)
        return false;
    QString stored_pass(this->curr_customer->password.data());


    if (QString::compare(stored_pass, inputted_password) == STR_EQUAL) {
        return true;
    }
    return false;

}

customer_s* Customer::find_user(QString username)
{
    customer_s curr_customer;
    customer_s *result;

    if (this->customers == nullptr)
        return nullptr;
    for (int i = 0; i < this->customers->length(); ++i) {
        curr_customer = this->customers->value(i);
        if (username.toUtf8() == curr_customer.username) {
            result = new customer_s;
            result->username = curr_customer.username;
            result->email = curr_customer.email;
            result->password = curr_customer.password;
            result->address = curr_customer.address;
            return result;
        }
    }

    return nullptr;
}
