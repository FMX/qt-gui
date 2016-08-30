#include "verifydialog.h"
#include "ui_verifydialog.h"
#include <QLibrary>

typedef void (*init)(DatabaseInfoItem dbitem,LeakinfoItem leakitem );
typedef void (*run)();
typedef void (*clean)();

VerifyDialog::VerifyDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::VerifyDialog)
{
    ui->setupUi(this);
}

VerifyDialog::~VerifyDialog()
{
    delete ui;
}

void VerifyDialog::setDindex(int did, int lid)
{
    this->dbix=did;
    this->lkix=lid;
    this->loadinfos();
}

void VerifyDialog::loadinfos()
{
    this->leakitem= databaseFactory::buildDatabaseForPreset()->getOneById(this->lkix);
    this->dbitem=databaseFactory::buildDataBaseSourceForUser()->getOneByid(this->dbix);
}

void VerifyDialog::on_btnConfirm_clicked()
{

    QLibrary *lib=NULL;
    QString libpath= QDir::homePath();
    libpath.append(QDir::separator());
    libpath.append(".dbfw");
    libpath.append(QDir::separator());
    libpath.append("libexample1.1.0.0.dylib");
    lib=new QLibrary(libpath);
    if(!lib)
    {
        QMessageBox::warning(thi s,"WARN","没有找到可执行代码");
    }
    lib->load();
    if(!lib->isLoaded())
    {
        QMessageBox::warning(this,"WARN","加载失败");
        return ;
    }

    init initfun=(init)lib->resolve("init");
    run runfun=(run)lib->resolve("run");
    clean clefun=(clean)lib->resolve("clean");

    initfun(this->dbitem,this->leakitem);
    runfun();
    clefun();

    lib->unload();

}
