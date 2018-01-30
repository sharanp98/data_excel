import matplotlib.pyplot as plt 
import pandas as pd

df =   pd.read_excel('sample_file.xlsx', 'Sheet 1' )

plt.plot(df['Year'], df['DS'] , color = 'r')
plt.plot(df['Year'], df['DCS'], color = 'k')
plt.plot(df['Year'], df['LS'] , color = 'c')

plt.xlabel('Year')
plt.ylabel('Total Score')
plt.title('DATA \n')
plt.legend()

plt.show()

print (df.head())
