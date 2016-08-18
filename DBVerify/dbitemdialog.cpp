#include "dbitemdialog.h"
#include "ui_dbitemdialog.h"

DbitemDialog::DbitemDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DbitemDialog)
{
    ui->setupUi(this);
}

DbitemDialog::~DbitemDialog()
{
    delete ui;
}
