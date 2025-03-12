import pandas as pd

def remove_duplicates(input_file, output_file):
    # 读取文件
    if input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    elif input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        print("不支持的文件格式")
        return
    
    # 去除完全重复的行
    df_deduplicated = df.drop_duplicates()
    
    # 保存去重后的数据到新的文件
    if output_file.endswith('.xlsx'):
        df_deduplicated.to_excel(output_file, index=False)
    elif output_file.endswith('.csv'):
        df_deduplicated.to_csv(output_file, index=False)
    else:
        print("不支持的输出文件格式")
        return
    
    print(f"去重后的文件已保存至: {output_file}")

if __name__ == "__main__":
    input_file = "tzgc.xlsx"  # 输入文件名
    output_file = "tzgc_deduplicated.xlsx"  # 输出文件名
    remove_duplicates(input_file, output_file)
    
    input_file_csv = "tzgc.csv"  # 输入 CSV 文件名
    output_file_csv = "tzgc_deduplicated.csv"  # 输出 CSV 文件名
    remove_duplicates(input_file_csv, output_file_csv)
