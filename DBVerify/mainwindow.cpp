#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setUpTables();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnAddDbitem_clicked()
{

}

void MainWindow::on_btnNetdet_clicked()
{

}

void MainWindow::on_btnVerify_clicked()
{

}

void MainWindow::setUpTables()
{

}
