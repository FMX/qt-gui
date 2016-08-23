#include "dbitemdialog.h"
#include "ui_dbitemdialog.h"

DbitemDialog::DbitemDialog(QWidget *parent,bool modify) :
    QDialog(parent),
    ui(new Ui::DbitemDialog)
{
    ui->setupUi(this);
    if(modify)
        initForModify();
}

DbitemDialog::~DbitemDialog()
{
    delete ui;
}

void DbitemDialog::initForModify()
{

}
