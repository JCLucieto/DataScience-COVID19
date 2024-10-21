#===================================================#
# COVID-19 - PARANÁ                                 #
#===================================================#
# Utilização de Dados sobre a Covid-19 em Curitiba  #
# Estado do Paraná para estudos e desenvolvimento   #
# dos conhecimentos sobre fundamentos, técnicas e   #
# ferramentas de tratamento (Pandas) e apresentação #
# (Streamlit) de dados que são utilizadas em        #
# trabalhos e pesquisas da área de Data Science.    #
#===================================================#
# Autor : Julio Cesar de Campos Lucieto             #
# Data  : Outubro 2024                              #
#===================================================#

import chardet
import pandas as pd
import streamlit as st

# Variáveis Globais
encoding = None
df_dados = None

#----------------------------------------------------------#
# DEFINIÇÃO DAS FUNÇÕES                                    #
#----------------------------------------------------------#

# Configurar Streamlit
def configurar_st():
    # Formato da Tela
    st.set_page_config(layout='wide', page_title='Ayit Digital - Covid-19 - Curitiba - PR')
    # Link da Fonte Inter
    st.markdown(
        ''' <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
            body {font-family: 'Inter', sans-serif;}
            </style>
        ''',
        unsafe_allow_html=True
    )


# Exibir o Logotipo Ayit
def exibir_logotipo():
    st.image('logoayit.png')


# Exibir o Título da Página
def exibir_titulo():
     st.title('COVID-19 - PR')  


# Exibe as Informações do Projeto
def exibir_info_projeto():
  st.markdown(
      '''
      <p style="color:black;">
        <strong>Projeto desenvolvido como parte dos estudos de Data Science.</strong>
      </p>
      <span style="color:blue;">
        Utilização de dados sobre a Covid-19 na cidade de Curitiba, capital do estado do Paraná, 
        para estudos e desenvolvimento de conhecimentos sobre fundamentos, técnicas e ferramentas 
        de tratamento (Pandas) e apresentação de dados (Streamlit), que são utilizadas em 
        trabalhos e pesquisas na área de Data Science."
      </span>
      <br><br>
      <p style="color:black;">
        <strong>Fonte das Informações</strong>
      </p>
      <p style="color:blue;"> Governo do Estado do Paraná - Secretaria da Saúde </p>
      <p style="color:black;">
        <strong>Autor do Projeto</strong>
      </p>
      <p style="color:blue;"> Julio Cesar de Campos Lucieto</p>
      <p style="color:black;">
        <strong>Local e Data</strong>
      </p>
      <p style="color:blue;"> São Paulo - Outubro de 2024</p>        
      ''', unsafe_allow_html=True
  )


# Verificar Encoding do arquivo .CSV
def verificar_encoding():
    global encoding
    try:
        with open('PR-COVID-19.csv', 'rb') as file:
            raw_data = file.read(2000)  # Lê os primeiros 2000 bytes
            result = chardet.detect(raw_data)
            encoding = result['encoding']
    except FileNotFoundError:
        st.error(body='Arquivo de Dados Não Encontrado!')
        st.stop()
    except Exception as erro:
        st.error(body='Erro Na Verificação do Encoding do Arqivo!')
        st.write(erro)
        st.stop()


# Importar a base de Dados (Arquivo vendas.json)
def importar_dados():
    global df_dados
    try:
        df_dados = pd.read_csv('PR-COVID-19.csv', delimiter=';', index_col=None, encoding=encoding)
    except FileNotFoundError as erro:
        st.error(body='Arquivo de Dados Não Encontrado!')
        st.stop()
    except Exception as erro:
        st.error(body='Erro Na Leitura do Arquivo!')
        st.write(erro)
        st.stop()


# Retirar coluna CLASSIFICAÇÃO FINAL
def retirar_coluna():
    global df_dados
    df_dados = df_dados.drop(columns=['CLASSIFICAÇÃO FINAL'])


# Unificar Valores Sexo
def unificar_valores_sexo():
    global df_dados
    df_dados['SEXO'] = df_dados['SEXO'].replace('f', 'F')
    df_dados['SEXO'] = df_dados['SEXO'].replace('m', 'M')


# Unificar Valores Internado
def unificar_valores_internado():
    global df_dados
    df_dados['INTERNADO (SIM/NÃO)'] = df_dados['INTERNADO (SIM/NÃO)'].replace('Não', 'NÃO')
    df_dados['INTERNADO (SIM/NÃO)'] = df_dados['INTERNADO (SIM/NÃO)'].replace('Sim', 'SIM')
    df_dados['INTERNADO (SIM/NÃO)'] = df_dados['INTERNADO (SIM/NÃO)'].replace('sIM', 'SIM')


# Unificar Valores Bairro e Distrito Residencia
def unificar_valores_bairro_distrito():
    global df_dados
    df_dados['BAIRRO'] = df_dados['BAIRRO'].fillna('DESCONHECIDO')
    df_dados['DISTRITO RESIDÊNCIA'] = df_dados['DISTRITO RESIDÊNCIA'].fillna('DS??')


# Preencher Data Obito quando nula
def preencher_data_obito():
    global df_dados
    df_dados['DATA ÓBITO'] = df_dados['DATA ÓBITO'].fillna('00/00/0000')

# Criar Coluna com as Faixas de Idade
def criar_faixas_idade():
    # Definindo as faixas de idade
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]  # limites das faixas
    labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100','101-110']  # rótulos das faixas
    # Criando a coluna de faixas
    df_dados['FAIXA'] = pd.cut(df_dados['IDADE (anos)'], bins=bins, labels=labels, right=False)


# Altera o Formato das Colunas de Data
def alterar_colunas_datas():
    df_dados['DATA INCLUSÃO/ NOTIFICAÇÃO'] = pd.to_datetime(df_dados['DATA INCLUSÃO/ NOTIFICAÇÃO'], format = '%d/%m/%Y', errors='coerce')
    df_dados['DATA COLETA EXAME'] = pd.to_datetime(df_dados['DATA COLETA EXAME'], format = '%d/%m/%Y', errors='coerce')
    df_dados['DATA ÓBITO'] = pd.to_datetime(df_dados['DATA ÓBITO'], format = '%d/%m/%Y', errors='coerce')


# Cria colunas com Datas Formatadas DD/MM/AAAA
def criar_datas_formatadas():
    df_dados['DATA_INCLUSAO_FORMATADA'] = df_dados['DATA INCLUSÃO/ NOTIFICAÇÃO'].dt.strftime('%d/%m/%Y')
    df_dados['DATA_COLETA_FORMATADA'] = df_dados['DATA COLETA EXAME'].dt.strftime('%d/%m/%Y')
    df_dados['DATA_OBITO_FORMATADA'] = df_dados['DATA ÓBITO'].dt.strftime('%d/%m/%Y')



#----------------------------------------------------------#
# FUNÇÃO PRINCIPAL                                         #
#----------------------------------------------------------#
def main():

    configurar_st()
    exibir_logotipo()
    exibir_titulo()
    with st.spinner('AGUARDE... - Estamos Carregando e Preparando os Dados !',):
        exibir_info_projeto()
        verificar_encoding()
        importar_dados()
        unificar_valores_sexo()
        unificar_valores_internado()
        unificar_valores_bairro_distrito()
        preencher_data_obito()
        criar_faixas_idade()
        alterar_colunas_datas()
        criar_datas_formatadas()
    st.success('Dados Carregados e Preparados Com Sucesso!')
        
    if 'df' not in st.session_state:
      st.session_state.df = df_dados
    

if __name__ == '__main__':
    main()
