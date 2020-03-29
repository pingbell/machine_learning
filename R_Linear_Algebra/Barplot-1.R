

data <- matrix(nrow=3 ,ncol=5 ,byrow=TRUE, data =c(1,2,3,4,5,6,7,8,5,4,4,5,6,8,9))
barplot(data , 
        col=c("green","yellow","red"),
        width=4,
        space=4,
        xlab="karma",
        ylab="punya",
        main="actual life",
        names.arg = c("life","alife","tmom", "pka","akarma") )

