#ifndef DATABASEOPERATOR_H
#define DATABASEOPERATOR_H
#include <QString>

class DataBaseOperator
{
private:
    QString *fname=nullptr;
public:
    DataBaseOperator(QString filename);
};

#endif // DATABASEOPERATOR_H
