# -*- coding: utf-8 -*-
"""
数据清洗报告生成器
生成详细的数据清洗报告
"""

import pandas as pd
import os

def generate_report():
    """生成数据清洗报告"""
    
    print("=" * 80)
    print(" " * 25 + "数据清洗报告")
    print("=" * 80)
    
    # 检查文件是否存在
    original_file = './data/book_comments.csv'
    cleaned_file = './data/cleaned_comments.csv'
    
    if not os.path.exists(original_file):
        print("错误：找不到原始数据文件")
        return
    
    if not os.path.exists(cleaned_file):
        print("错误：找不到清洗后的数据文件")
        print("请先运行：python data_cleaning.py")
        return
    
    # 读取数据
    original_df = pd.read_csv(original_file, encoding='utf-8-sig')
    cleaned_df = pd.read_csv(cleaned_file, encoding='utf-8-sig')
    
    print("\n" + "=" * 80)
    print("1. 数据概览")
    print("=" * 80)
    print(f"原始数据记录数：{len(original_df)} 条")
    print(f"清洗后记录数：{len(cleaned_df)} 条")
    print(f"删除记录数：{len(original_df) - len(cleaned_df)} 条")
    print(f"数据保留率：{len(cleaned_df)/len(original_df)*100:.2f}%")
    
    print("\n" + "=" * 80)
    print("2. 数据质量对比")
    print("=" * 80)
    
    print("\n原始数据质量：")
    print(f"  缺失值总数：{original_df.isnull().sum().sum()} 个")
    print(f"  重复记录数：{original_df.duplicated().sum()} 条")
    
    print("\n清洗后数据质量：")
    print(f"  缺失值总数：{cleaned_df.isnull().sum().sum()} 个")
    print(f"  重复记录数：{cleaned_df.duplicated().sum()} 条")
    
    print("\n" + "=" * 80)
    print("3. 各列数据质量")
    print("=" * 80)
    
    print("\n原始数据各列缺失情况：")
    for col in original_df.columns:
        missing = original_df[col].isnull().sum()
        if missing > 0:
            print(f"  {col}: {missing} 条 ({missing/len(original_df)*100:.2f}%)")
        else:
            print(f"  {col}: 0 条")
    
    print("\n清洗后数据各列缺失情况：")
    for col in cleaned_df.columns:
        missing = cleaned_df[col].isnull().sum()
        print(f"  {col}: {missing} 条")
    
    print("\n" + "=" * 80)
    print("4. 数据分布对比")
    print("=" * 80)
    
    print("\n评分分布：")
    print("原始数据：")
    print(original_df['评分'].value_counts().sort_index())
    print("\n清洗后数据：")
    print(cleaned_df['评分'].value_counts().sort_index())
    
    print("\n" + "=" * 80)
    print("5. 清洗操作总结")
    print("=" * 80)
    
    print("\n已完成的清洗操作：")
    print("  ✓ 任务点i：检查缺失数据项")
    print("  ✓ 任务点ii：对缺失'评论评分'进行均值插补")
    print("  ✓ 任务点iii：删除缺失'评论作者'的记录")
    print("  ✓ 任务点iv：删除冗余数据记录")
    print("  ✓ 任务点v：保存清洗后的数据")
    
    print("\n输出文件：")
    print("  - ./清洗数据结果.txt (制表符分隔)")
    print("  - ./data/cleaned_comments.csv (CSV格式)")
    
    print("\n" + "=" * 80)
    print("6. 清洗后数据预览")
    print("=" * 80)
    print("\n前10条记录：")
    print(cleaned_df.head(10).to_string())
    
    print("\n" + "=" * 80)
    print("7. 数据统计信息")
    print("=" * 80)
    print("\n清洗后数据统计：")
    print(cleaned_df.describe(include='all').to_string())
    
    print("\n" + "=" * 80)
    print("报告生成完成！")
    print("=" * 80)

if __name__ == '__main__':
    generate_report()
