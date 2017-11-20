#
from ctypes import * 

msvcrt = cdll.msvcrt
message_string = "hello world\n"
msvcrt.printf("Testing:%s",message_string)

'''
# linux 平台下 python2.5
from ctypes import *
libc = CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("Testing: %s",message_string)
'''
'''
函数调用约定：
    描述了如何以正确的方式调用某些特定类型的函数。
    这包括了函数参数在栈上的分配顺序，有那些参数会被压入栈中，而哪些参数将通过寄存器传入，以及在函数返回时
    函数栈的回收方式等。 
    cdecl： 函数的参数列表从右向左依次的顺序入栈，并有函数的调用者清除栈上的参数
        例如： 
            int python_rocks(reason_one, reason_two,reason_three);

            push reason_three
            push reason_two
            push reason_one
            call python_rocks
            add esp, 12

    stdcall: Win32API所广泛使用
        例如：
            int my_socks(color_one, color_two, color_three);

            push color_three
            push color_two
            push color_one
            call my_socks
            ; 与cdecl唯一的区别在于回收函数栈的工作有调用者本身my_socks在函数返回前自己负责平衡栈

    这两种调用约定都选用EAX寄存器存放函数返回值。 

按引用传参
    function_main(byref(parameter))

结构体与联合体
    struct beer_recipe
    {
    int amt_barley;
    int amt_water;
    };

    class beer_recipe(Structure):
        _filelds_ = [
        ("amt_barley",c_int),
        ("amt_water",c_int),
        ]


    union {
        long barley_long;
        int barley_int;
        char barley_char[8];
        }barley_amount;

    class barley_amount(Union):
        _fields_ = [
            ("barley_long",c_long),
            ("barley_int",c_int),
            ("barley_char",c_char * 8),
        ]


第二章 调试器原理和设计
用户态调试器 内核态调试器

PyDbg Immunity Debgger

通用寄存器
    8个  EAX EBX ECX EDX 
         ESI EDI EBP ESP 

    乘法和除法必须在eax中进行
    EDX 数据寄存器
    ECX 计数器
    ESI 源变址寄存器
    EDI 目的变址寄存器
    ESP 栈指针 始终指向栈顶
    EBP 基址指针 
       
EIP 指令指针寄存器 通常保存着下一条要执行的指令的地址
        【EIP中的值始终在引导cpu的执行】

段寄存器 
    （16位）
    cs 代码段
    ds 数据段
    ss 堆栈段
    es 附加段
    （32位多了两个）
    fs gs 附加段

标志寄存器FLAGS   PSW
         EFLAGS  
         11 OF 溢出 溢出为1
         10 DF 方向标志  在串指令中用于控制方向
         9  IF 中断
         8  TF 陷阱
         7  SF 符号 运算结果为负时，为1
         6  ZF 零   运算结果为0时，为1
         4  AF 辅助进位标志，记录运算结果时第三位（半字节）产生的进位，有进位时为1，
         2  PF 奇偶标志  结果操作数1 的个数为偶数时，为1， 
         0  CF 进位标志 产生进位时为1

常用汇编指令集
    mov 数据传送指令
    mov 目的操作数,源操作数  
    mov指令可以实现寄存器与寄存器之间，寄存器与内存，寄存器与立即数，内存与立即数的数据传送。 
        【注意：内存与内存无法直接传送数据，目的操作数不能为立即数】

    xchg 交换两个操作数
    xchg eax,ebx
    xchg [00401000h],eax
    xchg eax,[0040100h]

    push pop 入栈 出栈

    lea 装入有效地址 

    add 加法指令，
    sub 减法指令
    adc 带进位的加法 目的操作数 源操作数相加后在加上CF
    sbb 带进位的减法
    inc 加一
    dec 减一
    【注： 在操作内存的时候，如果无法明确内存长度，必须明确指出需要操作内存的长度。】
    【dword ptr表示要操作的内存是4字节的长度，word ptr 2字节 byte ptr 1字节】

    and 逻辑按位与  
    or  逻辑或
    not 求反
    xor 按位异或 不同为1
    test 测试指令 影响标志位 但不改变目的操作数的内容

    cmp 比较 （设置标志位，但不改变目的操作数）
    jmp 无条件跳转
    jcc 有条件跳转 j0 jn0 jb jc jnae jae je jz ...........
    loop 循环 
    call     push eip jmp 目的地址
    ret 过程返回   pop eip
    eip寄存器无法通过指令明确进行操作的，只有通过流程控制指令来改变eip寄存器中的值

寻址方式
    指令中给出的数据   立即数寻址
    数据在寄存器中     寄存器寻址
    数据在内存中       直接寻址    mov eax,[0040200h]
                       寄存器间接寻址 mov eax,[eax]
                       变址寻址 
                       基址变址寻址



翼云书
第六章 加密与解密
PE（Portable Executable）文件结构
DOS头
    IMAGE_DOS_HEADER
        第一个字段： e_magic  0x5A4D     
                #define IMAGE_DOS_SIGNATRE 0x5A4D   // MZ
        最后一个字段：e_lfanew 保存着nt头的起始位置
PE头 
    IMAGE_NT_HEADERS
        DWORD Signature   // PE标识符 4550 #define IMAGE_NT_SIGNATURE 0x00004550  //PE\0\0  
        IMAGE_FILE_HEADER  // 文件头
                
        IMAGE_OPTIONANL_HEADER  // 可选头  
节表
    
节表数据

'''
'''
栈
先进后出FILO
        

调试器
CreateProcessA()

'''