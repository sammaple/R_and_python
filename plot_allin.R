dose <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
plot(dose, drugA,
     type="b",              # 图表类型，b为折线图
     bg="green",            # 背景颜色 绿色
     fg="blue",             # 前景颜色 蓝色
     col="red",             # 折线和点的颜色 红色
     col.axis="grey",       # 坐标轴文本颜色 灰色
     col.lab="#3EB4EA",     # 坐标轴标签颜色 我也叫不上来啥颜色
     lty=3,                   # 线类型(line type) 
     lwd=3,                 # 线宽度 默认2
     pch=15,                # 点的类型 实心方块
     cex=2,                 # 指定符号大小 2为 200%
     col.main=rgb(1,1,1)    # 标题的颜色 
)
lines(dose,drugB,
     type="o",              # 图表类型，b为折线图
     bg="green",            # 背景颜色 绿色
     fg="blue",             # 前景颜色 蓝色
     col="yellow",             # 折线和点的颜色 红色
     col.axis="grey",       # 坐标轴文本颜色 灰色
     col.lab="#3EB4EA",     # 坐标轴标签颜色 我也叫不上来啥颜色
     lty=3,                   # 线类型(line type) 
     lwd=3,                 # 线宽度 默认2
     pch=15,                # 点的类型 实心方块
     cex=2,                 # 指定符号大小 2为 200%
     col.main=rgb(1,1,1)    # 标题的颜色 
)
title("Regression of MPG on Weight(Colorful)") 
