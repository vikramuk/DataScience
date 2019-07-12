import pandas as pd
Dataset = pd.read_csv("C:\\Users\\vikram.uk\\PycharmProjects\\Test\\test_Y3wMUE5_7gLdaTN.csv", names =["Loan_ID","Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
Dataset['Loan_Status']=Dataset.apply(lambda row: 'Y' if (row.Married =='Yes' and row.Self_Employed =='Yes' or row.Education == "Graduate" and row.Property_Area =="Semiurban" and  row.CoapplicantIncome > "100")else 'N', axis=1)
Dataset.to_csv("CalculatedEligibility.csv",mode = 'w', index=False)
