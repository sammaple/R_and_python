#https://zhuanlan.zhihu.com/p/27009299
library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")
library("gridExtra")

osupdate <- read.csv("D:\\new\\R\\638\\638_osupdate.csv", header=TRUE)  
str(osupdate)


osupdate_info <- tbl_df(osupdate) ##转化为dplyr处理的更优雅的数据结构

osupdate_choosen <- select(osupdate_info,"date","region","net")


#所有638升级统计图
p1 <- ggplot(osupdate_choosen,aes(x=date)) + geom_bar() + ggtitle("638升级柱统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

p2 <- ggplot(osupdate_choosen,aes(x=date,y=region)) + geom_point() + ggtitle("638升级二维统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) + stat_bin2d()

p3 <- ggplot(osupdate_choosen,aes(x=date,fill=region)) + geom_bar() + ggtitle("638升级分柱统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

p4 <- ggplot(osupdate_choosen) + geom_bar(aes(x=date,fill=region), position = 'dodge') + ggtitle("638升级分柱统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

p5 <- ggplot(osupdate_choosen) + geom_bar(aes(x=region,fill=region), position = 'dodge') + ggtitle("638升级分柱统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))+
  facet_grid(.~date)

p6 <- ggplot(osupdate_choosen) + geom_density(aes(x=date,color=net))
#grid.arrange(p1, p2, p3,p4,p5,p6, ncol=2)
grid.arrange(p1,p2,ncol=2)