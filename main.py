from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QMessageBox
from mainWin import *
import time
import os
import sys
class Main(QWidget,Ui_MainWin):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.lineEdit.setText(os.getcwd() + '\配置.txt')
        self.pushButton_openfile.clicked.connect(self.OpenExcel)
        self.pushButton_startcreat.clicked.connect(self.StartCreat)
        self.pushButton_filesave.clicked.connect(self.choiceDir)
        self.timeCurrent = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.lineEdit_codesave_path.setText(os.getcwd())
        self.saveDir = self.lineEdit_codesave_path.text()
        self.show()

    def OpenExcel(self):
        fname = QFileDialog.getOpenFileName(self,'打开文件','./',('Text(*.txt)'))
        if fname[0]:
            self.lineEdit.setText(fname[0])

    def choiceDir(self):
        Dir_path = QFileDialog.getExistingDirectory(self,'请选择保存源代码路径','./')
        if Dir_path:
            self.lineEdit_codesave_path.setText(Dir_path)
        self.saveDir = self.lineEdit_codesave_path.text()
    def StartCreat(self):
        self.config_list = []
        #尝试打开选定路径文件,若是文件不存在则弹窗警告
        try:
            f_read = open(self.lineEdit.text(),'r',encoding='utf-8')
        except FileNotFoundError:
            QMessageBox.warning(self,'提示','并未找到所选路径文件,请检查路径')
            return
        #将配置文件中的每一行读取出来
        for line in f_read.readlines():
            line = line[:-1].split('\t')
            self.config_list.append(line)
        f_read.close()
        self.Creat_Rte_c()
        self.Creat_Rte_h()
        self.Creat_ComCfg_c()
        self.Creat_ComCfg_h()
        QMessageBox.information(self,'提示','代码生成完毕')

        #以下部分为Rte_Com_Can.c文件生成
    def Creat_Rte_c(self):
        #创建一个新的文件,将静态变量定义写入到文件开头
        try:
            with open(self.saveDir + '\Rte_Com_Can.c','w') as f_write:
                for config in self.config_list:
                    valdef_write_str = 'static TsRTECOMMCAN_h_' + config[2] + config[3] + config[1] + '0x' + config[0] + '_MsgType'\
                                + '\t' + 'SsRTECOMMCAN_h_' + config[2] + config[3] + config[1] + '0x' + config[0] + '_Msg'\
                                + '\t\t' + '= {0,};\n'
                    f_write.write(valdef_write_str)
        except Exception:
            pass
        #变量定义完以后再进行函数定义
        try:
            with open('.\demo.txt','r',encoding = 'utf-8') as f:
                demo_str = f.read()
        except Exception:
            pass
        f_write = open(self.saveDir + '\Rte_Com_Can.c','a')
        for config in self.config_list:
            fundef_write_str = demo_str.replace('($Channel$)',config[2]).replace('($Dic$)',config[3]).replace('($Node$)',config[1])\
                                .replace('($ID$)',config[0]).replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
            f_write.write(fundef_write_str)
            print('ok')
        f_write.close()
    #以下函数生成Rte_Com_Can.h文件
    def Creat_Rte_h(self):
        Tpdef_str = '''typedef struct TsRTECOMMCAN_h_(Node)_0x(ID)_msgTypeTag
{
} TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType;\n'''
        Fundec_str ='''extern void GetRTECOMMCAN_(Chl)(Dic)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)0x(ID)_MsgType **pMsg);
extern void SetRTECOMMCAN_(Chl)(Dic)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)0x(ID)_MsgType *pMsg);\n'''
        with open(self.saveDir + '\Rte_Com_Can.h','w') as f:
            for config in self.config_list:
                write_str = Tpdef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                f.write(write_str)
        with open(self.saveDir + '\Rte_Com_Can.h','a') as f:
            for config in self.config_list:
                write_str = Fundec_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                f.write(write_str)
    def Creat_ComCfg_c(self):
        RsvFundef_str = '''/*******************************************************************************
| Function Name   : MngCOMCFGCAN_RcvMsg_(Chl)(Dic)(Node)0x(ID)
| Called by       :
| Preconditions   :
| Input Parameters: pCanMsg : not used
| Return Value    :
| Description     : Receive CAN (Chl)(Dic)(Node)0x(ID) message from buffer
| ------------------------------------------------------------------------------
| History:
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   ($Date$)    ($Author$)       
*******************************************************************************/
void MngCOMCFGCAN_RcvMsg_(Chl)(Dic)(Node)0x(ID)(const void *pCanMsg)
{
    TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType LpCOMCFGCAN_h_(Chl)(Dic)(Node)0x(ID)_Msg;
    // TODO: to be checked
    SetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(&LpCOMCFGCAN_h_(Chl)(Dic)(Node)0x(ID)_Msg);
}\n'''
        TrsFundef_str = '''/*******************************************************************************
| Function Name   : MngCOMCFGCAN_TrsMsg_(Chl)(Dic)(Node)0x(ID)
| Called by       :
| Preconditions   :
| Input Parameters: none
| Return Value    : E_OK / E_NOT_OK
| Description     : Send Transmit CAN (Chl)(Dic)(Node)0x(ID) message into buffer
| ------------------------------------------------------------------------------
| History:
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   ($Date$)    ($Author$)      
*******************************************************************************/
Std_ReturnType MngCOMCFGCAN_TrsMsg_(Chl)(Dic)(Node)0x(ID)(void)
{
    const TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType *LpCOMCFGCAN_h_(Chl)(Dic)(Node)0x(ID)_Msg = NULL;

    return (E_OK);
}
'''
        with open(self.saveDir + '\Com_Cfg_Can.c','w') as f:
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = RsvFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])\
                                .replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
                    f.write(write_str)
            for config in self.config_list:
                if config[3] == 'Tx':
                    write_str = TrsFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])\
                                .replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
                    f.write(write_str)
    def Creat_ComCfg_h(self):
        RsvFundef_str = 'extern void MngCOMCFGCAN_RcvMsg_(Chl)(Dic)(Node)0x(ID)(const void *pCanMsg);\n'
        TrsFundef_str = 'extern Std_ReturnType MngCOMCFGCAN_TrsMsg_(Chl)(Dic)(Node)0x(ID)(void);'
        with open(self.saveDir + '\Com_Cfg_Can.h','w') as f:
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = RsvFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                    f.write(write_str)
            for config in self.config_list:
                if config[3] == 'Tx':
                    write_str = TrsFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                    f.write(write_str)
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        MainFun = Main()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex.args)