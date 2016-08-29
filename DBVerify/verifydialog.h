#ifndef VERIFYDIALOG_H
#define VERIFYDIALOG_H

#include <QDialog>
#include "databasefactory.h"
#include "databaseinfoitem.h"
#include "leakinfoitem.h"

namespace Ui {
class VerifyDialog;
}

class VerifyDialog : public QDialog
{
    Q_OBJECT

public:
    explicit VerifyDialog(QWidget *parent = 0);
    ~VerifyDialog();
    void setDindex(int did,int lid);
    void loadinfos();
private slots:
    void on_btnConfirm_clicked();

private:
    Ui::VerifyDialog *ui;
    int dbix;
    int lkix;
    DatabaseInfoItem dbitem;
    LeakinfoItem leakitem;

};

#endif // VERIFYDIALOG_H
