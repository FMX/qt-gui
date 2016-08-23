#include "presetdboperator.h"

PresetdbOperator::PresetdbOperator()
{
    this->database=QSqlDatabase::addDatabase("QSQLITE","qt-presetdb-con");
    QString path=QDir::currentPath();
    path.append(QDir::separator());
    path.append("preset.db");
    this->database.setDatabaseName(path);
    if(!this->database.open())
    {
        QMessageBox msg;
        msg.warning(nullptr,QString("数据库丢失"),QString("数据库打开异常"));
        qDebug()<< this->database.lastError()<<endl;
    }
    else
    {

    }
}

LeakinfoItem PresetdbOperator::getOneById(int id)
{
    LeakinfoItem item;
    QSqlQuery query(this->database);
    QString query_sql="select * from leaks where id = ?";
    query.prepare(query_sql);
    query.addBindValue(id);
    if(!query.exec()){

    }else{
        item.setId(query.value("id").toInt());
        item.setLeakname(query.value("leakname").toString());
        item.setCvename(query.value("leakdesc").toString());
        item.setDbtypes(query.value("dbtypes").toInt());
        item.setDbtype(query.value("dbtype").toString());
        item.setDbversion(query.value("dbversion").toString());
        item.setOstypecnt(query.value("ostypeCnt").toInt());
        item.setOstype(query.value("ostype").toString());
        item.setOsversion(query.value("osversion").toString());
        item.setReqpwd(query.value("reqpwd").toInt());
        item.setModulename(query.value("scriptname").toString());
    }

    return item;
}

QList<LeakinfoItem> PresetdbOperator::getAll()
{
    QList<LeakinfoItem> lst;
    QSqlQuery query(this->database);
    if(query.exec(QString("select * from leaks")))
    {
        while(query.next())
        {
            LeakinfoItem item;
            item.setId(query.value("id").toInt());
            item.setLeakname(query.value("leakname").toString());
            item.setCvename(query.value("leakdesc").toString());
            item.setDbtypes(query.value("dbtypes").toInt());
            item.setDbtype(query.value("dbtype").toString());
            item.setDbversion(query.value("dbversion").toString());
            item.setOstypecnt(query.value("ostypeCnt").toInt());
            item.setOstype(query.value("ostype").toString());
            item.setOsversion(query.value("osversion").toString());
            item.setReqpwd(query.value("reqpwd").toInt());
            item.setModulename(query.value("scriptname").toString());
            lst.append(item);
        }
    }
    else
    {

    }
    return lst;
}

void PresetdbOperator::saveOne(LeakinfoItem item)
{
    QString insert_sql="INSERT INTO leaks ( leakname, cvename, leakdesc,"
                       " dbtypes, dbtype, dbversion, ostypeCnt, ostype, "
                       "osversion, reqpwd, scriptname)"
                       " VALUES (?,?,?,?,?,?,?,?,?,?,?):";
    QSqlQuery query(this->database);
    query.prepare(insert_sql);
    query.addBindValue(item.getLeakname());
    query.addBindValue(item.getCvename());
    query.addBindValue(item.getLeakdesc());
    query.addBindValue(item.getDbtypes());
    query.addBindValue(item.getDbtype());
    query.addBindValue(item.getDbversion());
    query.addBindValue(item.getOstypecnt());
    query.addBindValue(item.getOstype());
    query.addBindValue(item.getOsversion());
    query.addBindValue(item.getReqpwd());
    query.addBindValue(item.getModulename());

    if(!query.exec())
    {
        qDebug()<< query.lastError().text();
    }
    else
    { //operation complete.

    }
}

void PresetdbOperator::saveAll(QList<LeakinfoItem> lst)
{
    QString insert_sql="INSERT INTO leaks ( leakname, cvename, leakdesc,"
                       " dbtypes, dbtype, dbversion, ostypeCnt, ostype, "
                       "osversion, reqpwd, scriptname)"
                       " VALUES (?,?,?,?,?,?,?,?,?,?,?):";

    QList<LeakinfoItem>::const_iterator ite=lst.constBegin();
    for(ite;ite!=lst.constEnd();++ite)
    {

        LeakinfoItem item=(*ite);

        QSqlQuery query(this->database);
        query.prepare(insert_sql);
        query.addBindValue(item.getLeakname());
        query.addBindValue(item.getCvename());
        query.addBindValue(item.getLeakdesc());
        query.addBindValue(item.getDbtypes());
        query.addBindValue(item.getDbtype());
        query.addBindValue(item.getDbversion());
        query.addBindValue(item.getOstypecnt());
        query.addBindValue(item.getOstype());
        query.addBindValue(item.getOsversion());
        query.addBindValue(item.getReqpwd());
        query.addBindValue(item.getModulename());


        if(!query.exec())
        {
            qDebug()<< query.lastError().text();
        }
        else
        { //operation complete.
            qDebug()<<query.lastError().text()<<endl;
        }

    }
}

void PresetdbOperator::updateOneByid(int id,LeakinfoItem item)
{
    QString update_sql="UPDATE leaks SET leakname=?, cvename=?,"
                       " leakdesc=?, dbtypes=?, dbtype=?, dbversion=?, "
                       "ostypeCnt=?, ostype=?, osversion=?, reqpwd=?,"
                       " scriptname=? WHERE id=?;";
    QSqlQuery query(this->database);
    query.prepare(update_sql);
    query.addBindValue(item.getLeakname());
    query.addBindValue(item.getCvename());
    query.addBindValue(item.getLeakdesc());
    query.addBindValue(item.getDbtypes());
    query.addBindValue(item.getDbtype());
    query.addBindValue(item.getDbversion());
    query.addBindValue(item.getOstypecnt());
    query.addBindValue(item.getOstype());
    query.addBindValue(item.getOsversion());
    query.addBindValue(item.getReqpwd());
    query.addBindValue(item.getModulename());
    query.addBindValue(item.getId());

    if(!query.exec())
    {
        qDebug()<<query.lastError().text()<<endl;
    }
    else
    {

    }

}


void PresetdbOperator::removeByid(int id)
{
    QSqlQuery query(this->database);
    QString remove_sql="delete from leaks where id = ?;";
    query.addBindValue(id);
    if(!query.exec())
    {
        qDebug()<<query.lastError().text()<<endl;
    }
    else
    {

    }
}


