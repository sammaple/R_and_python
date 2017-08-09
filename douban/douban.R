#https://zhuanlan.zhihu.com/p/27009299
library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")
library("gridExtra")

douban <- read.csv("D:\\new\\R\\douban\\result_new.csv", header=TRUE)  
str(douban)

douban_info <- tbl_df(douban) ##转化为dplyr处理的更优雅的数据结构

douban_choosen <- select(douban_info,"result__date","result__rate","result__time","result__country")


#所有638升级统计图
p1 <- ggplot(douban_choosen,aes(x=result__date)) + geom_bar() + ggtitle("豆瓣电影年份") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

p2 <- ggplot(douban_choosen,aes(x=result__date,y=result__rate)) + geom_point() + ggtitle("豆瓣电影年份及评分热力图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) + stat_bin2d()

#p3 <- ggplot(douban_choosen,aes(x=result__date,fill=result__country)) + geom_bar() + ggtitle("638升级分柱统计图") +
#theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

#p4 <- ggplot(douban_choosen) + geom_bar(aes(x=result__date,fill=result__country), position = 'dodge') + ggtitle("638升级分柱统计图") +
#theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

#p5 <- ggplot(osupdate_choosen) + geom_bar(aes(x=region,fill=region), position = 'dodge') + ggtitle("638升级分柱统计图") +
#theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))+
#  facet_grid(.~date)

#p6 <- ggplot(osupdate_choosen) + geom_density(aes(x=date,color=net))
#grid.arrange(p1, p2, p3,p4,p5,p6, ncol=2)
grid.arrange(p1,p2,ncol=2)