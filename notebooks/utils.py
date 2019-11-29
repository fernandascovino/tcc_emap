tp_etapa_ensino = { 25: 'Ensino Médio - 1ª Série',
                    26: 'Ensino Médio - 2ª Série',
                    27: 'Ensino Médio - 3ª Série',
                    28: 'Ensino Médio - 4ª Série',
                    29: 'Ensino Médio - Não Seriada',
                    30: 'Curso Técnico Integrado (Ensino Médio Integrado) 1ª Série',
                    31: 'Curso Técnico Integrado (Ensino Médio Integrado) 2ª Série',
                    32: 'Curso Técnico Integrado (Ensino Médio Integrado) 3ª Série',
                    33: 'Curso Técnico Integrado (Ensino Médio Integrado) 4ª Série',
                    34: 'Curso Técnico Integrado (Ensino Médio Integrado) Não Seriada',
                    35: 'Ensino Médio - Normal/Magistério 1ª Série',
                    36: 'Ensino Médio - Normal/Magistério 2ª Série',
                    37: 'Ensino Médio - Normal/Magistério 3ª Série',
                    38: 'Ensino Médio - Normal/Magistério 4ª Série',
                    39: 'Curso Técnico - Concomitante',
                    40: 'Curso Técnico - Subsequente',
                    0: 'Evadido'
                  }

# Indicadora de evasão
dic_evasao = {0: 'Não evadido', 1: 'Evadido'}

# Cor/Raça no Censo
dic_cor =  {0: "Não declarada",
            1: "Branca",
            2: "Preta",
            3: "Parda",
            4: "Amarela",
            5: "Indígena"}

# Indicadora de sexo adaptada (Censo: 1 - Homem / 2 - Mulher)
dic_sexo = {0: 'Homem', 1: 'Mulher'}

# Indicadora de distorção idade-serie
dic_distorcao = {0: 'Abaixo de 17 anos', 1: 'Acima de 17 anos'}

# Tipos de variáveis do Censo
dic_tipos = {'IN': 'Indicadora', 'TP': 'Categórica', 
             'ID': 'Identificadora', 'CO': 'Categórica',
             'NU': 'Numérica', 'NO': 'Nominal', 'DT': 'Data'}

# Textos para crosstab
dic_alunos = {'L1_IN_EVASAO': dic_evasao, 'L1_IN_SEXO': dic_sexo, 'L1_IN_DISTORCAO': dic_distorcao,
              'L1_IN_TRANSPORTE_PUBLICO': {0: 'Não utiliza', 1: 'Utiliza transporte público'},
              'L1_IN_MUNICIPIO_NASC': {'L1_IN_MUNICIPIO_NASC_RIO': 'Rio de Janeiro', 
                                       'L1_IN_MUNICIPIO_NASC_MET': 'Região metropolitana', 
                                       'L1_IN_MUNICIPIO_NASC_OUT': 'Outro município'},
              'L1_TP_COR_RACA': {0: 'Não declarada', 1: 'Branca', 2: 'Preta',
                                 3: 'Parda', 4: 'Amarela', 5: 'Indígena'},
              'L1_IN_DIF_MUN_ESCOLA_NASC': {0: 'Estuda no mesmo município', 1: 'Estuda num município diferente da residência'}}


dic_escolas = {'L1_IN_EVASAO': dic_evasao,
              'L2_IN_COMUNIDADE_1KM': {1: 'Comunidade num raio de 1KM', 0: 'Sem comunidade próxima'},
              'L2_IN_COMUNIDADE_5KM': {1: 'Comunidade num raio de 5KM', 0: 'Sem comunidade próxima'},
              'L2_IN_TIROTEIO_1KM': {1: 'Tiroteio num raio de 1KM', 0: 'Sem tiroteio registrado'},
              'L2_IN_TIROTEIO_5KM': {1: 'Tiroteio num raio de 5KM', 0: 'Sem tiroteio registrado'},
              'L2_IN_MUNICIPIO': {'L2_IN_MUNICIPIO_RIO': 'Rio de Janeiro', 
                                  'L2_IN_MUNICIPIO_MET': 'Região metropolitana', 
                                  'L2_IN_MUNICIPIO_OUT': 'Outro município'},
               'L2_IN_AGUA_CACIMBA': {1: 'Abastecimento de água (Cacimba/Cisterna)', 0: 'Outros'},
               'L2_IN_QUADRA_ESPORTES_DESCOBERTA': {1: 'Possui quadra descoberta', 0: 'Não possui'},
               'L2_IN_BANHEIRO_FORA_PREDIO': {1: 'Possui banheiro fora do prédio', 0: 'Não possui'},
               'L2_IN_AUDITORIO': {1: 'Possui auditório', 0: 'Não possui'},
               'L2_IN_EQUIP_VIDEOCASSETE': {1: 'Possui videocassete', 0: 'Não possui'},
               'L2_IN_EQUIP_PARABOLICA': {1: 'Possui antena parabólica', 0: 'Não possui'},
               'L2_IN_EQUIP_RETROPROJETOR': {1: 'Possui retroprojetor', 0: 'Não possui'},
               'L2_IN_EQUIP_IMPRESSORA': {1: 'Possui impressora', 0: 'Não possui'},
               'L2_IN_EQUIP_FAX': {1: 'Possui equipamento de fax', 0: 'Não possui'},
               'L2_IN_EJA': {1: 'Oferta de EJA', 0: 'Não possui'},
               'L2_IN_COMUM_FUND_AF': {1: 'Oferta de E.F.', 0: 'Não possui'},
#               'L2_IN_INSE': {'L2_IN_INSE_NIVEL1': 'INSE - Nível 1', 
#                              'L2_IN_INSE_NIVEL2': 'INSE - Nível 2', 
#                              'L2_IN_INSE_NIVEL3': 'INSE - Nível 3',
#                              'L2_IN_INSE_NIVEL4': 'INSE - Nível 4',
#                              'L2_IN_INSE_NIVEL5': 'INSE - Nível 5',
#                              'L2_IN_INSE_NIVEL6': 'INSE - Nível 6'},
              'L2_IN_ALOJAM_ALUNO': {1: 'Possui alojamento para aluno', 0: 'Não possui'},
              'L2_IN_LABORATORIO_CIENCIAS': {1: 'Possui laboratório de ciências', 0: 'Não possui'},
              'L2_IN_LABORATORIO_INFORMATICA': {1: 'Possui laboratório de informática', 0: 'Não possui'},
              'L2_IN_AREA_VERDE': {1: 'Possui área verde', 0: 'Não possui'},
              'L2_IN_ESGOTO_REDE_PUBLICA': {1: 'Esgoto sanitário – Rede pública', 0: 'Não possui / Outro'},
              'L2_IN_FINAL_SEMANA': {1: 'Escola abre aos finais de semana', 0: 'Não abre'}}
               