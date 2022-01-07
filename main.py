from typing import final
from addressNormalize import addNormalizer
from utils import expander, preProcessAddress
import json

with open('./address.txt') as file:
    # print(addNormalizer(preProcessAddress('aakruthi nilaya ashwathnarayana layout 7th cross 3rd floor puttenhalli j p nagar 7th phase near jain public school bengaluru 560-062')))
    finalAddresses= []
    for i, line in enumerate(file):
        # addNormalizer(preProcessAddress(line.rstrip()))
        if(i in range(1000, 2000)):
            # print("Input : \n")
            add = line.rstrip()
            finalAddresses.append(addNormalizer(preProcessAddress(add)))
            print("DONE: " + str(i))
            print("\n\n\n")

    finalJSON = {"addresses": finalAddresses}


with open("outputFile.json", "w") as outfile:
    # outfile.write(finalJSON, outfile)
    json.dump(finalJSON, outfile)
        
#-------TESTING--------------------------------------------------------------------------
# import random

# lines = open('address.txt').read().splitlines()
# finalAddresses= []

# for i in range(20) :     
#     myline =random.choice(lines)
#     finalAddresses.append(addNormalizer(preProcessAddress(myline)))
#     print(i)
# finalJSON = {"addresses": finalAddresses}
# print(finalJSON)
# with open("outputFile.json", "w") as outfile:
#     # outfile.write(finalJSON, outfile)
#     json.dump(finalJSON, outfile)

#--------------------------------------------------------------------------------------

# print(addNormalizer(preProcessAddress('C-T-90910 SILVER CROWN silver crown , silver county road Cambridge international Bangalore Karnataka India 560068')))
# print(addNormalizer(preProcessAddress('a31230 ramban lane college of military engineering dapori near regimental school pune maharashtra 411031')))
# print(addNormalizer(preProcessAddress('A T-90375 Brigade Omega , Uttarahalli 80 feet road , Banashankari 6th stage , Subramanyapura KSIT college , Kanakapura Road banglore Karnataka India 560062')))
