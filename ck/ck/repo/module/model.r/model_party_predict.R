#
# Collective Knowledge (Predictive modeling using R)
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin
#

# model package
library(party)

# get arguments
args <- commandArgs(trailingOnly = TRUE)

fmodel=args[1]
finput=args[2]
foutput=args[3]

# get data
data_set = read.csv(finput, header=FALSE, sep=";")

# variables
x=data.frame(data_set)

# loading saved prediction model
load(fmodel)

# Predicting
p=predict(model, data=x)

# Saving results
write.csv(p, file=foutput)
