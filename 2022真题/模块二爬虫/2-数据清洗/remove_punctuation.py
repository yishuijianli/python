# -*- coding: utf-8 -*-
"""
第7题：编写Python程序对书籍评论数据进行处理
任务要求：去除书籍评论中所有的标点符号
"""

import pandas as pd
import re
import os

def remove_punctuation_from_text(text):
    """
    任务点i：去除文本中的标点符号"，"和"、"
    同时去除其他常见标点符号
    """
    # 定义要去除的标点符号
    punctuation = '，。！？；：""''（）【】《》、·…—'
    
    # 去除标点符号
    for p in punctuation:
        text = text.replace(p, '')
    
    # 也可以使用正则表达式去除所有中文标点
    # text = re.sub(r'[，。！？；：""''（）【】《》、·…—]', '', text)
    
    return text

def process_comments():
    """处理评论数据，去除标点符号"""
    print("=" * 60)
    print("第7题：去除书籍评论中的标点符号")
    print("=" * 60)
    
    # 读取数据
    input_file = './data/book_comments.csv'
    if not os.path.exists(input_file):
        print(f"错误：找不到数据文件 {input_file}")
        print("请先运行 python book_comment_real_data.py 生成数据")
        return
    
    print(f"\n正在读取数据：{input_file}")
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print(f"读取了 {len(df)} 条记录")
    
    # 显示处理前的数据示例
    print("\n处理前的评论示例：")
    for i in range(min(3, len(df))):
        print(f"{i+1}. {df.loc[i, '内容']}")
    
    # 任务点i：去除评论内容中的标点符号
    print("\n正在去除标点符号...")
    df['内容_处理后'] = df['内容'].apply(remove_punctuation_from_text)
    
    # 显示处理后的数据示例
    print("\n处理后的评论示例：")
    for i in range(min(3, len(df))):
        print(f"{i+1}. {df.loc[i, '内容_处理后']}")
    
    # 任务点ii：保存处理后的数据
    output_dir = './data/数据处理结果'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n创建目录：{output_dir}")
    
    # 保存为CSV格式
    output_file_csv = os.path.join(output_dir, '评论处理结果.csv')
    df.to_csv(output_file_csv, index=False, encoding='utf-8-sig')
    print(f"\n数据已保存到：{output_file_csv}")
    
    # 保存为TXT格式（只保存处理后的内容）
    output_file_txt = os.path.join(output_dir, '评论处理结果.txt')
    with open(output_file_txt, 'w', encoding='utf-8-sig') as f:
        for content in df['内容_处理后']:
            f.write(content + '\n')
    print(f"数据已保存到：{output_file_txt}")
    
    # 统计信息
    print("\n" + "=" * 60)
    print("处理统计")
    print("=" * 60)
    print(f"处理记录数：{len(df)}")
    
    # 统计去除的标点符号数量
    total_removed = 0
    for i in range(len(df)):
        original_len = len(df.loc[i, '内容'])
        processed_len = len(df.loc[i, '内容_处理后'])
        total_removed += (original_len - processed_len)
    
    print(f"去除标点符号总数：{total_removed} 个")
    print(f"平均每条评论去除：{total_removed/len(df):.1f} 个标点符号")
    
    print("\n" + "=" * 60)
    print("处理完成！")
    print("=" * 60)

def main():
    """主函数"""
    process_comments()

if __name__ == '__main__':
    main()
