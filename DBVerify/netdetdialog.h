#ifndef NETDETDIALOG_H
#define NETDETDIALOG_H

#include <QDialog>

namespace Ui {
class NetdetDialog;
}

class NetdetDialog : public QDialog
{
    Q_OBJECT

public:
    explicit NetdetDialog(QWidget *parent = 0);
    ~NetdetDialog();

private slots:
    void on_pushButton_2_clicked();

    void on_btnConfirm_clicked();

private:
    Ui::NetdetDialog *ui;
};

#endif // NETDETDIALOG_H
