import numpy as np
import pandas as pd

# 读取 .npy 文件
npy_file_path = 'generateddatafromctgan.csv.npy'  # 替换为您的 .npy 文件路径
data = np.load(npy_file_path)

# 将数据转换为 DataFrame
df = pd.DataFrame(data)

# 保存为 .csv 文件
csv_file_path = 'generateddatafromctgan.csv'  # 替换为您希望保存的 .csv 文件路径
df.to_csv(csv_file_path, index=False)
