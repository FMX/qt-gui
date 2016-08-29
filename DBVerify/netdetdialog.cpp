#include "netdetdialog.h"
#include "ui_netdetdialog.h"
#include "dbitemdialog.h"
#include <QMessageBox>
#include "ping.h"
#include <QStringList>
#include "netdetthread.h"
NetdetDialog::NetdetDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::NetdetDialog)
{
    ui->setupUi(this);
    this->setupTable();
    ui->lnEdtNetworkSegment->setToolTip(QString("输入网段即可，如192.168.30.*"));
    ui->lnEdtNetworkSegment->setText(QString("192.168.30.*"));
    ui->progressBar->setRange(0,255);
    ui->progressBar->setValue(0);
}

NetdetDialog::~NetdetDialog()
{
    delete ui;
}


void NetdetDialog::on_btnConfirm_clicked()
{
    this->accept();
}

void NetdetDialog::on_btnCancel_clicked()
{
    this->reject();
}

void NetdetDialog::on_btnScan_clicked()
{
    if(!thread)
    {
        thread=new NetdetThread(this->ui->lnEdtNetworkSegment->text());

    }
    else
    {
        ;
    }

    thread->start();
    connect(thread,&NetdetThread::inforProcess,this,&NetdetDialog::on_recvprocess);
    connect(thread,&NetdetThread::insertItem,this,&NetdetDialog::on_insert);

    this->ui->btnScan->setEnabled(false);
}

void NetdetDialog::setupTable()
{
    QStringList lst;
    lst.append(QString("IP ADDRESS"));
    this->ui->tbvFound->setColumnCount(1);
    this->ui->tbvFound->setHorizontalHeaderLabels(lst);
    this->ui->tbvFound->setSelectionMode(QAbstractItemView::SingleSelection);
    ui->tbvFound->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tbvFound->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tbvFound->horizontalHeader()->setStretchLastSection(true);
    ui->tbvFound->setContextMenuPolicy(Qt::CustomContextMenu);
}

void NetdetDialog::addItem(QString buf)
{
    int rowIndex= ui->tbvFound->rowCount();
    ui->tbvFound->setRowCount(rowIndex+1);
    QTableWidgetItem *item=new QTableWidgetItem(buf);
    ui->tbvFound->setItem(rowIndex,0,item);
    qDebug()<<buf<<endl;
}

void NetdetDialog::on_recvprocess(int val)
{
    this->ui->progressBar->setValue(val);
}

void NetdetDialog::on_insert(QString buf)
{
    this->addItem(buf);
}

void NetdetDialog::on_finishthread()
{
    this->ui->btnScan->setEnabled(true);
}
