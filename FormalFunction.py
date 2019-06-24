# Import pandas package  
import pandas as pd 
  
# Function to add 
def LoanEligibility(a, b, c, d): 
    return "Y" if(a =='Yes' and b == 'Yes' or c ==  'Graduate' and d == 'SemiUrban') else "N"
  
def main():	  
	# Convert the dictionary into DataFrame  
	df = pd.read_csv("C:\\Users\\vikram.uk\\PycharmProjects\\untitled\\test_Y3wMUE5_7gLdaTN.csv", names =["Loan_ID","Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"], header=1) 
	print("Original DataFrame:\n", df) 	  
	df['Loan_Status'] = df.apply(lambda row : LoanEligibility(row['Loan_ID'], 
					 row['Self_Employed'], row['Education'], row['Property_Area']), axis = 1) 
	print('\nAfter Applying Function: ', df) 
	# printing the new dataframe 
	df.to_csv("CalculatedEligibility.csv",mode = 'w', index=False) 
   
if __name__ == '__main__': 
    main() 
    
  '''  
Loan_ID,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area
LP001015,Male,Yes,0,Graduate,No,5720,0,110,360,1,Urban
LP001022,Male,Yes,1,Graduate,No,3076,1500,126,360,1,Urban
LP001031,Male,Yes,2,Graduate,No,5000,1800,208,360,1,Urban
LP001035,Male,Yes,2,Graduate,No,2340,2546,100,360,,Urban
LP001051,Male,No,0,Not Graduate,No,3276,0,78,360,1,Urban
LP001054,Male,Yes,0,Not Graduate,Yes,2165,3422,152,360,1,Urban
LP001055,Female,No,1,Not Graduate,No,2226,0,59,360,1,Semiurban
LP001056,Male,Yes,2,Not Graduate,No,3881,0,147,360,0,Rural
LP001059,Male,Yes,2,Graduate,,13633,0,280,240,1,Urban
LP001067,Male,No,0,Not Graduate,No,2400,2400,123,360,1,Semiurban
LP001078,Male,No,0,Not Graduate,No,3091,0,90,360,1,Urban
LP001082,Male,Yes,1,Graduate,,2185,1516,162,360,1,Semiurban
LP001083,Male,No,3+,Graduate,No,4166,0,40,180,,Urban
LP001094,Male,Yes,2,Graduate,,12173,0,166,360,0,Semiurban
LP001096,Female,No,0,Graduate,No,4666,0,124,360,1,Semiurban
LP001099,Male,No,1,Graduate,No,5667,0,131,360,1,Urban
LP001105,Male,Yes,2,Graduate,No,4583,2916,200,360,1,Urban
LP001107,Male,Yes,3+,Graduate,No,3786,333,126,360,1,Semiurban
LP001108,Male,Yes,0,Graduate,No,9226,7916,300,360,1,Urban
LP001115,Male,No,0,Graduate,No,1300,3470,100,180,1,Semiurban
LP001121,Male,Yes,1,Not Graduate,No,1888,1620,48,360,1,Urban
LP001124,Female,No,3+,Not Graduate,No,2083,0,28,180,1,Urban
LP001128,,No,0,Graduate,No,3909,0,101,360,1,Urban
LP001135,Female,No,0,Not Graduate,No,3765,0,125,360,1,Urban
LP001149,Male,Yes,0,Graduate,No,5400,4380,290,360,1,Urban
'''
