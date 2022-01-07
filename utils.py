import re

acronyms = {
    "3 rd":"3rd",
    "2 nd":"2nd",
    "1 st" :"1st",
    "co op|co-op":"Cooperative",
    "opp":"Opposite",
    "rd":"Road",
    "bld":"Building",
    "nr":"Near",
    "nex":"Next",
    "apt|appartm":"Apartment",
    "adj":"Adjacent",
    "flr|flor":"Floor",
    "sec":"Sector",
    "blk":"Block",
    "soc":"Society",
    "st|strt|str":"Street",
    "sch":"School",
    "nbr|num|no":"Number",
    "chk|chok":"Chowk",
    "div":"Division"
}

def expander(text):
  for short, long in acronyms.items():
   text = re.sub(rf'\b{short}(?!\S)', long, text, flags=re.IGNORECASE)
  return text

def preProcessAddress(address):
    if(address[0] == '#'):
        address = address[1:]
    addressArray = re.split(" ", re.sub(' +', ' ',address.replace('.', '').replace(',', '')))
    addressArray = [expander(x).lower() for x in addressArray]
    if(addressArray[0] == ''):
        addressArray = addressArray[1:]
    if 'india' in addressArray:
        addressArray.remove('india')
    return addressArray
