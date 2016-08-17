/********************************************************************************
** Form generated from reading UI file 'leaktooldialog.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LEAKTOOLDIALOG_H
#define UI_LEAKTOOLDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_LeakToolDialog
{
public:
    QPushButton *pushButton;
    QLineEdit *lineEdit;

    void setupUi(QDialog *LeakToolDialog)
    {
        if (LeakToolDialog->objectName().isEmpty())
            LeakToolDialog->setObjectName(QStringLiteral("LeakToolDialog"));
        LeakToolDialog->resize(536, 99);
        pushButton = new QPushButton(LeakToolDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(394, 36, 113, 32));
        lineEdit = new QLineEdit(LeakToolDialog);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(40, 40, 351, 21));

        retranslateUi(LeakToolDialog);

        QMetaObject::connectSlotsByName(LeakToolDialog);
    } // setupUi

    void retranslateUi(QDialog *LeakToolDialog)
    {
        LeakToolDialog->setWindowTitle(QApplication::translate("LeakToolDialog", "\345\256\232\344\275\215\345\267\245\345\205\267\344\275\215\347\275\256", 0));
        pushButton->setText(QApplication::translate("LeakToolDialog", "\346\214\207\345\256\232\345\267\245\345\205\267\344\275\215\347\275\256", 0));
    } // retranslateUi

};

namespace Ui {
    class LeakToolDialog: public Ui_LeakToolDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LEAKTOOLDIALOG_H
