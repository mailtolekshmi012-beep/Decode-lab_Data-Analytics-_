
import pandas as pd
f1= pd.read_csv("C:/Users/Asus/Music/Decodelabs _Internship/Dataset for Data Analytics - Sheet1.csv")
print(f1) # Read CSV file  and print the data
print (list(f1.index)) # entire data
print (list(f1.columns))# entire coioumns 
print(f1.head(3))# print only first 3 rows
print(f1.tail())# print last files from the data


import pandas as pd
f1= pd.read_csv("C:/Users/Asus/Music/Decodelabs _Internship/Dataset for Data Analytics - Sheet1.csv")

print(f1.head()) 
print(f1.info())

#Check the Dataset Shape
print("Rows and columns:",f1.shape)

#check the count of null values
print(f1.isnull().sum())


#Handle Missing Coupon Codes

f1["CouponCode"] = f1["CouponCode"].fillna("No Coupon")
print("\nAfter filling missing values:")
print(f1["CouponCode"].isnull().sum())


# check duplicates
print("Duplicate rows:",f1.duplicated().sum())


#Convert Date Column

f1["Date"]= pd.to_datetime(f1["Date"])
print(f1["Date"].dtype)

#Check Numeric Columns
print(f1.describe())

print((f1["Quantity"]<0).sum())
print((f1["UnitPrice"]<0).sum())

#Check for Inconsistent Text
f1["PaymentMethod"]=f1["PaymentMethod"].str.strip().str.title()
print(f1["PaymentMethod"].unique())

f1["OrderStatus"] = f1["OrderStatus"].str.strip().str.title()
print(f1["OrderStatus"].unique())

f1["ReferralSource"] = f1["ReferralSource"].str.strip().str.title()
print(f1["ReferralSource"].unique())

#Final qauality check 
print("\n ==final check==")
f1.info()

print("\nmissing value:")
print(f1.isnull().sum())

print("\nduplicates:")
print(f1.duplicated().sum())

#After cleaning, save the dataset:
f1.to_csv("Cleaned_Dataset.csv", index=False)
print("cleaned dataset saved succesfully")



          




      
      

















