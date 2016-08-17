#ifndef LEAKTOOLDIALOG_H
#define LEAKTOOLDIALOG_H

#include <QDialog>
#include <QSqlDatabase>
#include <QSqlDriver>
#include <QString>
#include <QFileDialog>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QDebug>
#include <iostream>

namespace Ui {
class LeakToolDialog;
}

class LeakToolDialog : public QDialog
{
    Q_OBJECT

public:
    explicit LeakToolDialog(QWidget *parent = 0);
    ~LeakToolDialog();

private slots:
    void on_pushButton_clicked();

private:
    Ui::LeakToolDialog *ui;
    QSqlDatabase *database;
    QString filename;
    QFileDialog *dlg;

};

#endif // LEAKTOOLDIALOG_H
