import re
import time
class CreatCode:
    def __init__(self,saveDirpath,msg_array,busChl,authorName):
        self.saveDirpath = saveDirpath
        self.msg_array = msg_array
        self.busChl = busChl
        self.authorName = authorName
        self.timeCurrent = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    def Creat_Rte_c(self):
            demo_str = '''/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMCAN_($Channel$)($Dirc$)($Node$)($ID$)_Msg / SetRTECOMCAN_($Channel$)($Dirc$)($Node$)($ID$)_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set ($Channel$)($Dirc$)($Node$)($ID$) message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   ($Date$)   ($Author$)        
------------------------------------------------------------------------------*/
void GetRTECOMCAN_($Channel$)bus($Dirc$)($Node$)($ID$)_Msg(const TsRTECOMCAN_h_($Channel$)($Dirc$)($Node$)($ID$)_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMCAN_h_($Channel$)($Dirc$)($Node$)($ID$)_Msg);
}
void SetRTECOMCAN_($Channel$)($Dirc$)($Node$)($ID$)_Msg(const TsRTECOMCAN_h_($Channel$)($Dirc$)($Node$)($ID$)_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMCAN_h_($Channel$)($Dirc$)($Node$)($ID$)_Msg = *pMsg;
}\n'''
            #创建一个新的文件,将静态变量定义写入到文件开头
            try:
                with open(self.saveDirpath + '\Rte_Com_Can.c','w') as f_write:
                    for msg_Info in self.msg_array:
                        valdef_write_str = 'static TsRTECOMCAN_h_' + self.busChl + msg_Info.msg_dirc + msg_Info.msg_node + msg_Info.msg_id + '_MsgType'\
                                    + '\t' + 'SsRTECOMCAN_h_' + self.busChl + msg_Info.msg_dirc + msg_Info.msg_node + msg_Info.msg_id + '_Msg'\
                                    + '\t\t' + '= {0,};\n'
                        f_write.write(valdef_write_str)
            except Exception:
                pass

            f_write = open(self.saveDirpath + '\Rte_Com_Can.c','a')
            for msg_Info in self.msg_array:
                fundef_write_str = demo_str.replace('($Channel$)',self.busChl).replace('($Dirc$)',msg_Info.msg_dirc).replace('($Node$)',msg_Info.msg_node)\
                                    .replace('($ID$)',msg_Info.msg_id).replace('($Date$)',self.timeCurrent).replace('($Author$)',self.authorName)
                f_write.write(fundef_write_str)
            f_write.close()
    #以下函数生成Rte_Com_Can.h文件
    def Creat_Rte_h(self):
        Tpdef_str = '''typedef struct TsRTECOMMCAN_h_(Node)_0x(ID)_msgTypeTag
{
} TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType;\n'''
        Fundec_str ='''extern void GetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType **pMsg);
extern void SetRTECOMMCAN_(Chl)(Dic)(Node)0x(ID)_Msg(const TsRTECOMMCAN_h_(Chl)(Dic)(Node)0x(ID)_MsgType *pMsg);\n'''
        with open(self.saveDirpath + '\Rte_Com_Can.h','w') as f:
            for msg_Info in self.msg_array:
                write_str = '''typedef struct TsRTECOMMCAN_h_(Node)_0x(ID)_msgTypeTag\n{'''
                for signal_info in msg_Info.signal_array:

                f.write(write_str)
        with open(self.saveDir + '\Rte_Com_Can.h','a') as f:
            for config in self.config_list:
                write_str = Fundec_str.replace('(Node)',config[1]).replace('(ID)',config[0]).replace('(Chl)',config[2]).replace('(Dic)',config[3])
                f.write(write_str)
                f.write('\n')