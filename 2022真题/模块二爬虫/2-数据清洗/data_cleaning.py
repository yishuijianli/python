# -*- coding: utf-8 -*-
"""
第6题：利用Pandas对书籍数据进行清洗
任务要求：
1. 检查缺失数据项
2. 对缺失"评论评分"数据项进行均值插补
3. 对缺失"评论作者"数据项的那条记录进行删除
4. 对冗余数据记录进行删除
5. 把清洗后的数据保存至本地磁盘"清洗数据结果.txt"文件中
"""

import pandas as pd
import numpy as np
import os

def load_data():
    """加载数据"""
    print("=" * 60)
    print("开始加载数据...")
    print("=" * 60)
    
    # 检查数据文件是否存在
    csv_file = './data/book_comments.csv'
    if not os.path.exists(csv_file):
        print(f"错误：找不到数据文件 {csv_file}")
        print("请先运行 python book_comment_real_data.py 生成数据")
        return None
    
    # 读取CSV数据
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
    print(f"成功加载数据，共 {len(df)} 条记录")
    print(f"数据列：{list(df.columns)}")
    
    return df

def create_dirty_data(df):
    """
    创建包含缺失值和重复数据的脏数据
    用于演示数据清洗过程
    """
    print("\n" + "=" * 60)
    print("创建测试用的脏数据...")
    print("=" * 60)
    
    # 复制数据
    dirty_df = df.copy()
    
    # 任务点1：添加缺失值
    # 随机设置5条记录的"评论评分"为缺失值
    missing_rating_indices = np.random.choice(dirty_df.index, 5, replace=False)
    dirty_df.loc[missing_rating_indices, '评分'] = np.nan
    print(f"添加了 5 条缺失的评论评分")
    
    # 随机设置3条记录的"评论作者"为缺失值
    missing_author_indices = np.random.choice(dirty_df.index, 3, replace=False)
    dirty_df.loc[missing_author_indices, '作者'] = np.nan
    print(f"添加了 3 条缺失的评论作者")
    
    # 任务点2：添加重复数据
    # 随机选择5条记录进行复制
    duplicate_indices = np.random.choice(dirty_df.index, 5, replace=False)
    duplicate_rows = dirty_df.loc[duplicate_indices].copy()
    dirty_df = pd.concat([dirty_df, duplicate_rows], ignore_index=True)
    print(f"添加了 5 条重复记录")
    
    print(f"\n脏数据总记录数：{len(dirty_df)}")
    
    return dirty_df

def check_missing_data(df):
    """
    任务点i：检查缺失数据项
    """
    print("\n" + "=" * 60)
    print("任务点i：检查缺失数据项")
    print("=" * 60)
    
    # 检查每列的缺失值数量
    missing_count = df.isnull().sum()
    print("\n各列缺失值统计：")
    for col, count in missing_count.items():
        if count > 0:
            percentage = (count / len(df)) * 100
            print(f"  {col}: {count} 条 ({percentage:.2f}%)")
        else:
            print(f"  {col}: 0 条")
    
    # 总缺失值
    total_missing = missing_count.sum()
    print(f"\n总缺失值数量：{total_missing}")
    
    # 显示包含缺失值的记录
    if total_missing > 0:
        print("\n包含缺失值的记录示例：")
        missing_rows = df[df.isnull().any(axis=1)]
        print(missing_rows.head(10))
    
    return missing_count

def fill_missing_rating(df):
    """
    任务点ii：对缺失"评论评分"数据项进行均值插补
    """
    print("\n" + "=" * 60)
    print("任务点ii：对缺失'评论评分'数据项进行均值插补")
    print("=" * 60)
    
    # 检查评分列的缺失情况
    missing_rating_count = df['评分'].isnull().sum()
    print(f"缺失的评论评分数量：{missing_rating_count}")
    
    if missing_rating_count > 0:
        # 将评分转换为数值（提取星级数字）
        # 例如："5星" -> 5
        df['评分_数值'] = df['评分'].str.extract('(\d+)').astype(float)
        
        # 计算均值（忽略缺失值）
        rating_mean = df['评分_数值'].mean()
        print(f"评分均值：{rating_mean:.2f}星")
        
        # 对缺失值进行均值插补
        # 先找出缺失的位置
        missing_mask = df['评分'].isnull()
        
        # 用均值填充（四舍五入到整数）
        fill_value = f"{int(round(rating_mean))}星"
        df.loc[missing_mask, '评分'] = fill_value
        df.loc[missing_mask, '评分_数值'] = round(rating_mean)
        
        print(f"已用均值 {fill_value} 填充 {missing_rating_count} 条缺失记录")
        
        # 删除临时列
        df = df.drop('评分_数值', axis=1)
    else:
        print("没有缺失的评论评分")
    
    return df

