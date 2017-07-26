library("geosphere")
library(dplyr) ##����dplyr��
library("ggplot2")

loushi <- read.csv("D:\\new\\R\\lou20170606.csv", header=TRUE)  
str(loushi)


loushi_info <- tbl_df(loushi) ##ת��Ϊdplyr�����ĸ����ŵ����ݽṹ

loushi_info_hushu <- select(loushi_info,"¥������","�ܻ���","��ҵ����")
set.seed(42)
small <- loushi_info_hushu[sample(nrow(loushi_info_hushu), 10), ]
#small <- head(loushi_info_hushu,5)

class(small$�ܻ���) #�鿴�ܻ���������

#small <- small[order(as.numeric(as.character(small$�ܻ���))),] #fator ���ͻ�char,Ȼ��ת����
#small

#gp <- ggplot(data=small, mapping=aes(x=¥������ , y=�ܻ��� ,colour="blue"))
#gp + geom_point(alpha = 1,size = 3.8)
#print(gp)

#��׼���10��¥����Ϣ��������¥�̡���ҵ��
ggplot(small, aes(x=as.numeric(as.character(small$�ܻ���)) , y=¥������ ,color=��ҵ����)) +
	geom_point(size = 3.8) +
	geom_line(size = 0.8) +
	geom_text(aes(label = �ܻ���, vjust = 1.1, hjust = -0.5, angle = 45), show.legend = FALSE) +
      xlab("�ܻ���") + ylab("¥����") + ggtitle("�����10��¥����Ϣ") + #���Ӻ����������ƣ�����ͼ������
	xlim(150,2500) #�޸�X�᷶Χ