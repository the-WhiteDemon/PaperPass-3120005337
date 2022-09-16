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


