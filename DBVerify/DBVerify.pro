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
    databaseoperator.cpp \
    databasefactory.cpp

HEADERS  += mainwindow.h \
    databaseoperator.h \
    databasefactory.h

FORMS    += mainwindow.ui
