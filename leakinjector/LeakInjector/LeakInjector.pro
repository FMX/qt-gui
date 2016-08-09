#-------------------------------------------------
#
# Project created by QtCreator 2016-08-09T18:19:51
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = LeakInjector
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    leaktooldialog.cpp

HEADERS  += mainwindow.h \
    leaktooldialog.h

FORMS    += mainwindow.ui \
    leaktooldialog.ui
