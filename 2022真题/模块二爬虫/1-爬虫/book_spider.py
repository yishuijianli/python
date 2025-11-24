# -*- coding: utf-8 -*-
"""
书籍爬虫程序
功能：爬取热门书籍的名称、评分、图片链接
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import random

# 任务点1：设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'https://www.douban.com/'
}

# 目标网站URL - 豆瓣Top250
url = 'https://book.douban.com/top250'

def create_directories():
    """创建保存数据的目录"""
    directories = [
        './data/书籍名称',
        './data/书籍图片',
        './data/书籍评分'
    ]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"创建目录: {directory}")

def get_book_data(url):
    """
    任务点2：发送HTTP请求获取网页内容
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
    except Exception as e:
        print(f"请求出错: {e}")
        return None

def parse_book_info(html):
    """
    任务点3：解析HTML，提取书籍信息
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    books_name = []
    books_rating = []
    books_image = []
    
    # 任务点4：查找书籍信息元素
    # 豆瓣Top250使用tr.item结构
    book_items = soup.find_all('tr', class_='item')
    
    for item in book_items:  # 爬取所有找到的书籍
        try:
            # 提取书籍名称
            title_div = item.find('div', class_='pl2')
            if title_div:
                title_link = title_div.find('a')
                if title_link:
                    title = title_link.get('title', '').strip()
                    if not title:
                        title = title_link.get_text().strip()
                    books_name.append(title)
                else:
                    continue
            else:
                continue
            
            # 提取书籍评分
            rating_element = item.find('span', class_='rating_nums')
            if rating_element:
                rating = rating_element.get_text().strip()
            else:
                rating = "暂无评分"
            books_rating.append(rating)
            
            # 提取书籍图片链接
            img_element = item.find('img')
            if img_element and img_element.get('src'):
                img_url = img_element.get('src')
            else:
                img_url = "无图片"
            books_image.append(img_url)
            
        except Exception as e:
            print(f"解析书籍信息出错: {e}")
            continue
    
    return books_name, books_rating, books_image

def save_to_file(data, filepath):
    """
    任务点5：保存数据到文件
    """
    try:
        with open(filepath, 'w', encoding='utf-8-sig') as f:
            for item in data:
                f.write(item + '\n')
        print(f"数据已保存到: {filepath}")
    except Exception as e:
        print(f"保存文件出错: {e}")

def main():
    """主函数"""
    print("=" * 50)
    print("开始爬取书籍数据...")
    print("=" * 50)
    
    # 创建保存目录
    create_directories()
    
    # 获取网页内容
    html = get_book_data(url)
    
    if html:
        # 解析书籍信息
        books_name, books_rating, books_image = parse_book_info(html)
        
        if books_name:
            print(f"\n成功爬取 {len(books_name)} 本书籍信息")
            
            # 任务点6：保存数据到指定路径
            save_to_file(books_name, './data/书籍名称/书籍mingcl.txt')
            save_to_file(books_rating, './data/书籍评分/书籍评分.txt')
            save_to_file(books_image, './data/书籍图片/书籍图片.txt')
            
            print("\n" + "=" * 50)
            print("爬取完成！")
            print("=" * 50)
        else:
            print("未能提取到书籍信息，可能网站结构已变化")
    else:
        print("无法获取网页内容")

if __name__ == '__main__':
    main()
