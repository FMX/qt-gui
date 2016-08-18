#-------------------------------------------------
#
# Project created by QtCreator 2016-08-17T16:07:54
#
#-------------------------------------------------

QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = DBVerify
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    databasefactory.cpp \
    leakinfoitem.cpp \
    databaseinfoitem.cpp \
    netdetdialog.cpp \
    dbitemdialog.cpp

HEADERS  += mainwindow.h \
    leakinfoitem.h \
    databaseinfoitem.h \
    databasefactory.h \
    netdetdialog.h \
    dbitemdialog.h \
    databaseoperator.hpp

FORMS    += mainwindow.ui \
    netdetdialog.ui \
    dbitemdialog.ui
