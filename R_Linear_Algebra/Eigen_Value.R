library(pracma)

mat1<-matrix(nrow=3,ncol=3,data = 1:9)

ev = eigen(mat1)

value <- ev$values

vect <-ev$vectors

trace <- prod(ev$values)

eigen_orthogonality_test = zapsmall(crossprod(vect))

trace_of_vect = trace(vect) 
 

