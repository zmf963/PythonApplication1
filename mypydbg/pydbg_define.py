
from ctypes import *

# 为ctype类型的变量创建符合匈牙利命名风格的匿名，这样可以使代码更接近win32风格
WORD   = c_ushort
DWORD  = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 常值定义
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# 定义函数CreateProcessA()所需要的结构体
