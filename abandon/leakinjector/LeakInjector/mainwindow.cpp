#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "leaktooldialog.h"
#include <qmessagebox.h>
#include <sqlite3.h>
#include <QSqlDriver>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    LeakToolDialog *dlg=new LeakToolDialog();
    if(dlg->exec()==QDialog::Accepted)
    {
//        QMessageBox *msg=new QMessageBox("","");
//        msg->show();
    }
    else
    {
//        QMessageBox *msg=new QMessageBox("漏洞工具定位失败","没有发现有效的漏洞工具，程序关闭");
//        exit(0);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
