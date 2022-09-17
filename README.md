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
    



