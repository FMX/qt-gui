#include "netdetdialog.h"
#include "ui_netdetdialog.h"
#include "dbitemdialog.h"
#include <QMessageBox>

NetdetDialog::NetdetDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::NetdetDialog)
{
    ui->setupUi(this);
}

NetdetDialog::~NetdetDialog()
{
    delete ui;
}

void NetdetDialog::on_pushButton_2_clicked()
{

}

void NetdetDialog::on_btnConfirm_clicked()
{
    QMessageBox::warning(this,tr("hello world"),tr("you hello"),QMessageBox::Yes);
//    DbitemDialog *dbItmDl=new DbitemDialog();
//    dbItmDl->show();

}
