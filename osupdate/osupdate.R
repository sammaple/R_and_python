#https://zhuanlan.zhihu.com/p/27009299
library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")
library("gridExtra")

osupdate <- read.csv("D:\\new\\R\\osupdate\\osupdate.csv", header=TRUE)  
str(osupdate)


osupdate_info <- tbl_df(osupdate) ##转化为dplyr处理的更优雅的数据结构

osupdate_choosen <- select(osupdate_info,"设备号","操作类型","操作状态","原因")

head(osupdate_choosen)

dim(osupdate_choosen)

osupdate_choosen_quchong<-unique(osupdate_choosen,fromLast=TRUE)

dim(osupdate_choosen_quchong)

p1 <- ggplot(osupdate_choosen_quchong,aes(x=操作类型,y=操作状态)) + geom_point() + ggtitle("xxx升级二维统计图") +
  theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) + stat_bin2d()

p2 <- ggplot(osupdate_choosen_quchong,aes(x=操作类型,fill=操作状态)) + geom_bar() + ggtitle("638升级分柱统计图") +
  theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

grid.arrange(p1,p2,ncol=2)