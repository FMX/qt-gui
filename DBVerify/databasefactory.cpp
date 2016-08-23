#include "databasefactory.h"

UserdbOperator* databaseFactory::m_userDatabase=nullptr;
PresetdbOperator*  databaseFactory::m_presetDatabas=nullptr;

UserdbOperator* databaseFactory::buildDataBaseSourceForUser()
{
    if(databaseFactory::m_userDatabase==nullptr)
    {
        databaseFactory::m_userDatabase=new UserdbOperator();
//        databaseFactory::m_userDatabase->setFilename(path);
    }
    return databaseFactory::m_userDatabase;

}

PresetdbOperator* databaseFactory::buildDatabaseForPreset()
{
    if(databaseFactory::m_presetDatabas==nullptr)
    {
        databaseFactory::m_presetDatabas=new PresetdbOperator();
//        databaseFactory::m_presetDatabas->setFilename("preset.db");
    }
    return databaseFactory::m_presetDatabas;
}
