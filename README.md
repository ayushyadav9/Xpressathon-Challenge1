
<div id="top"></div>
<!-- PROJECT LOGO -->
<br>
<br>
<p align="center">
  <img width="300px" src="https://www.xpressbees.com/Xpressathon/assets/img/Logo-Big%20(1).png">
</p>
</p>
<br />
<div align="center">
    <h1>Team: <strong>Disruptors</strong></H1>
    <H3>Xpressathon - XpressBees Logistics Hackathon </h3>
    <h3> Team Members: <strong>Sushil Adwe | Chirag Hegde | Ayush Yadav</strong></h3>
    <h3> Indian Institute of Technology, Guwahati </h3>
</div>


<br/>

## **Challenge 1: Address Normalization**
Normalize unstructured raw Indian addresses by segregating personal information and address
to a defined json structure. Addresses can contain spelling mistakes which need to be
corrected and addresses need to be geocoded.
<br>
<br>

## **Our Solution**

This project aims to establish a Python framework to perform Indian Address Standardization using RapidFuzzy string comparision with an additional layer of correction backed by Google Maps API.

**Address Standardization includes**:

* Address Correction is mainly used to identify, complete and format some address characters with confusing formats
* Address validation for verification of the corrected address using Google Maps API.
* Address Normalization creates a systematic and consistent basis for record-keeping across the country 

<p align="right"><br/></p>

## **Sample Input**
<br>

### **Input Address**
----------------

```
  Flat- DH102804 floor , GoodLuck Apt , opp Eliphanta tower Subhash Lane , Daftary Road Malad East Mumbai Maharashtra India 400047
```

### **Formatted Address**
----------------

```

{
   "addressline1":"Flat- Dh102804 Floor Goodluck Apartment Opposite Eliphanta Tower",
   "addressline2":"Subhash Lane Daftary Road Malad East",
   "locality":"Malad East",
   "city":"MUMBAI",
   "state":"MAHARASHTRA",
   "pincode":"400097",
   "geocodes":"19.1858629,72.852386"
}
 
```

<br>

### **Input Address**
----------------

```
  vardayani soc. plot no. A32167 Aishwarya bldg flat no 2 sus road pashan opp Abhinav collage Pune Maharashtra India 411021
```
### **Formatted Address**
----------------
```

{
   "addressline1":"Vardayani Society Plot Number A32167 Aishwarya Building",
   "addressline2":"Flat Number 2 Sus Road Pashan Opposite Abhinav Collage",
   "locality":"Pashan",
   "city":"PUNE",
   "state":"MAHARASHTRA",
   "pincode":"411021",
   "geocodes":"18.5454142,73.7778275"
}
 
```

<br>
<!-- GETTING STARTED -->

## **Installation**

_Below are the steps to clone the repository and  setting up the app in local._

### Prerequisites
* Python must be installed on your computer<br>
* You must have an google maps API key which can be accessed from [here](https://console.cloud.google.com/google/maps-apis/start)

<br>
<br>

1. Clone the Repository
   ```sh
   git clone https://github.com/soul0101/Xpressathon-Challenge1.git
   ```

2. Install Python packages that are used 
   ```sh
   pip install -r requirements.txt
   ```
   
3. Run main.py file
   ```sh
   python main.py
   ```


<p align="right"><br/></p>


<!-- ACKNOWLEDGMENTS -->
## **Acknowledgments**

* [RapidFuzz](https://pypi.org/project/rapidfuzz/)
* [All India Pincode Directory](https://data.gov.in/resources/all-india-pincode-directory-till-last-month)
* [Google maps API](https://console.cloud.google.com/google/maps-apis/start)



<p align="right"><a href="#top"><img src="https://img.icons8.com/external-kiranshastry-gradient-kiranshastry/64/000000/external-up-arrow-alignment-and-tools-kiranshastry-gradient-kiranshastry.png"/></a></p>

