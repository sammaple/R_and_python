#https://wklchris.github.io/R-plotting-basic.html
OutputColors <- function(color.names, titleStr="", showText=F) {
    plot(1,1, axes=F, xlim=c(0, 6), ylim=c(0, 6), main=titleStr, xlab="", ylab="")
    for (i in c(1:5)) {
        for (j in c(1:5)) {
            par(new=T)
            plot(i, 6-j, cex=3, xlim=c(0, 6), ylim=c(0, 6), axes=F,
                 main="", xlab="", ylab="", pch=19, 
                 col=color.names[(i-1)*5+j])
            if (showText) {
                text(i, 6-j-0.1, pos=1, color.names[(i-1)*5+j])
            }
        }
    }
}

colorLst <- c("white", "red", "green", "blue", "brown",
              "cyan", "gold", "gray", "plum", "magenta",
              "orange", "purple", "yellow", "black", "violet",
              "darkblue", "darkgreen", "darkred", "darkgray", "dimgray",
              "lightblue", "lightgreen", "lightgray", "orchid", "pink")
OutputColors(colorLst, "25 Useful Colors", T)