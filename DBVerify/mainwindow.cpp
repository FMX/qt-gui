#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "verifydialog.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    userOpt=(databaseFactory::buildDataBaseSourceForUser());
    predbOpt=(databaseFactory::buildDatabaseForPreset());

    this->initDbtable();
    this->initLeaktable();
}

MainWindow::~MainWindow()
{
    delete ui;
    if(modifyAction!=nullptr)
    {
        modifyAction->disconnect(SIGNAL(triggered()));
        delete modifyAction;
    }
    if(delteAction!=nullptr)
    {
        delteAction->disconnect(SIGNAL(triggered()));
        delete delteAction;
    }
}

void MainWindow::on_btnAddDbitem_clicked()
{
    DbitemDialog dlg(this,false);
    if(QDialog::Accepted==dlg.exec())
    {
        this->refreshTables(true,false);
    }
}

void MainWindow::on_btnNetdet_clicked()
{
    NetdetDialog dlg;
    if(QDialog::Accepted==dlg.exec())
    {

    }
}

void MainWindow::on_btnVerify_clicked()
{
    VerifyDialog dlg;
    dlg.setDindex(ui->tbvDbitems->currentIndex().row(),ui->tbvLeaks->currentIndex().row());
    if(dlg.exec()==QDialog::Accepted)
    {

    }
}

void MainWindow::refreshTables(bool db,bool leak)
{
    if(db)
        this->refreshDbTable();
    if(leak)
        this->refreshLeakTable();
}

void MainWindow::refreshDbTable()
{
    dbsLst=this->userOpt->getAll();
}

void MainWindow::refreshLeakTable()
{

}
void MainWindow::initDbtable()
{
    ui->tbvDbitems->setSelectionMode(QAbstractItemView::SelectionMode::SingleSelection);
    ui->tbvDbitems->setColumnCount(4);
    QStringList header;
    header.append("数据库名称");
    header.append("IP 地址");
    header.append("数据库类型");
    header.append("操作系统类型");
    ui->tbvDbitems->setHorizontalHeaderLabels(header);
    ui->tbvDbitems->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tbvDbitems->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tbvDbitems->setContextMenuPolicy(Qt::CustomContextMenu);
    ui->tbvDbitems->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
    ui->tbvDbitems->horizontalHeader()->setStretchLastSection(true);

    //    ui->tbvDbitems->customContextMenuRequested.connect(this->dbtMenu);
    //    connect(ui->tbvDbitems->customContextMenuRequested,this->dbtMenu);

    modifyAction= dbtMenu.addAction("修改");

    delteAction=dbtMenu.addAction("删除");

    connect(modifyAction,SIGNAL(triggered()),this,SLOT(on_modify_activated()));
    connect(delteAction,SIGNAL(triggered()),this,SLOT(on_delete_activated()));

    dbsLst=userOpt->getAll();
    int rowcount=0;
    ui->tbvDbitems->setRowCount(dbsLst.size());
    foreach (DatabaseInfoItem item, dbsLst)
    {
        //        ui->tbvDbitems->setRowCount(rowcount);
        ui->tbvDbitems->setItem(rowcount,0,new QTableWidgetItem(item.getDbname()));
        ui->tbvDbitems->setItem(rowcount,1,new QTableWidgetItem(item.getDbip()));
        ui->tbvDbitems->setItem(rowcount,2,new QTableWidgetItem(ConverUtil::TypeToString(item.getDbtype())));
        ui->tbvDbitems->setItem(rowcount,3,new QTableWidgetItem(ConverUtil::TypeToString(item.getOstype())));
        rowcount++;
    }

}

void MainWindow::initLeaktable()
{
    ui->tbvLeaks->setSelectionMode(QAbstractItemView::SelectionMode::SingleSelection);
    ui->tbvLeaks->setColumnCount(4);
    QStringList header;
    header.append("漏洞名称");
    header.append("数据库类型");
    header.append("操作系统类型");
    header.append("是否需要密码");
    ui->tbvLeaks->setHorizontalHeaderLabels(header);
    ui->tbvLeaks->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tbvLeaks->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tbvLeaks->setContextMenuPolicy(Qt::CustomContextMenu);
    ui->tbvLeaks->horizontalHeader()->setStretchLastSection(true);

    leakLst=predbOpt->getAll();
    int rowcount=0;
    ui->tbvLeaks->setRowCount(leakLst.size());
    foreach(LeakinfoItem item,leakLst)
    {
        ui->tbvLeaks->setItem(rowcount,0,new QTableWidgetItem(item.getLeakname()));
        ui->tbvLeaks->setItem(rowcount,1,new QTableWidgetItem(ConverUtil::TypeToString(item.getDbtypes(),item.getDbtype())));
        ui->tbvLeaks->setItem(rowcount,2,new QTableWidgetItem(ConverUtil::TypeToString(item.getOstypecnt(),item.getOstype())));
        ui->tbvLeaks->setItem(rowcount++,3,new QTableWidgetItem(ConverUtil::ReqpwdToString(item.getReqpwd())));
    }

}

void MainWindow::on_tbvDbitems_customContextMenuRequested(const QPoint &pos)
{
    dbtMenu.exec(QCursor::pos());
}

void MainWindow::on_modify_activated()
{
    DbitemDialog dlg(this,true);
    dlg.modifyItem(this->dbsLst.at(ui->tbvDbitems->currentIndex().row()));

    if(QDialog::Accepted==dlg.exec())
    {
        this->refreshTables(true,false);
    }


}

void MainWindow::on_delete_activated()
{
    qDebug()<<"Delete One Item!"<<endl;

}
