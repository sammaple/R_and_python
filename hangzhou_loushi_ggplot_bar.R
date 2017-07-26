#https://zhuanlan.zhihu.com/p/27009299
library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")

loushi <- read.csv("D:\\new\\R\\lou20170606.csv", header=TRUE)  
str(loushi)


loushi_info <- tbl_df(loushi) ##转化为dplyr处理的更优雅的数据结构

loushi_info_hushu <- select(loushi_info,"板块名称")
set.seed(42)
#small <- loushi_info_hushu[sample(nrow(loushi_info_hushu), 10), ]
#small <- head(loushi_info_hushu,5)


#所有楼盘板块统计图
ggplot(loushi_info_hushu,aes(x=板块名称)) + geom_bar() + ggtitle("所有楼盘板块统计图") +
theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red")) +
xlab("板块") + 
ylab("楼盘个数") +
geom_text(stat="count",label=paste(table(loushi_info_hushu)/sum(table(loushi_info_hushu))*100,'%',sep=''),colour = "black", vjust=-0.5, size=4.7)