import pandas as pd

df = pd.read_excel('D:/迅雷下载/联系人.xls', header=None)
df.to_excel('D:/迅雷下载/联系人.xlsx', index=False, header=False)
