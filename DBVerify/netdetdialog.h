#ifndef NETDETDIALOG_H
#define NETDETDIALOG_H

#include <QDialog>
#include "netdetthread.h"


namespace Ui {
class NetdetDialog;
}

class NetdetDialog : public QDialog
{
    Q_OBJECT

public:
    explicit NetdetDialog(QWidget *parent = 0);
    ~NetdetDialog();

    void setupTable();

    void addItem(QString buf);

private slots:

    void on_btnConfirm_clicked();

    void on_btnCancel_clicked();

    void on_btnScan_clicked();

    void on_recvprocess(int val);

    void on_insert(QString buf);

    void on_finishthread();
private:
    Ui::NetdetDialog *ui;
    NetdetThread *thread;
};

#endif // NETDETDIALOG_H
