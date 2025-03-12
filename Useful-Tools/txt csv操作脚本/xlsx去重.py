import pandas as pd

def remove_duplicates(input_file, output_file):
    # 读取 Excel 文件
    df = pd.read_excel(input_file)
    
    # 去除完全重复的行
    df_deduplicated = df.drop_duplicates()
    
    # 保存去重后的数据到新的 Excel 文件
    df_deduplicated.to_excel(output_file, index=False)
    
    print(f"去重后的文件已保存至: {output_file}")

if __name__ == "__main__":
    input_file = "tzgc.xlsx"  # 输入文件名
    output_file = "tzgc_deduplicated.xlsx"  # 输出文件名
    remove_duplicates(input_file, output_file)
