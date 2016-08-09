#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "leaktooldialog.h"
#include <QDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    LeakToolDialog *dlg=new LeakToolDialog();
    if(dlg->exec()==QDialog.Accepted)
    {

    }
    else
    {

    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
