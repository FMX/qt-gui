#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "leaktooldialog.h"
#include <qmessagebox.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    LeakToolDialog *dlg=new LeakToolDialog();
    if(dlg->exec()==QDialog::Accepted)
    {
        QMessageBox *msg=new QMessageBox();
        msg->show();
    }
    else
    {

        exit(0);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
