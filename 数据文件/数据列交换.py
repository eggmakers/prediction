import pandas as pd

def swap_columns(csv_file, column1, column2):
    # 读取CSV文件为DataFrame
    df = pd.read_csv(csv_file)

    # 交换列的顺序
    cols = df.columns.tolist()
    idx1 = cols.index(column1)
    idx2 = cols.index(column2)
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]
    df = df[cols]

    # 将结果保存回CSV文件
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    csv_file_path = "F:/code/prediction/数据文件(处理)/daily_paper.csv"
    column1 = "vf_fr_s"
    column2 = "vf_su_s"
    swap_columns(csv_file_path, column1, column2)
