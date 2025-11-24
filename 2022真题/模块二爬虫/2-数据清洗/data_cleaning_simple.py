# -*- coding: utf-8 -*-
"""
第6题：利用Pandas对书籍数据进行清洗
按照任务点要求完成数据清洗
"""

import pandas as pd
import numpy as np

# 加载数据
print("加载数据...")
df = pd.read_csv('./data/book_comments.csv', encoding='utf-8-sig')
print(f"原始数据：{len(df)} 条记录\n")

# 创建包含缺失值和重复数据的测试数据
print("创建测试数据（包含缺失值和重复数据）...")
# 添加缺失的评论评分
df.loc[10:14, '评分'] = np.nan
# 添加缺失的评论作者
df.loc[20:22, '作者'] = np.nan
# 添加重复数据
duplicate_rows = df.iloc[0:5].copy()
df = pd.concat([df, duplicate_rows], ignore_index=True)
print(f"测试数据：{len(df)} 条记录\n")

# 任务点i：检查缺失数据项
print("=" * 60)
print("任务点i：检查缺失数据项")
print("=" * 60)
missing_count = df.isnull().sum()
print("各列缺失值统计：")
print(missing_count)
print(f"\n总缺失值：{missing_count.sum()} 个\n")

# 任务点ii：对缺失"评论评分"数据项进行均值插补
print("=" * 60)
print("任务点ii：对缺失'评论评分'数据项进行均值插补")
print("=" * 60)
# 提取评分数值
df['评分_数值'] = df['评分'].str.extract('(\d+)').astype(float)
# 计算均值
rating_mean = df['评分_数值'].mean()
print(f"评分均值：{rating_mean:.2f}星")
# 填充缺失值
fill_value = f"{int(round(rating_mean))}星"
df['评分'].fillna(fill_value, inplace=True)
print(f"已用 {fill_value} 填充缺失的评论评分\n")
# 删除临时列
df = df.drop('评分_数值', axis=1)

# 任务点iii：对缺失"评论作者"数据项的记录进行删除
print("=" * 60)
print("任务点iii：对缺失'评论作者'数据项的记录进行删除")
print("=" * 60)
before_count = len(df)
df = df.dropna(subset=['作者'])
after_count = len(df)
print(f"删除了 {before_count - after_count} 条缺失作者的记录")
print(f"剩余记录：{after_count} 条\n")

# 任务点iv：对冗余数据记录进行删除
print("=" * 60)
print("任务点iv：对冗余数据记录进行删除")
print("=" * 60)
before_count = len(df)
df = df.drop_duplicates(keep='first')
after_count = len(df)
print(f"删除了 {before_count - after_count} 条重复记录")
print(f"剩余记录：{after_count} 条\n")

# 任务点v：保存清洗后的数据
print("=" * 60)
print("任务点v：保存清洗后的数据")
print("=" * 60)
output_file = './清洗数据结果.txt'
df.to_csv(output_file, sep='\t', index=False, encoding='utf-8-sig')
print(f"数据已保存到：{output_file}")
print(f"保存记录数：{len(df)}\n")

# 显示清洗后的数据预览
print("=" * 60)
print("清洗后数据预览")
print("=" * 60)
print(df.head(10))

print("\n数据清洗完成！")
