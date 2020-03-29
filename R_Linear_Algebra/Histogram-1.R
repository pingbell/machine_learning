data <-c(seq(1,10,by=1))

par(mfrow=c(1,6))
plot(density(data ,adjust=.5),
     xlab="save me from fakes",
     ylab="save me from reals",
     main="histograms plots",
     col=c("red"))

plot(density(data ,adjust=.5,kernel="gaussian"),
     xlab="save me from fakes",
     ylab="save me from reals",
     main="histograms plots",
     col=c("red"))

plot(density(data ,adjust=.5,kernel="triangular"),
     xlab="save me from fakes",
     ylab="save me from reals",
     main="histograms plots",
     col=c("red"))





hist(data ,
     xlab="save me from fakes",
     ylab="save me from reals",
     main="histograms plots",
     col=c("red","green","blue"))

