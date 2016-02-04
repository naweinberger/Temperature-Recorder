library(ggplot2)
dat <- read.csv('temperature.data', stringsAsFactors = F, header = F)
names(dat) <- c("temp", "time")

ggplot(dat, aes(x=time, y=temp)) + ylim(20, 30) + stat_smooth()
