data_sample <- read.csv("./uchigawa.csv", header=TRUE)

add_step = data.frame(data_sample$step * 5) #step -> minutes
names(add_step) <- c("min") # add title as min
scaled_sample = apply(data_sample[2:3], 2, function(x, y){ return (x/1.89) }) # scaled
scaled_sample <- cbind(add_step, scaled_sample)

# 速度を計算
source("./method/calc_velocity.R")
source("./method/moving_average.R")

velocity <- calc_velocity(scaled_sample, 5)

velocity <- moving_average(velocity, 5)

plot(x = scaled_sample$min, y = velocity)
