#ifndef DATABASEFACTORY_H
#define DATABASEFACTORY_H

#include "leakinfoitem.h"
#include "databaseinfoitem.h"
#include "userdboperator.h"
#include "presetdboperator.h"

class databaseFactory
{
private:
    static UserdbOperator*  m_userDatabase;
    static PresetdbOperator* m_presetDatabas;

public:
    static const UserdbOperator* buildDataBaseSourceForUser();
    static const PresetdbOperator* buildDatabaseForPreset();
};

UserdbOperator*  databaseFactory::m_userDatabase=nullptr;
PresetdbOperator*  databaseFactory::m_presetDatabas=nullptr;
#endif // DATABASEFACTORY_H
