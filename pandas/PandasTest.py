# pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple

# pip install pandas xlrd openpyxl xlsxwriter requests lxml html5lib BeautifulSoup4 matplotlib seaborn plotly bokeh scipy statsmodels -i https://pypi.tuna.tsinghua.edu.cn/simple


import pandas as pd
print(pd.__version__)

df = pd.read_excel("E:/PythonWorkspaces/curtis-python/file/team.xlsx")
print(df)