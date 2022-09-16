import re
import gensim.corpora
import jieba

# 获取指定路径的文件内容
def get_file_contents(path):
    str = ''
    f = open(path,'r',encoding='UTF-8')   #打开文件
    line = f.readline(    #读取当前行
    while line:
        str = str + line  #拼接文本
        line = f.readline()  #读取下一行
    f.close()  #关闭文件
    return str  #返回文本

# 将文本进行jieba分词
def filter(str):
    str = jieba.lcut(str) #对文本进行jieba分词
    result = []   #用于存储分词结果
    for tags in str:
        if(re.match(u"[a-zA-Z0-9\u4e00-u9fa5]",tags)):  #对字母a-z，A-Z，数字0-9，汉字进行保存
            result.append(tags)
        else:pass




