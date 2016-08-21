#ifndef PRESETDBOPERATOR_H
#define PRESETDBOPERATOR_H
#include <leakinfoitem.h>
#include <QList>

class PresetdbOperator
{
public:
    PresetdbOperator();
    LeakinfoItem getOneById(int id);
    void saveOne(LeakinfoItem item);
    void saveAll(QList<LeakinfoItem> lst);
    void updateOneByid(int id,LeakinfoItem item);

};

#endif // PRESETDBOPERATOR_H
