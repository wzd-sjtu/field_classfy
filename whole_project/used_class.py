# 本文件用于存储基本的数据结构和一些小巧的函数

class Single_Data:
    can_id = None
    time = None
    data_in_hex = None
    data_in_binary = None

# 这个大数据结构需要进行适当的改变
class Classfy_Results:
    classfy_begin_loc = None
    classfy_length = None
    classfy_class = None # 可以是0/1/2/3/4 分别代表const、multi-value、snesor、counter、no_meaning 五种类型

    classfy_value_type = None # type分为0和1  0表示某几个值，1表示取值范围
    # 使用列表是比较好的
    classfy_value_store = None # 这个是用来存储数据类型的，尽量提高判断的效率

    classfy_score = None # 合适的打分

hex2bin_map = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "A":"1010",
   "B":"1011",
   "C":"1100",
   "D":"1101",
   "E":"1110",
   "F":"1111",
}
def hex_str_to_binary_str(hex_str):
    tmp = ""
    for i in hex_str:
        tmp = tmp + hex2bin_map[i]
    return tmp


# 这段代码是选择最优解的核心逻辑
def choose_max(s1, s2, s3, s4):
    # 简单的优先级变化
    if s1 is not None:
        return s1
    if s2 is not None:
        return s2
    if s3 is not None:
        return s3
    if s4 is not None:
        return s4
    # return None
    # print("unhappy")
def choose_max_plus(s1, s2, s3, s4, s5):
    if s1 is not None:
        return s1
    if s2 is not None:
        return s2
    if s3 is not None:
        return s3
    if s4 is not None:
        return s4
    if s5 is not None:
        return s5