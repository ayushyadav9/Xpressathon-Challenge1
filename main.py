from addressNormalize import addNormalizer
from utils import preProcessAddress
import json

#-------MAIN CODE-------------------------#

with open('./address.txt') as file:
    finalAddresses= []
    for i, line in enumerate(file):
        if(i in range(0, 5000)):
            add = line.rstrip()
            finalAddresses.append(addNormalizer(preProcessAddress(add)))
            print("DONE: " + str(i))

    finalJSON = {"addresses": finalAddresses}


with open("outputFile.json", "w") as outfile:
    json.dump(finalJSON, outfile)
        
#-------TESTING-------------------------#
# import random

# lines = open('address.txt').read().splitlines()
# finalAddresses= []

# for i in range(20) :     
#     myline =random.choice(lines)
#     parsedAddress = addNormalizer(preProcessAddress(myline))
#     finalAddresses.append(parsedAddress)
#     print("-----------INPUT---------------")
#     print(myline)
#     print("-----------OUTPUT---------------")
#     print(parsedAddress)
#     print("Done: " + str(i))
#     print("\n\n")
    
# finalJSON = {"addresses": finalAddresses}

# with open("outputFile.json", "w") as outfile:
#     json.dump(finalJSON, outfile)

#----------------------------------------#

