import os.path
import re
import gensim.corpora
import jieba

# 获取指定路径的文件内容
def get_file_contents(path):
    str = ''
    f = open(path,'r',encoding='UTF-8')   #打开文件
    line = f.readline()   #读取当前行
    while line:
        str = str + line  #拼接文本
        line = f.readline()  #读取下一行
    f.close()  #关闭文件
    return str  #返回文本

# 将文本进行jieba分词
def str_filter(str):
    str = jieba.lcut(str) #对文本进行jieba分词
    result = []   #用于存储分词结果
    for tags in str:
        if(re.match(u'[a-zA-Z0-9\u4e00-\u9fa5]',tags)):  #对字母a-z，A-Z，数字0-9，汉字进行保存
            result.append(tags)
        else:pass
    return result

#计算余弦相似度
def calcuate_similarity(text1,text2):
    #计算文本中每个单词出现的频率
    texts = [text1,text2]
    dictionary = gensim.corpora.Dictionary(texts) #生成两个文本的词典
    corpus = [dictionary.doc2bow(text) for text in texts] #将两个词列表转换成稀疏词袋向量
    #计算余弦相似度
    similarity = gensim.similarities.Similarity(None,corpus=corpus,num_features=len(dictionary))
    text_corpus = dictionary.doc2bow(text1)
    cosine_similarity = similarity[text_corpus][1]
    cosine_similarity =float("%.8f"%cosine_similarity)
    return cosine_similarity

if __name__ == '__main__':
    #给出文件的绝对路径
    original_file = 'E:\软件工程作业\PaperPass-3120005337\作业要求测试文本/orig.txt'
    add_file = 'E:\软件工程作业\PaperPass-3120005337\作业要求测试文本/orig_0.8_add.txt'
    answer_file = 'E:\软件工程作业\PaperPass-3120005337/answer.txt'
    #异常模块
    if not os.path.exists(original_file):
        print("论文原文文件不存在")
        exit(0)
    if not os.path.exists(add_file):
        print("论文抄袭版文件不存在")
        exit(0)
    #读取文件
    original_str = get_file_contents(original_file)
    add_file = get_file_contents(add_file)
    #对文本进行jieba分词
    original_str_filter = str_filter(original_str)
    add_str_filter = str_filter(add_file)
    #计算余弦相似度
    cosine_similarity = calcuate_similarity(original_str_filter,add_str_filter)
    print("文章相似度：%.8f"%cosine_similarity)
    #将结果写入answer.txt文件中
    f = open(answer_file,'w',encoding="UTF-8")
    f.write("文章相似度：%.8f"%cosine_similarity)
    f.close()
    print("文件写入完成")










