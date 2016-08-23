#ifndef DBITEMDIALOG_H
#define DBITEMDIALOG_H

#include <QDialog>
#include <databaseinfoitem.h>
#include "databasefactory.h"

namespace Ui {
class DbitemDialog;
}

class DbitemDialog : public QDialog
{
    Q_OBJECT

public:
    explicit DbitemDialog(QWidget *parent = 0,bool modify=false);
    ~DbitemDialog();

    void initForModify();
    void initForAdd();

    void modifyItem(DatabaseInfoItem item);

    DatabaseInfoItem getNewItem();


private slots:
    void on_btnConfirm_clicked();

    void on_btnCancel_clicked();

    void on_cmbDbtype_activated(int index);

    void on_cmbOstype_activated(int index);

private:
    Ui::DbitemDialog *ui;
    bool isModify=false;
    int id;
};

#endif // DBITEMDIALOG_H
