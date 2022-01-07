from typing import final
from addressNormalize import addNormalizer
from utils import expander, preProcessAddress
import json

with open('./address.txt') as file:
    # print(addNormalizer(preProcessAddress('aakruthi nilaya ashwathnarayana layout 7th cross 3rd floor puttenhalli j p nagar 7th phase near jain public school bengaluru 560-062')))
    finalAddresses= []
    for line in file:
        # addNormalizer(preProcessAddress(line.rstrip()))
        print("Input : \n")
        add = line.rstrip()
        finalAddresses.append(addNormalizer(preProcessAddress(add)))
        print("\n\n\n")

#     for i in range(5):
#         add = next(file).rstrip()
#         finalAddresses.append(addNormalizer(preProcessAddress(add)))
    finalJSON = json.dump({"addresses": finalAddresses})
    # print(finalAddresses)
    finalJSON = {"addresses": finalAddresses}
    # print(finalJSON)


with open("outputFile.json", "w") as outfile:
    # outfile.write(finalJSON, outfile)
    json.dump(finalJSON, outfile)
        
#-------TESTING--------------------------------------------------------------------------
# import random

# lines = open('address.txt').read().splitlines()

# for i in range(200) : 
#     myline =random.choice(lines)
#     print(addNormalizer(preProcessAddress(myline)))

#--------------------------------------------------------------------------------------

# print(addNormalizer(preProcessAddress('M02739 ali nagar ghaziabanda ek minar k masjid Hyderabad Telangana India 500023')))