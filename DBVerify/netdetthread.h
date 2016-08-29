#ifndef NETDETTHREAD_H
#define NETDETTHREAD_H
#include <QThread>
#include "ping.h"
#include <QDebug>

class NetdetThread : public QThread
{
    Q_OBJECT
public:
    NetdetThread(QString netseg);
    void run() Q_DECL_OVERRIDE
    {
        Ping ping=Ping();

        for(volatile int  i=0;i<=255;i++)
        {
            PingResult pingresult;
            QString str(this->seg);
            QString buf=str.replace("*",QString::number(i));
            qDebug()<<buf<<endl;
            if(ping.ping(buf.toStdString(),pingresult))
            {

                if(pingresult.icmpEchoReplys.size()>0)
                {
                    for(unsigned int index=0;index<pingresult.icmpEchoReplys.size();index++)
                    {
                        IcmpEchoReply reply=pingresult.icmpEchoReplys.at(index);
                        if(reply.isReply)
                        {
//                            qDebug()<<buf<<endl;
//                            qDebug()<<"Adding new item!"<<endl;
                            //                            this->addItem(buf);
                            emit insertItem(buf);
                            //                            emit inforProcess(i);
                        }
                    }
                }
            }
            emit inforProcess(i);
        }
        //        emit resultReady();
        emit finish();
    }
signals:
    void inforProcess(int val);
    void insertItem(QString item);
    void finish();

private:
    QString seg;

private slots:


};

#endif // NETDETTHREAD_H
