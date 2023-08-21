import pandas as pd
path = r'D:\Regression Models\HousingLoan\Data'
train_data = pd.read_csv(path+"\\train.csv")
print('Features : ',[val for val in train_data.columns])

categorical_variabes,numerical_variables,boolean_variables = [], [], []
for col in train_data.columns:
    if train_data[col].dtypes == 'object':
        categorical_variabes.append(col)
    elif train_data[col].dtypes in ['int64','int32','float64','float32']:
        numerical_variables.append(col)
    else:
        boolean_variables.append(col)
        
'''Check Null Values'''
train_data.isnull().sum()








    