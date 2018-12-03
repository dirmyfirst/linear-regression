import pandas as pd


path = r'test.xlsx'
df = pd.read_excel(path)
print(df)

x = df[['活动推广费']]

y = df[['销售额']]

from sklearn.linear_model import LinearRegression

linreg = LinearRegression() #建立模型
linreg.fit(x,y)   #训练模型
print(linreg.score(x,y))  #模型评估
print(linreg.predict([[60]]))   #模型预测


print(linreg.intercept_[0]) #查看截距
print(linreg.coef_[0][0]) ##查看参数
print(linreg.intercept_[0] + linreg.coef_[0][0] * 60)
