#ifndef DATABASEOPERATOR_H
#define DATABASEOPERATOR_H
#include <QString>
#include <QDebug>
#include <QSqlDatabase>
#include <QSqlQuery>

#include "databaseinfoitem.h"
#include "leakinfoitem.h"
#include <QVector>
#include <QList>

template<typename T>
class DataBaseOperator
{
private:
    QString fname;
public:
    DataBaseOperator();
    void setFilename(QString filename);
    T getOneItemById(int id);
    QList<T> getItems();
    void saveOneItem(T item);
};


template <typename T>
DataBaseOperator<T>::DataBaseOperator()
{

}


template <typename T>
void DataBaseOperator<T>::setFilename(QString filename)
{

}

template <typename T>
QList<T> DataBaseOperator<T>::getItems()
{
    return nullptr;
}

template <typename T>
T DataBaseOperator<T>::getOneItemById(int id)
{
    return nullptr;
}

template <typename T>
void DataBaseOperator<T>::saveOneItem(T item)
{

}


#endif // DATABASEOPERATOR_H
