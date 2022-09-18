#软件工程第一次编程作业

|   这个作业属于哪个课程    |   [广工软件工程课程][班级的链接]  |
|   --  |   --  |
|   这个作业的要求在哪里    |   [个人项目作业-论文查重][作业的链接] |
|   这个作业的目标  |   1.学习并制作一个论文查重的软件</br> 2.学习单元测试</br>  3.学习性能分析及代码覆盖率</br>    4.学习PSP表格   |
|   GitHub链接  |   [论文查重代码仓库链接][仓库链接]    |
|   参考文献    |   1.参考文献1[参考文献链接1]</br> |

[toc]

##项目地址
[GitHub代码仓库链接][仓库链接]

##  PSP表格
|   PSP2.1  |   Personal Software Process Stages    |   预估耗时(分钟)  |   实际耗时(分钟)  |
|   ----  |   ----  |   ----    |   ----    |
|   **Planning**    |   **计划**    |   **10**  |   **20**  |
|   Estimate    |   估计这个任务需要多长时间    |   10  |   20  |
|   **Development** |   **开发**    |   **270** |   **310** |
|   Analysis    |   需求分析(包括学习新技术)    |   60  |   70  |
|   Design Spec |   生成设计文档    |   15  |   10  |
|   Design Review   |   设计复审    |   15  |   15  |
|   Coding Standard |   代码规范(为目前的开发制定合适的规范)    |   10  |   10  |
|   Design  |   具体设计    |   45  |   45  |
|   Coding  |   具体编码    |   45  |   45  |
|   Code Review |   代码复审    |   20  |   20  |
|   Test    |   测试(自我测试，修改代码，提交修改)  |   60  |   95  |
|   **Reporting**   |   **报告**    |   **50**  |   **65**  |
|   Test Report |   测试报告    |   30  |   45  |
|   Size Measurement    |   计算工作量  |   10  |   10  |
|   Postmortem & Process Improvement Plan   |   事后总结，并提出过程改进计划    |   10  |   10  |
|   |   合计    |   330 |   395 |

##  设计与实现
####    Python中的jieba包
jieba是目前表现不错的Python中文分词组件。调用Python中的jieba包以对文本进行分词。
详细介绍：[基于python中jieba包的详细使用介绍][jieba介绍链接]

*   使用到的接口jieba.lcut
>   默认采用精准模式，该模式下会试图将句子最精准地切开，适合文本分析(使用方法可在介绍链接中查看)，而使用lcut将返回list类型。

####    Python中的re模块
在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个Python自带模块，名为re。
详细介绍：[python——正则表达式(re模块)详解][re介绍链接]

*   使用到的接口re.match
>   功能：对字符串中的字符进行匹配
>   语法：re.match(pattern,string,flags=0)
>   其中，pattern为要匹配的正则表达式，string为即将进行匹配的字符串，flags为标志位，默认为0。
```Python
import re
str = string
#匹配字符串中的字母、数字、汉字，直到其他字符出现
result = re.match("[a-zA-Z0-9\u4e00-\u9fa5]*",str,flags = 5) 
print(result.group())
```

####    Python中的Gensim库
Gensim是在做自然语言处理时较为经常使用到的一个工具库，主要用来以无监督的方式从原始的非结构化文本当中来学习到文本隐藏层的主题向量表达。
详细介绍：[Gensim库的使用——Gensim库的核心概念介绍][Gensim介绍链接]
这里主要使用到的是Gensim库中的语料库(Corpus)。
引用方法为
```Python
import Gensim.corpora
```
详细使用：[【python】gensim corpora的简单使用][corpora使用链接]
*   使用到的接口Gensim.corpora.Dictionary
>   用法：生成词典
>   语法：dictionary = gensim.corpora.Dictionary([word_list1,word_list2]) 
>   利用list1和list2生成一个词典

例如

