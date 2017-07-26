library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")

loushi <- read.csv("D:\\new\\R\\lou20170606.csv", header=TRUE)  
str(loushi)


loushi_info <- tbl_df(loushi) ##转化为dplyr处理的更优雅的数据结构

loushi_info_hushu <- select(loushi_info,"楼盘名称","总户数","物业类型")
set.seed(42)
small <- loushi_info_hushu[sample(nrow(loushi_info_hushu), 10), ]
#small <- head(loushi_info_hushu,5)

class(small$总户数) #查看总户数的类型

#small <- small[order(as.numeric(as.character(small$总户数))),] #fator 类型换char,然后转数字
#small

#gp <- ggplot(data=small, mapping=aes(x=楼盘名称 , y=总户数 ,colour="blue"))
#gp + geom_point(alpha = 1,size = 3.8)
#print(gp)

#标准随机10个楼盘信息（户数、楼盘、物业）
ggplot(small, aes(x=as.numeric(as.character(small$总户数)) , y=楼盘名称 ,color=物业类型)) +
	geom_point(size = 3.8) +
	geom_line(size = 0.8) +
	geom_text(aes(label = 总户数, vjust = 1.1, hjust = -0.5, angle = 45), show.legend = FALSE) +
      xlab("总户数") + ylab("楼盘名") + ggtitle("随机10个楼盘信息") + #添加横纵坐标名称，添加图的名称
	xlim(150,2500) #修改X轴范围
