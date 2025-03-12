import pandas as pd

# 读取数据集（假设数据存储在 'intrusion_data.csv'）
df = pd.read_csv('NSL-KDD-train.csv')

# 确保 class 列存在
if 'class' not in df.columns:
    raise ValueError("The dataset does not contain a 'class' column.")

# 合并除 class 以外的所有列
df['flow'] = df.drop(columns=['class']).astype(str).apply(lambda row: ','.join(row), axis=1)

# 只保留 merged_features 和 class 列
df = df[['flow', 'class']]

# 保存处理后的数据
df.to_csv('train.csv', index=False)
