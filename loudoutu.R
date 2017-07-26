#效果很好

plot.tran<-function(input.filter,main=" "){#input.data由小到大排列
  data<-unname(input.filter)
  num<-length(data)
  tmp.data<-data/min(data);#把data等比例放大，使得全部数据均是整数，最小整数是1  
  for(i in 1:num){
    if(i==1){
      data1<-rep(i,tmp.data[i]+tmp.data[num])
      data2<-rep(i,tmp.data[num]-tmp.data[i])
    }else{
      data1<-c(data1,rep(i,tmp.data[i]+tmp.data[num]))
      data2<-c(data2,rep(i,tmp.data[num]-tmp.data[i]))
    }
  }
  dev.new()#新建一个绘图页面
  lab<-" "
  for(i in 1:num){
    lab[i]<-paste(100*tmp.data[i]/max(tmp.data),"%",sep="");
  }
  label<-names(input.filter)
  level<-paste(label,lab,sep=" / ")
  par(mar=c(1,6,4,2), col.axis=0.8,font.axis=1,col.axis="gray30",cex.main=1.3,font.main=2,col.main="gray30")
  cols=terrain.colors(num)   #terrain.colors(num) #rainbow(num)  #heat.colors(num)
  barplot(table(data1),horiz= T,border="white",col=cols,axes=F,names.arg=level,main=main, las = 2)#横向绘制分类数据的barplot
  barplot(table(data2),horiz= T,add=T,col="white",border="white",axisnames=F , axes=F , las = 2)#使用白色画出漏斗样式
}
filter<-c(0.04,0.08,0.3,0.6,1)
names(filter)<-c('alipay','gmv','cart','detail','pv')
graphics.off()
plot.tran(filter)