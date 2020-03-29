library(plotrix)

data = c(2,4,5)

par(mfrow=c(1,3)) 


#pie3d direct data
pie3D(data,
      radius =1,
      height = .2,
      main="Piechart 3D",
      labels = c("earining","expenditure","savings"),
      explode=.1,
      col=c("red","green","pink"),
) 


#pie3d table(data)
pie3D(table(data),
      radius =1,
      height = .2,
      main="Piechart 3D",
      labels = c("earining","expenditure","savings"),
      explode=.1,
      col=c("red","green","pink"),
      )


#piechart
pie(data,
    radius = 1, 
    col = c("blue" ,"green","orange"),
    main="2D piechart",
    labels=c("anger","peace","curse")
    )




