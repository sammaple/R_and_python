library("ggplot2")

p <- data.frame(Probability<-c(1,1.1,1.2,1.3,1.7,1),SNP<-c(1,2,3,4,5,6))

qplot(SNP,Probability,  data=p , colour=Probability, xlab="")+
geom_line(aes(y=Probability, x=SNP))+
theme(legend.position="none")+
geom_point(aes(y=Probability, x=SNP),size=5, shape=15)+
theme(axis.text.x=element_text(face="bold",size=10,angle=90,color="red"))

#ÑÕÉ«ÊÇ¹Ø¼ü