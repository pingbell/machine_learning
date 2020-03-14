

# read data from file
data1 <- read.delim("C:\\Users\\HP\\Desktop\\Data_science_for_engineers\\bonds.txt",row.names = 1)

# create model
model_linear = lm(data1$BidPrice~data1$CouponRate)

#plot graph
eruption = rstandard(model_linear$fitted.values)
plot(data1$BidPrice, eruption, ylab="Standardized Residuals",xlab="Waiting Time",main="Old Faithful Eruptions") 
 
abline(0,0)
#summary of model

summary(model_linear)

#Test for obtained statistics :
 beta0 = model_linear$coefficients[1]
 beta1 = model_linear$coefficients[2]

 sse = sum((model_linear$fitted.values - (data1$BidPrice))^2)
 sst = sum((data1$BidPrice - mean(data1$BidPrice))^2)
 ssr = sst-sse
 
 Fscore = (ssr/sse)*(35-2) 
  
 