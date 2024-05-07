import csv
import json


# 提取文件中包含簇中心和剩余视点
def extract_and_save(csv_file_path, txt_file_path):
    """
    读取CSV文件中每行的后两个元素，并将它们存储到一个文本文件中。

    参数:
    csv_file_path (str): CSV文件的路径。
    txt_file_path (str): 输出文本文件的路径。
    """
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile, \
            open(txt_file_path, 'w', encoding='utf-8') as txtfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:  # 确保行里至少有两个元素
                last_two = row[-2:]  # 获取最后两个元素
                txtfile.write(','.join(last_two) + '\n')  # 写入文件，并以逗号分隔


# 提取本发明算法中心视点(字典) ECHVF
def our_extract_and_save(input_file_path, output_file_path):
    # 从txt文件读取字典
    with open(input_file_path, 'r') as file:
        clusters = json.load(file)
    with open(output_file_path, 'w') as file:
        for i in range(len(clusters)):
            i = str(i)
            for key, value in clusters[i].items():
                if key == 'points':  # 检查键是否为'points'
                    # 假设value是一个列表或元组，包含两个元素
                    x = int(value[0][0])
                    y = int(value[0][1])
                    point_str = f"{x}, {y}\n"  # 格式化字符串
                    file.write(point_str)  # 写入文件


# 本算法
def ours_extract_point(input_file_path, output_file_path):
    our_extract_and_save(input_file_path, output_file_path)


# CVF算法
def cvf_extract_point(input_file_path, output_file_path):
    extract_and_save(input_file_path, output_file_path)
