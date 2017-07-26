library("geosphere")
library(dplyr) ##导入dplyr包
library("ggplot2")

loushi <- read.csv("D:\\new\\R\\lou20170606.csv", header=TRUE)  
str(loushi)


loushi_info <- tbl_df(loushi) ##转化为dplyr处理的更优雅的数据结构

loushi_info_hushu <- select(loushi_info,"index","楼盘名称","总户数","物业类型")

loushi_info_hushu_filter <- filter(loushi_info_hushu, as.character(loushi_info_hushu$物业类型)  == "别墅" | as.character(loushi_info_hushu$物业类型)  == "公寓" | as.character(loushi_info_hushu$物业类型)  == "住宅" | as.character(loushi_info_hushu$物业类型)  == "普通住宅")

ggplot(loushi_info_hushu_filter)+geom_point(aes(x=index, y=总户数,color=物业类型))+facet_wrap(~物业类型)