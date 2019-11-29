# Modelos de regressão logística padrão e multinível

# ----------------------------------
# Reference materials and resources:
#   
# https://www.jstatsoft.org/article/view/v067i01/v67i01.pdf
# https://rdrr.io/cran/merTools/man/hsb.html
# https://cran.r-project.org/web/packages/lme4/lme4.pdf
# https://www.ssc.wisc.edu/sscc/pubs/MM/MM_TestEffects.html
# ----------------------------------

# ==== Pacotes intalados =====
# install.packages("rms", dependencies = TRUE)
# install.packages('htmlwidgets')
# install.packages("remotes")
# remotes::install_github("schmettow/bayr")

# ==== Importação dos pacotes, treino e teste ====
library(merTools)
library(lme4)
library(rms)
library(nlme)
# library(bayr)

df_train <- read.csv('../data/treated/modelo/df_train_strat.csv')
colnames(df_train)

df_test <- read.csv('../data/treated/modelo/df_test_strat.csv')
colnames(df_test)

# Criando tabela das probabilidades geradas no treino
df_pred_test <- data.frame(list('L1_ID'=df_test$L1_ID))
df_pred_test$true <- df_test$L1_IN_EVASAO

# Criando tabela das probabilidades geradas no teste
df_pred_train <- data.frame(list('L1_ID'=df_train$L1_ID))
df_pred_train$true <- df_train$L1_IN_EVASAO

# ==> Análise das variáveis de aluno: PYTHON
# ======= (nullmod1): Modelo nulo (grupo) =================
nullmod1 <- glmer(L1_IN_EVASAO~1+(1|L2_CO_ENTIDADE),  data=df_train, family=binomial(link="logit"))
summary(nullmod1)

