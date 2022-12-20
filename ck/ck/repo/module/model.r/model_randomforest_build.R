#
# Collective Knowledge (Predictive modeling using R)
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin
#

# model package
library(randomForest)

# get arguments
args <- commandArgs(trailingOnly = TRUE)

finput=args[1]
foutput=args[2]

# get data
#data_set = read.table(args[1], header=T, sep=";")
data_set = read.csv(finput, header=FALSE, sep=";")

# variables
x=data.frame(data_set[,1:ncol(data_set)-1])

# value
y=data_set[,ncol(data_set)]

# model
model=randomForest(y~.,data=x)

# Saving model
save(model, file=paste(foutput,'',sep=''))

print(model)

summary(model)

plot(model)
#post(model, file='tree.ps')
