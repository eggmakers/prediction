import csv

def sort_csv_and_add_ids(input_file, output_file):
    # 读取CSV文件并按照"id"列进行排序
    with open(input_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)
        sorted_rows = sorted(csv_reader, key=lambda x: int(x["id"]))

    # 为排序后的数据添加新的"id"序号
    for idx, row in enumerate(sorted_rows, start=1):
        row["id"] = str(idx)

    # 将排序后的数据写入新的CSV文件
    with open(output_file, 'w', newline='') as csv_output:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(sorted_rows)

if __name__ == "__main__":
    input_file = "F:/code/预测模型/数据文件(处理)/daily_paper.csv"   # 替换为你的输入文件路径
    output_file = "F:/code/预测模型/数据文件(处理)/daily_paper.csv" # 替换为你的输出文件路径
    sort_csv_and_add_ids(input_file, output_file)
