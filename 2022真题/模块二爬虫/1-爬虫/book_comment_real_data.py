# -*- coding: utf-8 -*-
"""
书籍评论数据生成器 - 真实风格数据
生成适合做情感分析和评论分析的真实风格评论数据
"""

import os
import csv
import random
from datetime import datetime, timedelta

def create_directories():
    """创建保存数据的目录"""
    directories = ['./data', './data/评论作者', './data/评论内容', 
                   './data/评论评分', './data/评论标题', './data/评论日期']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def generate_comments():
    """生成真实风格的书籍评论数据"""
    
    books = ['活着', '三体', '百年孤独', '人类简史', '原则', '红楼梦', '平凡的世界', 
             '围城', '白夜行', '解忧杂货店', '追风筝的人', '小王子', '1984', 
             '挪威的森林', '月亮与六便士']
    
    # 真实风格的评论内容（正面、中性、负面）
    positive_comments = [
        "这本书真的太好看了！情节跌宕起伏，让人欲罢不能。强烈推荐给大家！",
        "读完之后内心久久不能平静，作者的文笔太棒了，每个细节都描写得很到位。",
        "非常值得一读的好书，给我带来了很多思考和启发。五星好评！",
        "书的质量很好，内容更是精彩。已经推荐给身边的朋友了。",
        "看了好几遍，每次都有新的感悟。这是一本可以反复阅读的经典之作。",
        "故事情节引人入胜，人物刻画生动，是近期读过最好的一本书。",
        "文笔优美，思想深刻，读完让人受益匪浅。强烈推荐！",
        "这本书改变了我的很多想法，非常有启发性。感谢作者！",
        "内容丰富，逻辑清晰，是一本不可多得的好书。",
        "读起来很流畅，故事很吸引人，一口气就读完了。",
        "书中的观点很新颖，给了我很多新的思考角度。",
        "非常喜欢这本书，已经买了好几本送给朋友。",
        "作者的见解独到，文字功底深厚，值得细细品味。",
        "这是我今年读过最好的一本书，强烈推荐！",
        "内容充实，结构完整，是一本很有价值的书。",
        "读完这本书，感觉自己的视野开阔了很多。",
        "故事感人至深，让我流了好几次眼泪。",
        "书的装帧精美，内容更是精彩绝伦。",
        "这本书让我重新思考了人生的意义。",
        "非常棒的一本书，值得每个人都读一读。"
    ]
    
    neutral_comments = [
        "书的内容还可以，但是感觉有些地方写得不够深入。",
        "整体来说还不错，就是节奏有点慢，需要耐心读下去。",
        "书的质量挺好的，内容中规中矩，适合打发时间。",
        "有些观点比较有意思，但整体感觉一般般。",
        "书是正版的，印刷质量不错，内容见仁见智吧。",
        "读了一半，感觉还行，但没有想象中那么精彩。",
        "书的内容比较平淡，但也有一些可取之处。",
        "整体还可以，就是有些地方感觉有点啰嗦。",
        "书的装帧不错，内容还在慢慢品读中。",
        "还没读完，目前感觉一般，继续看看吧。"
    ]
    
    negative_comments = [
        "书的内容和介绍差距太大，有点失望。",
        "读了几页就读不下去了，内容太枯燥了。",
        "感觉被过度吹捧了，实际内容很一般。",
        "翻译得不太好，读起来很别扭。",
        "内容空洞，没什么实质性的东西。",
        "书的质量一般，而且有些错别字。",
        "期望太高，结果有点失望。",
        "故事情节太拖沓，看得很累。",
        "内容比较老套，没什么新意。",
        "不太适合我，可能是个人口味问题吧。"
    ]
    
    authors = [
        "读书爱好者", "小明", "书虫一枚", "文学青年", "张三", "李四",
        "爱读书的猫", "静静", "阳光少年", "梦想家", "思考者", "王五",
        "书香门第", "文艺范", "知识分子", "学生党", "上班族", "退休老人",
        "全职妈妈", "大学生", "研究生", "教师", "工程师", "设计师",
        "程序员", "医生", "律师", "记者", "编辑", "作家"
    ]
    
    titles = [
        "非常好看", "强烈推荐", "值得一读", "不错的书", "还可以",
        "有点失望", "一般般", "很喜欢", "太棒了", "不推荐",
        "经典之作", "必读好书", "感人至深", "引人深思", "平淡无奇",
        "超出预期", "符合预期", "低于预期", "惊喜之作", "浪费时间"
    ]
    
    all_comments = []
    
    # 生成200条评论
    for i in range(200):
        # 70%正面，20%中性，10%负面
        rand = random.random()
        if rand < 0.7:
            content = random.choice(positive_comments)
            rating = random.choice(["5星", "5星", "5星", "4星"])
            title = random.choice(titles[:10])
        elif rand < 0.9:
            content = random.choice(neutral_comments)
            rating = random.choice(["3星", "4星"])
            title = random.choice(titles[10:15])
        else:
            content = random.choice(negative_comments)
            rating = random.choice(["1星", "2星", "3星"])
            title = random.choice(titles[15:])
        
        # 随机日期（最近一年内）
        days_ago = random.randint(0, 365)
        date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        comment = {
            '书名': random.choice(books),
            '作者': random.choice(authors),
            '标题': title,
            '内容': content,
            '评分': rating,
            '日期': date
        }
        
        all_comments.append(comment)
    
    return all_comments

