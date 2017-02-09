library(jsonlite)

setwd("~/Projects/mixpanel-r") # SET THE WORKING DIRECTORY TO THE LOCATION OF main.r

events   <- "'Session Started,SettingsViewController'" # "event1,event2,..."
fromDate <- "2017-01-01" # "YYYY-MM-DD"
toDate   <- "2017-02-05" # "YYYY-MM-DD"
command  <- paste("python ./export.py", events, fromDate, toDate, sep=" ")

# Export data from mixpanel into a data frame
EventData <- fromJSON(system(command, intern = TRUE))

# Fill in your R code here