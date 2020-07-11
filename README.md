# Consumer Complaints
This goal of the project is to identify the number of complaints filed for each financial prodcut, and year and how they're spread across different companies.

## Description
The project is divided into following steps:
- identifies unique pairs of product and year.
- find the total number of complaints for that product and year
- find the total number of companies receiving at least one complaint for that product and year
- find the highest percentage of total complaints filled against one company.

This information is extracted and written to a csv file (report.csv) that is exported to the output file.

## Python Modules 
- sys
- csv
- math
- collections

## Setup/ Installation
Using terminal type the command 'bash run.sh' or './run.sh'. run.sh is provided to execute the company_complaints.py file as well as provide a path for the input and output files. 

## Project Flow
- The first step was to open the csv file and read it into a list. Only columns that were needed were kept , the header was removed and then stored into a new list called data. The columns we choose were : Date received(0) , Product (1) and Companies(7).
- Now comes processing the date under the function processing_data. The date was striped at '-' and only the year at index 0 was selected and applied to each list.
- Now each list inside the list('data') has the date, product and company. I processed each list into a dictionary as key:value pairs. where key was 'date '|' product 'and the value was the company. This way we can now have unique pairs of product and year as the keys of the dictionary and companies as thier values.
- This dictionary is now used for the rest of the processing. we count the number of companies within the value assigned to each key (unique pair of product and year) and this is our total number of complaints for that unique product and year. Finding the unique companies inside the value, gives us the total number of companies receiving at least one complaint for that product and year(key). then Used counter from collections (faster than creating a dictioanry) to find the company with the maximum frequency within the value for each key, which is then divided by the total number of complaints and multiplied by 100 to get the percentage for the highest complaint.
- To have an output with the structure as requested in the challenge, The keys isnide the dictionary were split at '|' to get date and product which were stored under thier respective variables. Our final output writes the data (product, Year, number of complaints, unique companies (companies with at least one complaint), highest percenatge of complaint for a company) to a csv file 'export.csv'.

