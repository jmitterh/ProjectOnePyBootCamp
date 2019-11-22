
![](https://myrealdomain.com/images/job-application-clip-art-5.png)

# ProjectOnePyBootCamp

Team of three:
* Eliana Suarez 
* Zoe Liu
* Jean-Paul Mittehofer

In what part of the Unites States are job offers, specifically job posting, widespread in a particular area in a particular time? 
To answer this a search was conducted for the appropiate source of data. Then determined what useful information the data should have:
* Category
* Time
* Lat/Lng
* Unique ID
* Company Name

With the source determined the data cleansing process was incorporated with the help of pandas. After, the data visualization process proceeded, and decided what information was important to extract.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install jupyter notebook
pip install pandas
pip install gmaps
pip install numpy
pip install matplotlib
pip install opencage
pip install random
```

## Folder And File Description

#### Repository description:
1. classResources   (*Contains related material needed to complete the project assignment.*)
2. data             (*Contains all data sources.*)
    * cleanData     (*Data that is ready for visualization. 1_master_clean_data is the data used analysis8*)
    * rawData       (*Data that is not formatted strait from the source*)
    * vizData       (*Visual output of the data*)
3. notebooks        (*working not book for each team member*)
4. reports          (*final notebook and presentation*)


#### The main files to execute, in ordered fashion, are in the below path:
***ProjectOnePyBootCamp\reports:***

1. Final_API.ipynb (*Key needed to connect to Azduna and Google Geocoding*)
2. Final_Cleaning_Up_Data.ipynb
3. Final_API_City_State.ipynb (*Key need to connect to OpenCage Geocoding*)
4. Final_Visualization.ipynb
5. Final_Gmaps.ipynb

#### Output of the visualization and gmaps ipyb file are located in the following path:
***ProjectOnePyBootCamp\data\vizData***

* 1_master_Graph_Top_5_Categories
* 2_master_Graph_Top_5_Cities
* 3_master_Graph_Top_5_State
* 4_master_Graph_Top_City_Top_5_Category
* 5_master_Graph_Top_State_Top_5_Category
* 6_master_Plot_Category_Job_Postings_Month
* 7_master_Plot_City_Job_Postings_Month
* 8_master_Plot_State_Job_Postings_Month
* 9_master_Plot_Total_Job_Postings_Month


## Sources
* [***Azduna***](https://developer.adzuna.com/)
 is a search engine for job advertisements. 
 The company operates in 16 countries worldwide and the UK website aggregates job ads from several thousand sources. This is our dataset source and also the source of our lat and lng data containing the exact location of the job offer.

* [***OpenCage Geocoder***](https://opencagedata.com/)
is open geocoding. Their API combines multiple geocoding systems in the background. 
Each is optimized for different parts of the world and types of requests. This was used to get the lat and lng for cities in the United States.

* [***Google Geocoding***](https://cloud.google.com/maps-platform/)
 is the Google Maps Platform. This service was used to provide the reverse geocoding process of converting geographic coordinates into a readable address of city, state, and country\.
## Considerations
Our main raw data set could not be pushed into github since the csv file was in excess of 200MB.
Once the raw data was cleansed, its size was below 50MB, more than enough to meet GitHubs polices of file size.
## License
[MIT](https://choosealicense.com/licenses/mit/)