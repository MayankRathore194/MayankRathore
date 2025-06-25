# Create two DataFrames, df1 and df2, with a common column (e.g., 'ID').
# Perform an inner merge on this common column and display the resulting DataFrame.
#Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame.
# Right Join and Index-Based Join.
# Perform a right join using pd.merge() on a common column,
# then perform a join using df.join() based on the index. Compare the results.
# Merging with Multiple Keys.



import pandas as pd

df1=pd.DataFrame({"Name":['A1','A2','A3','A4','A5'],
                  'Subject':['Sub1','Sub2','Sub3','Sub4','Sub5'],
                  'Marks':[10,20,30,40,50],
                    'Id':[1,2,3,4,5]
                  },index=[1,2,3,1,5])
df2=pd.DataFrame({"Name":['B1','B2','B3','B4','B5'],
                  'Subject':['Sub1','Sub2','Sub3','Sub4','Sub5'],
                  'Marks':[10,20,30,40,50],
                  'Id':[1,2,3,4,6]
                  },index=[1,2,3,4,5])
print(df1)
print(df2)
#Merge
res=df1.merge(df2,on='Id',how="inner")
print("After inner merge")
print(res)

#left join
res2=df1.join(df2,on='Id',how="left",lsuffix='_left',rsuffix='_right')
print("left join")
print(res2)

#right join
res3=df1.join(df2,on='Id',how="right",lsuffix='_left',rsuffix='_right')
print("right join")
print(res3)


#index join
res4=df1.join(df2,lsuffix='_left',rsuffix='_right')
print("index join")
print(res4)


#right join using merge join
res5=df1.merge(df2,how="right",on='Id')
res6=df1.join(df2,lsuffix='_left',rsuffix='_right')
print("right join using merge join")
print(res6)
print("compare join using df.join() based on the index")
print(res5)


#Merge with multiply key
res8=df1.merge(df2,on=['Id','Marks'],how="inner")
print("Merge with multiply key")
print(res8)
