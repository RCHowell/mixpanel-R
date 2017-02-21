library(jsonlite)

setwd("~/Projects/mixpanel-r") # SET THE WORKING DIRECTORY TO THE LOCATION OF main.r

events   <- "'Session Started'" # "event1,event2,..."
fromDate <- "2017-01-01" # "YYYY-MM-DD"
toDate   <- "2017-02-20" # "YYYY-MM-DD"
command  <- paste("python ./export.py", events, fromDate, toDate, sep=" ")
library(mosaic, quietly = T)
# Export data from mixpanel into a data frame
EventData <- fromJSON(system(command, intern = TRUE))
print(command)

USData = data.frame(
  EventData$properties$`$duration`[EventData$properties$mp_country_code != "US"]
)
USData <- USData$EventData.properties...duration..EventData.properties.mp_country_code....
bwplot(USData$time, pch = "|", main = "Session Time on Crcl in the U.S.", xlab="Time in Seconds")
# library(ggplot2)
# library(maps)
# # Fill in your R code here
# states <- map_data("state")
# EventData$properties$`$region` <- tolower(EventData$properties$`$region`)
# cleanData <- data.frame(
#   region= EventData$properties$`$region`
# )
# 
# cleanData <- merge(cleanData, states, by = "region")
# 
# ggplot(cleanData, aes(long, lat)) +
#   geom_polygon(aes(group = group, fill = 1)) +
#   coord_map("albers",  at0 = 45.5, lat1 = 29.5)
# 
# p <- ggplot()
# p <- p + geom_polygon(data=Total, aes(x=long, y=lat, group = group, fill=Total$bwRatio),colour="white"
# ) + scale_fill_continuous(low = "thistle2", high = "darkred", guide="colorbar")
# P1 <- p + theme_bw()  + labs(fill = "Black to White Incarceration Rates \n Weighted by Relative Population" 
#                              ,title = "State Incarceration Rates by Race, 2010", x="", y="")
# P1 + scale_y_continuous(breaks=c()) + scale_x_continuous(breaks=c()) + theme(panel.border = element_blank())
# 
