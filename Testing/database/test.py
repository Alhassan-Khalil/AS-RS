
import numpy as np
import pandas as pd


## Storge [A1 , A2 ,A3]
##        [B1 , B2 ,B3]
##
# storge = np.array([[1,0,3],[0,2,0]])
#
# print(storge)
#
#
# A1 = [storge[0,0] , (50 , 25)]
# A2 = storge[0,1]
# A3 = storge[0,2]
# B1 = storge[1,0]
# B2 = storge[1,1]
# B3 = storge[1,2]
#
# list = [A1, A2 , A3 ,B1 ,B2 ,B3]
#
#
#
# print(list[0][1])

#create 2D numpy array with zeros
S = np.zeros((8, 4), int)

#print numpy array
print(S)
A1 = S[0,0]
A2 = S[0,1]
A3 = S[0,2]
B1 = S[1,0]
B2 = S[1,1]
B3 = S[1,2]
list = [A1, A2 , A3 ,B1 ,B2 ,B3]


print(A1)

for i in range(0,8):
    for j in range(0,4):

        if S[i,j] == 0:
            S[i,j] = 1
            print(S[i,j])
            print(S)

print(S)

# open a binary file in write mode
file = open("Storge", "wb")
# save array to the file
np.save(file, S)
# close the file
file.close

print("the old array")

file = open("Storge", "rb")
#read the file to numpy array
arr1 = np.load(file)
#close the file
print(arr1)


## convert your array into a dataframe
df = pd.DataFrame (S)

## save to xlsx file

filepath = 'my_excel_file.xlsx'

df.to_excel(filepath, index=False)
