import os
import sys
import re
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QMessageBox
from mainWin import *
import time
import Message
import Signal
class Main(QWidget,Ui_MainWin):
    def __init__(self):
        super(Main, self).__init__()

        self.setupUi(self)
        self.lineEdit.setText(os.path.abspath(os.path.dirname(os.getcwd())) + '\配置.txt')
        self.pushButton_openfile.clicked.connect(self.OpenDBC)
        self.pushButton_startcreat.clicked.connect(self.StartCreat)
        self.pushButton_filesave.clicked.connect(self.choiceDir)
        self.checkBox_Evbus.stateChanged.connect(self.checkBox_Evbus_checked)
        self.checkBox_Pbus.stateChanged.connect(self.checkBox_Pbus_checked)
        self.comboBox_choseNode.currentIndexChanged[str].connect(self.Get_NodeName)
        #self.timeCurrent = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.lineEdit_codesave_path.setText(os.path.abspath(os.path.dirname(os.getcwd())))
        self.saveDir = self.lineEdit_codesave_path.text()
        self.show()
    #复选框选中处理函数
    def checkBox_Evbus_checked(self):
        if self.checkBox_Evbus.isChecked() == True:
            self.busChl = 'Evbus'
            self.checkBox_Pbus.setChecked(False)
    def checkBox_Pbus_checked(self):
        if self.checkBox_Pbus.isChecked() == True:
            self.busChl = 'Pbus'
            self.checkBox_Evbus.setChecked(False)
    #打开需要读取的DBC文件
    def OpenDBC(self):
        self.fname = QFileDialog.getOpenFileName(self,'打开文件','./',('DBC文件(*.dbc)'))
        if self.fname[0]:
            self.lineEdit.setText(self.fname[0])  #记录文件位置
            if 'DBC文件(*.dbc)'== self.fname[1]:
                self.Get_signalInfo(self.lineEdit.text()) #获取dbc文件内容
                self.comboBox_choseNode.addItems(self.nodeName_array)
    #获取下拉框内当前选择节点的名称
    def Get_NodeName(self,nodeName):
        self.nodeName = nodeName
        for msg_info in self.msg_array:
            if nodeName == msg_info.msg_node:
                msg_info.msg_dirc = 'Tx'
            else:
                msg_info.msg_dirc = 'Rx'

    #选择生成代码存放目录
    def choiceDir(self):
        Dir_path = QFileDialog.getExistingDirectory(self,'请选择保存源代码路径','./')
        if Dir_path:
            self.lineEdit_codesave_path.setText(Dir_path)
        self.saveDir = self.lineEdit_codesave_path.text()
    #开始生成代码
    def StartCreat(self):
        #尝试打开选定路径文件,若是文件不存在则弹窗警告
        try:
            f_read = open(self.lineEdit.text(),'r',encoding='utf-8')
        except FileNotFoundError:
            QMessageBox.warning(self,'提示','并未找到所选路径配置文件,请检查路径')
            return
        try:
            self.Creat_Rte_c()
            self.Creat_ComCfg_h()
            self.Creat_Rte_h()
            self.Creat_ComCfg_c()
            #os.system('start explorer ' + self.lineEdit_codesave_path.text().replace('/','\\'))
            QMessageBox.information(self,'提示','代码生成完毕')
            os.system('start explorer ' + self.lineEdit_codesave_path.text().replace('/','\\'))
        except Exception as e:
            QMessageBox.warning(self,'提示','代码生成失败:' + e.args[0])

        #以下部分为Rte_Com_Can.c文件生成
    def Creat_Rte_c(self):
        #创建一个新的文件,将静态变量定义写入到文件开头
        try:
            with open(self.saveDir + '\Rte_Com_Can.c','w') as f_write:
                for msg_Info in self.msg_array:
                    valdef_write_str = 'static TsRTECOMCAN_h_' + self.busChl + msg_Info.msg_dirc + msg_Info.msg_node + msg_Info.msg_id + '_MsgType'\
                                + '\t' + 'SsRTECOMCAN_h_' + self.busChl + msg_Info.msg_dirc + msg_Info.msg_node + msg_Info.msg_id + '_Msg'\
                                + '\t\t' + '= {0,};\n'
                    f_write.write(valdef_write_str)
        except Exception:
            pass
        #变量定义完以后再进行函数定义
        '''
        try:
            with open('.\demo.txt','r',encoding = 'utf-8') as f:
                demo_str = f.read()
        except Exception:
            QMessageBox.warning(self,'警告','软件安装路径未找到模板文件,终止生成代码')
            os.remove(self.saveDir + '\Rte_Com_Can.c')
            raise Exception
        '''
        demo_str = '''/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_($Channel$)($Dic$)($Node$)0x($ID$)_Msg / SetRTECOMMCAN_($Channel$)($Dic$)($Node$)0x($ID$)_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set ($Channel$)($Dic$)($Node$)0x($ID$) message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   ($Date$)   ($Author$)        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_($Channel$)bus($Dic$)($Node$)0x($ID$)_Msg(const TsRTECOMMCAN_h_($Channel$)($Dic$)($Node$)0x($ID$)_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_($Channel$)($Dic$)($Node$)0x($ID$)_Msg);
}
void SetRTECOMMCAN_($Channel$)($Dic$)($Node$)0x($ID$)_Msg(const TsRTECOMMCAN_h_($Channel$)($Dic$)($Node$)0x($ID$)_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_($Channel$)($Dic$)($Node$)0x($ID$)_Msg = *pMsg;
}\n'''
        f_write = open(self.saveDir + '\Rte_Com_Can.c','a')
        for config in self.config_list:
            fundef_write_str = demo_str.replace('($Channel$)',config[2]).replace('($Dic$)',config[3]).replace('($Node$)',config[1])\
                                .replace('($ID$)',config[0]).replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
            f_write.write(fundef_write_str)
        f_write.close()
    #以下函数生成Rte_Com_Can.h文件
    def Creat_Rte_h(self):
        Tpdef_str = '''typedef struct TsRTECOMMCAN_h_(Node)_0x(ID)_msgTypeTag
{
} TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType;\n'''
        Fundec_str ='''extern void GetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType **pMsg);
extern void SetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType *pMsg);\n'''
        with open(self.saveDir + '\Rte_Com_Can.h','w') as f:
            for config in self.config_list:
                write_str = Tpdef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                f.write(write_str)
        with open(self.saveDir + '\Rte_Com_Can.h','a') as f:
            for config in self.config_list:
                write_str = Fundec_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                f.write(write_str)
                f.write('\n')
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
    GetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(&LpCOMCFGCAN_h_(Chl)(Dic)(Node)0x(ID)_Msg);
    return (E_OK);
}
'''
        LostFundef_str="""void MngCOM_(Chl)RxLost_(Node)0x(ID)(void)
{
    SetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(&CsCOM_h_(Chl)Lost(Node)0x(ID)_Msg);
}
"""
        PrecopyFundef_str='''vuint8 MngCOM_(Chl)RxPrecopy_(Node)0x(ID)(CanRxInfoStructPtr rxStruct)
{
    MngCOM_ConfirmRx(CeCOM_e_(Chl)Rx(Node)0x(ID));
    return (kCanCopyData);
}
'''
        with open(self.saveDir + '\Com_Cfg_Can.c','w') as f:
            #生成报文丢失回调函数默认值变量
            for config in self.config_list:
                if config[3] == 'Rx':
                    Lostvaldef_write_str = 'static TsRTECOMMCAN_h_' + config[2] + config[3] + config[1] + '0x' + config[0] + '_MsgType'\
                                + '\t' + 'CsCOM_h_' + config[2] + "Lost" + config[1] + '0x' + config[0] + '_Msg'\
                                + '\t\t' + '= {0,};\n'
                    f.write(Lostvaldef_write_str)
            #生成主函数
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = RsvFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])\
                                .replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            for config in self.config_list:
                if config[3] == 'Tx':
                    write_str = TrsFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])\
                                .replace('($Date$)',self.timeCurrent).replace('($Author$)',self.lineEdit_authorName.text())
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            #生成Lost函数
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = LostFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            #生成Precopy函数
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = PrecopyFundef_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2].replace('Dic',config[3]))
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = "CeCOM_e_ID_(Chl)Rx(Node)0x(ID),\n".replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2])
                    f.write(write_str)

    def Creat_ComCfg_h(self):
        RsvFundcl_str = 'extern void MngCOMCFGCAN_RcvMsg_(Chl)(Dic)(Node)0x(ID)(const void *pCanMsg);\n'
        TrsFundcl_str = 'extern Std_ReturnType MngCOMCFGCAN_TrsMsg_(Chl)(Dic)(Node)0x(ID)(void);\n'
        LostFundcl_str = 'extern void MngCOM_(Chl)RxLost_(Node)0x(ID)(void);\n'
        PrecopyFundcl_str = 'extern vuint8 MngCOM_(Chl)RxPrecopy_(Node)0x(ID)(CanRxInfoStructPtr rxStruct);\n'
        with open(self.saveDir + '\Com_Cfg_Can.h','w') as f:
            #生成主函数声明代码
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = RsvFundcl_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            for config in self.config_list:
                if config[3] == 'Tx':
                    write_str = TrsFundcl_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            #生成Lost函数声明代码
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = LostFundcl_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2])
                    f.write(write_str)
            f.write('-----------------------------------------------------------------------------------------------------------\n')
            #生成Precopy函数声明代码
            for config in self.config_list:
                if config[3] == 'Rx':
                    write_str = PrecopyFundcl_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2])
                    f.write(write_str)
    def Get_signalInfo(self,dbc_path):
        with open(dbc_path) as f:
            dbc_str = f.readlines()
        self.msg_array = []
        self.nodeName_array = []
        msg_array_index = 0
        message_flag = False
        oldtime = time.time()
        for line in dbc_str:
            if re.match('BO_ (\d+) (\S+): (\d+) (\S+)',line) != None:
                message_flag = True
            if True == message_flag:
                if re.match('BO_ (\d+) (\S+): (\d+) (\S+)',line) != None:
                    message_groups = re.search('BO_ (\d+) (\S+): (\d+) (\S+)', line).groups()
                    msg_id   = message_groups[0]
                    msg_name = message_groups[1]
                    msg_dlc  = message_groups[2]
                    msg_node = message_groups[3]
                    message_ins = Message.Message(msg_id, msg_name, msg_dlc, msg_node)
                    if ('VECTOR__INDEPENDENT_SIG_MSG' == message_ins.msg_name) | ('Test_' in message_ins.msg_name):
                        message_flag = False
                    else:
                        self.msg_array.append(message_ins)
                        self.nodeName_array.append(message_ins.msg_node)
                elif re.match(' SG_ (\S+) : \d+\|\d+@0\+ \((\d+\.?\d*),(-?\d+)\) \[(-?\d+\.?\d*)\|(-?\d+\.?\d*)\] "(\S+)"*',line) != None:
                    signal_groups = re.search(' SG_ (\S+) : \d+\|(\d+)@0\+ \((\d+\.?\d*),(-?\d+)\) \[(-?\d+\.?\d*)\|(-?\d+\.?\d*)\] "(\S+)"*', line).groups()
                    signal_name     = signal_groups[0]
                    signal_dlc      = signal_groups[1]
                    signal_factor   = signal_groups[2]
                    signal_offset   = signal_groups[3]
                    signal_minValue = signal_groups[4]
                    signal_maxValue = signal_groups[5]
                    signal_unit     = signal_groups[6]
                    signal_ins = Signal.signal(signal_name,signal_dlc,signal_factor,signal_offset,signal_minValue,signal_maxValue,signal_unit)
                    self.msg_array[msg_array_index].__signal_add(signal_ins)
                    pass
                elif '\n' == line:
                    msg_array_index = msg_array_index + 1
                    message_flag = False
            if re.match('CM_ .*',line) != None:
                self.nodeName_array = list(set(self.nodeName_array))
                break
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        MainFun = Main()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex.args)