# -*- coding: utf-8 -*-
"""
评论数据分析示例
展示如何分析生成的评论数据
"""

import csv
from collections import Counter
import os

def load_comments(filepath):
    """加载CSV格式的评论数据"""
    comments = []
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            comments = list(reader)
        return comments
    except Exception as e:
        print(f"读取文件出错: {e}")
        return []

def analyze_ratings(comments):
    """分析评分分布"""
    print("\n" + "=" * 60)
    print("评分分布分析")
    print("=" * 60)
    
    ratings = [c['评分'] for c in comments]
    rating_count = Counter(ratings)
    
    total = len(ratings)
    for rating in sorted(rating_count.keys()):
        count = rating_count[rating]
        percentage = (count / total) * 100
        bar = "█" * int(percentage / 2)
        print(f"{rating}: {count:3d} 条 ({percentage:5.1f}%) {bar}")

def analyze_books(comments):
    """分析各书籍的评论数量"""
    print("\n" + "=" * 60)
    print("各书籍评论数量")
    print("=" * 60)
    
    books = [c['书名'] for c in comments]
    book_count = Counter(books)
    
    for book, count in book_count.most_common(10):
        bar = "█" * (count // 2)
        print(f"{book:15s}: {count:2d} 条 {bar}")

def analyze_sentiment(comments):
    """简单的情感分析"""
    print("\n" + "=" * 60)
    print("情感倾向分析")
    print("=" * 60)
    
    positive_words = ['好看', '推荐', '喜欢', '棒', '精彩', '感人', '经典', '值得']
    negative_words = ['失望', '一般', '枯燥', '别扭', '空洞', '拖沓', '老套']
    
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    for comment in comments:
        content = comment['内容']
        has_positive = any(word in content for word in positive_words)
        has_negative = any(word in content for word in negative_words)
        
        if has_positive and not has_negative:
            positive_count += 1
        elif has_negative and not has_positive:
            negative_count += 1
        else:
            neutral_count += 1
    
    total = len(comments)
    print(f"正面评论: {positive_count} 条 ({positive_count/total*100:.1f}%)")
    print(f"负面评论: {negative_count} 条 ({negative_count/total*100:.1f}%)")
    print(f"中性评论: {neutral_count} 条 ({neutral_count/total*100:.1f}%)")

def analyze_time(comments):
    """分析评论时间分布"""
    print("\n" + "=" * 60)
    print("评论时间分布（按月份）")
    print("=" * 60)
    
    months = [c['日期'][:7] for c in comments]  # 提取年-月
    month_count = Counter(months)
    
    for month, count in sorted(month_count.items())[-6:]:  # 显示最近6个月
        bar = "█" * (count // 2)
        print(f"{month}: {count:2d} 条 {bar}")

def word_frequency(comments):
    """词频统计（简单版）"""
    print("\n" + "=" * 60)
    print("高频词汇（前20个）")
    print("=" * 60)
    
    # 简单的分词（按字符）
    all_text = ' '.join([c['内容'] for c in comments])
    
    # 常见的高频词
    keywords = ['好看', '推荐', '喜欢', '不错', '一般', '失望', '精彩', '感人',
                '值得', '经典', '内容', '故事', '作者', '文笔', '情节']
    
    word_count = {}
    for word in keywords:
        count = all_text.count(word)
        if count > 0:
            word_count[word] = count
    
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:20]:
        bar = "█" * (count // 5)
        print(f"{word:6s}: {count:3d} 次 {bar}")

def main():
    print("=" * 60)
    print("书籍评论数据分析")
    print("=" * 60)
    
    # 检查文件是否存在
    filepath = './data/book_comments.csv'
    if not os.path.exists(filepath):
        print(f"\n错误：找不到数据文件 {filepath}")
        print("请先运行 python book_comment_real_data.py 生成数据")
        return
    
    # 加载数据
    print(f"\n正在加载数据: {filepath}")
    comments = load_comments(filepath)
    
    if not comments:
        print("没有数据可分析")
        return
    
    print(f"共加载 {len(comments)} 条评论")
    
    # 执行各种分析
    analyze_ratings(comments)
    analyze_books(comments)
    analyze_sentiment(comments)
    analyze_time(comments)
    word_frequency(comments)
    
    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)
    print("\n💡 提示：")
    print("  - 可以使用 pandas 进行更深入的数据分析")
    print("  - 可以使用 jieba 进行中文分词")
    print("  - 可以使用 wordcloud 生成词云")
    print("  - 可以使用 matplotlib 绘制图表")

if __name__ == '__main__':
    main()
