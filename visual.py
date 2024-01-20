import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')

df=pd.DataFrame(df)

x=df['ename']

y=df['salary']

plt.bar(x,y,label='EMPLOYEE DATA',color='red')

plt.xlabel('EMPLOYEE NAME')
plt.ylabel('EMPLOYEE SALARY')

plt.title('MICROSOFT INC')

plt.legend()

plt.show()