from paths import RAW_PATH, TREAT_PATH
import os
import pandas as pd

def unique_id(df):
    
    # Código único por pessoa
    v = df['ID'].value_counts()
    print('CPFs que aparecem mais de uma vez: ', len(v[v > 1]))

    # Separando duplicados
    duplicate = df[df['ID'].isin(v[v > 1].index)]
    df = df[df['ID'].isin(v[v > 1].index) == False]
    
    return df, duplicate

def clean_aluno(df_name):
    
    df = pd.read_csv(RAW_PATH / 'censo' / df_name)
    
    # Criptografa os CPFs
    df['ID'] = df['CO_PESSOA_FISICA'].apply(hash)
    df = df.drop('CO_PESSOA_FISICA', axis=1)
    
    # Checa duplicados
    df, df_duplicate = unique_id(df)
    
    # Salva as bases tratadas
    clean_name = 'cleaned_'+str(df_name)
    duplicate_name = df_name[:-4]+'duplicado.csv'
    
    df.to_csv(TREAT_PATH / 'censo' / clean_name)
    df_duplicate.to_csv(TREAT_PATH / 'censo' / duplicate_name)
    
dfs = list(filter(lambda x: x.endswith('.csv'), os.listdir(RAW_PATH / 'censo')))

for df in dfs:
    if 'matricula' in df:
        clean_df(df)