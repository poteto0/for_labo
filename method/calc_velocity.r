# 速度を計算
calc_velocity <- function(data, min){
  velocity = apply(combn(nrow(data),1), 2, function(i){
    diff_x <- data$X[i[1]] - data$X[i[1]-1]
    diff_y <- data$Y[i[1]] - data$Y[i[1]-1]
    distance <- sqrt(diff_x ^ 2 + diff_y ^ 2)
    return (distance/min)
  })
  return (velocity)
}