def remove_missing_author(df):
    """
    任务点iii：对缺失"评论作者"数据项的那条记录进行删除
    """
    print("\n" + "=" * 60)
    print("任务点iii：对缺失'评论作者'数据项的记录进行删除")
    print("=" * 60)
    
    # 检查作者列的缺失情况
    missing_author_count = df['作者'].isnull().sum()
    print(f"缺失的评论作者数量：{missing_author_count}")
    
    if missing_author_count > 0:
        # 显示要删除的记录
        print("\n要删除的记录：")
        print(df[df['作者'].isnull()])
        
        # 删除缺失作者的记录
        original_count = len(df)
        df = df.dropna(subset=['作者'])
        removed_count = original_count - len(df)
        
        print(f"\n已删除 {removed_count} 条缺失作者的记录")
        print(f"剩余记录数：{len(df)}")
    else:
        print("没有缺失的评论作者")
    
    return df

def remove_duplicates(df):
    """
    任务点iv：对冗余数据记录进行删除
    """
    print("\n" + "=" * 60)
    print("任务点iv：对冗余数据记录进行删除")
    print("=" * 60)
    
    # 检查重复记录
    original_count = len(df)
    duplicate_count = df.duplicated().sum()
    
    print(f"重复记录数量：{duplicate_count}")
    
    if duplicate_count > 0:
        # 显示重复记录示例
        print("\n重复记录示例：")
        duplicates = df[df.duplicated(keep=False)]
        print(duplicates.head(10))
        
        # 删除重复记录（保留第一条）
        df = df.drop_duplicates(keep='first')
        removed_count = original_count - len(df)
        
        print(f"\n已删除 {removed_count} 条重复记录")
        print(f"剩余记录数：{len(df)}")
    else:
        print("没有重复记录")
    
    return df

def save_cleaned_data(df, filepath='./清洗数据结果.txt'):
    """
    任务点v：把清洗后的数据保存至本地磁盘"清洗数据结果.txt"文件中
    """
    print("\n" + "=" * 60)
    print("任务点v：保存清洗后的数据")
    print("=" * 60)
    
    try:
        # 保存为TXT格式（使用制表符分隔）
        df.to_csv(filepath, sep='\t', index=False, encoding='utf-8-sig')
        print(f"数据已保存到：{filepath}")
        print(f"保存记录数：{len(df)}")
        
        # 同时保存为CSV格式（方便后续使用）
        csv_filepath = './data/cleaned_comments.csv'
        df.to_csv(csv_filepath, index=False, encoding='utf-8-sig')
        print(f"同时保存CSV格式到：{csv_filepath}")
        
    except Exception as e:
        print(f"保存文件出错：{e}")
    
    return df

def show_cleaning_summary(original_df, cleaned_df):
    """显示清洗总结"""
    print("\n" + "=" * 60)
    print("数据清洗总结")
    print("=" * 60)
    
    print(f"\n原始数据记录数：{len(original_df)}")
    print(f"清洗后记录数：{len(cleaned_df)}")
    print(f"删除记录数：{len(original_df) - len(cleaned_df)}")
    
    print("\n清洗操作：")
    print("  ✓ 检查了缺失数据项")
    print("  ✓ 对缺失的评论评分进行了均值插补")
    print("  ✓ 删除了缺失评论作者的记录")
    print("  ✓ 删除了重复记录")
    print("  ✓ 保存了清洗后的数据")
    
    print("\n清洗后数据预览：")
    print(cleaned_df.head(10))
    
    print("\n清洗后数据统计：")
    print(cleaned_df.describe(include='all'))

def main():
    """主函数"""
    print("=" * 60)
    print("第6题：利用Pandas对书籍数据进行清洗")
    print("=" * 60)
    
    # 1. 加载数据
    df = load_data()
    if df is None:
        return
    
    # 2. 创建脏数据（用于演示清洗过程）
    dirty_df = create_dirty_data(df)
    original_df = dirty_df.copy()
    
    # 3. 任务点i：检查缺失数据项
    check_missing_data(dirty_df)
    
    # 4. 任务点ii：对缺失"评论评分"数据项进行均值插补
    dirty_df = fill_missing_rating(dirty_df)
    
    # 5. 任务点iii：对缺失"评论作者"数据项的记录进行删除
    dirty_df = remove_missing_author(dirty_df)
    
    # 6. 任务点iv：对冗余数据记录进行删除
    dirty_df = remove_duplicates(dirty_df)
    
    # 7. 任务点v：保存清洗后的数据
    cleaned_df = save_cleaned_data(dirty_df)
    
    # 8. 显示清洗总结
    show_cleaning_summary(original_df, cleaned_df)
    
    print("\n" + "=" * 60)
    print("数据清洗完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()
