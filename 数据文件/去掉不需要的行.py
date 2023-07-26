import pandas as pd

def sort_csv_and_remove_rows_with_zero(input_file, output_file):
    # 读取CSV文件并按照"id"列进行排序
    df = pd.read_csv(input_file)
    df = df.sort_values(by='id')

    # 去掉包含0的行
    df = df.loc[(df != 0).all(axis=1)]

    # 将排序后的数据写入新的CSV文件
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "F:/code/预测模型/数据文件(处理)/daily_paper.csv"   # 替换为你的输入文件路径
    output_file = "F:/code/预测模型/数据文件(处理)/daily_paper.csv" # 替换为你的输出文件路径
    sort_csv_and_remove_rows_with_zero(input_file, output_file)
