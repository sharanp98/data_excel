import matplotlib.pyplot as plt 
import pandas as pd

df =   pd.read_excel('original.xlsx', 'Sheet1' ) #original_file_name,sheetname

#convert phone number to string
df['PhNo'] = df.PhNo.astype(str)    #Convert Phone numbers, if any 
df1 = df[['Name','PhNo','Year','Branch','FOI']]
df2 = df1.loc[df['FOI'] == 'AR']    #AR is the keyword to be searched
final = df2[['Name','PhNo','Year','Branch']]
#print final
final.to_csv('AR.csv')
