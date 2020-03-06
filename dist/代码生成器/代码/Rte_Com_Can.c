static TsRTECOMMCAN_h_EvbusRxVCU0x103_MsgType	SsRTECOMMCAN_h_EvbusRxVCU0x103_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxGW0x15D_MsgType	SsRTECOMMCAN_h_EvbusRxGW0x15D_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxVCU0x2A1_MsgType	SsRTECOMMCAN_h_EvbusRxVCU0x2A1_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxBMS0x2A6_MsgType	SsRTECOMMCAN_h_EvbusRxBMS0x2A6_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxGW0x33B_MsgType	SsRTECOMMCAN_h_EvbusRxGW0x33B_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxVCU0x34E_MsgType	SsRTECOMMCAN_h_EvbusRxVCU0x34E_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxGW0x358_MsgType	SsRTECOMMCAN_h_EvbusRxGW0x358_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxGW0x371_MsgType	SsRTECOMMCAN_h_EvbusRxGW0x371_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxBMS0x382_MsgType	SsRTECOMMCAN_h_EvbusRxBMS0x382_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxBMS0x3A9_MsgType	SsRTECOMMCAN_h_EvbusRxBMS0x3A9_Msg		= {0,};
static TsRTECOMMCAN_h_EvbusRxGW0x3AC_MsgType	SsRTECOMMCAN_h_EvbusRxGW0x3AC_Msg		= {0,};
/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxVCU0x103_Msg / SetRTECOMMCAN_EvbusbusRxVCU0x103_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxVCU0x103 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxVCU0x103_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x103_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxVCU0x103_Msg);
}
void SetRTECOMMCAN_EvbusbusRxVCU0x103_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x103_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxVCU0x103_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxGW0x15D_Msg / SetRTECOMMCAN_EvbusbusRxGW0x15D_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxGW0x15D message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxGW0x15D_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x15D_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxGW0x15D_Msg);
}
void SetRTECOMMCAN_EvbusbusRxGW0x15D_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x15D_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxGW0x15D_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxVCU0x2A1_Msg / SetRTECOMMCAN_EvbusbusRxVCU0x2A1_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxVCU0x2A1 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxVCU0x2A1_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x2A1_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxVCU0x2A1_Msg);
}
void SetRTECOMMCAN_EvbusbusRxVCU0x2A1_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x2A1_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxVCU0x2A1_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxBMS0x2A6_Msg / SetRTECOMMCAN_EvbusbusRxBMS0x2A6_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxBMS0x2A6 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxBMS0x2A6_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x2A6_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxBMS0x2A6_Msg);
}
void SetRTECOMMCAN_EvbusbusRxBMS0x2A6_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x2A6_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxBMS0x2A6_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxGW0x33B_Msg / SetRTECOMMCAN_EvbusbusRxGW0x33B_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxGW0x33B message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxGW0x33B_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x33B_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxGW0x33B_Msg);
}
void SetRTECOMMCAN_EvbusbusRxGW0x33B_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x33B_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxGW0x33B_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxVCU0x34E_Msg / SetRTECOMMCAN_EvbusbusRxVCU0x34E_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxVCU0x34E message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxVCU0x34E_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x34E_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxVCU0x34E_Msg);
}
void SetRTECOMMCAN_EvbusbusRxVCU0x34E_Msg(const TsRTECOMMCAN_h_EvbusbusRxVCU0x34E_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxVCU0x34E_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxGW0x358_Msg / SetRTECOMMCAN_EvbusbusRxGW0x358_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxGW0x358 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxGW0x358_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x358_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxGW0x358_Msg);
}
void SetRTECOMMCAN_EvbusbusRxGW0x358_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x358_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxGW0x358_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxGW0x371_Msg / SetRTECOMMCAN_EvbusbusRxGW0x371_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxGW0x371 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxGW0x371_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x371_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxGW0x371_Msg);
}
void SetRTECOMMCAN_EvbusbusRxGW0x371_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x371_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxGW0x371_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxBMS0x382_Msg / SetRTECOMMCAN_EvbusbusRxBMS0x382_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxBMS0x382 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxBMS0x382_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x382_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxBMS0x382_Msg);
}
void SetRTECOMMCAN_EvbusbusRxBMS0x382_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x382_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxBMS0x382_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxBMS0x3A9_Msg / SetRTECOMMCAN_EvbusbusRxBMS0x3A9_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxBMS0x3A9 message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxBMS0x3A9_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x3A9_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxBMS0x3A9_Msg);
}
void SetRTECOMMCAN_EvbusbusRxBMS0x3A9_Msg(const TsRTECOMMCAN_h_EvbusbusRxBMS0x3A9_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxBMS0x3A9_Msg = *pMsg;
}/*------------------------------------------------------------------------------
| Function Name   : GetRTECOMMCAN_EvbusRxGW0x3AC_Msg / SetRTECOMMCAN_EvbusbusRxGW0x3AC_Msg
| Called by       :
| Preconditions   :
| Input Parameters: pMsg : message info pointer
| Return Value    :
| Description     : Get / Set EvbusbusRxGW0x3AC message
| History         :
|   DATE        AUTHOR          Description
|   ----------  --------------  ------------------------------------------------
|   2020-02-20   CJL        
------------------------------------------------------------------------------*/
void GetRTECOMMCAN_EvbusbusRxGW0x3AC_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x3AC_MsgType **pMsg)
{
    assert_param(NULL != pMsg);
    *pMsg = &(SsRTECOMMCAN_h_EvbusbusRxGW0x3AC_Msg);
}
void SetRTECOMMCAN_EvbusbusRxGW0x3AC_Msg(const TsRTECOMMCAN_h_EvbusbusRxGW0x3AC_MsgType *pMsg)
{
    assert_param(NULL != pMsg);
    SsRTECOMMCAN_h_EvbusbusRxGW0x3AC_Msg = *pMsg;
}