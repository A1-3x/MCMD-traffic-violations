##### Alexandra Vermeychik
##### INST 326: Object-Oriented Programming for Information Science
##### Professor Lou
##### December 7, 2025

# Homework 4: Analyze a Dataset of Your Choice

## Dataset
### Traffic Violations

This [dataset](https://data.montgomerycountymd.gov/Public-Safety/Traffic-Violations/4mse-ku6q/about_data) includes information on all traffic violations recorded within Montgomery County, Maryland since January 1st, 2012. It can be found using the dataMontgomery [repository](https://data.montgomerycountymd.gov/). Data recorded includes driver demographics, vehicle descriptions, and incident categorization.

## Pandas Operations Performed

| Operation | Purpose |
|-----------|---------|
| read_csv()| import csv as Dataframe |

## Observations

## Limitations

The "Year" column corresponds to the year of the vehicle model involved in the traffic violation. The the range of years is surprisingly large. The lowest is 0, which may represent the absense of that data or a mistake in data entry. 25% of the vehicles represented in the data are recorded as released prior to 2003. That comes out to approximately 500,000 traffic violations since 2012. Are all of the older years (some in the 1800s) accurate or merely mistakes? Was there confusion over whether "Year" denotes the model of the vehicle or the year of birth of the driver?
