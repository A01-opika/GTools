import time, platform

###### Normal function definition ######

def IsPrime(n: int) -> bool:
    """
    判断给定的整数 n 是否为质数。
    
    参数:
    n -- int, 需要判断的整数
    
    返回:
    bool -- 如果 n 是质数返回 True，否则返回 False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def IsPal(n: any) -> bool:
    """
    判断给定的整数 n 是否为回文数。
    
    参数:
    n -- 可转换为str的类型
    
    返回:
    bool -- 如果 n 是回文数返回 True，否则返回 False
    """
    return str(n) == str(n)[::-1]

def IsArmstrong(n: int) -> bool:
    """
    判断给定的整数 n 是否为阿姆斯特朗数(自幂数)。
    
    参数:
    n -- int, 需要判断的整数
    
    返回:
    bool -- 如果 n 是阿姆斯特朗数返回 True，否则返回 False
    """
    s = str(n)
    l = len(s)
    tot = 0
    for i in range(l):
        tot += int(s[i]) ** l
    return tot == n

def IsHappy(n: int) -> bool:
    """
    判断给定的整数 n 是否为幸福数。
    
    参数:
    n -- int, 需要判断的整数
    
    返回:
    bool -- 如果 n 是幸福数返回 True, 否则返回 False
    """
    seen = set()
    while n!= 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return True

def IsEven(n: int) -> bool:
    '''
    判断给定的整数 n 是否为偶数.
    
    参数:
    n -- int, 需要判断的整数
    
    返回:
    bool -- 如果 n 是偶数返回 True, 否则返回 False
    '''
    if n % 2 == 0:
        return True
    else:
        return False

def IsPerfect(n: int) -> bool:
    """
    判断给定的整数 n 是否为完数。
    
    参数:
    n -- int, 需要判断的整数
    
    返回:
    bool -- 如果 n 是完数返回 True, 否则返回 False
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def gcd(x: int, y: int) -> int:
    """
    计算两个数的最大公约数。
    
    参数:
    x -- int, 第一个数
    y -- int, 第二个数
    
    返回:
    int -- 最大公约数
    """
    while y:
        x, y = y, x % y
    return x

def lcm(x: int, y: int) -> int:
    """
    计算两个数的最小公倍数。
    
    参数:
    x -- int, 第一个数
    y -- int, 第二个数
    
    返回:
    int -- 最小公倍数
    """
    return x * y // gcd(x, y)

