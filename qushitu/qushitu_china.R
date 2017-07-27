library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")
library("gridExtra")

china <- read.csv("D:\\new\\R\\qushitu\\2015_2016_china_bench.csv", header=TRUE)  
str(china)


china_info <- tbl_df(china) ##转化为dplyr处理的更优雅的数据结构

china_choosen <- select(china_info,"指标","X2014年","X2015年","X2016年")

head(china_choosen)

count_all <- dim(china_choosen)[1]

count_all
p1 <- ggplot(china_choosen, aes(x=1:count_all,y=X2014年))+geom_point()+stat_smooth()

p2 <- ggplot(china_choosen, aes(x=1:count_all,y=X2015年))+geom_point()+scale_y_log10()+stat_smooth()

grid.arrange(p1,p2,ncol=2)