```Python
# 导入模块
from gensim import corpora
from pprint import pprint  # 格式化输出

# 三个存放分好词的文本列表
word_list1 = ['我', '来自', '中国', '我']
word_list2 = ['我们', '来自', '火星']
word_list3 = ['你', '来自', '何方']

# 利用list1和list2生成一个词典
dict = corpora.Dictionary([word_list1, word_list2])
print('由list1和list2生成的词典：')
print(dict)
dict.add_documents([word_list3])
print('由list3拓展生成的词典：')
print(dict)

dict.save('test.dict')  # 保存字典
dict = corpora.Dictionary.load('test.dict')  # 加载字典
```
运行结果
```Python
由list1和list2生成的词典：
Dictionary<5 unique tokens: ['中国', '我', '来自', '我们', '火星']>
由list3拓展生成的词典：
Dictionary<7 unique tokens: ['中国', '我', '来自', '我们', '火星']...>
```

*   使用到的接口dictionary.doc2bow
>   用法：将词典列表转换成稀疏词袋向量
>   语法：bow = dictionary.doc2bow(list)

例如
```Python
word_bow1 = dict.doc2bow(word_list1, allow_update=False)  #词袋[(id,num)],稀疏向量
word_bow2 = dict.doc2bow(word_list2) #将词列表转换成稀疏词袋向量
word_bow3 = dict.doc2bow(word_list3) #将词列表转换成稀疏词袋向量
print ('word_bow1:', word_bow1)
print ('word_bow2:', word_bow2)
print ('word_bow3:', word_bow3)
corpus = [word_bow1, word_bow2, word_bow3] #由词袋向量组成的列表构成语料
print(corpus)
```
运行结果
```Python
word_bow1: [(0, 1), (1, 2), (2, 1)]
word_bow2: [(2, 1), (3, 1), (4, 1)]
word_bow3: [(2, 1), (5, 1), (6, 1)]
[[(0, 1), (1, 2), (2, 1)], [(2, 1), (3, 1), (4, 1)], [(2, 1), (5, 1), (6, 1)]]
```
*   使用到的接口Gensim.similarities.Similarity
>   用法：用于计算余弦相似度

####    程序实现思路
调用jieba.lcut对各文本进行分词→调用re.match进行匹配→调用Gensim.corpora.Dictionary生成词典→调用dictionary.doc2bow转换成稀疏词袋向量→调用Gensim.similarities.Similarity计算余弦相似度得出结果

####    关键函数

*   jieba分词及匹配
```Python
def str_filter(str):
    str = jieba.lcut(str) #对文本进行jieba分词
    result = []   #用于存储分词结果
    for tags in str:
        if(re.match(u'[a-zA-Z0-9\u4e00-\u9fa5]',tags)):  #对字母a-z，A-Z，数字0-9，汉字进行保存
            result.append(tags)
        else:pass
    return result
```

*   计算余弦相似度
```Python
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
```

##  性能分析

![性能分析图](性能分析图地址)
主要调用的是库函数

##  单元测试

*   第一个单元测试unit_test.py
```Python
import unittest
import src.main as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.calcuate_similarity(['这是', '一个', '软件工程', '作业', '的', '测试用例'],
                                                  ['这是', '一个', '软件工程', '的', '测试用例']), 0.912871)


if __name__ == '__main__':
    unittest.main()
```
测试结果
![单元测试1结果图](unit_test结果截图)

*   第二个单元测试unit_test2.py
```Python
import unittest
import src.main as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.calcuate_similarity(['今天','是','星期天','天气','晴','今天','晚上','我','要去','看电影'],
                                                  ['今天','是','周天','天气','晴朗','我','晚上','要去','看电影']),0.76980036)  # add assertion here


if __name__ == '__main__':
    unittest.main()
```
测试结果
![单元测试2结果图](unit_test2结果截图)

##  异常模块
当所在路径的文件不存在时，程序会出现异常，因此添加该模块检查文件是否存在。
```Python
    #异常模块
    if not os.path.exists(original_file):
        print("论文原文文件不存在")
        exit(0)
    if not os.path.exists(add_file):
        print("论文抄袭版文件不存在")
        exit(0)
```

##  覆盖率
文本