#include "presetdboperator.h"

PresetdbOperator::PresetdbOperator()
{
    this->database=QSqlDatabase::addDatabase("SQLITE");
    this->database.setDatabaseName(("preset.db"));
    if(!this->database.open())
    {
        QMessageBox msg;
        msg.warning(nullptr,QString("数据库丢失"),QString("数据库打开异常"));

    }
    else
    { }
}

LeakinfoItem PresetdbOperator::getOneById(int id)
{
    LeakinfoItem item;
    QSqlQuery query;
    QString query_sql="select * from dbs where id = ?";
    query.prepare(query_sql);
    query.addBindValue(id);
    if(!query.exec()){

    }else{

    }

    return item;
}

QList<LeakinfoItem> PresetdbOperator::getAll()
{

}

void PresetdbOperator::saveOne(LeakinfoItem item)
{

}

void PresetdbOperator::saveAll(QList<LeakinfoItem> lst)
{
    QString insert_sql="INSERT into dbs (dbname,dbip,dbtype,dbversion,ostype,osversion,"
                       "dbport,orasid,username,userpwd) VALUES (?,?,?,?,?,?,?,?,?,?);";
    QSqlQuery query;
    query.prepare(insert_sql);


    if(!query.exec())
    {
        qDebug()<< query.lastError().text();
    }
    else
    { //operation complete.

    }
}

void PresetdbOperator::updateOneByid(int id,LeakinfoItem item)
{

}
