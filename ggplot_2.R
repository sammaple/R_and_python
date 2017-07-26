library(ggplot2)
dt = data.frame(A = 1:10, B = c(2,15,6,18,9,7,13,15,10,3), C = c('A','C','A','B','C','D','A','C','D','B'))
ggplot(dt, aes(x = A, y = B, color = C, group = factor(1))) + 
  geom_point(size = 3.8) +
  geom_line(size = 0.8) +
  geom_text(aes(label = B, vjust = 1.1, hjust = -0.5, angle = 45), show.legend = FALSE)   ## 添加点的数值