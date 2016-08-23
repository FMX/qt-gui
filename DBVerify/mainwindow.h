#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "dbitemdialog.h"
#include "netdetdialog.h"
#include "databasefactory.h"
#include "presetdboperator.h"
#include "userdboperator.h"
#include <QAbstractTableModel>
#include <QTableWidget>
#include <Qt>
#include <QAction>
#include <QMenu>
#include <QActionEvent>
#include <QTableWidgetItem>
#include "converutil.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

private:
    PresetdbOperator *predbOpt=nullptr;
    UserdbOperator *userOpt=nullptr;

    QList<LeakinfoItem> leakLst;
    QList<DatabaseInfoItem> dbsLst;

    void refreshTables(bool db,bool leak);
    void refreshDbTable();
    void refreshLeakTable();
    void initDbtable();
    void initLeaktable();

    QMenu dbtMenu;
    QAction* modifyAction=nullptr;
    QAction* delteAction=nullptr;


public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_btnAddDbitem_clicked();

    void on_btnNetdet_clicked();

    void on_btnVerify_clicked();

    void on_tbvDbitems_customContextMenuRequested(const QPoint &pos);

    void on_modify_activated();

    void on_delete_activated();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
