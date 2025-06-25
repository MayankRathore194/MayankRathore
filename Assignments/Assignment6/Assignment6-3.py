# Create three DataFrames. Vertically concatenate two of them using pd.concat(),
# then merge the resulting DataFrame with the third DataFrame on a common key.
# Understand join() vs. merge().


import pandas as pd
student={'Id':['1','2','3','4'],
         'sub':['maths','English','Hindi','Science'],
         'class':[11,12,11,13]}
a=pd.DataFrame(student)
teacher={'Id':['1','2','3','4'],
         'salary':[20000,10000,100000,30000],
         'class':['11','12','11','13'],}
b=pd.DataFrame(teacher)
non_teaching= {'Id': ['11', '12', '13', '14'],
         'salary': [2000, 1000, 10000, 3000],
         'block': ['A1','A2','A3','A4']}
c=pd.DataFrame(non_teaching)
k=pd.concat([a,b])
print(""" 
after cocatenation 

      """,k)
res=pd.merge(k,c,on='Id',how='outer')
print(""" 
after merge  

""",res)