# -*- coding: utf-8 -*-
"""
第8题：编写Python程序，查找目录下的指定文件格式
任务要求：查找指定路径下所有的word、pdf、txt格式文件
"""

import os

def find_files_by_extension(start_path, extensions):
    """
    任务点i：查找指定路径下的所有指定格式文件
    
    参数：
        start_path: 开始搜索的路径
        extensions: 文件扩展名列表，例如 ['.docx', '.pdf', '.txt']
    
    返回：
        找到的文件路径列表
    """
    found_files = []
    
    print(f"开始搜索路径：{start_path}")
    print(f"搜索文件类型：{', '.join(extensions)}")
    print("=" * 60)
    
    # 遍历目录及其子目录
    try:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                # 获取文件扩展名
                file_ext = os.path.splitext(file)[1].lower()
                
                # 检查是否是目标格式
                if file_ext in extensions:
                    # 获取完整路径
                    full_path = os.path.join(root, file)
                    found_files.append(full_path)
                    print(f"找到文件：{full_path}")
        
    except Exception as e:
        print(f"搜索出错：{e}")
    
    return found_files

def save_file_list(file_list, output_file):
    """
    保存文件列表到指定文件
    
    参数：
        file_list: 文件路径列表
        output_file: 输出文件路径
    """
    try:
        # 确保输出目录存在
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"\n创建目录：{output_dir}")
        
        # 保存文件列表
        with open(output_file, 'w', encoding='utf-8-sig') as f:
            f.write(f"文件搜索结果\n")
            f.write(f"=" * 60 + "\n")
            f.write(f"共找到 {len(file_list)} 个文件\n")
            f.write(f"=" * 60 + "\n\n")
            
            for i, file_path in enumerate(file_list, 1):
                f.write(f"{i}. {file_path}\n")
        
        print(f"\n文件列表已保存到：{output_file}")
        
    except Exception as e:
        print(f"保存文件列表出错：{e}")

def main():
    """主函数"""
    print("=" * 60)
    print("第8题：查找目录下的指定文件格式")
    print("=" * 60)
    
    # 任务点i：用户输入搜索路径
    print("\n请输入开始搜索的路径：")
    print("（直接按回车使用当前目录）")
    start_path = input("路径：").strip()
    
    # 如果用户没有输入，使用当前目录
    if not start_path:
        start_path = '.'
        print(f"使用当前目录：{os.path.abspath(start_path)}")
    
    # 检查路径是否存在
    if not os.path.exists(start_path):
        print(f"错误：路径不存在 - {start_path}")
        return
    
    # 定义要搜索的文件扩展名
    # Word文件：.doc, .docx
    # PDF文件：.pdf
    # 文本文件：.txt
    extensions = ['.doc', '.docx', '.pdf', '.txt']
    
    print("\n" + "=" * 60)
    print("开始搜索...")
    print("=" * 60 + "\n")
    
    # 查找文件
    found_files = find_files_by_extension(start_path, extensions)
    
    # 显示统计信息
    print("\n" + "=" * 60)
    print("搜索完成")
    print("=" * 60)
    print(f"共找到 {len(found_files)} 个文件")
    
    # 按文件类型统计
    file_types = {}
    for file_path in found_files:
        ext = os.path.splitext(file_path)[1].lower()
        file_types[ext] = file_types.get(ext, 0) + 1
    
    print("\n文件类型统计：")
    for ext, count in sorted(file_types.items()):
        print(f"  {ext}: {count} 个")
    
    # 任务点ii：保存文件列表
    if found_files:
        # 保存到当前目录的data/数据处理结果文件夹
        output_file = './data/数据处理结果/fileList.txt'
        save_file_list(found_files, output_file)
    else:
        print("\n未找到任何文件")
    
    print("\n" + "=" * 60)
    print("程序执行完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()
