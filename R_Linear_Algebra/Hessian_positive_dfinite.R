
#define polynomial 

poly <-function (u){
  x<-u[1]
  y<-u[2]
  z<-u[3]
  
  return (x^2 +y^2 +z^2)
}

#define a point of evaluation , staionary point
vec <- c(2,3,4)

# evaluate hessian 
hessian_matrix<-hessian(poly,vec)

# test for hessian to be positive definite 
ev=eigen(hessian_matrix)
# extract components
(values <- ev$values)
## [1] 17  8  7
(vectors <- ev$vectors)

flag = FALSE
for  ( i in lengths(values) ){
  if (values[i]>0){
    flag =TRUE

  }
  else 
    flag =FALSE
}

if (flag==TRUE)
  print("positive definite")
