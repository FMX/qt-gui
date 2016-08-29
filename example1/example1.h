#ifndef EXAMPLE1_H
#define EXAMPLE1_H

#include "example1_global.h"

#include "../DBVerify/databaseinfoitem.h"
#include "../DBVerify/leakinfoitem.h"
#include <QString>
#include <QDebug>

extern "C"
{
    void init(DatabaseInfoItem dbitem,LeakinfoItem leakitem );
    void run();
    void clean();
}

class EXAMPLE1SHARED_EXPORT Example1
{

public:
    Example1();
};

#endif // EXAMPLE1_H
