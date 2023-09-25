# West Nile Virus Final Project: All US Data Combinations

For the final project in my internship, I was tasked with compiling a spreadsheet of climate data for every West Nile Virus case that had occurred in the US in the last 20 years. 

# API Downloads
First, I wrote the api_downloads script to download the 500 GB of climate data from the Copernicus Database, which took over a week to download running on a cluster

# Threadings
Originally, I was going to run the code that compiled and mapped the data together one at a time, but that was going to take too long. So, I set out to learn multi-threading in python using the Process Pool Executor, and used the cluster to run 6 compilations at a time, which helped decrease the time the code was going to take from 5 days to under 1!
