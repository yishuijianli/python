# -*- coding: utf-8 -*-
"""
第9题：编写Python程序对书籍评论数据进行统计分析并进行可视化展示
任务要求：
1. 对评分进行频次统计并绘制折线图
2. 对评论内容生成词云图
3. 保存统计分析结果
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def load_data():
    """加载数据"""
    print("=" * 60)
    print("第9题：书籍评论数据统计分析与可视化")
    print("=" * 60)
    
    input_file = './data/book_comments.csv'
    if not os.path.exists(input_file):
        print(f"错误：找不到数据文件 {input_file}")
        return None
    
    print(f"\n正在读取数据：{input_file}")
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print(f"读取了 {len(df)} 条记录")
    
    return df

def analyze_rating_frequency(df, output_dir):
    """
    任务点i：对评分进行频次统计并绘制折线图
    """
    print("\n" + "=" * 60)
    print("任务点i：评分频次统计与折线图")
    print("=" * 60)
    
    # 提取评分数值
    df['评分_数值'] = df['评分'].str.extract('(\d+)').astype(int)
    
    # 统计评分频次
    rating_counts = df['评分_数值'].value_counts().sort_index()
    
    print("\n评分频次统计：")
    for rating, count in rating_counts.items():
        print(f"  {rating}星: {count} 条 ({count/len(df)*100:.1f}%)")
    
    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(rating_counts.index, rating_counts.values, 
             marker='o', linewidth=2, markersize=8, color='#2E86AB')
    
    # 在每个点上标注数值
    for x, y in zip(rating_counts.index, rating_counts.values):
        plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=10)
    
    plt.xlabel('评分（星级）', fontsize=12)
    plt.ylabel('评论数量', fontsize=12)
    plt.title('书籍评分频次分布折线图', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xticks(rating_counts.index)
    
    # 保存图片
    output_file = os.path.join(output_dir, '评分频次折线图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n折线图已保存到：{output_file}")
    plt.close()
    
    return rating_counts

def generate_wordcloud(df, output_dir):
    """
    任务点ii：对评论内容生成词云图
    """
    print("\n" + "=" * 60)
    print("任务点ii：评论内容词云图")
    print("=" * 60)
    
    try:
        from wordcloud import WordCloud
        
        # 合并所有评论内容
        all_text = ' '.join(df['内容'].astype(str))
        
        print(f"\n评论总字数：{len(all_text)}")
        
        # 生成词云
        wordcloud = WordCloud(
            font_path='C:/Windows/Fonts/simhei.ttf',  # 黑体
            width=1200,
            height=600,
            background_color='white',
            max_words=100,
            relative_scaling=0.5,
            colormap='viridis'
        ).generate(all_text)
        
        # 绘制词云图
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('书籍评论词云图', fontsize=16, fontweight='bold', pad=20)
        
        # 保存图片
        output_file = os.path.join(output_dir, '评论词云图.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\n词云图已保存到：{output_file}")
        plt.close()
        
    except ImportError:
        print("\n警告：未安装 wordcloud 库")
        print("请运行：pip install wordcloud")
        print("\n使用简单的词频统计代替...")
        
        # 简单的词频统计
        words = []
        for text in df['内容']:
            words.extend(list(text))
        
        word_freq = Counter(words).most_common(20)
        
        print("\n高频字符（前20个）：")
        for word, freq in word_freq:
            if word.strip():
                print(f"  '{word}': {freq} 次")
        
        # 绘制词频柱状图
        chars = [w[0] for w in word_freq if w[0].strip()][:15]
        freqs = [w[1] for w in word_freq if w[0].strip()][:15]
        
        plt.figure(figsize=(12, 6))
        plt.bar(chars, freqs, color='#A23B72')
        plt.xlabel('字符', fontsize=12)
        plt.ylabel('频次', fontsize=12)
        plt.title('评论高频字符统计', fontsize=14, fontweight='bold')
        plt.xticks(rotation=0)
        
        output_file = os.path.join(output_dir, '词频统计图.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\n词频统计图已保存到：{output_file}")
        plt.close()

def save_statistics(df, rating_counts, output_dir):
    """保存统计结果到文本文件"""
    output_file = os.path.join(output_dir, '统计分析结果.txt')
    
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.write("=" * 60 + "\n")
        f.write("书籍评论数据统计分析结果\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("一、数据概览\n")
        f.write("-" * 60 + "\n")
        f.write(f"总评论数：{len(df)} 条\n")
        f.write(f"涉及书籍：{df['书名'].nunique()} 本\n")
        f.write(f"评论作者：{df['作者'].nunique()} 人\n\n")
        
        f.write("二、评分频次统计\n")
        f.write("-" * 60 + "\n")
        for rating, count in rating_counts.items():
            percentage = count / len(df) * 100
            f.write(f"{rating}星: {count} 条 ({percentage:.1f}%)\n")
        
        f.write(f"\n平均评分：{df['评分_数值'].mean():.2f}星\n")
        f.write(f"评分中位数：{df['评分_数值'].median():.1f}星\n")
        f.write(f"评分众数：{df['评分_数值'].mode()[0]}星\n\n")
        
        f.write("三、书籍评论统计（Top 10）\n")
        f.write("-" * 60 + "\n")
        book_counts = df['书名'].value_counts().head(10)
        for i, (book, count) in enumerate(book_counts.items(), 1):
            f.write(f"{i}. {book}: {count} 条评论\n")
        
        f.write("\n四、评论时间分布\n")
        f.write("-" * 60 + "\n")
        df['日期'] = pd.to_datetime(df['日期'])
        df['月份'] = df['日期'].dt.to_period('M')
        month_counts = df['月份'].value_counts().sort_index()
        for month, count in month_counts.items():
            f.write(f"{month}: {count} 条评论\n")
        
        f.write("\n" + "=" * 60 + "\n")
        f.write("统计分析完成\n")
        f.write("=" * 60 + "\n")
    
    print(f"\n统计结果已保存到：{output_file}")

def main():
    """主函数"""
    # 加载数据
    df = load_data()
    if df is None:
        return
    
    # 创建输出目录
    output_dir = './data/数据分析与可视化结果'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n创建目录：{output_dir}")
    
    # 任务点i：评分频次统计与折线图
    rating_counts = analyze_rating_frequency(df, output_dir)
    
    # 任务点ii：生成词云图
    generate_wordcloud(df, output_dir)
    
    # 保存统计结果
    save_statistics(df, rating_counts, output_dir)
    
    print("\n" + "=" * 60)
    print("第9题完成！")
    print("=" * 60)
    print(f"\n所有结果已保存到：{output_dir}")
    print("\n生成的文件：")
    print("  - 评分频次折线图.png")
    print("  - 评论词云图.png (或 词频统计图.png)")
    print("  - 统计分析结果.txt")

if __name__ == '__main__':
    main()
