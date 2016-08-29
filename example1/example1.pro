#-------------------------------------------------
#
# Project created by QtCreator 2016-08-29T13:48:38
#
#-------------------------------------------------

QT       += sql

QT       -= gui

TARGET = example1
TEMPLATE = lib

DEFINES += EXAMPLE1_LIBRARY

SOURCES += example1.cpp

HEADERS += example1.h\
        example1_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}
