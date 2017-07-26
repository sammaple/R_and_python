library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")

airports <- read.csv("airports.csv", header=TRUE)  
flights <- read.csv("flights.csv", header=TRUE, as.is=TRUE)  

head(flights,5)# 前五条数据 
airports_info <- tbl_df(airports) ##转化为dplyr处理的更优雅的数据结构
airports_info

airports_info_ex <- select(airports_info,state,country)
airports_info_ex
dim(airports_info_ex) #2列属性

airports_final <- summarize(group_by(airports_info_ex, state,country))
#View(airports_final)

flights_info <- tbl_df(flights)
airports_info_ex <- filter(flights_info,airline=='AA')
#airports_info_ex <- filter(flights_info)
airports_info_ex

#airports_dest_summry <- airports_info_ex %>% group_by(airport2) %>% summarise(sum = length(cnt))
#airports_dest_summry

##按照航站楼的航班数进行降序排序
#airports_dest_sorted <- arrange(airports_dest_summry, desc(sum))

##View(airports_dest_sorted)
#hot_airports <- airports_dest_sorted[airports_dest_sorted$sum > 10,]
#View(hot_airports)

#gp <- ggplot(airports_dest_summry, mapping = aes(x = c(1:58), y = sum))
#gp + geom_point(colour = "red", size = 2) + geom_line(colour = "blue", size = 1.5) + xlab("航班站") + ylab("航班总数") + scale_x_continuous(breaks = c(1:58)) + scale_y_continuous(breaks = seq(0,100,10))

gp <- ggplot(airports_info_ex, mapping = aes(x = airport1 , y = airport2))
#gp + geom_point(colour = "red", size = 2) + geom_line(colour = "blue", size = 1.5) + xlab("到达航站") + ylab("起始航站")
gp + geom_point(aes(colour = factor(airline),shape = factor(airline), size = cnt), alpha = 0.6, position = 'jitter')
#print(gp)