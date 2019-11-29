# install.packages("rms", dependencies = TRUE)
# install.packages('htmlwidgets')
# install.packages("remotes")
# remotes::install_github("schmettow/bayr")

# install.packages('ResourceSelection')
# library(ResourceSelection)
# hoslem.test(df_train$L1_IN_EVASAO, fitted(modl1), g=10)
# hoslem.test(df_train$L1_IN_EVASAO, fitted(modl2), g=10)
# hoslem.test(df_train$L1_IN_EVASAO, fitted(modl3), g=10)

# R-square
# models <- list(nullmod1, modl1, modl2, modl3)
# r2Models <- c()
# for (model in models){
#   r2 <- 1 - logLik(model)/logLik(nullmod1)
#   r2Models<- append(r2Models, r2)
# }
# r2Models

# Another way
# ll.null <- nullmod$null.deviance/-2
# ll.proposed <- modl2$deviance/-2
# (ll.null - ll.proposed)/ll.null

# Check for the p-value od the model
# 1 - pchisq(91690 - 82814, 66139 - 66133)

# Verificando resultado: ICC(outcome="L1_IN_EVASAO",group="L2_CO_ENTIDADE_NORM",data=df)
# plot(df_train$L2_CO_ENTIDADE, resid(nullmod1), ylab="Resíduos", xlab="Escolas") 
# abline(0, 0)

# Extract model results
# library(broom)
# model.data <- augment(nullmod1) %>% mutate(index = 1:n()) 
# ggplot(model.data, aes(index, .resid)) + 
#   geom_point(aes(color = L1_IN_EVASAO), alpha = .5) +
#   theme_bw()

# Extract model results
# library(broom)
# model.data <- augment(modl1) %>% mutate(index = 1:n()) 
# ggplot(model.data, aes(index, .resid)) + 
#   geom_point(aes(color = L1_IN_EVASAO), alpha = .5) +
#   theme_bw()