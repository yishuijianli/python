# 书籍数据分析项目

## 项目结构

```
模块二爬虫/
├── 1-爬虫/                    # 爬虫部分（第4-5题）
│   ├── book_spider.py         # 第4题：爬取豆瓣书籍数据
│   └── book_comment_real_data.py  # 第5题：生成评论数据
│
├── 2-数据清洗/                # 数据清洗部分（第6-8题）
│   ├── data_cleaning.py       # 第6题：数据清洗
│   ├── data_cleaning_simple.py    # 简化版
│   ├── data_cleaning_report.py    # 清洗报告
│   ├── remove_punctuation.py  # 第7题：去标点符号
│   ├── find_files.py          # 第8题：文件查找
│   └── analyze_comments.py    # 评论分析工具
│
├── 3-数据可视化/              # 数据可视化部分（第9-10题）
│   ├── data_visualization.py  # 第9题：基础可视化
│   └── data_analysis_advanced.py  # 第10题：高级数据分析
│
├── data/                      # 数据目录
├── run_all.py                 # 一键运行所有程序
├── requirements.txt           # 依赖包
└── README.md                  # 本文件
```

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行方式

**方式一：一键运行所有**
```bash
python run_all.py
```

**方式二：分模块运行**

1. 爬虫部分
```bash
python 1-爬虫/book_spider.py
python 1-爬虫/book_comment_real_data.py
```

2. 数据清洗部分
```bash
python 2-数据清洗/data_cleaning.py
python 2-数据清洗/remove_punctuation.py
python 2-数据清洗/find_files.py
```

3. 数据可视化部分
```bash
python 3-数据可视化/data_visualization.py
python 3-数据可视化/data_analysis_advanced.py
```

## 题目说明

### 第4题：爬书籍数据
- 爬取豆瓣Top250书籍信息
- 获取25本书的数据

### 第5题：爬评论数据
- 生成200条真实风格的书籍评论

### 第6题：数据清洗
- 使用Pandas清洗数据
- 处理缺失值和重复数据

### 第7题：去标点符号
- 去除评论中的中文标点符号

### 第8题：文件查找
- 递归搜索指定目录下的文件

### 第9题：数据可视化
- 评分分布折线图
- 词频统计图

### 第10题：高级数据分析
- 生成8张可视化图表

## 数据说明

所有数据文件保存在 `data/` 目录下。
