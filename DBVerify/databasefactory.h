#ifndef DATABASEFACTORY_H
#define DATABASEFACTORY_H
#include "databaseoperator.h"

class databaseFactory
{
private:
    static DataBaseOperator*  m_userDatabase;
    static DataBaseOperator* m_presetDatabas;

public:
    static const DataBaseOperator* buildUserDatabase();
    static const DataBaseOperator* buildPresetDatabase();
};

DataBaseOperator*  databaseFactory::m_userDatabase=nullptr;
DataBaseOperator*  databaseFactory::m_presetDatabas=nullptr;
#endif // DATABASEFACTORY_H
