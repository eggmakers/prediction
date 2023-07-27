import pandas as pd
from sklearn.model_selection import train_test_split

def split_train_test_data(input_file, train_file, test_file, test_size=0.2, random_state=None):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 去掉包含0的行
    df = df.loc[(df != 0).all(axis=1)]

    # 划分训练集和测试集
    train_data, test_data = train_test_split(df, test_size=test_size, random_state=random_state)

    # 将训练集和测试集写入CSV文件
    train_data.to_csv(train_file, index=False)
    test_data.to_csv(test_file, index=False)

if __name__ == "__main__":
    input_file = "F:/code/prediction/数据文件(处理)/daily_paper.csv"  #F:/code/prediction/数据文件(处理)/daily_paper.csv   
    train_file = "F:/code/prediction/数据文件(处理)/train.csv"     
    test_file = "F:/code/prediction/数据文件(处理)/test.csv"       
    test_size = 0.2             
    random_state = 42           # 设置随机种子

    split_train_test_data(input_file, train_file, test_file, test_size, random_state)
