import pandas as pd
#import numpy as np
Dataset = pd.read_csv("Data.csv", names =["Loan_ID","Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
#print(Dataset)
#https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
#print(Dataset[Dataset.Married =='No'][['Loan_ID','Gender','Married']])
#Dataset =Dataset.assign(Loan_Status= lambda x: (x["Married"=='No']))
#Dataset =Dataset.assign(Loan_Status= lambda x:(x['Married' =='Yes'] or x['Self_Employed'] or x['LoanAmount'] >100 or x['Loan_Amount_Term'] >360))
#https://stackoverflow.com/questions/53011136/python-dataframe-assign-new-column-using-lambda-function-with-2-variables-and-if
Dataset['Loan_Status']=Dataset.apply(lambda row: 'Y' if (row.Married =='Yes' and row.Self_Employed =='Yes' or row.Education == "Graduate" and row.Property_Area =="Semiurban" and  row.CoapplicantIncome > "100")else 'N', axis=1)
Dataset.to_csv("New.csv")


Data.csv
Loan_ID,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area
LP001015,Male,Yes,0,Graduate,No,5720,0,110,360,1,Urban
LP001022,Male,Yes,1,Graduate,No,3076,1500,126,360,1,Urban
LP001031,Male,Yes,2,Graduate,No,5000,1800,208,360,1,Urban
LP001035,Male,Yes,2,Graduate,No,2340,2546,100,360,,Urban
LP001051,Male,No,0,Not Graduate,No,3276,0,78,360,1,Urban
LP001054,Male,Yes,0,Not Graduate,Yes,2165,3422,152,360,1,Urban
LP001055,Female,No,1,Not Graduate,No,2226,0,59,360,1,Semiurban
