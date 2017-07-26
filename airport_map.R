library("geosphere")
airports <- read.csv("http://datasets.flowingdata.com/tuts/maparcs/airports.csv", header=TRUE)  
flights <- read.csv("http://datasets.flowingdata.com/tuts/maparcs/flights.csv", header=TRUE, as.is=TRUE)  
map("world",col="#00f2f2",fill=TRUE,bg="white",lwd=0.5)  #china world usa
fsub <- flights[flights$airline=="AA",]  
for (j in 1:length(fsub$airline)) {  
  air1 <- airports[airports$iata == fsub[j,]$airport1,]  
  air2 <- airports[airports$iata == fsub[j,]$airport2,]  
  inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)  
  lines(inter, col="black", lwd=0.8)
}