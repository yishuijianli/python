# -*- coding: utf-8 -*-
"""
第10题：编写Python程序，对书籍评论数据进行数据分析并进行可视化展示
任务要求：
1. 分析书籍上架后每天的评论数据走势，按天统计评论个数并绘制折线图
2. 分析每天评分的比例，并绘制柱状图
3. 保存数据分析和可视化结果
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def load_data():
    """加载数据"""
    print("=" * 60)
    print("第10题：书籍评论数据分析与可视化")
    print("=" * 60)
    
    input_file = './data/book_comments.csv'
    if not os.path.exists(input_file):
        print(f"错误：找不到数据文件 {input_file}")
        return None
    
    print(f"\n正在读取数据：{input_file}")
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print(f"读取了 {len(df)} 条记录")
    
    # 转换日期格式
    df['日期'] = pd.to_datetime(df['日期'])
    
    return df

def analyze_daily_comments(df, output_dir):
    """
    任务点i：分析书籍上架后每天的评论数据走势
    按天统计评论的个数，并且按照天进行排序，然后绘制折线图
    """
    print("\n" + "=" * 60)
    print("任务点i：每天评论数据走势分析")
    print("=" * 60)
    
    # 按天统计评论数量
    daily_counts = df.groupby(df['日期'].dt.date).size().sort_index()
    
    print(f"\n统计时间范围：{daily_counts.index[0]} 至 {daily_counts.index[-1]}")
    print(f"总天数：{len(daily_counts)} 天")
    print(f"平均每天评论数：{daily_counts.mean():.1f} 条")
    print(f"最多评论的一天：{daily_counts.idxmax()}，共 {daily_counts.max()} 条")
    
    print("\n每天评论数量（前10天）：")
    for date, count in daily_counts.head(10).items():
        print(f"  {date}: {count} 条")
    
    # 方案1：按周汇总的折线图（更清晰）
    plt.figure(figsize=(12, 6))
    
    # 按周汇总
    df['周'] = df['日期'].dt.to_period('W')
    weekly_counts = df.groupby('周').size().sort_index()
    
    plt.plot(range(len(weekly_counts)), weekly_counts.values, 
             marker='o', linewidth=2.5, markersize=8, color='#E63946', 
             alpha=0.8, label='每周评论数')
    
    # 添加趋势线
    z = np.polyfit(range(len(weekly_counts)), weekly_counts.values, 1)
    p = np.poly1d(z)
    plt.plot(range(len(weekly_counts)), p(range(len(weekly_counts))), 
             "--", color='#457B9D', alpha=0.6, linewidth=2, label='趋势线')
    
    # 在每个点上标注数值
    for i, v in enumerate(weekly_counts.values):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=9)
    
    plt.xlabel('周次', fontsize=12, fontweight='bold')
    plt.ylabel('评论数量', fontsize=12, fontweight='bold')
    plt.title('书籍评论每周走势图', fontsize=14, fontweight='bold', pad=15)
    plt.xticks(range(len(weekly_counts)), 
               [f'第{i+1}周' for i in range(len(weekly_counts))], 
               rotation=45, ha='right')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(loc='best', framealpha=0.9)
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每周评论走势图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n折线图已保存到：{output_file}")
    plt.close()
    
    # 方案2：按月汇总的柱状图
    plt.figure(figsize=(10, 6))
    
    df['月份'] = df['日期'].dt.to_period('M')
    monthly_counts = df.groupby('月份').size().sort_index()
    
    colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(monthly_counts)))
    bars = plt.bar(range(len(monthly_counts)), monthly_counts.values, 
                   color=colors_gradient, edgecolor='white', linewidth=1.5)
    
    # 在柱子上标注数值
    for i, (bar, v) in enumerate(zip(bars, monthly_counts.values)):
        plt.text(bar.get_x() + bar.get_width()/2, v + 1, str(v), 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.xlabel('月份', fontsize=12, fontweight='bold')
    plt.ylabel('评论数量', fontsize=12, fontweight='bold')
    plt.title('书籍评论每月统计图', fontsize=14, fontweight='bold', pad=15)
    plt.xticks(range(len(monthly_counts)), 
               [str(m) for m in monthly_counts.index], 
               rotation=0)
    plt.grid(True, alpha=0.3, axis='y', linestyle='--')
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每月评论统计图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"柱状图已保存到：{output_file}")
    plt.close()
    
    return daily_counts

def analyze_daily_rating_distribution(df, output_dir):
    """
    任务点ii：分析每天评分的比例，并绘制柱状图
    """
    print("\n" + "=" * 60)
    print("任务点ii：每天评分比例分析")
    print("=" * 60)
    
    # 提取评分数值
    df['评分_数值'] = df['评分'].str.extract('(\d+)').astype(int)
    
    # 按日期和评分分组统计
    daily_rating = df.groupby([df['日期'].dt.date, '评分_数值']).size().unstack(fill_value=0)
    
    # 计算每天各评分的比例
    daily_rating_pct = daily_rating.div(daily_rating.sum(axis=1), axis=0) * 100
    
    print("\n每天评分分布（前5天）：")
    print(daily_rating.head())
    
    print("\n每天评分比例（前5天）：")
    print(daily_rating_pct.head())
    
    # 方案1：按月汇总的柱状图（更清晰）
    plt.figure(figsize=(12, 6))
    
    # 按月汇总
    df['月份'] = df['日期'].dt.to_period('M')
    monthly_rating = df.groupby(['月份', '评分_数值']).size().unstack(fill_value=0)
    monthly_rating_pct = monthly_rating.div(monthly_rating.sum(axis=1), axis=0) * 100
    
    colors = ['#D62828', '#F77F00', '#FCBF49', '#90BE6D', '#43AA8B']
    
    x = np.arange(len(monthly_rating))
    width = 0.15
    
    for i, rating in enumerate([1, 2, 3, 4, 5]):
        if rating in monthly_rating.columns:
            offset = (i - 2) * width
            plt.bar(x + offset, monthly_rating[rating], width, 
                   label=f'{rating}星', color=colors[i], edgecolor='white', linewidth=0.5)
            
            # 在柱子上标注数值
            for j, v in enumerate(monthly_rating[rating]):
                if v > 0:
                    plt.text(j + offset, v + 0.5, str(v), 
                            ha='center', va='bottom', fontsize=8)
    
    plt.xlabel('月份', fontsize=12, fontweight='bold')
    plt.ylabel('评论数量', fontsize=12, fontweight='bold')
    plt.title('每月评分分布柱状图', fontsize=14, fontweight='bold', pad=15)
    plt.xticks(x, [str(m) for m in monthly_rating.index], rotation=0)
    plt.legend(title='评分', loc='upper left', framealpha=0.9)
    plt.grid(True, alpha=0.3, axis='y', linestyle='--')
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每月评分分布柱状图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n柱状图已保存到：{output_file}")
    plt.close()
    
    # 方案2：堆叠柱状图（按月，横向）
    plt.figure(figsize=(10, 8))
    
    # 使用横向柱状图，避免X轴标签重叠
    ax = monthly_rating_pct.plot(kind='barh', stacked=True, color=colors, 
                                  edgecolor='white', linewidth=1.5)
    
    plt.ylabel('月份', fontsize=12, fontweight='bold')
    plt.xlabel('评分比例 (%)', fontsize=12, fontweight='bold')
    plt.title('每月评分比例堆叠图（横向）', fontsize=14, fontweight='bold', pad=15)
    plt.legend(title='评分', labels=['1星', '2星', '3星', '4星', '5星'], 
               loc='lower right', framealpha=0.95, fontsize=10)
    plt.xlim(0, 100)
    plt.grid(True, alpha=0.3, axis='x', linestyle='--')
    
    # 反转Y轴，让最新的月份在上面
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每月评分比例堆叠图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"堆叠图已保存到：{output_file}")
    plt.close()
    
    # 方案3：分面图（每个评分一个子图）
    fig, axes = plt.subplots(1, 5, figsize=(16, 4), sharey=True)
    fig.suptitle('每月各评分分布对比', fontsize=14, fontweight='bold', y=1.02)
    
    rating_names = ['1星', '2星', '3星', '4星', '5星']
    
    for i, (rating, ax) in enumerate(zip([1, 2, 3, 4, 5], axes)):
        if rating in monthly_rating.columns:
            data = monthly_rating[rating]
            ax.bar(range(len(data)), data.values, color=colors[i], 
                   edgecolor='white', linewidth=1)
            ax.set_title(rating_names[i], fontsize=11, fontweight='bold')
            ax.set_xticks(range(len(data)))
            ax.set_xticklabels([str(m) for m in data.index], rotation=45, ha='right', fontsize=9)
            ax.grid(True, alpha=0.3, axis='y', linestyle='--')
            
            # 标注数值
            for j, v in enumerate(data.values):
                if v > 0:
                    ax.text(j, v + 0.5, str(v), ha='center', va='bottom', fontsize=8)
    
    axes[0].set_ylabel('评论数量', fontsize=11, fontweight='bold')
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每月评分分面对比图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"分面图已保存到：{output_file}")
    plt.close()
    
    # 方案3：选择部分日期的对比图（每周一个点）
    plt.figure(figsize=(14, 6))
    
    # 每7天选一个点
    sample_indices = list(range(0, len(daily_rating), 7))
    sample_dates = daily_rating.index[sample_indices]
    sample_data = daily_rating.loc[sample_dates]
    
    x = np.arange(len(sample_dates))
    width = 0.15
    
    for i, rating in enumerate([1, 2, 3, 4, 5]):
        if rating in sample_data.columns:
            offset = (i - 2) * width
            plt.bar(x + offset, sample_data[rating], width, 
                   label=f'{rating}星', color=colors[i], edgecolor='white', linewidth=0.5)
    
    plt.xlabel('日期（每周采样）', fontsize=12, fontweight='bold')
    plt.ylabel('评论数量', fontsize=12, fontweight='bold')
    plt.title('每周评分分布对比图', fontsize=14, fontweight='bold', pad=15)
    
    # 优化x轴标签显示
    date_labels = [d.strftime('%m-%d') for d in sample_dates]
    plt.xticks(x, date_labels, rotation=45, ha='right')
    
    plt.legend(loc='upper left', framealpha=0.9)
    plt.grid(True, alpha=0.3, axis='y', linestyle='--')
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, '每周评分对比图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"对比图已保存到：{output_file}")
    plt.close()
    
    return daily_rating, daily_rating_pct

def generate_additional_charts(df, output_dir):
    """生成额外的分析图表"""
    print("\n" + "=" * 60)
    print("生成额外分析图表")
    print("=" * 60)
    
    # 1. 评分分布饼图
    plt.figure(figsize=(8, 8))
    rating_counts = df['评分'].value_counts()
    colors_pie = ['#43AA8B', '#90BE6D', '#FCBF49', '#F77F00', '#D62828']
    
    plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%',
            colors=colors_pie, startangle=90, textprops={'fontsize': 12})
    plt.title('评分分布饼图', fontsize=14, fontweight='bold', pad=20)
    
    output_file = os.path.join(output_dir, '评分分布饼图.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"饼图已保存到：{output_file}")
    plt.close()
    
    # 2. 书籍评论数量排行
    plt.figure(figsize=(12, 6))
    book_counts = df['书名'].value_counts().head(10)
    
    plt.barh(range(len(book_counts)), book_counts.values, color='#577590')
    plt.yticks(range(len(book_counts)), book_counts.index)
    plt.xlabel('评论数量', fontsize=12)
    plt.title('书籍评论数量排行榜（Top 10）', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    
    # 在柱子上标注数值
    for i, v in enumerate(book_counts.values):
        plt.text(v + 0.3, i, str(v), va='center')
    
    output_file = os.path.join(output_dir, '书籍评论排行榜.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"排行榜已保存到：{output_file}")
    plt.close()

def save_analysis_results(df, daily_counts, daily_rating, daily_rating_pct, output_dir):
    """保存分析结果到文本文件"""
    output_file = os.path.join(output_dir, '数据分析结果.txt')
    
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.write("=" * 60 + "\n")
        f.write("书籍评论数据分析结果\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("一、每日评论走势分析\n")
        f.write("-" * 60 + "\n")
        f.write(f"统计时间范围：{daily_counts.index[0]} 至 {daily_counts.index[-1]}\n")
        f.write(f"总天数：{len(daily_counts)} 天\n")
        f.write(f"总评论数：{daily_counts.sum()} 条\n")
        f.write(f"平均每天评论数：{daily_counts.mean():.2f} 条\n")
        f.write(f"最多评论的一天：{daily_counts.idxmax()}，共 {daily_counts.max()} 条\n")
        f.write(f"最少评论的一天：{daily_counts.idxmin()}，共 {daily_counts.min()} 条\n\n")
        
        f.write("每日评论数量详情（前20天）：\n")
        for date, count in daily_counts.head(20).items():
            f.write(f"  {date}: {count} 条\n")
        
        f.write("\n二、每日评分分布分析\n")
        f.write("-" * 60 + "\n")
        f.write("各评分总体占比：\n")
        rating_total = df['评分'].value_counts().sort_index()
        for rating, count in rating_total.items():
            percentage = count / len(df) * 100
            f.write(f"  {rating}: {count} 条 ({percentage:.1f}%)\n")
        
        f.write("\n每日评分分布（前10天）：\n")
        for date in daily_rating.index[:10]:
            f.write(f"\n{date}:\n")
            for rating in [1, 2, 3, 4, 5]:
                if rating in daily_rating.columns:
                    count = daily_rating.loc[date, rating]
                    pct = daily_rating_pct.loc[date, rating]
                    f.write(f"  {rating}星: {count} 条 ({pct:.1f}%)\n")
        
        f.write("\n三、书籍评论统计\n")
        f.write("-" * 60 + "\n")
        book_counts = df['书名'].value_counts()
        f.write(f"涉及书籍总数：{len(book_counts)} 本\n\n")
        f.write("评论数量排行（Top 15）：\n")
        for i, (book, count) in enumerate(book_counts.head(15).items(), 1):
            f.write(f"  {i}. {book}: {count} 条\n")
        
        f.write("\n" + "=" * 60 + "\n")
        f.write("数据分析完成\n")
        f.write("=" * 60 + "\n")
    
    print(f"\n分析结果已保存到：{output_file}")

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
    
    # 任务点i：每日评论走势分析
    daily_counts = analyze_daily_comments(df, output_dir)
    
    # 任务点ii：每日评分分布分析
    daily_rating, daily_rating_pct = analyze_daily_rating_distribution(df, output_dir)
    
    # 生成额外的分析图表
    generate_additional_charts(df, output_dir)
    
    # 保存分析结果
    save_analysis_results(df, daily_counts, daily_rating, daily_rating_pct, output_dir)
    
    print("\n" + "=" * 60)
    print("第10题完成！")
    print("=" * 60)
    print(f"\n所有结果已保存到：{output_dir}")
    print("\n生成的文件：")
    print("  - 每周评论走势图.png")
    print("  - 每月评论统计图.png")
    print("  - 每月评分分布柱状图.png")
    print("  - 每月评分比例堆叠图.png（横向）")
    print("  - 每月评分分面对比图.png")
    print("  - 每周评分对比图.png")
    print("  - 评分分布饼图.png")
    print("  - 书籍评论排行榜.png")
    print("  - 数据分析结果.txt")

if __name__ == '__main__':
    main()
