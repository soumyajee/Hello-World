a <- c(1,2,3,100)
mean(a)
median(a)
install.packages("modeest")
library(modeest)
mfv(a)
scores <- c(1,2,2,2,3,4,4,4,5,6)
mfv(scores)

# Assignment Operator alt - or = 
#x = read.csv("E:\\Datasets\\Datasets_BA 2\\mba.csv")
mba <- read.csv("E:/Datasets/Datasets_BA 2/mba.csv")
# Path needs to be modified to either / or \\
# mba <- read.csv(file.choose())
#Measures of Central Tendency
View(mba)
mean(mba$gmat)
median(mba$gmat)
mfv(mba$gmat)


summary(mba)

attach(mba)
mean(gmat)
median(gmat)

detach(mba)
mean(gmat)
str(mba)


#Measures of Dispersion
var(mba$gmat)
sd(mba$gmat)
range(mba$gmat)
rangevalue <- function(x){max(x)-min(x)}
rangevalue(mba$gmat)

#Measures of skewness
install.packages("moments")
library(moments)

#Measures of skewness
skewness(mba$workex)
hist(mba$gmat)
hist(mba$worke)


#Measures of Kurtosis 
kurtosis(mba$gmat)
kurtosis(mba$workex)

#Graphical R,epresentation
#Boxplot
#Histogram
#Barplot

x = boxplot(mba$gmat)
boxplot(mba$gmat)$out
summary(mba$gmat)
x$out
hist(mba$gmat)
hist(mba$workex)
?hist
?mean
?median
barplot(mba$gmat)


library(moments)
skewness(mba$gmat)
data = c(15,24,38,54)
names = c("one","two","three","four")
pie(data,labels = names,radius =1 )


str(mba)
x = c(1,1,1,2,1,2,1,2,1,2,1,2,1,2,1)
y = as.factor(x)
str(y)
mba$datasrno <- as.numeric(mba$datasrno)
class(mba$datasrno)

summary(mba)
?describe

pnorm(740,711,29)-pnorm(697,711,29)

# to calculate Z score
qnorm(0.950)#90%
qnorm(0.975)#95%
qnorm(0.995)

#to calculate t score
qt(0.950,139)#0.90%

#qqplot
qqnorm(mba$gmat)
qqline(mba$gmat)

# Standardisation
attach(mba)
summary(mba)
View(mba)
standard_values = scale(mba)
summary(standard_values)
summary(mba)

normalize = function(x){
  return ((x-min(x))/(max(x)-min(x)))
}

normalized_data = as.data.frame(lapply(mba,normalize))
summary(normalized_data)
# transformations of data

qqnorm(mba$workex)
qqline(mba$workex)

x = log(mba$workex)
qqnorm(x)
qqline(x)

hist(mba$workex)
hist(x)


df <- read.table(text =
                   "x y
4     71.88
20    65.80
40    63.92
60    63.47", header = T);

library(ggplot2)
ggplot(df, aes(as.factor(y), x)) + 
  geom_point() + 
  labs(y = "Percentage correct", x = "Categorical variable")
?ggplot
# geom_jitter
plot(df$x,df$y)
library(ggplot2)
ggplot(df, aes(as.factor(y), x)) + 
  geom_line() + 
  labs(y = "Percentage correct", x = "Categorical variable")



















