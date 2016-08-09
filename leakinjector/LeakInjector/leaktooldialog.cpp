#include "leaktooldialog.h"
#include "ui_leaktooldialog.h"

LeakToolDialog::LeakToolDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LeakToolDialog)
{
    ui->setupUi(this);
}

LeakToolDialog::~LeakToolDialog()
{
    delete ui;
}

void LeakToolDialog::on_pushButton_clicked()
{
    emit this->accept();
}
