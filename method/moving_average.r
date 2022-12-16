# 移動平均法
moving_average <- function(x, n){
  filter(x, rep(1,n)) / n # c(1,1,1,....1)のベクトルフィルター(n個分)
}
