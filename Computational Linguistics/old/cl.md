# 计算语言学基础理论

<br>
渤海大学文学院

朱波

zhubo812@gmail.com

----
### 成绩评定
1. 平时成绩：作业+出勤（30%）
2. 期末作业（70%）
----

### 学习目标

1. 具备<font color = yellow>以计算机为背景思考语言学问题</font>，对<u>语言知识</u>进行<font color = yellow>形式化描述</font>的能力；
2. 了解计算语言学的基本理论和自然语言处理中的常用模型及算法，初步具备从事相关领域研究工作的能力。

----

### 主要参考书目

1. Introduction to Natural Language Processing, Harris,M.D.,Reston Publishing Co.,1985

2. Speech and Language Processing, Jurafsky, D.&Martin,J.H., PrenticeHall,2000(中译本：自然语言处理综论，冯志伟等译，电子工业出版社，2005)

3. Foundations of Statistical Natural Language Processing, Manning, C.D.&Schütze, The MIT press, 1999(有中译本)

4. Natural Language Understanding,Allen,J.,TheBenjamins/CumminsPublishingCo.,1994(有中译本)

----

5. Natural Language Processing: An Introduction to Computational Linguistics, Gazdar, G.&Mellish, C.,AddisonWesley,1989.
6. 计算语言学概论，俞士汶主编，商务印书馆，2003.
7. 现代汉语语法信息词典详解，俞士汶等，清华大学出版社，2003
8. 自然语言理解，姚天顺，清华大学出版社，2002
9. 自然语言处理技术基础，王晓捷、常宝宝，北京邮电大学出版社，2002
----
10. 计算语言学，刘颖，清华大学出版社，2002
11. 计算语言学基础，冯志伟，商务印书馆，2001
12. 计算语言学导论，翁富良、王野翊，中国社会科学出版社，1998
13. 自然语言的计算机处理，冯志伟，上海外语教育出版社，1997
14. 自然语言处理，刘开瑛、郭炳炎，科学出版社，1991

