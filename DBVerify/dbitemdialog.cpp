#include "dbitemdialog.h"
#include "ui_dbitemdialog.h"

DbitemDialog::DbitemDialog(QWidget *parent,bool modify) :
    QDialog(parent),
    ui(new Ui::DbitemDialog)
{
    ui->setupUi(this);

    QStringList dblst;
    dblst.append("Oracle");
    dblst.append("SQL Server");
    dblst.append("Mysql");

    QStringList oslst;
    oslst.append("Windows");
    oslst.append("Linux");
    oslst.append("Unix");

    ui->cmbDbtype->addItems(dblst);
    ui->cmbOstype->addItems(oslst);

    this->isModify=modify;

    if(this->isModify)
        initForModify();
    else
        initForAdd();
}

DbitemDialog::~DbitemDialog()
{
    delete ui;
}

void DbitemDialog::initForModify()
{
    this->setWindowTitle("修改数据库信息");
    ui->btnConfirm->setText("修改");
}

void DbitemDialog::initForAdd()
{
    this->setWindowTitle("添加数据库信息");
    ui->btnConfirm->setText("添加");
}

void DbitemDialog::on_btnConfirm_clicked()
{
    if(this->isModify)
    {
        databaseFactory::buildDataBaseSourceForUser()->updateOneByid(this->id,this->getNewItem());
    }
    else
    {
        databaseFactory::buildDataBaseSourceForUser()->saveOne(this->getNewItem());
    }
    this->accept();
}


void DbitemDialog::on_btnCancel_clicked()
{
    this->reject();
}

void DbitemDialog::on_cmbDbtype_activated(int index)
{
    if(index==0)
        ui->ledOrasid->setEnabled(true);
    if(index>0)
        ui->ledOrasid->setEnabled(false);
}

void DbitemDialog::on_cmbOstype_activated(int index)
{

}

void DbitemDialog::modifyItem(DatabaseInfoItem item)
{
    this->id=item.getId();
    ui->ledDbname->setText(item.getDbname());
    ui->ledDbip->setText(item.getDbip());
    ui->ledDbver->setText(item.getDbversion());
    ui->ledOrasid->setText(item.getOrasid());
    ui->ledOsver->setText(item.getOsversion());
    ui->ledPort->setText(QString::number(item.getDbport()));
    ui->ledUsername->setText(item.getUsername());
    ui->ledPwd->setText(item.getUserpwd());
    ui->cmbDbtype->setCurrentIndex(item.getDbtype()-1);
    ui->cmbOstype->setCurrentIndex(item.getOstype()-1);
}

DatabaseInfoItem DbitemDialog::getNewItem()
{
    DatabaseInfoItem item;
    item.setDbip(ui->ledDbip->text());
    item.setDbname(ui->ledDbname->text());
    item.setDbport(ui->ledPort->text().toInt());
    item.setDbtype(ui->cmbDbtype->currentIndex()+1);
    item.setOrasid(ui->ledOrasid->text());
    item.setOstype(ui->cmbOstype->currentIndex()+1);
    item.setOsversion(ui->ledOsver->text());
    item.setUsername(ui->ledUsername->text());
    item.setUserpwd(ui->ledPwd->text());
    return item;
}