# Probabilidades estimadas
df_pred_train$pred_null <- predict(nullmod1, newdata=df_train, type="response")
df_pred_train$logodd_null <- predict(nullmod1, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

df_pred_test$pred_null <- predict(nullmod1, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logodd_null <- predict(nullmod1, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# Coeficientes
write.csv(summary(nullmod1)$coefficients, file = '../data/output/mod_nulo_fcoeff.csv')
write.csv(VarCorr(nullmod1), file = '../data/output/mod_nulo_rcoeff.csv')

# Calculando partição da variância: https://github.com/jknowles/merTools/blob/master/R/helpers.R
between <- as.numeric(as.data.frame(VarCorr(nullmod1))$vcov)
within <- (pi^2)/3
ICC <- between / (within + between)
ICC

# Efeito escola: interceptos por grupo
nullmod1_ee <- ranef(nullmod1)
write.csv(nullmod1_ee, file = '../data/output/mod_nulo_efeito_escola.csv')

# ======= (nullmod_var): Variáveis de escola =====
nullmod3 <- glmer(L1_IN_EVASAO~1+(1|L2_CO_ENTIDADE) +
                    L2_IN_MUNICIPIO_RIO +
                    L2_IN_MUNICIPIO_MET +
                    L2_IN_LABORATORIO_CIENCIAS +
                    L2_NU_FUNCIONARIOS +
                    L2_NU_COMP_ALUNO +
                    L2_NU_INSE_VALOR +
                    L2_IN_COMUNIDADE_5KM ,
                  data=df_train, family=binomial(link="logit"))
summary(nullmod3)

# Probabilidades estimadas
df_pred_train$pred_null_var <- predict(nullmod3, newdata=df_train, type="response")
df_pred_train$logodd_null_var <- predict(nullmod3, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

df_pred_test$pred_null_var <- predict(nullmod3, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logodd_null_var <- predict(nullmod3, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# Coeficientes
write.csv(summary(nullmod3)$coefficients, file = '../data/output/mod_nulo_var_fcoeff.csv')
write.csv(VarCorr(nullmod3), file = '../data/output/mod_nulo_var_rcoeff.csv')

# Calculando partição da variância: https://github.com/jknowles/merTools/blob/master/R/helpers.R
between <- as.numeric(as.data.frame(VarCorr(nullmod3))$vcov)
within <- (pi^2)/3
ICC <- between / (within + between)
ICC

# ======= (modbase): Baseline (idade) ===============
formula = L1_IN_EVASAO ~ L1_NU_IDADE_REFERENCIA_NORM

# Modelo sem mixed effect:
modbase <- glm(formula, data=df_train, family=binomial(link="logit"))
summary(modbase, correlation=TRUE)
# confint(modbase)

# Coeficientes
write.csv(summary(modbase)$coefficients, file = '../data/output/mod_base_fcoeff.csv')

# Probabilidades estimadas
df_pred_train$pred_base <- predict(modbase, newdata=df_train, type="response")
df_pred_train$logood_base <- predict(modbase, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

# ==> Rodando no teste:
df_pred_test$pred_base <- predict(modbase, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logood_base <- predict(modbase, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# ======= (modl1): Logística padrão (aluno) ===============
# ==> Modelo l2: VARIÁVEIS DE ALUNO
formula = L1_IN_EVASAO ~ L1_IN_SEXO + 
  L1_IN_TRANSPORTE_PUBLICO + 
  L1_IN_MUNICIPIO_NASC_RIO + 
  L1_IN_MUNICIPIO_NASC_MET + 
  L1_IN_DIF_MUN_ESCOLA_NASC +
  L1_NU_IDADE_REFERENCIA_NORM
  # L1_IN_DISTORCAO

# Modelo com random intercept:
modl1 <- glm(formula, data=df_train, family=binomial(link="logit"))
summary(modl1, correlation = TRUE)
# confint(modl1)

# Probabilidades estimadas
df_pred_train$pred_l1 <- predict(modl1, newdata=df_train, type="response")
df_pred_train$logodd_l1 <- predict(modl1, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

# Coeficientes
write.csv(summary(modl1)$coefficients, file = '../data/output/mod_l1_fcoeff.csv')
write.csv(summary(modl1)$coefficients, file = '../data/output/mod_l1_rcoeff.csv')

# Rodando no teste:
df_pred_test$pred_l1 <- predict(modl1, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logodd_l1 <- predict(modl1, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# ======= (modl2): Intercepto aleatório ===============
# VARIÁVEIS DE ALUNO + AGRUPAMENTO ESCOLA + COMUNIDADE
formula = L1_IN_EVASAO ~ L1_IN_SEXO + 
  L1_IN_TRANSPORTE_PUBLICO + 
  L1_IN_MUNICIPIO_NASC_RIO + 
  L1_NU_IDADE_REFERENCIA_NORM + 
  L2_IN_MUNICIPIO_RIO +
  L2_IN_LABORATORIO_CIENCIAS +
  L2_NU_FUNCIONARIOS +
  L2_NU_COMP_ALUNO +
  L2_NU_INSE_VALOR +
  L2_IN_COMUNIDADE_5KM +
  (1 | L2_CO_ENTIDADE)
# L1_IN_DISTORCAO

# Modelo com random intercept:
modl2 <- glmer(formula, data=df_train, family=binomial(link="logit"),
               control=glmerControl(optimizer="bobyqa"))
summary(modl2)
# confint(modl2)

# Probabilidades estimadas
df_pred_train$pred_l2 <- predict(modl2, newdata=df_train, type="response")
df_pred_train$logodd_l2 <- predict(modl2, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

# Coeficientes
write.csv(summary(modl2)$coefficients, file = '../data/output/mod_l2_fcoeff.csv')
write.csv(VarCorr(modl2), file = '../data/output/mod_l2_rcoeff.csv')

# Rodando no teste:
df_pred_test$pred_l2 <- predict(modl2, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logodd_l2 <- predict(modl2, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# Efeito escola
modl2_ee <- ranef(modl2)
write.csv(modl2_ee, file = '../data/output/modl2_efeito_escola.csv')

# =============>> FALTA: Coeficiente aleatório ======
formula = L1_IN_EVASAO ~ L1_IN_SEXO + 
  L1_IN_TRANSPORTE_PUBLICO + 
  L1_IN_MUNICIPIO_NASC_RIO + 
  L1_NU_IDADE_REFERENCIA_NORM + 
  (1 + L1_IN_SEXO + 
     L1_IN_TRANSPORTE_PUBLICO +
     L1_IN_MUNICIPIO_NASC_RIO +
     L1_NU_IDADE_REFERENCIA_NORM | L2_CO_ENTIDADE)

# Modelo com random intercept:
modl3 <- glmer(formula, data=df_train, family=binomial(link="logit"),
               control=glmerControl(optimizer="bobyqa"))
summary(modl3)
# confint(modl2)

(L1_IN_TRANSPORTE_PUBLICO | L2_IN_COMUNIDADE_5KM:L2_CO_ENTIDADE) + 
  (L1_IN_MUNICIPIO_NASC_RIO | L2_IN_COMUNIDADE_5KM:L2_CO_ENTIDADE) + 

# Probabilidades estimadas
df_pred_train$pred_l3 <- predict(modl3, newdata=df_train, type="response")
df_pred_train$logodd_l3 <- predict(modl3, newdata=df_train, type="link")
write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')

# Coeficientes
write.csv(summary(modl3)$coefficients, file = '../data/output/mod_l3_fcoeff.csv')
write.csv(VarCorr(modl3), file = '../data/output/mod_l3_rcoeff.csv')

# Rodando no teste:
df_pred_test$pred_l3 <- predict(modl2, newdata=df_test, type="response", allow.new.levels = TRUE)
df_pred_test$logodd_l3 <- predict(modl2, newdata=df_test, type="link", allow.new.levels = TRUE)
write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')

# ======= (todos) Fit e comparação dos modelos ====
# Modelo nulo sem agrupamento (para cálculo do R-square)
nullmod <- glm(L1_IN_EVASAO~1, data=df_train, family=binomial(link="logit"))

# AIC
aicModels <- c(nullmod$aic, AIC(logLik(nullmod1)), modbase$aic, modl1$aic, AIC(logLik(modl2)), AIC(logLik(modl3)))
aicModels

models <- list(nullmod1, modl1, modl2, modl3, test)
# Deviance residuals
data.frame(models = c('nullmod1', 'modl1', 'modl2', 'modl3', 'idade*comun'),
           deviance = round(unlist(lapply(models, deviance)),2), 
           df       = unlist(lapply(models,df.residual)))

# ==== Salvando os resultados =======
# write.csv(df_pred_train, file = '../data/output/df_pred_train_str_lmer.csv')
# write.csv(df_pred_test, file = '../data/output/df_pred_test_str_lmer.csv')


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


# df_train_strat <- read.csv('../data/treated/modelo/df_train_strat.csv')
# colnames(df_train)