----
### 相关学术期刊
1. Computational Linguistics
2. Machine Translation
3. International Journal of Corpus Linguistics
4. 中文信息学报(中文信息学会)
5. 计算机学报
6. 软件学报
7. 汉语语言与计算学报
----
###  相关学术会议
1. [Annual Meeting of the Association for Computational Linguistics(ACL)](https://www.aclweb.org/anthology/)
2. International Conferenceon Computational Linguistics(COLING)
3. 全国计算语言学联合学术会议(JSCL)[CCL历年论文集,NLP-NABD历年论文集](http://cips-cl.org/anthology)
4. 全国学生计算语言学研讨会(SWCL)

---

### 课程内容
1. [概述](#/2)
2. [基本概念](#/3)
3. [形式语言与自动机](#/4)
4. [语言模型](#/5)
5. 自动分词与词性标注
6. 句法分析
7. 语法理论
8. 语义计算
9. 机器翻译

---




## 概述

1. [计算语言学的性质及特点](#/2/1)
2. [计算语言学的发展及学科位置](#/2/59)

[>](#/2/84)

----
### 计算语言学的性质及特点
1. 计算语言学的<font color = yellow>定义</font>
2. 计算语言学的<font color = yellow>特点</font>
3. 计算语言学的<font color = yellow>研究方法</font>
4. 计算语言学对人们<font color = yellow>语言观的影响</font>

----
#### 定义


计算语言学的中心任务是开发研制出一种人类能用自己的语言与之自由交谈的智能计算机。

——(德国计算语言学家 Roland Hausser,*Foundations of Computational Linguistics*）

----
Question

计算机能理解、会思维吗？
----
英国天才的数学家、计算机科学家图灵（Turing）提出了“图灵测试”,即,如果有<font color = yellow>超过30%的测试者不能确定出被测试者是人还是机器</font>，那么这台机器就通过了测试，并被认为具有人类智能。

![timg](pic/timg.jpg)

----
根据“图灵测试”的思想，计算机如果做到了下面四条中的一条，就可以认为它是智能的：
1. 问答（question-answering）
2. 生成文摘（summarizing）
3. 释义（paraphrase）
4. 翻译（translation）

----
#### 定义

计算语言学是通过建立形式化的计算模型，用计算机分析处理、理解并生成自然语言的学科。
----
自然语言生成（Nature Language Generation,NLG）

自然语言生成从知识库或逻辑形式等等机器表述系统去生成自然语言,可以说是一种将资料转换成自然语言表述的翻译器。
----
NLG一般通过多个子任务来解决问题。 一般可以分为以下六类：
1. 内容确定（Content determination）：决定在建文本中包含哪些信息；

2. 文本结构（Text structuring）：确定将在文本中显示的信息；

3. 句子聚合（Sentence aggregation）：决定在单个句子中呈现哪些信息；
----
4. 词汇化（Lexicalisation）：找到正确的单词和短语来表达信息；

5. 引用表达式生成（Referring expression generation）：选择单词和短语以识别域对象；

6. 语言实现（Linguistic realisation）：将所有单词和短语组合成格式良好的句子。
----
对计算语言学，也有广义和狭义两种理解。上述是狭义的理解。

广义的计算语言学不仅包括上述内容，还包括利用计算机研究自然语言的有关问题，如风格统计、词语计量研究等等。

----
| 作者   | 句平均词数 | 句平均字数 | 平均词长 |
| ------ | ---------- | ---------- | -------- |
| 巴金   | 24.75      | 40.65      | 1.642    |
| 倪海曙 | 15.79      | 24.05      | 1.523    |

----
《静静的顿河》的作者是…肖洛霍夫？克留柯夫？

1. 平均句长
2. 句长分档，每档百分比
3. 不同词类统计
4. 不同词类在句中的顺序
5. 某些词汇特点的统计
6. 比较样品中使用一次、二次、三次……的词
----
《红楼梦》的作者是一个人？还是两个人？

1. 上下文相关性（型例比/种次比）
2. 不同字符数的统计
3. 字符串的统计

----

##### 统计结果：
1. 前八十回<后四十回
2. 前八十回>后四十回
3. 前八十回双音节字符串<单音节字符串，后四十回双音节字符串>单音节字符串

----
##### 结论
作者应该是两个人

----
#### 语言计量研究的基本概念

- 词种（type）
- 词次（token）

----
句子“我明天要去上海看世博会，你去不去？” 的<font color = yellow>词种数</font>和<font color = yellow>词次数</font>分别是多少？
----
- 词种：9
- 词次：11
----
字符种？字符次？

----
#### 语言计量研究涉及的问题

1. 计量研究的目标是什么？
目标决定对象、方法和过程。

2. 如何得到数据？
需要掌握各种统计工具、计算方法。

3. 如何对数据进行分析？
综合运用各种知识挖掘数据背后潜藏的东西。

----
#### 计算语言学的特点

----
计算语言学的特点1

**元语言的形式化**
----
对象语言与元语言：

- 对象语言，就是你所要研究的那种语言;
- 元语言，是指研究者在研究描述对象（语言）时使用的语言。

----
**元语言的形式化**
1. 用自然语言作元语言的缺陷是歧义太多。
2. 数学公式、逻辑符号等都是形式化的元语言。
3. 形式化的元语言是人和计算机沟通的必要途径。
4. 计算语言学研究的是元语言应该如何设计才能更好地描述对象语言里的规律，而且计算机能够读懂。

----
**规则描述语言**

1. 一|这|那/Q1/ (a)/ n* = N4 [NP>N1 N2 of N3 N4]
2. a)/ n|r* = N2 [NP > N1 N2]
3. d/ a* = N2 [a > N1 N2]



----
计算语言学的特点2

**可操作性**

----
<font color = yellow>可操作性</font>是计算语言学最根本、最关键的方法论原则就是要指出各种语言形式出现和变换的条件。
----
所谓的<font color = yellow>条件</font>和与之想关联的<font color = yellow>动作</font>是一切计算机工作的最基本的方式，也是建立计算语言学语法的最基本、最关键的公式。
----
计算语言学的研究手段是计算，计算的<font color = yellow>表现形式</font>是算法。

算法是对解题方法的精确描述,可表示为一组有穷的操作规则。
1. 通用性：算法是针对一类问题的
2. 机械性：算法的每一步骤都是确定的
3. 有限性：算法必须在有限步骤内结束
4. 离散性：算法的输入及输出数据都是离散符号
----
N+N短语

- 偏正关系：学校图书馆、木头桌子
- 并列关系：工人农民、爸爸妈妈
- 复指关系：首都北京、鲁迅先生
- 主谓关系：今天星期二、鲁迅浙江人
----
今天星期六、今天三八节（主谓）

今天下午，今年三八节（偏正）？
----

计算语言学的特点3

**工程性**
----
1. 机器翻译（Machine Translation）
2. 文本分类（Text Classification）
3. 自动文摘（Automatic Text Abstraction）
4. 信息检索（Information Retrieval）
5. 信息提取（Information Extraction）
6. 语音合成（Speech Synthesis）
7. 语音识别（Speech Recognition）
8. ……
----
从本质上说，计算语言学是一门实验性、工程性的学科。
----
计算语言学的特点4

**语言研究的全局性、一般性**
----
歧义现象

- 咬死了猎人的狗（动宾/偏正，实例歧义）
- 咬死了猎人的鸡（动宾）
- 咬死了鸡的老虎（偏正）

VP + NP1 + 的 + NP2（格式歧义、潜在歧义）
----
#### 计算语言学的特点
1. 元语言的形式化
2. 可操作性
3. 工程性
4. 语言研究的全局性、一般性

----
#### 计算语言学的研究方法
----
1. 规则驱动的方法
2. 数据驱动的方法
3. 二者融合的方法

----
规则驱动的方法
1. 研究人员（例如语言学家）对语言的规律进行总结，形成规则形式的知识库。
2. 研制语言处理算法，利用这些规则对自然语言进行处理。
3. 研究人员根据处理结果，调整规则，改进处理效果。
----

根据如下6条规则，分析句子“The boy saw the girl with a telescope.”，并画出树形图。


1. `$S\rightarrow NP+VP$`
2. `$NP\rightarrow DET+N$`
3. `$NP\rightarrow NP+PP$`
4. `$VP\rightarrow VP+PP$`
5. `$VP\rightarrow V+NP$`
6. `$PP\rightarrow P+NP$`

----
<font color = yellow>规则驱动的方法的问题</font>

All grammar leak(Sapir1921)认为：

对于自然语言而言，不大可能写出一部完备的规则集，语言规则有很强的伸缩性。
一般而言，很多基于规则的系统不能满足真实语言文本处理的要求，而只能处理真实语言的某个很小的子集。
----
数据驱动的方法（统计方法）
----

All grammar leak(Sapir1921)

1. 建立可以反映语言使用情况的语料库；
2. 研究人员对自然语言进行统计；
3. 建模利用统计技术或机器学习技术，基于语料库训练统计语言模型；
4. 利用得到的模型设计算法对语言进行处理；
5. 根据处理效果改进模型，提高处理性能。

----

在数据驱动的方法中，语言模型通常体现为一组参数，这些参数通常表示某个语言形式发生的概率值。

对一个由三个词构成的字符串来说，其发生的概率可以表示为：`$P(w_3|w_1,w_2)$`

----
判断“今天是周末”和“今天是课堂”哪个句子概率大?

𝑃(周末│今天是)>𝑃(课堂│今天是)

----
<font color = yellow>数据驱动的方法（统计方法）的问题</font>

数据驱动的方法忽视了语言的深层结构。

----
二者融合的方法

1. 融合规则驱动、数据驱动的优劣不能简单评价
2. 很多研究人员（包括知名计算语言学家）建议如此
3. 已经提出了一些策略，但如何结合尚须进一步探索

----
两种方法的区别
----
1. 对研究对象语言知识的认识不同。

- 规则方法：语言知识在人的大脑里，即人的语言能力；(<font color = yellow>语言</font>)
- 统计方法：语言知识在语言数据之中。(<font color = yellow>言语</font>)

----
2. 获取语言知识的方法和途径不同。
- 规则方法：用内省方法，建立形式化的知识系统描述语言知识；
- 统计方法：用语料库方法，根据对语言数据的统计得到语言知识。
----
3. 使用语言知识K构建语言处理系统时使用的算法不同。

- 规则方法：发展出许多比较成熟的算法技术；
- 统计方法：主要使用概率统计模型的自然语言处理算法。
----
4. 对语言事实的评价不同。

- 规则方法：基于乔姆斯基的语言原则，语句是<font color = yellow>正确的/错误的</font>；
- 统计方法：基于先农(Shannon)的信息论,语句是<font color = yellow>常见的/罕见的</font>。

----
#### 计算语言学对人们语言观的影响
----
传统的语言观

- 语言是人类最重要的交际工具；
- 语言是一个符号系统。
----
 新的语言观

- 语言是人类最重要的交际工具；
- 语言是人类和计算机共同的表达知识、传递信息、实施控制的符号系统。
----
新的语言观

1. 语言是人类和计算机的共同的交际工具；
2. 语言是表达知识的最有效方法；
3. 语言是传递信息的最主要的载体；
4. 语言是实施控制的最方便的手段；
5. 语言是一个多层面的符号系统。
	- 语构层面:符号与符号之间的形式结构关系---句法学；
	- 语义层面:符号与其所指之间的意义关系---语义学；
	- 语用层面:符号与使用者之间的效用关系---语用学。
----
小结

1. [计算语言学的定义](#/2/6)
2. [语言计量研究的基本概念](2/16)
3. [计算语言学的特点](#/2/37)
4. [计算语言学的研究方法](#/2/39)
5. [新的语言观](#/2/56)
----
### 计算语言学的发展和学科位置
----
#### 计算语言学的发展

计算语言学的历史可以大致分为萌芽期、发展期和繁荣期三个阶段。

----
**1. 萌芽期**(1956年以前)

- <圣经•创世纪>巴别塔
- 20世纪30年代初，法国科学家阿尔楚尼（Artsouni）的“机械脑”（mechanicalbrain）;
- 1933年，苏联发明家特洛扬斯基（Tроянский）设计了语言翻译机.
- 1946年，美国宾夕法尼亚大学的埃克特（J.P.Eckert）和莫希来(J.W.Mauchly)设计并研制出世界上第一台电子计算机爱尼亚克(ENIAC)。
- 同年，美国洛克菲勒基金会副总裁韦弗(W.Weaver)和英国工程师布斯(A.D.Booth)在讨论电子计算机的应用范围时，就谈到了利用计算机进行语言自动翻译的想法。
----
- 1949年，韦弗发表题为《翻译》的备忘录，正式提出机器翻译问题。
- 1954年，美国乔治敦大学&IBM公司，用IBM-701计算机，进行了世界第一次机器翻译试验，把几个简单的俄语句子翻译成英语。

----
**机器翻译(Machine Translation,简称MT）**

机器翻译是利用计算机把一种语言的语句自动地转换为语义与之完全相同的另一种语言的语句。

----
| 源文   | 正确的译文 | 机器的译文 |
| ------ | ---------- | ---------- |
| How are you?   | 你好吗？      | 怎么是你？      |
| How old are you? | 你多大了？     | 怎么老是你      |

----

**2. 发展期(1957-20世纪70年代初)**


早期：<font color = yellow>关键词</font>匹配为主流

- [1968年维金鲍姆（J·Weizenbaum）的ELIZA系统 （模拟心理医生、能与患者谈话的系统）](http://www.manifestation.com/neurotoys/eliza.php3)
----
中后期：以<font color = yellow>句法-语义分析</font>技术为主流

- 维诺格拉德于1972年在美国麻省理工学院建成著名的SHRDLU系统（积木世界）。 
----
![SHRDLU系统（积木世界）](
pic/SHRDLU.jpg)

下面是 SHRDLU系统中人和计算机之间的一段对话：
- <font color = yellow>Person</font>: Pick up a big red block.
	- <font color = red>Computer</font>: Ok. (does it)
- <font color = yellow>Person</font>: Grasp the pyramid.
	- <font color = red>Computer</font>: I don't understand which pyramid you mean.
- <font color = yellow>Person</font>: Find a block which is taller than the one you are holding and put it into the box.
	- <font color = red>Computer</font>: By "it", I assume you mean the block which is taller than the one I am holding.
----
商克(Schannk)及其学生于1973年在斯坦福大学 建成MARGIE系统。 

MARGIE系统能以推理或释义两种方式运行。在推理方式下，它接受一个输入句，然后利用 推理器生成这个句子所蕴涵的事实。
----

输入 <font color = yellow>John gave Mary some aspirin. </font>（约翰给玛丽一些阿司匹林。）


系统就可以作出推理： <font color = yellow>John believes Mary wants an aspirin. Mary is sick.</font> （约翰相信玛丽需要阿司匹林。玛丽病了。）

----
**在释义方式下，它将以尽可能多的等价方式来复 述输入的句子。**

- 如输入<font color = yellow>John killed Mary by chokingher.</font>(约翰扼杀了玛丽。)

- 系统就会复述出如下的句子：
	- <font color = yellow>John strangled Mary.</font>(约翰勒死了玛丽。) 
	- <font color = yellow>John choked Mary and she died because she was unable to breathe. </font>(约翰扼住玛丽的脖子，她因为不能呼吸就死了。）

----
李家治、陈永明等人建成的“古汉语机器理解系统——ACLUS”。

ACLUS能分析句法，能把《郑人买履》、《刻舟求剑》文言译成现代汉语，并回答故事中的语法和词义问题。
----

- <font color = yellow>问</font>：‘先度其足’中的‘度’是什么意思？ 
	- <font color = red>答</font>：‘度’是动词，是测量某种东西尺寸的意思。 
- <font color = yellow>问</font>：‘吾忘持度’中的‘度’是什么意思？ 
	- <font color = red>答</font>：‘度’是名词，是尺寸的意思。

----
范继淹、徐志敏等人建成的“TK——84汉语人机 对话实验系统”。这是一个铁路客运咨询系统。

- <font color = yellow>问</font>：从北京到大连有高铁吗？
	- <font color = red>答</font>：有。 
- <font color = yellow>问</font>：开往沈阳的快车都有卧铺吗？ 
	- <font color = red>答</font>：11次没有卧铺，其他都有。 
- <font color = yellow>问</font>：11次为什么没有卧铺？ 
	- <font color = red>答</font>：11次8点从北京开，18点49分到沈阳，卧铺没有必要。

----
**发展期理论建设方面的成果**

- 英国数学家图灵(A·M·Turing)与美国语言学家乔姆斯基 (N·Chomsky)的贡献

----
**发展期句法分析方面的成果**

- 乔姆斯基的<font color = yellow>短语结构语法</font>（phrase structure grammar，简称PSG）
- 伍兹的<font color = yellow>扩充转移网络</font>(augemented transition network,简称ATN)； 
- 卡普兰等的<font color = yellow>词汇功能语法</font>（Lexical-functional grammar，简称 LFG）； 马丁·凯依的<font color = yellow>功能合一语法</font>(functional unificational grammar，简称 FUG)；
- 盖兹达等的<font color = yellow>广义短语结构语法</font>(generalized phrase structure grammar,简称GPSG)等等。

----
**发展期语义分析方面的成果**

- 菲尔摩的<font color = yellow>格语法</font>（case grammar); 
- 威尔克斯的<font color = yellow>优选语义学</font>(preference semantics)
- 商克的<font color = yellow>概念依存理论</font>(Conception Dependency Theory, 简称CD理论)  
----

发展期的计算语言学逐渐融入了<font color = yellow>人工智能</font>的研究领域。研究方法上出现了<font color = yellow>基于规则</font>和<font color = yellow>基于统计(概率)</font>两种思想，并形成了两大阵营。

- 基于规则方法的<font color = yellow>符号派</font>(symbolic)
- 基于统计方法的<font color = yellow>随机派</font>(stochastic)。
----
- 以Chomsky为代表的符号派学者开始了形式语言理论和生成句法的研究，20世纪60年代末又进行了形式逻辑系统的研究。

- 随机派学者采用基于贝叶斯方法的统计学研究方法。但由于在人工智能领域中，这一时期多数学者注重研究推理和逻辑问题，只有少数学者在研究基于概率的统计方法和神经网络。因此，这一时期基于规则方法的研究明显多于基于概率方法的研究。
----
随着研究的深入，人们发现计算语言学的很多应用在短时间内无法解决，而的新问题新需求又不断地涌现。因此，计算语言学研究受到较大影响。从70年代开始，计算语言学的很多研究领域进入了低谷时期。
但尽管如此，计算语言学仍然在这期间取得了一些成果。例如，
- <font color = yellow>基于隐马尔可夫模型</font>(Hidden Markov Model, HMM);
- <font color = yellow>话语分析</font>(Discourse Analysis)。

之后，由于计算语言学研究者对于过去的研究进行了总结，有限状态模型和经验主义研究方法也开始复苏。

----
**3. 繁荣期**(20世纪70年代中后期-20世纪80年代末)

 繁荣期主要以<font color = yellow>机器翻译</font>的出现及发展为标志
----

- 1976年，加拿大蒙特利尔大学与加拿大联邦政府翻译局联合开发的实用性英法机器翻译系统TAUM-METEO正式投入使用，提供天气预报的翻译服务。
- 美国的SYSTRAN系统
- 日本富士通公司的ATLAS系统
- 德国西门子公司与美国德克萨斯大学联合开发的METAL系统
----
- 1988年由中国军事科学院开发、中国计算机软件与技术公司投入 市场的第一个机器翻译系统“译星1号”实现了商品化
- 中国社科院与北京高立公司联合开发的“高立英汉机器翻译系统”
- 中科院计算所开发的“863-IMT/EC智能型英汉机器翻译系统”
- 先是国防科技大学开发、后由深圳桑夏公司进一步开发的“桑夏译王英汉机器翻译系统”

----

**4. 融合期发展期**(20世纪90年代至今）

20世纪90年代中期以后，计算机的处理速度和存储量等<font color = yellow>硬件</font>性能大幅提升，为计算语言学改善了物质基础，使得语言处理的商品化开发成为可能；

此外，1994年Internet商业化和同期<font color = yellow>网络技术</font>的发展使得基于自然语言的信息检索和信息抽取的需求变得尤为重要。

----
**Milestone**
- 2003年 [神经概率语言模型](#/2/85)
- 2008年 [多任务学习](#/2/88)
- 2013年 [词嵌入](#/2/92)
- 2013年 [NLP中的神经网络](#/2/94)
- 2014年 [序列到序列模型](#/2/107)
- 2015年 [注意力机制](#/2/110)
- 2015年 [基于记忆的神经网络](#/2/114)
- 2018年 [预训练语言模型](#/2/116)
----

<font color = yellow>神经概率语言模型（Neural Probabilistic language models）</font>

神经网络（Neural Network, NN）被应用于语言建模之前,主流语言模型是N-Gram模型，利用前面n个词语预测下一个单词。
神经网络语言模型引起广泛关注是在[Bengio et al. (2003)](https://jmlr.csail.mit.edu/papers/volume3/bengio03a/bengio03a.pdf)提出前向神经网络（Feed-forward Neural Network, FNN）语言模型之后.

[<](#/2/84)
----
神经概率语言模型以某个词语前面的n个词语作为输入向量。这样的向量现在被称为词嵌入（word embeddings）。这些词向量入被连接并输入隐含层，然后再将隐含层结果输入softmax层。


[<](#/2/84)
----
![nlm](pic/nlm.jpg)
----

<font color = yellow>多任务学习（Multi-task learning）</font>

多任务学习是在多个任务下训练的模型之间共享参数的方法。在神经网络中，这可以通过绑定不同层的权重来轻松完成。多任务学习的想法于年由Rich Caruana(1993)首次提出，
[Collobert,Jason(2008)](https://ronan.collobert.com/pub/matos/2008_nlp_icml.pdf)首次将多任务学习应用于NLP。在多任务学习框架下，词嵌入矩阵被两个在不同任务下训练的模型共享。

----
![mtl](pic/mtl.png)

----
共享词嵌入使模型能够在词嵌入矩阵中协作并共享一般的低级信息，这类信息常构成模型中大部分的参数。

[Collobert,Jason(2008)](https://ronan.collobert.com/pub/matos/2008_nlp_icml.pdf)证明了共享词嵌入在多任务学习中的应用，引领了诸如预训练词嵌入和使用卷积神经网络（CNN）相关的方法，他们因此获得了2018年机器学习国际会议（ICML）的“时间测试”奖。
----
多任务学习应用于多项NLP任务，实际应用中通常预先定义共享参数，然后通过参数优化学习到不同的共享模式。随着NLP各项任务对模型的泛化能力有更高的要求，使得多任务学习越来越重要。

[<](#/2/84)
----
<font color = yellow>词嵌入（Word embeddings）</font>

[Bengio et al. (2003)](https://jmlr.csail.mit.edu/papers/volume3/bengio03a/bengio03a.pdf)证明使用神经网络训练的语言模型可以生成更好的词向量,并且提出了很多优化训练的方法。

[Mikolov et al. (2003)](https://arxiv.org/pdf/1310.4546.pdf)通过删除隐含层和近似目标来使这些词嵌入的训练更有效。
----
<font color = yellow>word2vec--高效的词嵌入工具</font>

word2vec包含两种模式：

1. CBOW（continuous bag-of-words）
2. skip-gram

两种模式的目标不同：一个基于周围的单词预测中心词，而另一个则相反。

[<](#/2/84)
----
<font color=yellow>Neural networks for NLP</font>

2013、2014期间神经网络模型逐渐在NLP任务中广泛采用。主要有以下三种类型：

- 卷积神经网络（Convolutional Neural Networks）
- 循环神经网络（Recurrent Neural Networks）
- 递归神经网络（Recursive Neural Networks）



----
<font color=yellow>卷积神经网络</font>

卷积神经网络（CNN）被广泛用于计算机视觉，[Kalchbrenner,2014](https://arxiv.org/pdf/1404.2188.pdf)[Kim,2014](https://arxiv.org/pdf/1408.5882.pdf)将CNN应用于语言研究。下图显示了NLP中使用的典型CNN。

----
![cnn](pic/cnn.png)
----
<font color=yellow>循环神经网络（Recurrent Neural Networks）</font>

循环神经网络从<font color=yellow>时间维度</font>展开，表示信息在时间维度上的传递和积累，后一个信息的概率建立在前面信息的基础上，在神经网络结构上表现为后面隐含层的输入是前面的隐含层的输出。
----
<img align="left" src="pic/RecurrentNN0.jpg"/>

`$x$`是一个向量，它表示输入层的值；

`$s$`是一个向量，它表示隐含层的值；

`$U$`是输入层到隐藏层的权重矩阵；

`$o$`也是一个向量，它表示输出层的值；

`$V$`是隐藏层到输出层的权重矩阵;

`$W$`就是隐含层上一次的值作为这一次的输入的权重。
----
![recurrentNN](pic/RecurrentNN.jpg)
----
![recurrentNN1](pic/RecurrentNN1.png)
----
<font color=yellow>长短期记忆模型(Long-short Term Memory,LSTM)</font>
LSTM是Recurrent Neural Networks算法中的一种。LSTM很好的解决了原始RNN算法中的梯度消失弥散（Vanishing Gradient）问题。
----
一个LSTM神经元（Cell）可以接收两个信息，其中一个是序列的某一位输入，另一个是上一轮的隐藏状态。

同时，一个LSTM神经元也会产生两个信息，一个是当前轮的输出，另一个是当前轮的隐藏状态。
----
![LSTM](pic/lstm2.jpg)

相比RNN只有一个传递状态`$h^t$`，LSTM有两个传输状态，一个`$c^t$`（cell state），和一个`$h^t$`（hidden state）。（Tips：RNN中的`$h^t$`对于LSTM中的`$c^t$`）
----
<font color=yellow>递归神经网络（Recursive Neural Networks）</font>

递归神经网络从<font color=yellow>空间维度</font>的展开，是一个树结构。
![RecursiveNN](pic/RecursiveNN.png)
----

递归神经网络把一个<font color=yellow>树型结构</font>信息编码为一个<font color=yellow>向量</font>,也就是把信息映射到一个语义向量空间中,语义相似的向量距离更近。两句话内容不同，但意思是相近，那么这两句话的向量的距离也相近；反之，语义差异越大，向量的距离则很远。
----
![RecursiveNN1](pic/RecursiveNN1.png)
----

<font color=yellow>序列到序列模型（Sequence-to-sequence models）</font>

[Kyunghyun,Bengio et al. 2014](https://arxiv.org/pdf/1406.1078.pdf)提供了一种崭新的RNN Encoder-Decoder算法，并且将其应用于机器翻译中。
这种算法也是现在谷歌已经应用于线上机器翻译的算法，翻译质量基本达到、甚至超越人类水平。

----
![stsm](pic/stsm.jpg)
----
以机器翻译为例，"How are you"翻译为"你好吗"，模型示例如下：

![stsm](pic/stsm1.png)
[<](#/2/84)
----


<font color=yellow>注意力机制（Attention）</font>

RNN应用于翻译时依赖将整个句子压缩成固定输入的向量，当句子包含单词过多时，不可避免地造成信息丢失，导致翻译错误。

注意力机制使得机器翻译中利用原始的句子信息，减少信息损失。在解码层，生成每个时刻的`$y$`，都会利用到`$x_1,x_2,x_3....$`，而不再仅仅利用最后时刻的隐藏状态向量。
----
![stsm](pic/attention1.png)
----
[Bahdanau et al.2015](https://arxiv.org/pdf/1409.0473.pdf)提出了BahdanauAttention

[Luong et al.2015](https://arxiv.org/pdf/1508.04025.pdf)提出了LuongAttention
BahdanauAttention与LuongAttention的区别
1. BahdanauAttention对Encoder和Decoder的双向的RNN的state拼接起来作为输出，LuongAttention仅使用最上层的RNN输出
----

2. 计算流程不同。BahdanauAttention的计算流程为`$h_{t-1} \rightarrow a_t → c_t → h_t$`，它使用前一个位置`$t-1$`的state计算t时刻的ht$`。LuongAttention计算流程为`$h_t → a_t → c_t → h^t 使用t位置的state当前位置的`$h_t$`
3. BahdanauAttention只在concat对齐函数上进行了实验，LuongAttention在多种对齐函数进行了实验。


[<](#/2/84)
----
<font color=yellow>基于记忆的神经网络</font>

记忆网络可以看做一个框架，用于QA或者分类等任务。
传统的记忆架构做关系推理时有困难，DeepMind和伦敦大学学院提出关系推理模块[RMC](https://arxiv.org/pdf/1806.01822.pdf)，能够在序列信息中执行关系推理，在WikiText-103, Project Gutenberg和GigaWord 数据集上达到了当前最佳性能。

[<](#/2/84)
----
<font color=yellow>预训练的语言模型(Pre-trained Models)</font>

预训练语言模型可以在数据量十分少的情况下有效学习。由于语言模型的训练只需要无标签的数据，因此他们对于数据稀缺的低资源语言特别有利。

----
<font color=yellow>预训练模型的发展</font>
1. 词嵌入（Word Embedding）
	- Word2Vec和[GloVe](#/2/118)[(Global  Vectors for Word Representation)](http://nlp.stanford.edu/projects/glove/)
2. 上下文嵌入(Context Word Embedding)
	- [CoVe](#/2/120)(Context Vectors)和[ELMo](#/2/121)
3. 预训练模型
	- [GPT](#/2/123)和BERT(Bidirectional Encoder Representation from Transformers)
4. 改进型和领域定制型预训练模型
	- 改进型的代表为ALBERT和XLNet
	- 领域定制化代表为SciBert (Scientific Bert) 和BioBert(Biomedical Bert)
----
<font color=yellow>小结</font>

为什么各类神经网络被广泛应用于NLP任务?

<font color=yellow>缓解特征工程问题</font>。非神经NLP方法通常严重依赖于离散的手工特征，而神经方法通常使用低维和稠密的向量(又称分布式表示)隐式地表示语言的语法或语义特征。这些表示是在特定的NLP任务中学习的。因此，神经方法使人们可以很容易地开发各种NLP系统。

[<](#/2/84)
----
<font color=yellow>[预训练模型](#/2/116)--GloVe</font>

GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space. 
----
<font color=yellow>[预训练模型](#/2/116)--GloVe</font>

GloVe与skip-gram和CBOW相比，skip-gram与CBOW每次用一个窗口中的信息更新出词向量，GloVe则是用了全局的信息（共现矩阵），即同时使用多个窗口进行更新词向量。
----
<font color=yellow>[预训练模型](#/2/116)--CoVe</font>

[Bryan McCann et al.2017](https://arxiv.org/pdf/1708.00107.pdf)提出CoVe。与GloVe作为模型的输入时候的效果进行比较。实验结果表明他们提出的 Context Vectors 在不同任务中都带来了不同程度效果的提升。

CoVe更侧重于如何将现有数据上预训练得到的表征迁移到新任务场景中，而之前的句子级任务中大多数都只把迁移过程当做一个评估他们表征效果的手段，因此观念上有所不同。
----
<font color=yellow>[预训练模型](#/2/116)--[ELMo(Embeddings from Language Models)](https://allennlp.org/elmo)</font>

[ELMo](https://www.aclweb.org/anthology/N18-1202/) is a deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). 
----
<font color=yellow>[预训练模型](#/2/116)--ELMo(Embeddings from Language Models)</font>

双向语言模型（Bidirectionbbal language models, biLM）
![elmo](pic/elmo.png)
----
<font color=yellow>[预训练模型](#/2/116)-GPT</font>

[GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)的核心思想是先通过无标签的文本去训练生成语言模型，再根据具体的NLP任务利用有标签的数据对模型进行fine-tuning。
----
<font color=yellow>[预训练模型](#/2/116)--BERT</font>

GloVe与skip-gram和CBOW相比，skip-gram与CBOW每次用一个窗口中的信息更新出词向量，GloVe则是用了全局的信息（共现矩阵），即同时使用多个窗口进行更新词向量。
---
# 2 基本概念

[>](#/3/2)
----
计算语言学有两种基本研究方法

- 基于规则的方法
	- 理论基础：乔姆斯基文法理论
- 基于统计的方法
	- 理论基础：数理统计，信息论
----
主要内容
1. 概率论基本概念
2. [信息论基本概念](#/3/20)
----
#### 概率论基本概念

1. 概率
2. 条件概率
3. 乘法公式
4. 全概率公式
5. 贝叶斯公式
6. 最大似然估计
7. 二项式分布
8. 条件概率分布
9. 联合概率分布
10. 期望
11. 方差

----
概率是从随机实验中的事件到实数域的函数，用以 表示事件发生的可能性。如果用`$P(A)$`作为事件`$A$`的概率，`$\Omega$`是实验的样本空间，则概率函数必须满足如下公理：
- 公理1：`$P(A)\geq0$`（非负性） 
- 公理2：`$P(\Omega)=1$`（规范性）
- 公理3：如果对任意的`$i$`和`$j(i\neq j)$`,事件`$A_i$`和`$A_j$`不相交`$(A_i\bigcap A_j=\phi)$`,则有：`$P(\bigcup_{i=0}^\infty A_i)=\sum_{i=0}^\infty P(A_i)$`（可列可加性）

----

条件概率(Conditional probability)

在事件B发生的条件下事件A发生的概率：
$$
P(A|B)=\frac {P(A,B)}{P(B)}=\frac {\frac {n_{AB}}{N}}{\frac {n_B}{N}}=\frac{n_{AB}}{n_B}
$$
其中，`$n_B$`代表事件`$B$`出现的次数,`$n_{AB}$`代表事件`$A$`和`$B$`同时出现的次数。
`$N$`是试验总次数
----
![condipro](pic/condiprob.jpg)
----
乘法公式

- 设`$A$`、`$B\in S, P(A)>0$`,由`$P(B|A)=\frac {P(A,B)}{P(A)}$`可得`$P(A,B)=P(A)P(B|A)$`，称为事件`$A$`、`$B$`的概率乘法公式。
- 若`$P(B)>0$`,则还有`$P(AB)=P(B)P(A|B)$`
- 上式还可推广到三个事件的情况：`$P(ABC)=P(A)P(B|A)P(C|AB)$`
- 一般情况下，有下列公式：
- `$P(A_1A_2...A_n)=P(A_1)P(A_2|A_1)...P(A_n|A_1...A_{n-1})$`
- 注：乘法法则一般用于计算`$n$`个事件同时发生的概率
----

词性标注问题问题

- "a red apple"的词性序列为"det,adj,n",计算这三个词性出现的概率如下：
- `$P(det,adj,n)=P(det)\times P(adj|det)\times P(n|det,adj)$`
----
计算一个句子的概率如下：

`$P(w_1,w_2,...w_n)=P(w_1)\times P(w_2|w_1)\times ... P(w_n|w_1..w_{n-1})$`

其中，`$w_1,w_2,...w_n$`可以看做是组成句子的<font color=yellow>词</font>，也可以看成是组成句子的<font color=yellow>字</font>。
----
全概率公式

事件组`$A_1,A_2,...A_n$`(`$n$`可为`$\infty$`)称为样本空间`$S$`的一个划分，若一下条件满足：
1. `$\bigcup_{i=1}^nA_i=S$`
2. `$A_iA_j=\phi,(i\neq j)(i,j=1,2,...n)$`
![allprob](pic/allprob.jpg)
----
定理

设`$A_1,A_2,...A_n$`是`$S$`的一个划分,且`$P(A_i)>0,(i=1,2,...,n)$`则对任何事件`$B\in S$`有:

`$P(B)=\sum_{i=1}^nP(A_i)P(B|A_i)$`
称为全概率公式。
----
全概率公式的使用

把事件`$B$`看作某一过程的结果,把`$A_1,A_2,...A_n$`看作该过程的若干个原因。根据历史资料,每一原因发生的概率已知,即`$P(A_n)$`已知,而且每一原因对结果的影响程度已知,即`$P(B|A_n)$`已知,则我们可用全概率公式计算结果发生的概率,即求`$P(B)$`
----
市场上有甲、乙、丙三家工厂生产的同一品牌产品,已知三家工厂的市场占有率分别为`$\frac{1}{4},\frac{1}{4},\frac{1}{2}$`,且三家工厂的次品率分别为 2%、1%、3%,试求市场上该品牌产品的次品率。设:
- `$B$`为买到一件次品的时间
- `$A_1$`:买到一件丙厂的产品
- `$A_2$`:买到一件丙厂的产品
- `$A_3$`:买到一件丙厂的产品

`$P(B)=P(BA_1)P(BA_2)P(BA_3)$`
`$=P(B|A_1)P(A_1)P(B|A_2)P(A_2)P(B|A_3)P(A_3)$`
`$=0.02\times \frac{1}{4}+0.01\times \frac{1}{4}+0.03\times \frac{1}{2} \approx 0.0225$`
----
贝叶斯公式

贝叶斯公式（Bayesian formula）在统计自然语言处理中占据着重要的地位。 
当直接计算条件概率`$P(B|A)$`比较困难，而`$P(A|B)$`已知或是容易计算时，可以使用贝叶斯公式通过`$P(A|B)$`来计算`$P(B|A)$`。
$$
P(B|A)= \frac{P(AB)}{P(A)}=\frac{P(A|B)P(B)}{P(A)}
$$
- `$P(B)$`为先验概率，是指根据以往经验和分析得到的概率；
- `$P(B|A)$`为后验概率，是指事情已经发生，求事件发生的原因由某因素引起的可能性的大小
- `$P(AB)$`为联合概率
----
从机器学习的角度，可以视`$A$`为<font color=yellow>特征</font>、`$B$`为<font color=yellow>标签或类别</font>，那么贝叶斯公式可以表示为：

$$P(类别|特征)=\frac{P(特征|类别)P(类别)}{P(特征)}$$其中，

- `$P(类别|特征)$`为已知样本具有特定特征的条件下，该样本属于指定类别的概率
- `$P(特征|类别)$`为已知样本属于指定类别的条件下，该样本具有特定特征的概率
- `$P(类别)$`为未知样本具有特定特征的条件下，该样本属于指定类别的概率
- `$P(特征)$`为未知样本属于指定类别的条件下，该样本具有特定特征的概率
----
贝叶斯用于文本分类问题

句子<font color=yellow>“我司代开正规发票”</font>,其类别为<font color=yellow>垃圾邮件</font>

$$
P(垃圾邮件|我司代开正规发票)
$$
$$=\frac{P(我,司,代开,正规,发票)P(垃圾邮件)}{P(我,司,代开,正规,发票)}
$$
----
设标签“垃圾邮件”为`$S$`
$$
P(我,司,代开,正规,发票|S)
$$

$$
\approx P(我|S)P(司|S)P(代开|S)P(正规|S)P(发票|S)
$$
- 这就是<font color=yellow>条件独立假设</font>
- Bayes方法加上条件独立假设就是<font color=yellow>朴素贝叶斯方法(Naive Bayes)</font>
----
朴素贝叶斯失去了词语之间的顺序信息。这就相当于把所有的词汇扔进到一个袋子里随便搅和，贝叶斯都认为它们一样。因此这种情况也称作词袋子模型(bag of words)。

![bw](pic/bw.jpg)
----
最大似然估计(Maximum Likehood Estimation MLE)
----
信息论基本概念

| 名称 | 名称 | 名称 |
| :-----:| :----: | :----: |
| 信息量 | 熵 | 交叉熵 |
| 自信息 | 条件熵 | 互信息 |
| 联合自信息 | 联合熵 | 困惑度 |
| 条件自信息 | 相对熵 | ---- |
----
人们普遍认为，Claude Elwood Shannon 在1948年发表的“通信的数学理论”（A Mathmatical Theory of Communication, BSTJ,1948）这篇里程碑性的文章标志着信息论的产生，而Shannon本人也成为信息论的奠基人。

Shannon理论基本任务是设计有效而可靠的通信系统。

熵是信息论中重要的基本概念。

----
信息论研究的内容

- 狭义信息论
- 广义信息论
----
狭义信息论（经典信息论、香农信息论）

研究信息测度，信道容量以及信源和信道编码理论
一般信息论

研究信息传输和处理问题，除经典信息论外还包括噪声理论，信号滤波和预测，统计检测和估值理论，调制理论，信息处理理论和保密理论
----
广义信息论

除狭义信息论的研究内容外，还包括自然和社会领域有关信息的内容，如模式识别，计算机翻译，心理学，遗传学，神经生理学
----
<font color=yellow>信息量</font>

事件发生的不确定性与事件发生的概率有关。事件发生的概率越小，事件发生所包含的不确定性和信息量就越大。而事件发生的概率越大，人们猜测这件事发生的可能性就越大，不确定性就越小。

----
对于发生概率等于1的必然事件，就不存在不确定性。

因此，某事件发生所含有的信息量，应该是该事件发生的先验概率的函数，即$I(x_i)=f[P(x_i)]$

式中$P(x_i)$是事件$x_i$发生的先验概率，$I(x_i)$表示事件$x_i$发生所含有的信息量。
----
函数$I(x_i)$应满足以下条件：
1. $P(x_i)$越大,$I(x_i)$越小；
2. 当$P(x_i)=1$时，$I(x_i)=0$，必然事件信息量为零
3. 当$P(x_i)=0$时，$I(x_i)=\infty$，不可能发生的事件发生了，其信息量为无穷大;
4. 两个独立事件的联合信息量，应等于它们各自信息量之和$I(x_ix_j)=f[P(x_i)]+f[P(x_j)]$
----
可以看出，$I$与$P(x)$间若满足以上三点，则它们有如下关系式： 
$$
I=\log a\frac{1}{P(x)}=-\log aP(x)
$$
$I(x_i)$描述了事件$x_i$发生时的信息量，故称为自信息。

----
<font color=yellow>自信息</font>

事件集合$X$中的事件$x=a_i$的自信息定义为：<br>
$I_X(a_i)=-\log P_X(a_i)$<br>
简记为:$I(x)=-\log p(x)$

----
$\log$底数 | 单位
:-:|:-:
2 | bit(比特)
e(ln) | nat(奈特)
10(lg) | hart(哈特)

- 注：
	- 1nat=1.44bit 
	- 1hart=3.32bit
----
联合自信息

联合事件集合$XY$中的事件$x=a_i,y=b_j$的联合自信息定义为：

$I_{XY}(a_i,b_j)=-\log P_{XY}(a_i,b_j)$

简记为：$I(xy)=-\log p(xy)$。其中,$p(xy)$要满足非负和归一化的条件。
----

实际上,如果把联合事件$xy$ 视为一个单一事件,

那么联合自信息的含义与自信息的含义相同。
----
例题：

箱中有90个红球，10个白球,     箱中球不变，现从箱中先拿出一球，再拿出一球。
1. 求“两个球中有红、白各一球的”的不确定性
2. 求“两个球都是白球”所提供的信息量
3. 求“两个球都是白球”与“两个球都是红球”的发生,哪个更难预测
----
解：三种情况都是求联合自信息，设$x$为红球数,$y$为白球数

1. $P_{XY}(1,1)=\frac {C_{90}^1C_{10}^1}{C_{100}^2}=\frac {90 \times 10}{100\times 99 \div 2}=\frac {2}{11} $

$I(1,1)=-\log \frac{2}{11}=2.46bit$
----
2.$P_{XY}(0,2)=\frac {C_{10}^2}{C_{100}^2}=\frac {10 \times 9\div 2}{100\times 99 \div 2}=\frac {1}{110} $

$I(0,2)=-\log \frac{1}{110}=6.783bit$
----
3.$P_{XY}(2,0)=\frac {C_{90}^2}{C_{100}^2}=\frac {90 \times 89 \div 2}{100\times 99 \div 2}=\frac {89}{110} $

$I(2,0)=-\log \frac{89}{110}=0.306bit$

因$I(0,2)>I(2,0)$, 所以事件“两个球都是白球”的发生更难预测。
----
<font color=yellow>条件自信息</font>

事件$x=a_i$在事件$y=b_j$给定条件下的条件自信息定义为:
$I_{X|Y}(a_i|b_j)=-\log P_{X|Y}(a_i|b_j)$
简记为：
$I(x|y)=-\log p(x|y)$

其中,条件概率$p(x|y)$也要满足非负和归一化的条件。
----
条件自信息含义与子信息类似,只不过是概率空间有变化。条件自信息的含义两个方面：
1. 在事件$y=b_j$给定条件下,在$x=a_i$发生前的不确定性。
2. 在事件$y=b_j$给定条件下,在$x=a_i$发生后所得到的信息量。

证明:$I(xy)=I(x)+I(y|x)=I(y)I(x|y)$
----
例题：

箱中有90个红球，10个白球,     箱中球不变，现从箱中先拿出一球，再拿出一球。
1. 在第一个球是红球的条件下、第二个球是白球的不确定性
2. 求在第一个球是红球的条件下、第二个球是红球”所提供的信息量
----
解：这两种情况都是求条件自信息，设$r$为红球数,$w$为白球数
----
1. $p(y=w|x=r)=\frac{10}{99}$

$I(y=w|x=r)=-\log \frac{10}{99}=3.308bit$
----
2. $p(y=r|x=r)=\frac{89}{99}$

$I(y=r|x=r)=-\log \frac{89}{99}=0.154bit$
----
<font color=yellow>熵(entropy)</font>

离散随机变量$X$的熵定义为自信息的统计平均值，记为$H(X)$
----
$$
H(X)=E[I(x_i)]=-\sum_{i=1}^np(x_i)\log p(x_i)
$$
简记为：$H(X)=H(p(x_1),p(x_2),...,p(x_n))$

注：$p(x_1),p(x_2),...,p(x_n)$就是随机变量$X$的概率分布。

其中，约定$0\log0=0,H(X)$也可以写成$H(p)$。通常熵的单位为𝑏𝑖𝑡
----
熵又称为平均自信息（self-information），表示信源$X$每发一个符号（不论发什么符号）所提供的平均信息量。

熵也可以被视为描述一个随机变量的不确定性的数量。一个随机变量的熵越大，它的不确定性越大。那么，正确估计其值的可能性就越小。越不确定的随机变量越需要大的信息量用以确定其值。
----

例题：
A,B两城市天气情况概率分布如下表所示,问哪个城市的天气具有更大的不确定性。

 \\| 晴| 阴| 雨
---|---|---|---
A城市 | 0.8| 0.15| 0.05
B城市 | 0.4| 0.3| 0.3
----
解:
$$H(A)=H(0.8,0.15,0.05)$$
$$=-0.8\times \log0.8-0.15\times \log0.15-0.05$$
$$\times \log0.05=0.884bit$$

$$H(B)=H(0.4,0.3,0.3)$$
$$=-0.4\times \log0.4-0.3\times \log0.3-0.3$$
$$\times \log0.3=1.571bit$$
----


<font color=yellow>条件熵(conditional entropy) </font>

给定随机变量$X$的情况下，随机变量𝑌的条件熵定义为：
$$
H(Y|X)=\sum_ip(x_i)H(Y|X=x_i)
$$

$$
=\sum_ip(x_i)[-\sum_j^ip(y_j|x_i)\log p(y_j|x_i)]
$$

$$
=\sum_i\sum_jp(x_i)p(y_j|x_i)\log p(y_j|x_i)
$$

$$
=-\sum_i\sum_jp(x_i,y_j)\log p(y_j|x_i)
$$
----
上面条件熵定义所表示的是在已知X的情况下，传输$Y$额外所需的平均信息量。
----

<font color=yellow>联合熵(joint entropy)</font>

联合自信息量定义为：$I(x_i,y_j)=-\log p(x_i,y_j)$

$(X,Y)$被视为一个联合事件。
----
联合熵$H(X,Y)$是二维随机变量$XY$的不确定性的度量:
$$
H(X,Y)=\sum_{i=1}^n\sum_{j=1}^mp(x_i,y_j)I(x_i,y_j)$$
$$=-\sum_{i=1}^n\sum_{j=1}^mp(x_i,y_j)\log_2p(x_i,y_j)
$$
----
在给定$X=x_i$的条件下，随机变量$Y$的不确定性为：
$$
H(Y|x_i)=-\sum_jP(y_j|x_i)\log p(y_j|x_i)
$$
由于不同的$x_i$，$H(Y|x_i)$是变化的，对$H(Y|x_i)$的所有可能值进行平均，就得出给定$X$时，$Y$的条件熵$H(Y|X)$
----

信息熵、联合熵和条件熵的关系
1. 联合熵与信息熵、条件熵的关系:
$H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)$
2. 条件熵与信息熵的关系:
$H(X|Y)\geq H(X)$
$H(Y|X)\leq H(Y)$
3. 联合熵与信息熵的关系:
$H(X,Y)=H(X)+H(Y)$
----
<font color=yellow>相对熵(Kullback-Leibler Divergence, KL距离)</font>

相对熵(relative entropy)又称Kullback-Leibler距离(Kullback-Leibler divergence)，或简称KL距离，是衡量相同事件空间里两个概率分布相对差距的一个量度。
----
两个概率分布$p(x)$和$q(x)$的相对熵定义为：
$$
D(q||p)=\sum_{x\in\Omega}q(x)\log_2\frac{q(x)}{p(x)}=E_p(\log_2\frac{q(x)}{p(x)})
$$
该定义中约定：
$$
0\log(\frac{0}{q})=0
$$

$$
p\log(\frac{p}{0})=\infty
$$
----
相对熵常被用以衡量两个随机分布的差距。
1. 当两个随机分布相同时，其相对熵为0.
2. 当两个随机分布的差别增加时，其相对熵也增大。
----

<font color=yellow>交叉熵(cross entropy)</font>

对于n-gram，其概率为，$P(w_i|w_{i-n+1}^{i-1})$
可以计算句子的概率为：
$$
P(S)=\prod_{i=1}^{n+1}P(w_i|w_{i-n+1}^{i-1})
$$
----
假设测试语料$T$由$N$个句子构成$(n_1,n_2,...n_N)$则整个测试集的概率为:
$$
P(N)=\prod_{i=1}^N(n_i)
$$
----

<font color=yellow>互信息(mutual information)</font> 

互信息$I(x,y)$表示某一事件y所给出的关于另一个事件x的信息。

离散随机事件$x=a_i$和$y=b_j$之间的互信息定义为：
$$
I_{X;Y}(a_i;b_j)=\log \frac{P_{X|Y}(a_i|b_j)}{P_X(a_i)}
$$
简记为：
$$
I(x;y)=\log \frac{p(x|y)}{p(x)}
$$
----
通过简单计算，可以得到：$I(x;y)=I(x)-I(x|y),I(x;y)$也经常写成$I(x,y)$,因此,互信息有如下特点：

1. 互信息的单位与自信息单位相同
----
2. $x$与$y$的互信息等于x的自信息减去在$y$条件下$x$的自信息。$I(x)$表示x的不确定性。

$I(x|y)$表示在$y$发生下$x$的不确定性。

$I(x;y)$表示当y发生后$x$不确定性的变化。

两个不确定性之差，是不确定度消除的部分，代表已经确定的东西。实际上就是由$y$发生所得到的关于$x$的信息量。
----
3. 互信息反映了两个随机事件$x$和$y$之间的统计关联程度。在通信系统中，互信息的物理含义是，信道输出端接收到某消息(或消息序列)$y$后，获得的关于输入端某消息(或消息序列)x的信息量。互信息的引出，使信息传输问题进入例如定量分析的范畴，是信息论发展的一个重要的里程碑。
----
<font color=yellow>困惑度(perplexity)</font>
在设计语言模型时，我们常用困惑度代替交叉熵衡量语言模型的好坏。给定语言`$L$`的样本 如下：
$$
L_1^n=l_1l_2...l_n
$$
`$L$`的困惑度为:
$$
PP_q=2^{H(L,q)}\approx 2^{{\frac {1}{2}}\log(l_1^n)}=[q(l_1^n)]^{\frac {1}{n}}
$$
---
# 3 形式语言与自动机
----
主要内容
1. 基本概念
2. 语言研究的形式化
3. [形式语法](#/4/49)
4. 自动机

----

### 3.1 基本概念
----
#### 树（Tree）
一个连通的无回路的**无向图**称为树（或称自由树）。 
如果树中有一个结点被特别地标记，则这棵树被称之为根树，这个被特别标记的结点被称之为**根结点**。
----
<div class="firstTest mermaid" >
       graph LR;
        A-->B;
</div>
----

<div class="sec mermaid">
       graph LR;
        A---B;
        B---C;
        C---D;
        B---D;
</div>
----
<div class="firstTest mermaid">
       graph TD;
        C((C))--> D((D));
        C((C))--> E((E));
</div>
----
<div class="firstTest mermaid">
       graph TD;
        A((A))--> B((B));
        A((A))--> C((C));
        C((C))--> D((D));
        C((C))--> E((E));
</div>


----
#### 字符串（String）
字符串定义：假定`$\Sigma$`是字符的有限集合，它的每一个元素称之为字符。由`$\Sigma$`中字符相连而成的有限序列被称之为`$\Sigma$`上的字符串（或称符号串，或称链）。不包括任何字符的字符串称为空串，记作`$\epsilon$` 
**符号串的长度**:符号串中符号的个数。符号串`$x$`的长度用`$|x|$`表示。
`$|\epsilon|=0$`包括空串的`$\Sigma$`上字符串的全体记为`$\Sigma ^*$`
----
#### 字符串的操作
假定`$\Sigma$`是字符的有限集合，`$x,y$`是`$\Sigma$`上的符号串
1. 字符串的链接：
把`$y$`的各个符号写在x的符号之后得到的符号串称为`$x$`与`$y$`的连接，记作`$xy$`。 
> **例** 
>`$\Sigma =\{a,b,c\},x=ab,y=cba$` 
那么，`$xy=abcba$`
----
2. 字符串指数操作

设`$x$`是符号串，把`$x$`自身连接`$n$`次得到的符号串，即`$z=xx...x$`，当`$x$`的数量为`$n$`时，称为`$x$`的`$n$`次方，记做`$x^n$`<br>
注意：`$x^0=\epsilon$`
----
> **例** 
> 如果`$x=a$`,则`$x^1=a,x^2=aa,x^3=aaa$` 
> 
> 如果`$x=ab$`,则`$x^0=\epsilon,x^3=ababab$`
----
3. 字符串集合的乘机

设`$A,B$`是符号串的集合，则`$A,B$`的乘积定义为：`$AB=\{xy|x\in A,y\in B\}$`，相应地，`$A^0=\{\epsilon\},A^n=A^{n-1}A=AA^{(n-1)}$`
----
> **例** 
> 设`$A=\{aa,bb\},B=\{cc,dd,ee\}$`
> 则`$AB=\{aacc,aadd,aaee,bbcc,bbdd,bbee\}$`
> `$A^2=\{aaaa,aabb,bbaa,bbbb\}$`

----
#### 正则表达式(Regular Expression)
正则表达式是操作字符串的逻辑公式。用定义好的字符集或其组合表示规则字符串。
----
正则式对应于`$\Sigma$`上的一些子集(正则集)，并通过递归定义:
1. 空集`$\phi$`和空字符串`$\epsilon$`是正则式，它们的正则集分别为`$\phi$`和`$\{\epsilon\}$`
2. 任何`$x\in \Sigma,x$`是正则式，它对应的正则集是`$\{x\}$`
3. `$X,Y$`是`$\Sigma$`上的正则式，并且它们对应的正则集分别为`$U,V$`，那么,`$X|Y,X\cdot Y$`和`$X^*$`也是正则式，且它们对应的正则集分别为`$U\cup V,U\cdot V$`和`$U*$`
----
> **例**
> 假设`$\Sigma=\{0,1\}$`,那么,0和1都是正则表达式。 
> 如果令`$x=0,y=1$`,那么,`$y^*=1^*$`也是正则式，对应的正则集为：`$U=\{\epsilon,1,11,...\}$` 
> `$xy^*=01^*$`也是正则式，且它对应的正则集： 
> `$V=\{0,01,011,0111,...\}$`
> `$x|y^*=\{x\}\cup U=\{0,\epsilon,1,11,111,...\}$`
----


#### 栈(stack)
栈是一种线性表，`$A=A_0,A_1,...A_k$`。`$A_0$`是栈底,`$A_k$`是栈顶,当栈为空时`$A_0$`既是栈顶也是栈底。

----
`$A_k$`(Top) |
:---:|
... | 
`$A_2$` | 
`$A_1$` | 
`$A_0$`(Bottom) | 

----
### 3.2 语言的形式化

1. 形式语法(formal grammar)
2. 形式理论(formal theory)
3. 形式化的语法(formalized grammar)
4. 形式化的理论 (formalized theory)
----
汉语、英语等自然语言不是形式语言，但可以用符号、公式等形式化的手段来研究其语法，这种语法称“形式化的语法”，有时也称“形式语法”；这样表达的理论称“形式化的理论”，有时也称“形式理论”。

形式逻辑、数学公式、计算机程序等人工语言都可以视为为形式语言。这种语言的语法是形式语法。
----

#### 形式语言的定义
- 按照一定规律构成的句子和符号串的有限或无限的集合。(Chomsky)
- 语言可以被看成一个抽象的数学系统。(吴蔚天)

----

“**形式**”这一术语在语言学中至少有两个不同的含义：
1. 形式可与内容、语义相对，指语言单位的外部表现，为语言意义的物质载体，是语言中可听得着、可看得见的部分，包括语音单位的外形及排列顺序、分布、结构等。这一“形式”是与“意义(meaning)”相对的。
----
2. “形式”指语言中抽象的关系结构。它要靠符号、公式，把具体现象抽象化、概念化。我们说的“语言的形式化”指的就是这一意义。这一“形式”是与“实体（substance）”相对的。
----

#### 语言形式化的可能性和必要性
1. 必要性
它既是计算机处理自然语言的需要，也是语言研究提高科学性、可靠性的需要。
----

> 例如
> “这句话是假的。”语义悖论的出现是因为同一自然语言在这个句子内既是对象语言，又是元语言。
----
2. 可能性
袁毓林先生把自然语言和形式语言进行比较以后认为：
- 形式语言至少具有三个特点：
1. 基本单元的明确性；
2. 运算和关系的明确性；
3. 优先级的明确性。
- 自然语言在这三个方面是极不明确的。
----
**语言范畴的边界不明确**
1. 语素、词、词组的界限不是十分明确的。
> 例如
> 蝴蝶、蝶泳、蝶形花
> 鸡蛋、鸵鸟蛋、咸鸭蛋
----
2. 词类之间的界限也不是十分清楚的。
- 凡受“很”修饰而不能带宾语的谓词是形容词。
- 凡不受“很”修饰或能带宾语的谓词是动词。
----

例如
> 1. "我大他三岁" "我高你一头"
> 2. (\*)不(\*)
> 3. (\*)了没有
> 4. 比N(\*)
----
3. 句子合格性的界限也是模糊的。例如

>一片树叶飘落在了我的帽子上
----

**结构关系难于定义**
例如
> 1. 台上坐着主席团---(状-动-主？主-动-宾? 状-动-宾?)
> 2. 主席团坐在台上---(主-动-宾？ 主-动-补？)
----

例如

> 1. 小王推开了门---(施事)
> 2. 右手推开了门---(施事？/工具？)
> 3. 北风吹开了门---(?)
----

4. 层次不外现。例如

> 三个工厂的推销员
- 三个工厂的/推销员
- 三个/工厂的推销员

----
例如

> 不严肃地批评孩子的家长


- 不严肃地/批评孩子的/家长--NP
- 不严肃地/批评/孩子的家长--VP
- 不/严肃地批评孩子的/家长--NP
- 不/严肃地批评/孩子的家长--VP

----
**在词和短语层面层次的不外现**

汉语 |英语
:---:|:---:
鸡蛋 | egg
鸭蛋 | duck's egg
----
汉语 |英语
:---:|:---:
管理家务 | manage household(动)
管理家务 | managerial personnel(形)
企业管理 | management of enterprises(名)
----
**VP+NP1+的+NP2**
例如

- 穿着红衣服的姑娘
- 穿着节日的盛装
- 咬死了猎人的狗
----

- 穿着红衣服的--> 姑娘--> NP
- 穿着--> 节日的盛装-->VP
- 咬死了猎人的--> 狗-->NP
- 咬死了--> 猎人的狗-->VP

----
**VP+NP1+的+NP2 是一个潜在的歧义结构，转化为现实歧义要满足三个条件：**
1. NP1在语义上可以做VP的受事；
2. NP2在语义上也可做VP的受事, 在 NP1为VP的受事时, NP2又可做VP的施事;
3. NP1和NP2之间在语义上存在领属和被领属关系, NP1是领属者, NP2是被领属者.
----
**问题的关键在于:**
- NP1与V是否具有语义搭配性
- 如果我们在规则中加进去这项语义限制，那么具有搭配性的ａ归结为NP，不具有搭配性的ｂ则归结为VP；
- 但要确定ｃ仅仅靠结构内的语义分析就不够了，还要靠上下文语境的分析。
----

#### 小结
从理论上说，自然语言的形式化，不仅是必要的，也是可能的。但由于我们现在对自然语言，尤其是汉语的研究还很不深入，很不透彻，对句法语义关系以及人们对语言的认知理解缺乏精细的刻画，所以距离自然语言形式化的描写、距离计算机对非受限的自然语言理解的真正实现还有一段遥远的路程。这中间虽然也有待于计算机技术的进一步提高，但最主要的还是语言学问题。
----

一方面，我们要找到最适合自然语言形式化描写的切入理论，另一方面，更重要的，是我们必须扎扎实实地从一点一滴的语言事实开始研究，为计算机理解自然语言提供有效的语言学支持。
----
课外阅读：[Last Words: What Science Underlies Natural Language Engineering?](https://www.aclweb.org/anthology/J09-4012.pdf)

主要观点：当代的自然语言工程里，语言学整体上是缺位的！



----
#### 3.2.3 形式化的方法的条件
1. <font color=yellow>高度的抽象化</font>。形式化方法所表达的内容必须是语言的语法、语音、语义等系统的一般的、概括的、抽象的原则与规则，而不是上述系统中个别现象的具体描述。也就是说，形式化方法的目的是从具体语言现象中抽象出一般的规律并总结出形式化的理论。
----

2. <font color=yellow>元语言的形式化</font>。形式化方法的主要工具是形式语言（可以是数学语言、逻辑语言等），也就是说，形式化方法要用形式语言作元语言，而不能用自然语言作元语言。
3. <font color=yellow>过程的严密化</font>。即形式化方法的运用过程必须具有数学与逻辑的严密性。
----
#### 语言描述的三种途径
1. 穷举法——只适合句子数目有效的语言。
2. 语法描述——生成语言中合格的句子。
3. 自动机——对输入的句子进行检验，区别哪些是语言中的句子，哪些不是语言中的句子。
----
#### 形式语言的直观意义
形式语言是用来精确地描述语言(包括人工语言和自然语言)及其结构的手段。形式语言学也称<font color=yellow>代数语言学</font>。
----

以重写规则`$\alpha\rightarrow \beta$`的形式表示为例。其中，`$\alpha,\beta$`均为 字符串。顾名思义：字符串`$\alpha$`可以被改写成`$\beta$`。一个初步的字符串通过不断地运用重写规则,就可以得到另一个字符串。通过选择不同的规则并以不同的顺序来运用这些规则,就可以得到不同的新字符串。
----

#### 3.3 形式语法
句子“学生学习语言学。”



```mermaid
graph TD
A(学生)-->A1(N)
A1(N)-->A2(NP)
A2(NP)-->S
B(学习)-->B1(V)
B1(V)-->B2(VP)
C(语言学)-->C1(N)
C1(N)-->C2(NP)
C2(NP)-->B2
B2-->S
```
----
![31](pic/31.jpg)

----
> 推导过程：
> 1. `$句子\Rightarrow 名词短语+动词短语$`
> 2. `$动词短语\Rightarrow 动词+名词短语$`
> 3. `$名词短语\Rightarrow 名词$`
> 4. `$动词\Rightarrow 学习$`
> 5. `$名词\Rightarrow 学生$`
> 6. `$名词\Rightarrow 语言学$`

----
> 形式化推导过程：
> 1. `$S\Rightarrow NP+VP$`
> 2. `$VP\Rightarrow V+NP$`
> 3. `$NP\Rightarrow N$`
> 4. `$V\Rightarrow 学习$`
> 5. `$N\Rightarrow 学生$`
> 6. `$N\Rightarrow 语言学$`
----
- 句法树和重写规则都是形式语法常用的描述方法。
	- 从中可以看出乔姆斯基从结构主义语言学汲取的营养。
- 生成语言学与结构主义语言学的根本区别在于它把一种语言描写的方法转化成了一种解释语言生成的机制。

----
#### 形式语法的定义
形式语法是一个4元组`$G=\{N,\Sigma,P,S\}$`
----
其中,`$N$`是是<font color=yellow>非终结符</font>的有限集合(有时也叫变量集或句法种类集)；

----
`$\Sigma$`是<font color=yellow>终结符</font>的有限集合,`$N\bigcap \Sigma=\Phi;V=N\bigcup\Sigma$`称总词汇表;
----
`$P$`是一组<font color=yellow>重写规则</font>的有限集合：`$P=\{\alpha\rightarrow\beta\}$`,其中,`$\alpha,\beta$`是`$V$`中元素构成的串，但`$\alpha$`中至少应含有一个非终结符号;
----
`$S\in N$`称为<font color=yellow>句子符或初始符</font>。 
----
> **例**
> `$G=(\{A,S\},\{0,1\},P,S)$`<br>
> P：<br>
> - `$S\rightarrow 0A10$`
> - `$A\rightarrow 00A1$`
> - `$A\rightarrow 1$`

----
#### 推导的定义
设：`$G={N,\Sigma,P,S}$`是一个文法在`$(N\bigcup \Sigma)^*$`上定义关系`$\Rightarrow_G$`(直接派生或推导)如下：
> 如果`$\alpha \beta \gamma$`是`$(N\bigcup \Sigma)^*$`中的符号串，且`$\beta \rightarrow \delta$`是`$P$`的生产式，那么`$\alpha \beta \gamma \Rightarrow_G \alpha \delta \gamma$`
----

- 用`$\Rightarrow_G^+$`(按非一般方式派生)表示`$\Rightarrow_G$`的传递闭包(非空集合上的关系)，也就是`$(N\bigcup \Sigma)^*$`上的符号串`$\xi_i$`到`$\xi_{i+1}$`的`$n\{n \geq 1\}$`步推导或派生。
- 用`$\Rightarrow_G^*$`(派生)表示`$\Rightarrow_G$`的自反和传递闭包，也就是`$(N\bigcup \Sigma)^*$`上的符号串`$\xi_i$`到`$\xi_{i+1}$`经过`$n\{n \geq 1\}$`步推导或派生。
- 如果清楚文法`$G$`所产生的推导步骤,符号`$\Rightarrow_G^+$`或`$\Rightarrow_G^*$`可以省略不写。
----


$$G=(V_n,V_t,P,S)$$
$$V_n=(S,A,B,C)$$
$$V_t=(a,v,c)$$
----
#### P：
1. `$S\rightarrow ABC$`
2. `$A\rightarrow aA$`
3. `$A\rightarrow a$`
4. `$B\rightarrow Bb$`
5. `$B\rightarrow b$`
6. `$BC\rightarrow Bcc$`
7. `$ab\rightarrow ba$`
----
```mermaid
graph LR
A(S) --规则1--> B(ABC)
B --规则3--> C(aBC)
C --规则6--> D(aBcc)
D --规则5--> E(abcc)
E --规则7--> F(bacc)
```
----
![32](pic/32.jpg)
#### P：
1. `$S\rightarrow ABC$`
2. `$A\rightarrow aA$`
3. `$A\rightarrow a$`
4. `$B\rightarrow Bb$`
5. `$B\rightarrow b$`
6. `$BC\rightarrow Bcc$`
7. `$ab\rightarrow ba$`
----
这个派生过程被称为“完全的派生”，它从起始符Ｓ开始，一直到产生出一个终端语符列bacc来，才得以终止。因为只有bacc才能满足以下三个条件：

----
1. 它完全由终端语符组成；
2. 它不能再被语法中任何重写规则改写了；
3. 它是语法自`$Ｓ$`开始作派生的最后一行。

----

上例中，规则2与规则4可以无限重复，这样`$Ｇ$`的终极语符列的集合可写为`$b^na^mcc(n\ge1,m\ge1)$`。其中，b的个数，即`$n$`的值等于使用规则4的次数加1；`$a$`的个数，即`$m$`的值等于使用规则2的次数加1。

----
##### 最左推导、最右推导和规范推导
1. 约定每步推导中只改写<font color=yellow>最左边</font>的那个非终结符， 这种推导称为“最左推导”。
2. 约定每步推导中只改写<font color=yellow>最右边</font>的那个非终结符， 这种推导称为“最右推导”。最右推导也称规范推导。
----

文法`$G=\{\{E,F,T\}, \{a,+,*,(,)\},P,E\}$`

其中,`$\{E,F,T\}$`是非终极符号,`$\{a,+,*,(,)\}$`是终极符号,规则`$P$`如下:
1. `$E\rightarrow E+T|T$`
2. `$T\rightarrow T*F|F$`
3. `$F\rightarrow (E)|a$`
----
分别按照最左推导和最右推导得到字符串`$a+a*a$`
----
> 最左推导：
> 1. `$E\Rightarrow E+T$`
> 2. `$E+T\Rightarrow T+T$`
> 3. `$T+T\Rightarrow F+T$`
> 4. `$F+T\Rightarrow a+T$`
> 5. `$a+T\Rightarrow a+T*F$`
> 6. `$a+T*F\Rightarrow a+F*F$`
> 7. `$a+F*F\Rightarrow a+a*F$`
> 8. `$a+a*F\Rightarrow a+a*a$`
----
> 最右推导：
> 1. `$E\Rightarrow E+T$`
> 2. `$E+T\Rightarrow E+T*F$`
> 3. `$E+T*F\Rightarrow E+T*a$`
> 4. `$E+T*a\Rightarrow E+F*a$`
> 5. `$E+F*a\Rightarrow E+a*a$`
> 6. `$E+a*a\Rightarrow T+a*a$`
> 7. `$T+a*a\Rightarrow F+a*a$`
> 8. `$F+a*a\Rightarrow a+a*a$`
----
#### 形式语法的特点
1. 高度的形式化和抽象化。
2. 形式语法是一套演绎系统。
3. 形式语法具有算法的特点。
----
#### 算法的特点
1. 通用性：算法是针对一类问题的
1. 机械性：算法的每一步骤都是确定的
1. 有限性：算法必须在有限步骤内结束
1. 离散性：算法的输入及输出数据都是离散符号
----
#### 形式语法的类型
----
##### 无约束文法
如果`$P$`中的规则满足如下形式：
`$\alpha \rightarrow \beta$`,其中,`$\alpha, \beta$`是字符串,则称`$G$`为无约束文法,或称0型文法。

任何0型文语言都是递归可枚举的,反之,递归可枚举集必定是一个0型语言。

----

##### 上下文有关文法(CSG, context-sensitive grammar)


在0型文法的基础上每一个`$\alpha \rightarrow \beta$`,都有`$|\beta| \geq |\alpha|$`。这里的`$|\beta|$`表示的是`$\beta$`的长度。 

如有`$A \rightarrow Ba$`则`$|\alpha|=1$`,`$|\beta|=2$`符合1型文法要求。反之,如`$aA \rightarrow a$`则不符合1型文法。 
----
- 例
文法`$G=\{N,\Sigma,P,S\}$`,非终极符号`$N=\{S,A,B,C\}$`,终极符号 `$\Sigma=\{a,b,c\}$`,规则`$P$`如下：
1. `$S\rightarrow ABC$`
2. `$A\rightarrow aA|a$`
3. `$B\rightarrow bB|b$`
4. `$BC\rightarrow Bcc$`

求文法`$G$`生成的句子的集合。
----
`$L(G)=\{a^nb^mc^2\},(n\geq 1,m\geq 3),(n\geq 1,m\geq 1)$`
----
##### 上下文无关文法(CFG, context-free grammar)
2型文法是在1型文法的基础上,再满足：每一个`$\alpha \rightarrow \beta$`都有`$\alpha $`是非终结符。如`$A \rightarrow Ba$`,符合2型文法要求。

如`$Ab \rightarrow Bab$`虽然符合1型文法要求,但不符合2型文法要求，因为其`$\alpha=Ab$`，而`$Ab$`不是一个非终结符。
----
- 例
文法`$G=\{N,\Sigma,P,S\}$`,非终极符号`$N=\{S,A,B\}$`,终极符号 `$\Sigma=\{a,b\}$`,规则`$P$`如下：
1. `$S\rightarrow ABC$`
2. `$A\rightarrow aA|a$`
3. `$B\rightarrow bB|b$`
4. `$C\rightarrow BA|c$`

求文法`$G$`生成的句子的集合。
----

`$L(G)=\{a^nb^ma^kc^a\}$`,

`$(n\geq 1,m\geq 3)$`,

`$(n\geq 1,m\geq 1,k\geq 0,a\in\{0,1\})$`
----

##### 正则文法
它是在2型文法的基础上满足:

`$A\rightarrow \alpha$` |  `$B\alpha$`(左线性)或`$A \rightarrow \alpha | \alpha B$`（右线性）

----

例
文法`$G=\{N,\Sigma,P,S\}$`,非终极符号`$N=\{S,A,B\}$`,终极符号 `$\Sigma=\{a,b\}$`,规则`$P$`如下：
1. `$S\rightarrow aA$`
2. `$A\rightarrow aA$`
3. `$A\rightarrow bbB$`
4. `$B\rightarrow bB$`
5. `$B\rightarrow b$`

求文法`$G$`生成的句子的集合。
----

`$L(G)=\{a^nb^m\},(n\geq 1,m\geq 3)$`
----
每一个正则文法都是上下文无关文法,每一个上下无关文法都是上下文有关 文法,而每一个上下文有关文法都是0型文法。即： 
`$L(G_0)\supseteq L(G_1)\supseteq L(G_2) \supseteq L(G_3)$`
----
文法类型 | 文法名称 | 示例
---|---|---
0型文法 | 无约束文法 |`$AB\rightarrow CD$`;`$AB\rightarrow C$`
1型文法 | 上下文相关文法|`$aBa\rightarrow aba$`
2型文法 | 上下文无关文法|`$A\rightarrow a$`
3型文法 | 正则文法|`$A\rightarrow aB$`;`$A\rightarrow a$`

----

#### 3.3.6 用树形图表示上下文无关文法生成的句子
上下文无关文法产生一个句子的派生树的步骤如下： 
1. 对于`$\forall_x\in N\bigcup\Sigma$`给一个标记作为节点,`$S$`作为树的y根节点。
2. 如果一个节点的标记为`$A$`,并且它至少有一个除它自身以外的后裔，则`$A\in N$`
3. 如果一个节点的标记为`$A$`,他的`$k(k>0)$`个直接后裔节点按从左到右的次序依次标记为`$A_1,A_2,...,A_k$`则`$A\rightarrow A_1,A_2,...,A_k$`一定是`$P$`中的一个产生式。
----

例 
文法`$G=\{\{S,A\}\},\{a,b\},P,S\}$`,规则`$P$`如下：
1. `$S\rightarrow bA$`
2. `$A\rightarrow bAA$`
3. `$A\rightarrow a$`
`$G$`产生句子`$bbaa$`可以由下面的生树表示:
----
```mermaid
graph TD
A(("S"))-->B((A))
A(("S"))-->C((b))
B(("A"))-->D((b))
B(("A"))-->E((A))
B(("A"))-->F((A))
E((A))-->G((a))
F((A))-->H((a))

```
----
例 
`$G=\{V_n,V_t,P,S\}$` 
`$V_n=\{S,NP,VP\}$` 
`$V_t=\{n,r,v,a\}$` 
规则`$P$`如下： 
1. `$S\rightarrow NP+VP$`
1. `$NP\rightarrow n$`
1. `$NP\rightarrow r$`
1. `$NP\rightarrow a+NP$`
1. `$VP\rightarrow v$`
1. `$VP\rightarrow vNP$`
1. `$r\rightarrow$`我
1. `$v\rightarrow $`喜欢
1. `$a\rightarrow $`红
1. `$n\rightarrow $`苹果
----
根据文法`$G$`生成句子"我喜欢红苹果"，并画出树形图。
----
```mermaid
graph TD
A(S)-->B1(NP)
A(S)-->B2(VP)
B1(NP)-->C1(r)
C1(r)-->D1(我)
B2(VP)-->C2(v)
C2(v)-->D2(喜欢)
B2(VP)-->C3(NP)
C3(NP)-->D3(a)
D3(a)-->E1(红)
C3(NP)-->D4(NP)
D4(NP)-->E2(n)
E2(n)-->F1(苹果)
```
----
![33](pic/33.png)
----

#### 3.3.7 上下文无关文法的二义性
一个文法`$G$`,如果存在某个句子有不只一棵分析树与之对应,那么称这个文法是二义的。
----
例
文法`$G(E)$`的规则如下： 
1. `$E\rightarrow E+E$`
2. `$E\rightarrow E\times E$`
3. `$E\rightarrow E$`
4. `$E\rightarrow E-E$`
5. `$E\rightarrow i$` 

生成句子`$i+i\times i$`有两棵对应的分析树。

----

```mermaid
graph TD
A((E))-->B((E))
A((E))-->C((+))
A((E))-->D((E))
B((E))-->E((i))
D((E))-->F((E))
D((E))-->G((x))
D((E))-->H((E))
F((E))-->I((i))
H((E))-->J((i))
```
----
![3371](pic/3371.png)
----

```mermaid
graph TD
A((E))-->B((E))
A((E))-->C((+))
A((E))-->D((E))
B((E))-->F((E))
B((E))-->G((x))
B((E))-->H((E))
F((E))-->I((i))
H((E))-->J((i))
D((E))-->E((i))
```
----
![3372](pic/3372.png)


----
句子

"The boy saw a girl in a park with a telescope."

有多少意义?
----
```mermaid
graph TD
A(The boy saw a girl in a park with a telescope.)
A-->B1(NP)
A-->B2(VP)
B1-->C1(Det)
B1-->C2(n)
B2(VP)-->C3(VP)
C3(VP)-->D1(VP)
D1(VP)-->E1(v)
D1(VP)-->E2(NP)
E2(NP)-->F1(Det)
E2(NP)-->F2(n)
C3(VP)-->D2(PP)
D2(PP)-->C5(P)
D2(PP)-->C6(NP)
C6(NP)-->D3(Det)
C6(NP)-->D4(n)
B2(VP)-->C4(PP)
C4(PP)-->D5(p)
C4(PP)-->D6(NP)
D6(NP)-->E3(Det)
D6(NP)-->E4(n)


```
----
![3373](pic/3373.png)

----
### 自动机

1. 图灵机
2. 线性界限自动机
3. 下推自动机
4. 有限自动机
----
#### 图灵机

- 图灵机在计算机科学中的地位
	- 自动机的最高形式
	- 现代电子计算机的理论模型
	- 可计算性和计算复杂性的判断基准
----
从机械装置的角度来说，图灵机由一条可以（向右）无限延长的输入带、一个有限状态控制装置和一个连接控制器与输入带的读写头组成，如图所示

![3376](pic/3376.png)
----
有限状态控制器的状态转换和动作规则是图灵机的核心要素。图灵机在当前状态下扫描到带上的一个字符时，要执行3件工作：
1. 进行状态转换；
2. 读写头在带上的当前格写上新的字符；
3. 决定读写头向左还是向右移动一格。
----
图灵机`$M$`是一个七元组：

`$M=(\Sigma,Q,\delta,\Gamma,q_0,B,F)$`,

其中,`$\Sigma$`是输入符号的有穷集合;
`$Q$`是状态的有限集合;`$q_0$`是初始状态,`$q_0\in Q$`;`$\Gamma$`是带符号集;
`$F$`是终止状态集合,`$F\subseteq Q$`;`$B(B\in F)$`
`$\delta$`是`$Q$`与`$\Sigma$`的直积`$Q\times \Sigma$`到`$Q$`(下一个状态)的映射。
它支配着有限状态控制的行为,有时也称为状态转移函数。
----
#### 线性界限自动机
----
1. 线性界限自动机的`$\sigma$`中包括两个特殊符号#和$，分别表示输入链的左端和右端结束标志。
2. 线性界限自动机`$M$`的格局，以及两个格局之间转移关系的定义与图灵机的相同。
3. 线性界限自动机与图灵机的唯一不同是对读/写头位置的限制。
----
4. 在线性界限自动机中，对于读/写超出输入字符串长度范围时，转移动作没有定义。
5. 对于任何状态`$q\in Q$`和`$A\in\Gamma$`，如果映射`$\delta(q,A)$`包含的成员(下一个状态)不超过一个，则线性界限自动机是确定的。

如果`$L$`是一个上下文相关语言，则L由一个不确定的线性界限自动机所接受。反之，如果L被一个线性界限自动机所接受，则L是一个上下文相关语言。
----
#### 下推自动机(Push-Down Automata, PDA) 

PDA可以看成是一个带有附加的下推存储器的有 限自动机,下推存储器是一个栈。

----

定义:一个不确定的PDA可以表达成一个7元组,即`$M=(\Sigma,Q,\Gamma,\delta,q_0,F)$`其中, 
`$\Sigma$`是输入符号的有穷集合; 
`$Q$`是状态的有限集合; 
`$q_0\in Q$`是初始状态; 
`$\Gamma$`为下推存储器符号的有穷集合; 
`$Z_0\in \Gamma$`为最初出现在下推存储器顶端的开始符号; 
`$F$`是终止状态集合`$F\subseteq Q$`; 
`$\delta$`是从`$Q\times(\Sigma\bigcup\{\epsilon\})\times\Gamma$`到`$Q\times\Gamma*$`的子集的映射。
----
### 有限自动机
作为描述语言的一种途径，自动机对输入的句子进行检验，区别哪些是语言中的句子，哪些不是语言中的句子。
----

#### 3.3.1 确定的有限自动机(Definite Automata, DFA) 
----

确定的有限自动机`$M$`是一个五元组：

`$M=(\Sigma,Q,\delta,q_0,F)$`,

其中,`$\Sigma$`是输入符号的有穷集合;
`$Q$`是状态的有限集合;`$q_0$`是初始状态,`$q_0\in Q$`;
`$F$`是终止状态集合,`$F\subseteq Q$`;`$\delta$`是`$Q$`与`$\Sigma$`的直积`$Q\times \Sigma$`到`$Q$`(下一个状态)的映射。
它支配着有限状态控制的行为,有时也称为状态转移函数。
----

处在状态`$q_0\in Q$`中的有限控制器从左到右依次从
输入带上读入字符。开始时有限控制器处在状态`$q_0$`，
并注视`$\Sigma^*$`中一个链的最左符号。映射`$\delta(q,a)=q'(q,q'\in Q,a\in \Sigma)$` 表示在状态`$q$`时，若输入符号为`$a$`，则
自动机进入状态`$q'$`并且将输入头向右移动一个字符。
----
##### 状态变换图
映射`$\delta(q,a)=q'$`可以由状态变换图描述。
<!--
```mermaid
graph LR
A((q))--a--\>B((q'))
```
-->
![3374](pic/3374.png)

<!--为了明确起见，终止状态用双圈表示，起始状态用有“开始”标记的箭头表示。-->
----
#### 3.3.1 DFA定义的语言
如果一个句子`$x$`使得有限自动机`$M$`有`$\delta(q_0,x)=p$`,`$p\in F$`,那么,称句子`$x$`被`$M$`接受。

由`$M$`定义的语言`$T(M)$`就是被`$M$`接受的句子的全集。即,

`$T(M)=\{x|\delta(q_0,x)\in F\}$`

----

#### 不确定的有限自动机(Non-definite Automata, NFA)

----
不确定的有限自动机`$M$`是一个五元组：

`$M=(\Sigma,Q,\delta,q_0,F)$`

其中,`$\Sigma$`是输入符号的有穷集合;`$Q$`是状态的有限集合;`$q_0$`是初始状态,`$q_0\in Q$`;`$F$`是终止状态集合,`$F\subseteq Q$`;`$\delta$`是`$Q$`与`$\Sigma$`的直积`$Q\times \Sigma$`到`$Q$`的幂集`$2^Q$`的映射。
----
##### NFA与DFA的关系
设L是一个被NFA所接受的句子的集合，则存在一个DFA，它能够接受L。由于DFA与NFA所接受的是同样的链集，所以一般情况下无需区分它们，二者统称为有限自动机(Finite Automata, FA)。
----
NFA与DFA的唯一区别是:

在NFA中`$\delta(q,a)$`
是一个状态集合,而在DFA中`$\delta(q,a)$`是一个状态。
----
![3375](pic/3375.png)
<!--
```mermaid
graph TD
A((q0))--0,1--/>A
A--1--/>B((q1))
B--1--/>C((q2))
C--0,1--/>C
A--0--/>D((q3))
D--0--/>F((q4))
F--0,1--/> F
```
-->

该自动机为不确定自动机,
----
句子`$x=01011$`可以被接受。

<!--
##### 正则文法与有限自动机的关系
若`$G=(V_N,V_T,P,S)$`是一个正则文法，则存在一个有限自动机`$M=(\Sigma,Q,\delta,q_0,F)$`,使得`$T(M)=L(G)$`。

由`$G$`构造`$M$`的一般步骤：
1. 令`$\Sigma =V_T,Q=V_N\bigcup{T},q_0=S$`,其中`$T$`是一个新增加的非终结符。
2. 如果在`$P$`中有产生式`$S\rightarrow \epsilon$`,则`$F=\{S,T\}$`,否则`$F=\{T\}$`
3. 如果在`$P$`中有产生式`$B\rightarrow a, B\in V_N, a\in V_T$`,则`$T\in \delta(B,a)$`。
4. 如果在`$P$`中有产生式`$B\rightarrow aC, B,C\in V_N, a\in V_T$`,则`$C\in \delta(B,a)$`。
5. 对于每一个`$a\in V_T$`,有`$\delta(T,a)=\phi$`。

例如，给定正则文法`$G=\{V_N,V_T,P,S\}$`, 

其中,`$V_N=\{S,B\},V_T=\{a,b\}$`,

`$P=\{S\rightarrow aB, B\rightarrow bS|aB|a\}$`

构造与`$G$`等价的NFA


1. 设`$NFA=(\Sigma,Q,\delta,q_0,F)$` 根据上述步骤有: 

`$\Sigma=V_T=\{a,b\}$`,
`$Q=V_N\bigcup\{T\}=\{S,B,T\}$`,

`$q_0=S$` ,`$F=\{T\}$`

2. 映射`$\delta$`为`$\delta(S,a)=\{B\}$`(因为有规则`$S\rightarrow aB$`),`$\delta(S,b)=\phi$` 
,`$\delta(B,a)=\{B,T\}$`(因为有`$B\rightarrow aB,B\rightarrow a$`) 
,`$\delta(B,b)=\{S\}$`(因为有`$B\rightarrow bS$`) 
,`$\delta(T,a)=\phi$` 
,`$\delta(T,b)=\phi$` 

定理：若`$M=(\Sigma,Q,\delta,q_0,F)$`是一个有限自动机，则存在正则文法`$G=(V_N,V_T,P,S)$`使`$L(G)=T(M)$`。
由`$M$`构造`$G$`的一般步骤:
1. 令`$V_N=Q,V_T=\Sigma,S=q_0$`;
2. 如果`$C\in \delta(B,a),B,C\in Q, a\in \Sigma$`,则在`$P$`中有产生式`$B\rightarrow aC$`;
3. 如果`$C\in \delta(B,a),C\in F$`,则在`$P$`中有产生式`$B\rightarrow a$`; 
等价的NFA的状态变换图为：


```mermaid
graph LR
A(开始)--\>B((S))
B--a--\>C((B))
C--a--\>D((T))
C--a--\>C
C--a--\>B
```
结论：对于任意一正则文法，总可以构造一个识别器——DFA。
-->


<!--

##### 映射关系`$\delta$`的解释
映射关系`$\delta(q,a,Z)=\{(q_1,\gamma_1),(q_2,\gamma_2),...,(q_m,\gamma_m)\}$`其中, 
`$q_1,q_2,...,q_m\in Q$` 
`$a\in\Sigma$` 
`$Z\in\Gamma$` 
`$\gamma_1,\gamma_2,...,\gamma_m\in\Gamma*$` 
该映射的意思是：当PDA处于状态`$q$`,面临输入符号`$a$`时，自动机将进入到`$q_i,i=1,2,...,m$`状态,并以`$\gamma_i$`来代替下推存储器（栈）顶端符号`$Z$`,同时将输入头 指向下一个字符。当`$Z$`被`$\gamma_i$`取代时,`$\gamma_i$`的符号按照 从左到右的顺序依次从下向上推入到存储器。 
特殊情况下，`$\delta(q,\epsilon,Z)=\{(q_1,\gamma_1),(q_2,\gamma_2),...,(q_m,\gamma_m)\}$`时，输入头位置不移动,只用于处理下推存储器内部的操作,叫作"`$\epsilon$`移动"。

-->

----
#### 语言与识别器的对应关系 
识别器是有穷地表示无穷语言的另一种方法。每一个语言的句子都能被一定的识别器所接受。


语言类型 | 识别器类型 | 文法类型
:-: | :-: | :-: 
0型 | 图灵机 | 无约束文法
1型 | 线性界限自动机 | 上下文有关文法
2型 | 下推自动机 | 上下文无关文法
3型 | 有限自动机 | 正则文法


<!--

#### 3.3.5 语言与文法类型的约定
如果一种语言能由几种文法所产生，则把这种语言称为在这几种文法中受限制最多的那种文法所产生的语言。 

例如,文法`$G=\{\{S,A,B\}\},\{a,b\},P,S\}$`,非终极符号`$N=\{S,A,B,C\}$`,终极符号 `$\Sigma=\{a,b,c\}$`
,规则`$P$`如下：

1. `$S\rightarrow aB$`
2. `$S\rightarrow bA$`
3. `$A\rightarrow aS$`
4. `$A\rightarrow bAA$`
5. `$A\rightarrow a$`
6. `$B\rightarrow bS$`
7. `$B\rightarrow aBB$`
8. `$B\rightarrow b$`

`$G$`为上下文无关文法。 `$L(G)=\{$` 等数量的a和b构成的链`$\}$`

#### 3.3.6 句型与句子 
殊符号串为文法`$G=\{N,\Sigma,P,S\}$`的句型如下：
1. `$S$`是一个句型；
2. 如果`$\alpha \beta \gamma$`是一个句型，且`$\beta \rightarrow \sigma$`是`$P$`的生产式，则`$\alpha \sigma \gamma$`也是一个句型；
- 文法`$G$`的不含非终结符的句子形式称为`$G$`生成的句子。由文法`$G$`生成的语言，记作`$L(G)$`,指`$G$`生成的所有句子的集合。即`$L(G)=\{x|x \in \Sigma, S \Rightarrow_G^*x\}$`
-->
----

语言分析涉及的内容：
1. 句法范畴。如名词短语(NP)、动词短语(VP)、名词(N)、动词(V)等，用以表示句法单位的类别；
1. 词。例如：“学生”“学习”“语言学等”。它们是句子切分的最终结果；
1. 句法成分之间的关系。如句子由名词短语和动词短语组成，动词短语由动词和名词短语组成等；
1. 句子(S)。在语法分析中，“句子”这个语法范畴具有特殊性，它是句子切分和分析的出发点。
----
|  语言分析   | 自动机  |
|  ----  | ----  |
| 句法范畴  | 非终极词汇集 |
| 词  | 终极词汇集 |
| 句法成分之间的关系  | 重写规 |
| 句子  | 起始符 |

----
####  思考与练习
1. 人工语言与自然语言有什么不同？ 
2. “形式”是什么意思？什么叫语言研究的形式化方法？
3. 语言研究的形式化方法需要满足哪些条件？
4. 简述语言研究形式化的必要性和可能性。
5. 形式语言学的创始人是谁？奠基作品是什么？
6. 语言体系与数学体系是否具有可比性？为什么？
7. 乔姆斯基是如何证明“语言是句子的无限的集合”的？
8. 形式语法具有哪些构成要素？
9. 形式语法的特点是什么？
10. 举例说明上下文相关语法与上下文无关语法的不同。
11. 什么叫自动机？举例说明有限自动机是如何识别语句的。

---
## 4 语言模型
----
### 主要内容
1. 基本概念
2. 参数估计
3. 数据平滑
4. 语言模型的自适应
5. 神经概率语言模型
6. 语言模型的评价方法
7. 语言模型的应用

----
### 基本概念
大规模语料库的出现为自然语言统计处理方法的实现提供了可能，统计方法的成功使用推动了语料库语言学的发展。

基于大规模语料库和统计方法可以用于发现语言使用的普遍规律，通过机器学习自动获取语言知识推测未知语言现象。

如何计算一个句子出现的概率？
----
例如：
“人不能两次踏入同一条河流，因为无论是这条河还是这个人都已经不同。”

- 以句子为单位计算其在所有使用过的句子中的概率？

- 根据句子构成单位计算其联合概率？

----
#### 什么是语言模型

$$
P(s)=P(w_1)\times P(w_2|w_1)\times P(w_3|w_1w_2)\times ...
$$
$$
\times P(w_n|w_1...w_{n-1})
=\prod P(w_i|w_1...w_{i-1})
$$
当`$i=1$`时,`$P(w_1|w_0)=P(w_1)$`,这就是语言模型。
----
需要注意的是
- `$w_i$`可以是字、词、短语或词类等等，称为统计基元。通常以“词”代称。  
- `$w_i$`的概率由 `$w_i...w_{i-1}$`决定,由特定的一组`$w_i...w_{i-1}$`构成的一个序列，称为`$w_i$`的历史。
----
问题：

随着历史基元数量的增加，不同的“历史”(路径)成指数增长。对于第`$i(i>1)$`个统计基元,历史基元的数量为`$i-1$`个。如果共有`$L$`个不同的基元,如词表。理论上每一个词语都有可能出现在1到`$i-1$`的位置上，第`$i$`个基元就有`$L_{i-1}$`中不同的历史。这样，在考虑所有`$L_{i-1}$`种不同历史的情况下产生的第`$i$`个基元的概率，模型中就会有`$𝐿_𝑚$`个自由参数`$P(w_n|w_1...w_{n-1})$`  
如果`$L=5000,m=3$`,自由参数的数目为1250亿！

----
解决办法：

- 减少历史基元的个数,将`$w_iw_2...w_{i-1}$`映射到等价类 `$S(w_iw_2...w_{i-1})$`使等价类的数目远远小于原来不同历史基元的数目。

- 则有：  
`$P(w_i|w_1...w_{i-1})=P(w_i|S(w_1...w_{i-1}))$`


这就是划分等价类的方法

----
#### N元语言模型

这种情况下的语言模型称为n元文法(n-gram)。
1. 当`$n=1$`时,即出现在第`$i$`位上的基元`$w_i$`独立于历史,n-gram 被称为一阶马尔柯夫链(uni-gram 或monogram)
2. 当`$n=2$`时,n-gram被称为2阶马尔柯夫链(bi-gram)
3. 当`$n=3$`时,n-gram被称为3阶马尔柯夫链(tri-gram)

----

为了保证条件概率在`$i=1$`时有意义,同时为了保证句子内所有字符串的概率和为 1,即`$\Sigma_sp(s)=1$`,可以在句子首尾两端增加两个标志:
<BOS>`$w_1w_2...w_m$`<EOS>不失一般性，对于`$n>2$`的n-gram`$P(s)$`可以分解为：
$$
P(s)= \prod_{i=1}^{m+1}P(w_i|w_{i-n+1}^{i-1})
$$
其中,`$w_i^j$`表示词序列`$w_i...w_j$`,约定`$w_0$`为<BOS>,`$w_{m+1}$`为<EOS>。
----
例如，给定句子："John read a book"
- 首先，增加标记：\<BOS\> John read a book \<EOS\>

- 然后，2元文法的概率为：
`$P(John\ read\ a\ book) = $`
`$P( John|<BOS> )\times P(read | John)$`
`$\times P(a|read)\times P(book|a)\times P(<EOS> | book )$`
----

例如，给定拼音串：ta shi yan jiu sheng wu de

可能的汉字串:  
1. 踏实研究生物的  
2. 他实验救生物的  
3. 他使烟酒生物的  
4. 他是研究生雾的  
5. … …
----

如果使用2-gram：

`$P(CString1) =P(踏实|<BOS>)\times P(研究|踏实)\times$`
`$P(生物|研究)\times P(的|生物)\times P(<EOS>|的)$`

`$P(CString2) =P(他|<BOS>)\times P(实验|他)\times P(救|实验)$`
`$\times P(生物|救)\times P(的|生物)\times P(<EOS>|的)$`

`$P(CString3) =P(他|<BOS>)\times P(是|他)\times P(研究|是)$`
`$\times P(生物|研究)\times P(的|生物)\times P(<EOS>|的)$`
……
----
#### N元语法模型生成字符串的规模
当语料汉字的总数为`$N$`时
- 一元语法：
	1. 样本空间为`$N$`
	2. 只选择使用频率最高的汉字
- 二元语法：
	1. 样本空间为`$N^2$`
	2. 效果比一元语法明显提高

微软拼音输入法基于n-gram  
对汉字而言四元语法效果会好一些
----
例如,汉语分词问题  

给定汉字串：他是研究生物的。  
- 可能切分出的字符串组合：  

1. 他|是|研究生|物|的  
2. 他|是|研究|生物|的  
----
如果使用2-gram：  

`$P(Seg1)=P(他|<BOS>)\times P(是|他)\times P(研究生|是)$`
`$\times P(物|研究生)\times P(的|物|)\times P(<EOS>|的) $` 

`$P(Seg2)=P(他|<BOS>)\times P(是|他)\times P(研究|是)$`
`$\times P(生物|研究)\times P(的|生物|)\times P(<EOS>|的)$`
----
#### 问题：如何获得n元语法模型？

----
#### 两个重要概念：
- 训练语料(training data)：用于建立模型，确定模型参数的已知语料。
- 最大似然估计(maximum likelihood Evaluation,MLE)：用相对频率计算概率的方法。
参数：用来计算`$p(w|h)$` 的数值,从训练语料数据中得到
----

#### 数据准备
- 去掉格式符号
- 定义词的边界
- 定义句子边界(插入\<BOS\>和\<EOS\>等记号)
- 字母的大小写（保留、忽略或者智能识别）
- 数字（保留、替换为\<num\>等）
- ……
----
#### n-gram参数估计
对于n-gram,参`$P(w_i|w_{i-n+1}^{i-1})$`数可由最大似然估计求得
$$
P(w_i|w_{i-n+1}^{i-1})=f(w_i|w_{i-n+1}^{i-1})=\frac{c(w_{i-n+1}^i)}{\sum_{w_i}c(w_{i-n+1}^i)}
$$
----
其中,`$\sum_{w_i}c(w_{i-n+1}^i)$`是历史字符串`$w_{i-n+1}^{i-1}$`在给定语料中出现的次数,即`$c(w_{i-n+1}^{i-1})$`,不论`$w_i$`是什么。  
`$P(w_i|w_{i-n+1}^{i-1})$`是在给定`$w_{i-n+1}^{i-1}$`的条件下`$w_i$`出现的相对频率,分子为`$w_{i-n+1}^{i-1}$`与`$w_i$`同现的次数。

----
例如，给定训练语料：  
- “John read Moby Dick”  
- “Mary read a different book”  
- “She read a book by Carl”  
----
根据二元文法求句子的概率,把语料处理成如下：  

- \<BOS\> John read Moby Dick\<EOS\>  
- \<BOS\> Mary read a different book\<EOS\>  
- \<BOS\> She read a book by Carl\<EOS\>  
----
- `$P(John|<BOS>)=\frac{c(<BOS>\ John)}{\sum_wc(<BOS>\ w)}=\frac{1}{3}$`  
- `$P(read|John)=\frac{c(John\ read)}{\sum_wc(John\ w)}=\frac{1}{1}$`  
- `$P(a|read)=\frac{c(read\ a)}{\sum_wc(read\ w)}=\frac{2}{3}$`  
- `$P(book|a)=\frac{c(a\ book)}{\sum_wc(a\ w)}=\frac{1}{2}$`  
- `$P(<EOS>|book)=\frac{c(book\ <EOS>)}{\sum_wc(book\ w)}=\frac{1}{2}$`
- `$P(John\ read\ a\ book)=\frac{1}{3}\times 1\times \frac{2}{3}\times \frac{1}{2}\times \frac{1}{2}\approx 0.06$`

----
- `$P(Carl\ read\ a\ book)=?$`  
`$P(Carl\ read\ a\ book)=P(Carl|<BOS>)\times $`
`$P(read|Carl)\times P(a|read)\times$`
`$ P(book|a)\times P(<EOS>|book)$`  
- `$P(Carl|<BOS>)=\frac{c(<BOS>\ Carl)}{\sum_wc(<BOS>\ w)}=\frac{0}{3}=0$`  
- `$P(read|Carl)=\frac{c(Carl\ read)}{\sum_wc(Carl\ w)}=\frac{0}{1}=0$`  
- `$P(Carl\ read\ a\ book)=0$` 
----
<!--
  

-->
#### 问题:数据稀疏(Data Sparsness)

----
- 给定训练样本中未观察到的事件赋以0概率。
- 若某n-gram在训练语料中没有出现,则该n-gram的概率必定是0。
----
- 最直接的解决的办法是扩大训练语料的规模。但是无论怎样扩大训练语料，都不可能保证所有的词在训练语料中均出现。
----
- 由于训练样本不足而导致所估计的分布不可靠的问题，称为数据稀疏问题。
- 在NLP领域中，数据稀疏问题永远存在，不太可能有一个足够大的训练语料，因为语言中的大部分词都属于低频词。

----

#### 解决数据稀疏问题
对语言而言，由于数据稀疏的存在，最大似然估计(MLE) 不是一种很好的参数估计办法。 
----
#### 最大似然估计

例S = \<BOS\> He can buy you the can of soda  \<EOS\>   
- Unigram: (8 words in vocabulary)  
	- `$p_1(He) = p_1(buy) = p_1 (you) = p_1 (the) = p_1(of) = p_1(soda)= 0.125  $`  
	- `$ p_1(can) = 0.25$`
----  
- Bigram:  
	- `$p_2(He|<BOS>)=p_2(can|He) = 1$`  
	- `$p_2(buy|can)=p_2(of|can) = 0.5$`
	- `$,p_2(you|buy)= 1,...$`

----
1. 解决办法: 平滑技术
- 把在训练样本中出现过的事件的概率适当减小。即从大于0的MLE概率估算`$p(w)$`中得到`$p'(w)$`,`$p'(w)<p(w)$`
- 把减小得到的概率密度分配给训练语料中没有出现过的事件。即
`$\sum(p(w)-p'(w))=D$`
把`$D$`分配到`$p(w)=0$`的事件中，保证`$\sum p'(w)=1$`,这个过程有时也称为discounting(减值)
----
2. 基本目标：测试样本的语言模型困惑度越小越好。
3. 基本约束：`$\sum_{w_i}P(w_i|w_1,w_2,...,w_{i-1})=1$`
----
- 困惑度是交叉熵的指数形式
- 交叉熵
$$
H_p(T)=\frac{1}{W_T}\log P(T)
$$
其中，`$W_T$`是测试文本的词数。

- 困惑度
$$Perplexity=2^{H(T)}$$
----
例  
S = \<BOS\> It was the greatest buy of all \<EOS\>  

`$H_S(p_1)=H_S(p_2)=H_S(p_3) =\infty$`  
原因是：  
1. 所有的unigram除了`$p_1(the)$`, `$p_1(buy)$`, `$p_1(of)$`都是0
2. 所有bigram的概率都是 0.  
3. 所有trigram的概率都是 0.  

我们希望使每个概率都是非零的

----
### 数据平滑
目前已经提出了很多数据平滑技术，如：
- Add-one 平滑
- Add-delta 平滑
- Witten-Bell平滑
- Good-Turing平滑
- Church-Gale平滑
- Jelinek-Mercer平滑
- Katz平滑
- ……
----

#### Add-one平滑(Laplace’s law)
基本思想: 每一种情况出现的次数加1. 
`$count_{new}(n-gram)=count_{old}(n-gram) + 1$`  
没有出现过的n-gram的概率不再是0
----

平滑后的概率计算公式为：
$$
P_{addone}(w_1w_2..w_n)=\frac{c(w_1w_2...w_n)+1}{N+V}
$$

其中,`$N$`为训练语料中所有的n-gram的数量(token)  
`$V$`为所有的可能的不同的n-gram的数量(type)  

----
全部概率之和为：  
$$
\sum P_{addone}(w_1w_2...w_n)=\sum \frac{c(w_1w_2...w_n)+1}{N+V}
$$
$$
=\frac {\sum {c(w_1w_2...w_n)+1}}{N+V}
=\frac {N+V}{N+V}=1
$$
其中，`$T$`为训练数据,`$V$`为词表,`$w$`为词

Add-one平滑方法是出现n次的词，假设出现n+1次，这种方法最简单但效果较差。
----


#### Add-one平滑的问题
1. 训练语料中未出现的n-gram的概率不再为0,而是一个大于0的较小的概率值。
2. 但由于训练语料中未出现n-gram数量太多,平滑后,所有未出现的n-gram占据了整个概率分布中的一个很大的比例。
----
#### Add-one平滑的问题
3. 因此，在NLP中,Add-one给训练语料中没有出现过的n-gram分配了太多的概率空间。
4. 认为所有未出现的n-gram概率相等,这是否合理？
5. 出现在训练语料中的那些n-gram,都增加同样的频度值,这是否公平？(低频、高频)
----

各种平滑方法的详细介绍和比较请参阅

[Stanley Chen的研究相关研究](http://www.cs.cmu.edu/~sfc/html/publications.html)

----


### 4.4 语言模型的自适应
- 一方面,在训练语言模型时所采用的语料往往来自多种不同的领域,这些综合性语料难以反映不同领域之间在语言使用规律上的差异,而语言模型恰恰对于训练文本的类型、主题和风格等都十分敏感；
- 另一方面,`$n$`元语言模型的独立性假设的前提是一个文本中的当前词出现的概率只与它前面相邻的`$n-1$`个词相关,但这种假设在很多情况下是明显不成立的。
----
#### 4.4.1  数据平滑的问题
1. 跨领域的脆弱性
2. 独立性假设的无效性
3. 提高语言模型对语料的领域、主题、类型等因素的适应性
----
#### 4.4.2 自适应方法
1. 基于缓存的语言模型(cache-based LM)
2. 基于混合方法的语言模型
3. 基于最大熵的语言模型
----
#### (1) 基于缓存的语言模型(cache-based LM)
该方法针对的问题是：在文本中刚刚出现过的一些词在后边的句子中再次出现的可能性往往较大，比标准的n-gram模型预测的概率要大。针对这种现象，cache-based自适应方法的基本思路是：语言模型通过n-gram的线性插值求得：

$$
\hat P(w_i|w_1^{i-1})=\lambda\hat P_{Cache}(w_i|w_1^{i-1})
$$
$$
+(1-\lambda)\hat P_{n-gram}(w_i|w_{i-n+1}^{i-1})
$$
----
通常的处理方法是：在缓存中保留前面的`$K$`个单词，每个词的概率（缓存概率）用其在缓存中出现的相对频率计算得出：
$$
\hat P_{Cache}(w_i|w_1^{i-1})=\frac{1}{k}\sum_{j=i-K}^{i-1}I_{w_j=w_i}
$$
其中,`$I_{\epsilon}"$`为指示器函数(indicator function),如果`$\epsilon$`表示的情况出现，则`$I_{\epsilon}=1$`否则`$I_{\epsilon}=0$`
----
这种方法的缺陷是，缓存中一个词的重要性独立于该词与当前词的距离。P. R. Clarkson等人(1997) 的研究表明，缓存中每个词对当前词的影响随着与该词距离的增大呈指数级衰减，因此：
$$
\hat P_{Cache}(w_i|w_1^{i-1})=\beta\sum_{j=1}^{i-1}I_{w_i=w_j}e^{-\alpha(i-j)}
$$
----
$$
\sum_{w_i\in V}P_{Cache}(w_i|w_1^{i-1})=1
$$
其中,`$beta$`衰减率,`$e$`为归一化常数,以使得,`$V$`为词汇表
----
#### (2) 基于混合方法的语言模型
该方法针对的问题是：由于大规模训练语料本身是异源的(heterogenous)，来自不同领域的语料无论在主题(topic)方面，还是在风格(style)方面，或者两者都有一定的差异，而测试语料一般是同源的(homogeneous)，因此，为了获得最佳性能，语言模型必须适应各种不同类型的语料对其性能的影响。

----
处理方法:将语言模型划分成`$N$`个子模型`$M_1,M_2,...,M_n$`整个语言模型的概率通过下面的线性插值公式计算得到。
`$
\hat P(w_i|w_1^{i-1})=\sum_{j=1}^n\lambda_j\hat P_{M_j}(w_i|w_1^{i-1})
$`
其中,`$0\leq\lambda\leq 1,\sum_{j=1}\lambda_j=1$`值可以通过EM算法计算出来
----
1. 对训练语料按来源、主题或类型等聚类；
1. 在模型运行时识别测试语料的主题或主题的集合；
1. 确定适当的训练语料子集，并利用这些语料建立特定的语言模型；
1. 利用针对各个语料子集的特定语言模型和线性插值，获得整个语言模型。

----

#### (3) 基于最大熵的语言模型
基本思想:通过结合不同信息源的信息构建一个语言模型。每个信息源提供一组关于模型参数的约束条件，在所有满足约束的模型中，选择熵最大的模型。

----

### 4.5 神经概率语言模型
统计语言模型的目标是学习一种语言中词序列的联合概率函数，但是由于维数灾难的问题让这变得困难。  
n-gram模型是一种近似策略，作了一个马尔可夫假设：认为目标词`$w_i$`的条件概率只与其之前的`$n-1$`个词有关。一个词序列会被测视为与之前训练中出现的所有词序列都不同。通过训练重叠的短的词序列的联系从而得到泛化模型。
----
#### 4.5.1 基本思想
通过学习词的词向量，把每个句子的语义指数告诉模型，从而解决维数灾难的问题。这个模型同时也会学习每个词的词向量和这个词序列的概率函数，并用这种方式表达。如果出现此前从没见过的词序列，并且与出现过的句子在意思上相似有着相似的单词，则它会有一个较高的概率，因此这样就会获得泛化。显著的改善了最先进的n元语法模型，并且这个方法允许使用更长的上下文。
----
#### 4.5.2 相关概念

1. One-Hot Representation（独热）
2. Distributed Representation
----
1. One-Hot Representation（独热）
最早的词向量是很冗长的，大小为整个词汇表的大小，对于每个具体的词汇表中的词，它使用是词向量维度将对应的位置置为1。
比如我们有下面的5个词组成的词汇表，词"Queen"的序号为2， 那么它的词向量就是[0,1,0,0,0]。同样的道理，词"Woman"的词向量就是[0,0,0,1,0]。这种词向量的编码方式我们一般叫做one-hot representation.
----
#### One-Hot Representation存在的问题
最大的问题是我们的词汇表一般都非常大，比如达到百万级别，这样每个词都用百万维的向量来表示简直是内存的灾难。这样的向量其实除了一个位置是1，其余的位置全部都是0，表达的效率不高。
----
2. Distributed Representation
基本思想是通过训练，将每个词都映射到一个较短的词向量上来。所有的这些词向量就构成了向量空间，进而可以用普通的统计学的方法来研究词与词之间的关系。这种向量可以表示为：
[0.792, −0.177, −0.107, 0.109, −0.542, …]。
维度以50维和100维比较常见
----
#### 4.5.3 基本结构
神经概率语言模型可以分为四层，即输入层，embedding层，隐藏层，输出层。（也可以分为三层，即把embedding层当做输入层，然后隐藏层、输出层，其实在实际操作中实际的输入就是embedding层（词向量））
----
##### CBOW模型
![image](https://img-blog.csdnimg.cn/20190605104659312.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5MTYxMjE2,size_16,color_FFFFFF,t_70)
----
##### skip-gram模型
![image](https://img-blog.csdnimg.cn/20190605104845595.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5MTYxMjE2,size_16,color_FFFFFF,t_70)
----
1. 输入层  
用词在词表中的位置（下标），比如几个单词：我 是 教师，在词表中的位置是[3,220]，只要存这几个下标就行了。然后根据下标去embedding层的矩阵中找对应的行。
----
2. embedding层
embedding层实际上是一个矩阵，这个矩阵又叫look-up table。这个矩阵长这个样子，`$|V|$`行数为 ，就是词表的大小，列数为`$h_1$`，即每个词向量的维度，这个维度一般要比one-hot表示的词向量（维度为词表大小）小很多。矩阵的值开始时随机初始化。这样矩阵的每一行就为一个词向量（BP(back propagation)后，每行都是`$h_1$`的实数），可以用来表示一个单词。
----
3. 隐藏层
用的sigmoid函数作为激活函数，bengio的论文中用的tanh函数
4. 输出层
输出层用的softmax函数

----
### 4.6 语言模型的评价方法

- 最佳方法:  
 将语言模型用于某一个应用中，例如拼写检查、机器翻译等

----
- 困惑度(Perplexity):   
假定测试语料`$T$`由`$n$`个句子组成`$T={S_1,S_2,...,S_n }$`则整个测试语料的概率为:
$$
P(T)=\prod_{i=1}^nP(S_i)
$$
----
以对数形式表示的测试语料的概率为：
$$
\log P(T)=\log \prod_{i=1}^nP(S_i)=\sum_{i=1}^n\log P(S_i)
$$
----
测试语料的交叉熵为：
$$
H_p(T)=-\frac{1}{W_T}\log_2P(T)=-\frac{1}{W_T}\sum_{i=1}^n\log_2P(S_i)
$$
----
困惑度(Perplexity): 
$$
P(T)=2^{H_p(T)}
$$
----
### 4.7 语言模型的应用
----
#### 汉语分词问题
方法描述,设对于待切分的句子`$S=z_1,z_2,...z_m,W=w_1,w_2,...,w_k(1\leq k\leq n)$`是一种可能的切分。那么
$$
W=\arg \max P(W|S)=
$$
$$
\arg \max P(W)P(S|W)\cong \arg \max P(W)
$$
----

<!--
#### 4.7.2 word2vec
基本思想是通过训练将每个词映射成`$K$`维实数向量(`$K$`一般为模型中的超参数)，通过词之间的距离（比如 cosine相似度、欧氏距离等）来判断它们之间的语义相似度.其采用一个三层的神经网络，输入层-隐层-输出层。有个核心的技术是根据词频用Huffman编码
-->

### 语言模型的进展
参阅[Two decades of statistical language modeling:  where do we go from here](https://kilthub.figshare.com/articles/Two_Decades_of_Statistical_Language_Modeling_Where_Do_We_Go_From_Here_/6611138/files/12103316.pdf)
----

### 练习
阅读《统计自然语言处理基础》第6章例子，下载该书配套的[Austen 语料库(包括训练集和测试集)](http://nlp.stanford.edu/fsnlp/)。

尝试利用MLE、Good turing估计建立Austen语料库的bigram模型。并将计算结果与参考书给出的部分结果进行比较。