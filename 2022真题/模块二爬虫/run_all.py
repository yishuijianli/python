# -*- coding: utf-8 -*-
"""
一键运行所有爬虫
"""

import subprocess
import sys

def run_script(script_name, description):
    """运行指定的Python脚本"""
    print("\n" + "=" * 60)
    print(f"{description}")
    print("=" * 60)
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=False, 
                              text=True)
        if result.returncode == 0:
            print(f"✓ {script_name} 运行成功")
        else:
            print(f"✗ {script_name} 运行完成")
    except Exception as e:
        print(f"✗ {script_name} 运行失败: {e}")

def main():
    print("=" * 60)
    print("开始运行所有任务")
    print("=" * 60)
    
    # 第4题：爬取豆瓣Top250书籍数据
    run_script('1-爬虫/book_spider.py', '【第4题】爬取豆瓣Top250书籍数据')
    
    # 第5题：生成评论数据
    run_script('1-爬虫/book_comment_real_data.py', '【第5题】生成书籍评论数据')
    
    # 第6题：数据清洗
    run_script('2-数据清洗/data_cleaning.py', '【第6题】数据清洗')
    
    # 第7题：去除标点符号
    run_script('2-数据清洗/remove_punctuation.py', '【第7题】去除标点符号')
    
    # 第9题：数据统计分析与可视化
    run_script('3-数据可视化/data_visualization.py', '【第9题】数据统计分析与可视化')
    
    # 第10题：数据分析与可视化（高级）
    run_script('3-数据可视化/data_analysis_advanced.py', '【第10题】数据分析与可视化（高级）')
    
    print("\n" + "=" * 60)
    print("所有任务完成！")
    print("=" * 60)
    print("\n数据保存位置：./data/")
    print("\n第4题 - 书籍数据：")
    print("  - ./data/书籍名称/书籍mingcl.txt (25本书)")
    print("  - ./data/书籍评分/书籍评分.txt")
    print("  - ./data/书籍图片/书籍图片.txt")
    print("\n第5题 - 评论数据：")
    print("  - ./data/book_comments.csv (200条评论)")
    print("  - ./data/评论作者/评论作者.txt")
    print("  - ./data/评论内容/评论内容.txt")
    print("  - ./data/评论评分/评论评分.txt")
    print("  - ./data/评论标题/评论标题.txt")
    print("  - ./data/评论日期/评论日期.txt")
    print("\n第6题 - 清洗后数据：")
    print("  - ./清洗数据结果.txt")
    print("  - ./data/cleaned_comments.csv")
    print("\n第7题 - 处理后数据：")
    print("  - ./data/数据处理结果/评论处理结果.csv")
    print("  - ./data/数据处理结果/评论处理结果.txt")
    print("\n第8题 - 文件列表：")
    print("  - ./data/数据处理结果/fileList.txt")
    print("\n第9题 - 统计分析与可视化：")
    print("  - ./data/数据分析与可视化结果/评分频次折线图.png")
    print("  - ./data/数据分析与可视化结果/词频统计图.png")
    print("  - ./data/数据分析与可视化结果/统计分析结果.txt")
    print("\n第10题 - 数据分析与可视化：")
    print("  - ./data/数据分析与可视化结果/每日评论走势图.png")
    print("  - ./data/数据分析与可视化结果/每日评分分布柱状图.png")
    print("  - ./data/数据分析与可视化结果/评分分布饼图.png")
    print("  - ./data/数据分析与可视化结果/数据分析结果.txt")
    print("\n💡 提示：所有数据都保存在 ./data/ 目录下！")

if __name__ == '__main__':
    main()
