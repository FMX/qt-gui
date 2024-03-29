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
    dbitemdialog.cpp \
    userdboperator.cpp \
    presetdboperator.cpp \
    converutil.cpp \
    ping.cpp \
    netdetthread.cpp \
    verifydialog.cpp

HEADERS  += mainwindow.h \
    leakinfoitem.h \
    databaseinfoitem.h \
    databasefactory.h \
    netdetdialog.h \
    dbitemdialog.h \
    userdboperator.h \
    presetdboperator.h \
    converutil.h \
    ping.h \
    netdetthread.h \
    verifydialog.h

FORMS    += mainwindow.ui \
    netdetdialog.ui \
    dbitemdialog.ui \
    verifydialog.ui


