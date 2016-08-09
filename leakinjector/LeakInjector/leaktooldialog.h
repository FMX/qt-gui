#ifndef LEAKTOOLDIALOG_H
#define LEAKTOOLDIALOG_H

#include <QDialog>

namespace Ui {
class LeakToolDialog;
}

class LeakToolDialog : public QDialog
{
    Q_OBJECT

public:
    explicit LeakToolDialog(QWidget *parent = 0);
    ~LeakToolDialog();

private:
    Ui::LeakToolDialog *ui;
};

#endif // LEAKTOOLDIALOG_H
