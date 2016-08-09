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
