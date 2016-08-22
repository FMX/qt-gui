#ifndef PRESETDBOPERATOR_H
#define PRESETDBOPERATOR_H
#include <leakinfoitem.h>
#include <QList>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QMessageBox>
#include <QVariant>
#include <QSqlError>
#include <QDebug>

class PresetdbOperator
{
private:
    QSqlDatabase database;
public:
    PresetdbOperator();
    LeakinfoItem getOneById(int id);
    QList<LeakinfoItem> getAll();
    void saveOne(LeakinfoItem item);
    void saveAll(QList<LeakinfoItem> lst);
    void updateOneByid(int id,LeakinfoItem item);

};

#endif // PRESETDBOPERATOR_H
