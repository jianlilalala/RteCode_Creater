class Message:
    def __init__(self,msg_id,msg_name='',msg_dlc = 8,msg_node = ''):
        self.msg_id   = hex(msg_id)
        self.msg_name = msg_name
        self.msg_dlc  = msg_dlc
        self.msg_node = msg_node
        self.msg_dirc = ''
        self.signal_array = []
    def __signal_add(self,signal):
        self.signal_array.append(signal)
