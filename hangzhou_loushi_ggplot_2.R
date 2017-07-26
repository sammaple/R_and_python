library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")

par(las=2)

loushi <- read.csv("D:\\new\\R\\lou20170606.csv", header=TRUE)  
str(loushi)


loushi_info <- tbl_df(loushi) ##转化为dplyr处理的更优雅的数据结构

loushi_info_hushu <- select(loushi_info,"板块名称","总户数","物业类型")
set.seed(42)
small <- loushi_info_hushu[sample(nrow(loushi_info_hushu), 50), ]
#small <- head(loushi_info_hushu,5)

class(small$总户数) #查看总户数的类型

#small <- small[order(as.numeric(as.character(small$总户数))),] #fator 类型换char,然后转数字
#small

#标准随机50个楼盘板块信息（户数、楼盘、物业）
ggplot(small, aes(x=板块名称 , y=as.numeric(as.character(small$总户数)) ,color=物业类型)) +
	geom_point(size = 3.8) +
	geom_line(size = 0.8) +
	geom_text(aes(label = 总户数, vjust = 1.1, hjust = -0.5, angle = 45), show.legend = FALSE) +
      xlab("总户数") + ylab("楼盘名") + ggtitle("随机50个楼盘板块信息") +#添加横纵坐标名称，添加图的名称
	theme(axis.text.x=element_text(face="bold",size=8,angle=90,color="red"))