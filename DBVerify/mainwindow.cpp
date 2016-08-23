#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->refreshTables(true,true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnAddDbitem_clicked()
{
    DbitemDialog dlg(this,false);
    if(QDialog::Accepted==dlg.exec())
    {

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

}

void MainWindow::refreshTables(bool db,bool leak)
{

}
