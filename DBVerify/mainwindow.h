#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "dbitemdialog.h"
#include "netdetdialog.h"
#include "databasefactory.h"
#include "presetdboperator.h"
#include "userdboperator.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

private:
    PresetdbOperator *predbOpt=nullptr;
    UserdbOperator *userOpt=nullptr;
    void refreshTables(bool db,bool leak);


public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_btnAddDbitem_clicked();

    void on_btnNetdet_clicked();

    void on_btnVerify_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
