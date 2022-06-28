# Q1: Consider the dataframe df. How would you find the element in the second row and first column?
# df.ix[1,0] or df.iloc[1,0]

# Q2: Will the following code run?
import pandas as banana
df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})
print(df.head())
# Yes

# Q3: Consider the dataframe: 
import pandas as pd
df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# What type does the following return: df['a']==1 ?
print(df['a']==1)
# bool

# Q4: What task does the following method perform: df.to_csv("file.csv")?
# Save a dataframe to a csv file.

# Q5: What do the following lines of code do?
with open("Example1.txt","r") as file1:
    FileContent=file1.readlines()
    print(FileContent)
# Read the file "Example1.txt".

# Q6: What do the following lines of code do?
with open("Example2.txt","w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
# Write to the file "Example2.txt".

# Q7: What do the following lines of code do?
with open("Example3.txt","a") as file1:
    file1.write("This is line C\n")
# Append the file "Example3.txt".

# Q8: What is the result of applying the following method df.head() to the dataframe "df"?
# Prints the first 5 rows of the dataframe.

