# Udacity OpenStreet Map Project

As part of the Udacity Data Analyst Nanodegree course for Data Wrangling, I created this repo was to house my final work files for the OpenStreet Map (OSM) project.
In this project, I downloaded OSM data, audited several fields, iteratively cleaned the data while parsing the OSM into to five CSV files before importing the CSVs 
to SQL tables where I used SQL to query the data.

This repository consists of the following files : 

- __README.md__ : ReadMe file for this project containing an overal summary and details on the work that was done to complete this project.

- __project_report.md__ : The final project report that documents the work done on this project including the data wrangling process.

- __data.py__ : Python script containing the codes for gathering and extracting data from the OpenStreet Map (OSM) file. Data cleansing and manipulation is conducted per project 
requirements. Also the cleaned data is stored in CSV files.

- __csv-to-db.py__ : Python script containing code that exports each CSV file that was created as tables to be stored in a database. This database
is used to perform sql queries for research.

- __Get_OSM_Sample.ipynb__ : This file contains the code I use to obtain a subset of elements from the original OSM file.

- __irving_texas_osm.zip__ : Zip file containing the larger OSM file used in understanding the data involved and the basic structure of the code.

- __sample_irving_texas.osm__ : This smaller sample OSM file is used in understanding the data involved and the basic structure of the code.
I will use this subset of the larger file for auditing and data cleaning before proceeding to work on the larger OSM file.

- __References.txt__ : Contains a list of Web sites, forums, blog posts, etc referred to in this submission