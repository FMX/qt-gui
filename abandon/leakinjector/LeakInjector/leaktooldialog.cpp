#include "leaktooldialog.h"
#include "ui_leaktooldialog.h"


LeakToolDialog::LeakToolDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LeakToolDialog)
{
    ui->setupUi(this);
}

LeakToolDialog::~LeakToolDialog()
{
    if(dlg!=nullptr)
        delete dlg;
    if(database!=nullptr)
        delete database;
//    if(filename!=nullptr)
//        delete filename;
    delete ui;
}

void LeakToolDialog::on_pushButton_clicked()
{
    dlg=new QFileDialog(this,tr("打开目录"),tr(""),tr(""));
    this->filename(dlg->getExistingDirectory(this,tr("打开路径"),tr("")));
    QMessageBox::about(this,tr(""),this->filename);

    QDir dir(this->filename);
    if(!dir.exists())
    {
        emit this->rejected();
    }

    QString dbpath;
    dbpath.sprintf("%s%s%s",this->filename,QDir::separator(),"preset.db");
    QFile dbfile(dbpath);
    if(!dbfile.exists())
    {
        emit this->rejected();
    }

    QString launcherPath;
    launcherPath.sprintf("%s%s%s",this->filename,QDir::separator(),"Launcher.py");
    QFile launcherFile(launcherPath);
    if(!launcherFile.exists())
    {
        emit this->rejected();
    }

    QString scriptPath;
    scriptPath.sprintf("%s%s%s",this->filename,QDir::separator(),"script/");
    QDir scriptDir(scriptPath);
    if(!scriptDir.exists())
    {
        emit this->rejected();
    }

    emit this->accept();
}
