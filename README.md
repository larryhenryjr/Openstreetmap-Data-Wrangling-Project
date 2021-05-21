# OpenStreetMap Data Case Study

## Project Overview
This project is part of Udacity Data Analyst Nanodegree course for Data Wrangling. The main point of this Project is to learn how to access data and perform 
data cleaning with Python. First, I will access data in an XML file from OpenStreet Map and perform some data cleaning. Then, the cleaned data will then be imported 
into a DBMS or MongoDB. In this case, I will use a DBMS and run a few SQL queries on the cleaned data to complete the project.


### Map Area
Irving, TX, United States

- [https://www.openstreetmap.org/relation/5748832](https://www.openstreetmap.org/relation/5748832)

<p align="center">
  <img src=images/IrvingTX-W-LasColinas-area.png alt="LasColinas-area-IrvingTX" style="width: 350px;" style="height: 350px;" />
</p>


### Software and Application
- Jupyter Notebook
- Spyder
- Python 3
- sqlite3
- Excel
- SQLiteStudio


This repository consists of the following files : 

- __README.md__ : ReadMe file for this project containing an overal summary and details on the work that was done to complete this project.

- __data.py__ : Python script containing the codes for gathering and extracting data from the OpenStreet Map (OSM) file. Data cleansing and manipulation is conducted per project 
requirements. Also the cleaned data is stored in CSV files.

- __csv-to-db.py__ : Python script containing code that exports each CSV file that was created as tables to be stored in a database. This database
is used to perform sql queries for research.

- __Get_Sample_OSM.ipynb__ : This file contains the code I use to obtain a subset of elements from the original OSM file.

- __sample_IrvingTX-W-LasColinas.osm__ : This smaller sample OSM file is used in understanding the data involved and the basic structure of the code.
I will use this subset of the larger file for auditing and data cleaning before proceeding to work on the larger OSM file.

- __References.txt__ : Contains a list of Web sites, forums, blog posts, etc referred to in this submission