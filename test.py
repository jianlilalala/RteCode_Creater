import re
str = '''e_u_PID_switch
e_u_EXV_H_PID_switch
e_sw_EXV_H_SV
e_sw_EXV_H_P
e_sw_EXV_H_I
e_u_WTC_H_PID_switch
e_sw_WTC_H_SV
e_sw_WTC_H_P
e_sw_WTC_H_I
e_u_Comp_PID_switch
e_sw_Comp_SV
e_sw_Comp_P
e_sw_Comp_I
'''
str_zhushi = '''PID调试功能开关
热泵膨胀阀PID系数选择开关
热泵电子膨胀阀设定(SV)值
热泵电子膨胀阀P系数
热泵电子膨胀阀I系数
采暖加热器PID系数选择开关
采暖加热器设定（SV）值
采暖加热器P系数
采暖加热器I系数
压缩机PID系数选择开关
制冷模式压缩机设定值（SV）
乘客舱制冷压缩机P系数
乘客舱制冷压缩机I系数
'''
structVar_name = 'PID_Debug.'
zhushi_groups = str_zhushi.splitlines()
var_groups = str.splitlines()
str_result = 'typedef struct\n{\n'
fundef_str = '''
/*------------------------------------------------------------------------------
| Function Name   : MngSYSIF_($Function_name$)
| Called by       :
| Preconditions   :
| Input Parameters: none
| Return Value    : none
| Description     : refresh sensor data from RTE to SysCtrl
| ------------------------------------------------------------------------------
| History:
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020.03.04  CJL             add new
------------------------------------------------------------------------------*/
TsSYSCTRL_h_($Function_name$)       ($Function_name$);
static void MngSYSIF_($Function_name$)(void)\n{\n'''
index = 0
for var in var_groups:
    varLen_type = 'sint16'
    if ';' in var:
        var = var.replace(';','')
    tab_number =7 - (len(var)//4)
    fundef_tabNum =10 - (len(var + structVar_name)//4)
    if ('_sw_') in var:
        varLen_type = 'sint16'
    elif '_u_' in var:
        varLen_type = 'uint8'
    elif '_w_' in var:
        varLen_type = 'uint16'
    str_result += '\t' + varLen_type + '\t' +var +'\t'*tab_number + ';/* ' + zhushi_groups[index]+' */\n'
    fundef_str += '\t' + structVar_name + var + '\t'*fundef_tabNum + '=;\n'
    fundef_str = fundef_str.replace('($Function_name$)',structVar_name[:-1])
    index += 1
str_result += '}TsSYSCTRL_h_'+structVar_name[:-1] + ';'
fundef_str += '}'
print(str_result)
print(fundef_str)
