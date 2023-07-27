import pandas as pd

def sort_csv_and_remove_columns(input_file, output_file):
    # 读取CSV文件并按照"id"列进行排序
    df = pd.read_csv(input_file)

    df = df.drop(columns=["vf_fr", "vf_fr_s"])
    #daily_paper_code,data_time

    # 将排序后的数据写入新的CSV文件
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "F:/code/prediction/数据文件(处理)/test.csv"   
    output_file = "F:/code/prediction/数据文件(处理)/test.csv" 
    sort_csv_and_remove_columns(input_file, output_file)
