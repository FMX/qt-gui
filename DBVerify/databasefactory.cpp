#include "databasefactory.h"



const DataBaseOperator* databaseFactory::buildUserDatabase()
{
    if(databaseFactory::m_userDatabase!=nullptr)
        databaseFactory::m_userDatabase=new DataBaseOperator(QString::fromUtf8("user.db"));
    return databaseFactory::m_userDatabase;
}

const DataBaseOperator* databaseFactory::buildPresetDatabase()
{
    if(databaseFactory::m_presetDatabas!=nullptr)
        databaseFactory::m_presetDatabas=new DataBaseOperator(QString::fromUtf8("preset.db"));
    return databaseFactory::m_presetDatabas;
}
