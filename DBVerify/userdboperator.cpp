#include "userdboperator.h"

UserdbOperator::UserdbOperator()
{
    //    qDebug()<<"SQLite Initlized!";

    this->database=QSqlDatabase::addDatabase("QSQLITE","qt-user-dbconn");
    QString path=QDir::currentPath();
    path.append(QDir::separator());
    path.append("user.db");
    this->database.setDatabaseName(path);
    if(!this->database.open())
    {
        QMessageBox msg;
        msg.warning(nullptr,QString("数据库丢失"),QString("数据库打开异常"));
        qDebug()<<this->database.lastError().text()<<endl;
    }
    else
    {
    }
}

DatabaseInfoItem UserdbOperator::getOneByid(int id)
{
    DatabaseInfoItem item;
    QSqlQuery query(this->database);
    QString query_sql="select * from dbs where id = ?";
    query.prepare(query_sql);
    query.addBindValue(id);
    if(!query.exec()){

    }else{
        item.setId(query.value("id").toInt());
        item.setDbname(query.value("dbname").toString());
        item.setDbip(query.value("dbip").toString());
        item.setDbtype(query.value("dbtype").toInt());
        item.setDbversion(query.value("dbversion").toString());
        item.setOstype(query.value("ostype").toInt());
        item.setOsversion(query.value("osversion").toString());
        item.setDbport(query.value("dbport").toInt());
        item.setOrasid(query.value("orasid").toString());
        item.setUsername(query.value("username").toString());
        item.setUserpwd(query.value("userpwd").toString());
    }

    return item;
}

QList<DatabaseInfoItem> UserdbOperator::getAll()
{
    QList<DatabaseInfoItem> lst;
    QSqlQuery query(this->database);
    if(query.exec(QString("select * from dbs;")))
    {
        while(query.next())
        {
            DatabaseInfoItem item;
            item.setId(query.value("id").toInt());
            item.setDbname(query.value("dbname").toString());
            item.setDbip(query.value("dbip").toString());
            item.setDbtype(query.value("dbtype").toInt());
            item.setDbversion(query.value("dbversion").toString());
            item.setOstype(query.value("ostype").toInt());
            item.setOsversion(query.value("osversion").toString());
            item.setDbport(query.value("dbport").toInt());
            item.setOrasid(query.value("orasid").toString());
            item.setUsername(query.value("username").toString());
            item.setUserpwd(query.value("userpwd").toString());

            //qDebug()<<query.ValuesAsColumns<<endl;
            //qDebug()<<query.value("dbname")<<endl;
            lst.append(item);
        }
    }
    else
    {
        qDebug()<<query.lastError().text()<<endl;
    }
    return lst;
}
void UserdbOperator::saveOne(DatabaseInfoItem item)
{
    QString insert_sql="INSERT into dbs (dbname,dbip,dbtype,dbversion,ostype,osversion,"
                       "dbport,orasid,username,userpwd) VALUES (?,?,?,?,?,?,?,?,?,?);";
    QSqlQuery query(this->database);
    query.prepare(insert_sql);
    query.addBindValue(item.getDbname());
    query.addBindValue(item.getDbip());
    query.addBindValue(item.getDbtype());
    query.addBindValue(item.getDbversion());
    query.addBindValue(item.getOstype());
    query.addBindValue(item.getOsversion());
    query.addBindValue(item.getDbport());
    query.addBindValue(item.getOrasid());
    query.addBindValue(item.getUsername());
    query.addBindValue(item.getUserpwd());

    if(!query.exec())
    {
        qDebug()<< query.lastError().text();
    }
    else
    { //operation complete.

    }

}

void UserdbOperator::saveAll(QList<DatabaseInfoItem> lst)
{
    QList<DatabaseInfoItem>::const_iterator ite=lst.constBegin();
    for(ite;ite!=lst.constEnd();++ite)
    {
        DatabaseInfoItem item=(*ite);
        QString insert_sql="INSERT into dbs (dbname,dbip,dbtype,dbversion,ostype,osversion,"
                           "dbport,orasid,username,userpwd) VALUES (?,?,?,?,?,?,?,?,?,?);";
        QSqlQuery query(this->database);
        query.prepare(insert_sql);
        query.addBindValue(item.getDbname());
        query.addBindValue(item.getDbip());
        query.addBindValue(item.getDbtype());
        query.addBindValue(item.getDbversion());
        query.addBindValue(item.getOstype());
        query.addBindValue(item.getOsversion());
        query.addBindValue(item.getDbport());
        query.addBindValue(item.getOrasid());
        query.addBindValue(item.getUsername());
        query.addBindValue(item.getUserpwd());

        if(!query.exec())
        {
            qDebug()<< query.lastError().text();
        }
        else
        { //operation complete.

        }
        query.clear();
    }
}

void UserdbOperator::updateOneByid(int id, DatabaseInfoItem item)
{
    QString update_sql="UPDATE dbs SET dbname=?,dbip=?,"
                       "dbtype=?,dbversion=?,ostype=?,"
                       "osversion=?,dbport=?,orasid=?,"
                       "username=?,userpwd = ?  WHERE  id=?;";

    QSqlQuery query(this->database);
    query.prepare(update_sql);
    query.addBindValue(item.getDbname());
    query.addBindValue(item.getDbip());
    query.addBindValue(item.getDbtype());
    query.addBindValue(item.getDbversion());
    query.addBindValue(item.getOstype());
    query.addBindValue(item.getOsversion());
    query.addBindValue(item.getDbport());
    query.addBindValue(item.getOrasid());
    query.addBindValue(item.getUsername());
    query.addBindValue(item.getUserpwd());
    query.addBindValue(id);

    if(!query.exec())
    {
        qDebug()<< query.lastError().text();
    }
    else
    { //operation complete.

    }
}

void UserdbOperator::removeByid(int id)
{
    QSqlQuery query(this->database);
    QString remove_sql="delete from dbs where id = ?;";
    query.addBindValue(id);
    if(!query.exec())
    {
        qDebug()<<query.lastError().text()<<endl;
    }
    else
    {

    }
}