def save_to_csv(comments, filepath):
    """保存为CSV格式"""
    try:
        with open(filepath, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['书名', '作者', '标题', '内容', '评分', '日期'])
            writer.writeheader()
            writer.writerows(comments)
        print(f"CSV数据已保存到: {filepath}")
    except Exception as e:
        print(f"保存CSV出错: {e}")

def save_to_txt(comments):
    """保存为TXT格式（分类保存）"""
    try:
        authors = [c['作者'] for c in comments]
        contents = [c['内容'] for c in comments]
        ratings = [c['评分'] for c in comments]
        titles = [c['标题'] for c in comments]
        dates = [c['日期'] for c in comments]
        
        with open('./data/评论作者/评论作者.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(authors))
        
        with open('./data/评论内容/评论内容.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(contents))
        
        with open('./data/评论评分/评论评分.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(ratings))
        
        with open('./data/评论标题/评论标题.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(titles))
        
        with open('./data/评论日期/评论日期.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(dates))
        
        print("TXT文件保存完成")
        
    except Exception as e:
        print(f"保存TXT出错: {e}")

def main():
    print("=" * 60)
    print("生成书籍评论数据（适合评论分析）")
    print("=" * 60)
    
    create_directories()
    
    print("\n正在生成评论数据...")
    comments = generate_comments()
    
    print(f"共生成 {len(comments)} 条评论")
    
    # 显示统计信息
    rating_count = {}
    for comment in comments:
        rating = comment['评分']
        rating_count[rating] = rating_count.get(rating, 0) + 1
    
    print("\n评分分布：")
    for rating in sorted(rating_count.keys()):
        print(f"  {rating}: {rating_count[rating]} 条")
    
    # 保存数据
    print("\n正在保存数据...")
    save_to_csv(comments, './data/book_comments.csv')
    save_to_txt(comments)
    
    print("\n" + "=" * 60)
    print("数据生成完成！")
    print("=" * 60)
    print("\n数据文件：")
    print("  - ./data/book_comments.csv (CSV格式，推荐用于分析)")
    print("  - ./data/评论作者/评论作者.txt")
    print("  - ./data/评论内容/评论内容.txt")
    print("  - ./data/评论评分/评论评分.txt")
    print("  - ./data/评论标题/评论标题.txt")
    print("  - ./data/评论日期/评论日期.txt")
    print("\n这些数据可以用于：")
    print("  - 情感分析")
    print("  - 评分预测")
    print("  - 词云生成")
    print("  - 用户行为分析")

if __name__ == '__main__':
    main()
