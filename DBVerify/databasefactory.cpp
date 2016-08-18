#include "databasefactory.h"


const DataBaseOperator<DatabaseInfoItem>* databaseFactory::buildDataBaseSourceForUser()
{
    if(databaseFactory::m_userDatabase!=nullptr)
    {
        databaseFactory::m_userDatabase=new DataBaseOperator<DatabaseInfoItem>();
        databaseFactory::m_userDatabase->setFilename("user.db");
    }
    return databaseFactory::m_userDatabase;

}

const DataBaseOperator<LeakinfoItem>* databaseFactory::buildDatabaseForPreset()
{
    if(databaseFactory::m_presetDatabas!=nullptr)
    {
        databaseFactory::m_presetDatabas=new DataBaseOperator<LeakinfoItem>();
        databaseFactory::m_presetDatabas->setFilename("preset.db");
    }
    return databaseFactory::m_presetDatabas;
}
