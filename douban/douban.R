#https://zhuanlan.zhihu.com/p/27009299
library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")
library("gridExtra")

douban <- read.csv("D:\\new\\R\\douban\\result_new_rm_countries.csv", header=TRUE)  
douban_direct <- read.csv("D:\\new\\R\\douban\\director_count.csv", header=TRUE)  

#str(douban)

douban_info <- tbl_df(douban) ##转化为dplyr处理的更优雅的数据结构
douban_direct_info <- tbl_df(douban_direct) ##转化为dplyr处理的更优雅的数据结构
douban_direct_info <- reorder(douban_direct_info,Count)
douban_direct_info <- head(douban_direct_info,40)

douban_choosen <- select(douban_info,"result__date","result__rate","result__time","result__country","result__time_rate")


#所有豆瓣统计图
p1 <- ggplot(douban_choosen,aes(x=result__date)) + geom_bar() + ggtitle("豆瓣电影年份") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

p2 <- ggplot(douban_choosen,aes(x=result__date,y=result__rate)) + geom_point() + ggtitle("豆瓣电影年份及评分热力图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) + stat_bin2d()

p3 <- ggplot(douban_choosen,aes(x=result__rate,y=result__time)) + geom_point() + ggtitle("豆瓣电影评分及时长热力图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) + stat_bin2d()

p4 <- ggplot(douban_choosen,aes(x=result__date,fill=result__country)) + geom_bar() + ggtitle("豆瓣电影年份分国家") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

#标准随机10个楼盘信息（户数、楼盘、物业）
p5 <- ggplot(douban_choosen, aes(x=douban_choosen$result__date,y=result__rate,color=result__country,shape=result__time_rate)) +
	geom_point(size = 3.8) 
#	geom_line(size = 0.8) 
#	geom_text(aes(label = result__date, vjust = 1.1, hjust = -0.5, angle = 45), show.legend = FALSE) +
#      xlab("总户数") + ylab("楼盘名") + ggtitle("随机10个楼盘信息") + #添加横纵坐标名称，添加图的名称
#	xlim(1900,2500) #修改X轴范围

p6 <- ggplot(douban_direct_info,aes(x=Director,fill=as.numeric(Count))) + geom_bar() + ggtitle("豆瓣电影导演产出") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

#p4 <- ggplot(douban_choosen) + geom_bar(aes(x=result__date,fill=result__country), position = 'dodge') + ggtitle("638升级分柱统计图") +
#theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))

#p5 <- ggplot(osupdate_choosen) + geom_bar(aes(x=region,fill=region), position = 'dodge') + ggtitle("638升级分柱统计图") +
#theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))+
#  facet_grid(.~date)

#p6 <- ggplot(osupdate_choosen) + geom_density(aes(x=date,color=net))
#grid.arrange(p1, p2, p3,p4,p5,p6, ncol=2)
grid.arrange(p6,ncol=2)