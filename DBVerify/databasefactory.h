#ifndef DATABASEFACTORY_H
#define DATABASEFACTORY_H
#include "databaseoperator.hpp"
#include "leakinfoitem.h"
#include "databaseinfoitem.h"

class databaseFactory
{
private:
    static DataBaseOperator<DatabaseInfoItem>*  m_userDatabase;
    static DataBaseOperator<LeakinfoItem>* m_presetDatabas;

public:
    static const DataBaseOperator<DatabaseInfoItem>* buildDataBaseSourceForUser();
    static const DataBaseOperator<LeakinfoItem>* buildDatabaseForPreset();
};

DataBaseOperator<DatabaseInfoItem>*  databaseFactory::m_userDatabase=nullptr;
DataBaseOperator<LeakinfoItem>*  databaseFactory::m_presetDatabas=nullptr;
#endif // DATABASEFACTORY_H