def factorial(n: int) -> int:
    """
    计算 n 的阶乘。
    
    参数:
    n -- int, 需要计算阶乘的数
    
    返回:
    int -- n 的阶乘
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def ToAscii(s: str) -> list:
    """
    将字符串转换为 ASCII 码。
    
    参数:
    s -- str, 需要转换的字符串
    
    返回:
    list -- 转换后的 ASCII 码列表
    """
    AsciiCode = []
    for i in s:
        AsciiCode.append(ord(i))
    return AsciiCode

def ToString(AC: list) -> str:
    """
    将 ASCII 码列表转换为字符串。
    
    参数:
    AC -- list, 需要转换的 ASCII 码列表
    
    返回:
    str -- 转换后的字符串
    """
    s = ""
    for i in AC:
        s += chr(i)
    return s

def sprint(m, delay = 0.25):
    for i in m:
        print(i, end = "", flush = True)
        time.sleep(delay)

def LocalTime() -> list:
    # 获取当前本地时间的元组
    local_time_tuple = time.localtime()
    
    # 将元组中的时间信息提取到列表中
    TimeDict = {
        "year":local_time_tuple.tm_year,     # 年
        "month":local_time_tuple.tm_mon,     # 月
        "day":local_time_tuple.tm_mday,      # 日
        "hour":local_time_tuple.tm_hour,     # 时
        "minute":local_time_tuple.tm_min,    # 分
        "second":local_time_tuple.tm_sec     # 秒
    }
    return TimeDict

def TimeSubtract(time1: list, time2: list) -> int:
    # verity input
    if len(time1) != 2 or len(time2) != 2:
        raise ValueError("time format doesn't match, should be [hour, minute].")
    if not (0 <= time1[0] < 24 and 0 <= time1[1] < 60) or not (0 <= time2[0] < 24 and 0 <= time2[1] < 60):
        raise ValueError("time's hour should be between 0-23, minute should be between 0-59.")
    
    # change to total minutes
    total_minutes1 = time1[0] * 60 + time1[1]
    total_minutes2 = time2[0] * 60 + time2[1]
    
    # calculate difference
    difference = total_minutes1 - total_minutes2
    
    # return difference(in minutes)
    return difference

def DeRepeat(ls: list) -> list:
    return list(set(ls))

def NumberDigits(n: int) -> int:
    """
    计算一个整数的位数。
    
    参数:
    n -- int, 需要计算位数的整数
    
    返回:
    int -- 整数的位数
    """
    return len(str(abs(n)))

###### Error class definition ######
    """
    系统无法验证异常类。
    """
    def __init__(self):
        self.message = "系统无法识别。"
        super().__init__(self.message)

def NtoD(s: str) -> tuple:
    '''
    将一个数转化为十进制数。
    
    参数:
    s -- str, 待转换的n进制数
    
    返回:
    tuple -- (转换后的十进制数, 进制数, 原始输入)
    '''
    s = s.lower()  # 统一转小写处理
    try:
        if s.startswith('0x'):
            base = 16
            num = int(s, 16)
        elif s.startswith('0b'):
            base = 2
            num = int(s, 2)
        elif s.startswith('0'):
            base = 8
            num = int(s, 8)
        else:
            base = 10
            num = int(s)
    except ValueError as e:
        raise InputFormatError(f"无效的进制格式: {s}") from e
    
    return (num, base, s)

def DtoM(s: int, m: int) -> str:
    '''
    将一个十进制数转化为m进制数。
    
    参数:
    s -- int, 待转换的十进制数
    m -- int, 进制数
    
    返回:
    str -- 转换后的m进制数
    '''
    if m not in {2, 8, 10, 16}:
        raise InputFormatError("只支持2/8/10/16进制")
    
    prefix = {
        2: '0b',
        8: '0o',
        16: '0x'
    }
    
    if m == 10:
        return str(s)
    
    converted = format(s, f'#0{prefix[m]}0')  # 使用标准格式化方法
    return converted

def BinSearch(data: list, target: any) -> list:
    '''
    二分查找data列表中所有targets元素位置
    
    参数:
    data -- list, 待查找的列表
    targets -- any, 需要找的量, 类型推荐与list中元素的类型一致
    
    返回:
    list -- target在data中的所有位置索引
    '''
    # record data type
    data_type = type(data[0])
    # convert elements in data to int
    data = [int(i) for i in data]
    # convert target to int
    target = int(target)
    # main algorithm
    left, right = 0, len(data) - 1
    res = []
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            res.append(mid)
            left = mid + 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # convert res to data_type
    res = [data_type(i) for i in res]
    return res
    
###### Error class definition #######

class NegativeNumberFactorialError(Exception):
    """
    负数阶乘异常类。
    """
    def __init__(self, message):
        self.message = "负数阶乘无定义。"
        super().__init__(self.message)

class InputFormatError(Exception):
    """
    输入错误异常类。
    """
    def __init__(self, message):
        self.message = "输入参数有误。"
        super().__init__(self.message)

class QueueEmptyOutError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class QueueFullInError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class StackFullInError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
    	return self.message
    
class StackEmptyOutError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
    	return self.message

###### Lib supported func class definition ######

class Inf:
    def __init__(self, message = True):
        self.message = message    # 控制是否显示配置库信息
        self.system = ""
        if platform.system() == "Windows":
            self.system = "Windows"
        elif platform.system() == "Linux":
            self.system = "Linux"
        elif platform.system() == "Darwin":
            self.system = "MacOS"
        elif platform.system() == "Java":
            self.system = "Java"
        else:
            self.system = ""

    def info(self, use_sprint = False, sp_delay = 0.25):
        if use_sprint:
            if self.message:
                sprint(f"System: {self.system}", sp_delay)
                sprint('required Python version: 3.11 or later', sp_delay)
                sprint(f"Python version: {platform.python_version()}", sp_delay)
                # VVVVVVVVVVVVV 下方更改版本号 VVVVVVVVVVVVVV
                sprint("GTools V1.2.4", sp_delay)
                sprint("GLUE®. All rights reserved.", sp_delay)
            else:
                sprint(f"System: {self.system}", sp_delay)
        else:
            if self.message:
                print(f"System: {self.system}")
                print('required Python version: 3.11 or later')
                print(f"Python version: {platform.python_version()}")
                # VVVVVVVVVVVV 下方更改版本号 VVVVVVVVVVVVV
                print("GTools V1.2.4 2025(1).")
                print("GLUE®. All rights reserved.")
            else:
                print(f"System: {self.system}", sp_delay)

    def systemReturn(self):
        return self.system

class Queue:
    def __init__(self, size = 0):
        self.__private_items = []
        self.__private_size = size
    def qout(self):
        if len(self.__private_items) == 0:
            raise QueueEmptyOutError("Queue is empty")
        else:
            return self.__private_items.pop(0)
    
    def qin(self, item):
        if self.__private_size == 0 or len(self.__private_items) < self.__private_size:
            self.__private_items.append(item)
        else:
            raise QueueFullInError("Queue is full")
    
    def qcontent(self):
        return tuple(self.__private_items)
    
    def qlen(self):
        return len(self.__private_items)

class Stack:
    def __init__(self, size = 0):
        self.__private_items = []
        self.__private_size = size
    
    def sin(self, item):
        if self.__private_size == 0 or len(self.__private_items) < self.__private_size:
            self.__private_items.append(item)
        else:
            raise StackFullInError("Stack is full")
    
    def sout(self):
        if self.__private_items != []:
            return self.__private_items.pop()
        else:
            raise StackEmptyOutError("Stack is empty")
    def qcontent(self):
        return tuple(self.__private_items)
    
    def qlen(self):
        return len(self.__private_items)

class Log:
    def __init__(self, real_time = True, log_name = 'untitled.log'):
        self.real_time = real_time
        self.logs = []
        self.log_name = log_name
        self.log_colors = {
   			'error': '\033[0;31;m',  # 红色
    		'info': '\033[0;32;m',  # 绿色
    		'debug': '\033[0;34;m',  # 蓝色
    		'warning': '\033[0;33;m',  # 黄色
		}
        # 创建日志文件
        with open(f'{self.log_name}.log', mode = 'w'):
            pass
    def inf(self, message):
        if(self.real_time):
            self.logs.append(message)
            with open(f'{self.log_name}.log', mode = 'a') as f:
                f.write(f'{self.log_colors["info"]}[info]{message}\033[0m\n')
        self.logs.append(f'{self.log_colors["info"]}[info]{message}\033[0m')

    def err(self, message):
        if(self.real_time):
            self.logs.append(message)
            with open(f'{self.log_name}.log', mode = 'a') as f:
                f.write(f'{self.log_colors["error"]}[error]{message}\033[0m\n')
        self.logs.append(f'{self.log_colors["error"]}[error]{message}\033[0m')

    def dbg(self, message):
        if(self.real_time):
            self.logs.append(message)
            with open(f'{self.log_name}.log', mode = 'a') as f:
                f.write(f'{self.log_colors["debug"]}[debug]{message}\033[0m\n')
        self.logs.append(f'{self.log_colors["debug"]}[debug]{message}\033[0m')

    def wrn(self, message):
        if(self.real_time):
            self.logs.append(message)
            with open(f'{self.log_name}.log', mode = 'a') as f:
                f.write(f'{self.log_colors["warning"]}[warning]{message}\033[0m\n')
        self.logs.append(f'{self.log_colors["warning"]}[warning]{message}\033[0m')
    
    def show_logs(self, level = 'info'):
        # 查看所有level级别的日志
        if(level == 'info'):
            for log in self.logs:
                if(log.startswith(self.log_colors['info'])):
                    print(log)
        elif(level == 'error'):
            for log in self.logs:
                if(log.startswith(self.log_colors['error'])):
                    print(log)
        elif(level == 'debug'):
            for log in self.logs:
                if(log.startswith(self.log_colors['debug'])):
                    print(log)
        elif(level == 'warning'):
            for log in self.logs:
                if(log.startswith(self.log_colors['warning'])):
                    print(log)
        else:
            print('Invalid level')
    def save_logs(self):
        # 保存日志到文件
        with open(f'{self.log_name}.log', mode = 'a') as f:
            for log in self.logs:
                f.write(log+'\n')
