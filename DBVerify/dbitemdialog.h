#ifndef DBITEMDIALOG_H
#define DBITEMDIALOG_H

#include <QDialog>

namespace Ui {
class DbitemDialog;
}

class DbitemDialog : public QDialog
{
    Q_OBJECT

public:
    explicit DbitemDialog(QWidget *parent = 0);
    ~DbitemDialog();

private:
    Ui::DbitemDialog *ui;
};

#endif // DBITEMDIALOG_H
