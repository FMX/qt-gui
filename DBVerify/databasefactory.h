#ifndef DATABASEFACTORY_H
#define DATABASEFACTORY_H

#include "leakinfoitem.h"
#include "databaseinfoitem.h"
#include "userdboperator.h"
#include "presetdboperator.h"
#include <QDir>
#include <QFile>


class databaseFactory
{
private:
    static UserdbOperator*  m_userDatabase;
    static PresetdbOperator* m_presetDatabas;

public:
    static UserdbOperator* buildDataBaseSourceForUser();
    static PresetdbOperator* buildDatabaseForPreset();
};


#endif // DATABASEFACTORY_H
