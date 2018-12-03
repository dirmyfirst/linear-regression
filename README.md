# linear-regression
简单的线性回归学习  
将每次的机器学习记录上传，记录学习过程  

import pandas as pd

#读取数据
path = r'test.xlsx'
df = pd.read_excel(path)
print(df)

#确定自变量为x和因变量为y
x = df[['活动推广费']]
y = df[['销售额']]

#导入线性回归模型
from sklearn.linear_model import LinearRegression

linreg = LinearRegression() #建立模型  
linreg.fit(x,y)   #训练模型  
print(linreg.score(x,y))  #模型评估  
print(linreg.predict([[60]]))   #模型预测，导入60成活动推广费用，预测可以达到多少销售额  

print(linreg.intercept_[0]) #查看截距  
print(linreg.coef_[0][0]) #查看参数  
print(linreg.intercept_[0] + linreg.coef_[0][0] * 60)  
