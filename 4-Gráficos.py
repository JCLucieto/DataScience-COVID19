#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 4-Graficos.py                            #
# - Constroi e Apresenta Gráficos                 #
#=================================================#

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


# Variáveis Globais

estatisticas = None
df_dados = None
dados_graficos = None


#----------------------------------------------------------#
# DEFINIÇÃO DAS FUNÇÕES                                    #
#----------------------------------------------------------#

# Configurar Streamlit
def configurar_st():
    # Formato da Tela
    st.set_page_config(layout='wide', page_title='Ayit Digital - Covid-19 - PR')
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


# Preparar Grafico de Idade
def preparar_grafico_idade():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de IDADE
    dados_graficos = df_dados.groupby(['IDADE (anos)'], observed=True).size().reset_index(name='FREQUENCIA')


# Exibir o Gráfico de Idade
def exibir__grafico_idade():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras
    fig = px.bar(dados_graficos, 
                x='IDADE (anos)', 
                y='FREQUENCIA', 
                color='IDADE (anos)', 
                title='Casos de COVID-19 por Idade',
                labels={'FREQUENCIA': 'Número de Casos', 'IDADE (anos)': 'Idade'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Idades', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Preparar Grafico de Faixa de Idade
def preparar_grafico_faixa_idade():
    global df_dados, dados_graficos
    # Contar a frequência de combinações FAIXA DE IDADE
    dados_graficos = df_dados.groupby(['FAIXA'], observed=True).size().reset_index(name='FREQUENCIA')


# Exibir o Gráfico de Faixa de Idade
def exibir_grafico_faixa_idade():
    global df_dados, dados_graficos
    # Criar o gráfico de barras
    fig = px.bar(dados_graficos, 
                x='FAIXA', 
                y='FREQUENCIA', 
                color='FAIXA', 
                title='Casos de COVID-19 por Faixa de Idade',
                labels={'FREQUENCIA': 'Número de Casos', 'FAIXA DE IDADE': 'Faixa de Idade'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Faixas de Idade', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Preparar Grafico de Sexo
def preparar_grafico_sexo():
    global df_dados, dados_graficos
    # Contar a frequência por SEXO
    dados_graficos = df_dados.groupby(['SEXO'], observed=True).size().reset_index(name='FREQUENCIA')


# Exibir o Gráfico de Sexo
def exibir_grafico_sexo():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='SEXO', 
                y='FREQUENCIA', 
                color='SEXO', 
                title='Casos de COVID-19 por Sexo',
                labels={'FREQUENCIA': 'Número de Casos', 'SEXO': 'Sexo'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Sexo', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Preparar Grafico de Bairro
def preparar_grafico_bairro():
    global df_dados, dados_graficos
    # Contar a frequência por BAIRRO
    dados_graficos = df_dados.groupby(['BAIRRO'], observed=True).size().reset_index(name='FREQUENCIA')


# Exibir o Gráfico de Bairro
def exibir_grafico_bairro():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='BAIRRO', 
                y='FREQUENCIA', 
                color='BAIRRO', 
                title='Casos de COVID-19 por Bairro',
                labels={'FREQUENCIA': 'Número de Casos', 'BAIRRO': 'Bairro'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Bairro', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Preparar Grafico de Encerramento
def preparar_grafico_encerramento():
    global df_dados, dados_graficos
    # Contar a frequência por BAIRRO
    dados_graficos = df_dados.groupby(['ENCERRAMENTO'], observed=True).size().reset_index(name='FREQUENCIA')


# Exibir o Gráfico de Encerramento
def exibir_grafico_encerramento():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='ENCERRAMENTO', 
                y='FREQUENCIA', 
                color='ENCERRAMENTO', 
                title='Casos de COVID-19 por Encerramento',
                labels={'FREQUENCIA': 'Número de Casos', 'ENCERRAMENTO': 'Encerramento'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Encerramento', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara gráfico Idade e Bairro
def preparar_grafico_idade_bairro():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de IDADE E SEXO
    dados_graficos = (df_dados.groupby(['IDADE (anos)', 'BAIRRO'], observed=True)
                      .size()
                      .reset_index(name='FREQUENCIA')
                      .sort_values(by=['BAIRRO', 'IDADE (anos)'], ascending=[False, True]))
   

# Exibe Gráfico Idade e Bairro    
def exibir_grafico_idade_bairro():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras
    fig = px.bar(dados_graficos, 
                x='IDADE (anos)', 
                y='BAIRRO', 
                color='BAIRRO', 
                title='Casos de COVID-19 por Idade e Bairro',
                labels={'FREQUENCIA': 'Número de Casos', 'IDADE (anos)': 'Idade'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(
        xaxis_title='Idades e Número de Casos',
        yaxis_title='Bairros',
        bargap=0.1,
        height=3000,  # Aumenta a altura do gráfico
        yaxis=dict(
            automargin=True,  # Adiciona margens automáticas
            tickmode='linear',
            tick0=5
        )
    )
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara gráfico Idade e Encerramento
def preparar_grafico_idade_encerramento():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de IDADE E ENCERRAMENTO
    dados_graficos = (df_dados.groupby(['IDADE (anos)', 'ENCERRAMENTO'], observed=True)
                      .size()
                      .reset_index(name='FREQUENCIA')
                      .sort_values(by='IDADE (anos)', ascending=False))

# Exibe Gráfico Idade e Encerramento     
def exibir__grafico_idade_encerramento():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras
    fig = px.bar(dados_graficos, 
                x='ENCERRAMENTO', 
                y='IDADE (anos)', 
                color='ENCERRAMENTO', 
                title='Casos de COVID-19 por Idade e Encerramento',
                labels={'FREQUENCIA': 'Número de Casos', 'IDADE (anos)': 'Idade'},
                text='FREQUENCIA')
    # Ajustar o layout
    fig.update_layout(
        xaxis_title='Encerramento',
        yaxis_title='Idades e Número de Casos',
        height=1000
    )
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara gráfico Faixa de Idade e Bairro
def preparar_grafico_faixa_idade_bairro():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de FAIXA IDADE E SEXO
    dados_graficos = (df_dados.groupby(['FAIXA', 'BAIRRO'], observed=True)
                      .size()
                      .reset_index(name='FREQUENCIA')
                      .sort_values(by=['BAIRRO', 'FAIXA'], ascending=[True, True]))
    # Garantir que todos os bairros sejam exibidos com frequência zero
    todos_bairros = df_dados['BAIRRO'].unique()
    todas_faixas = df_dados['FAIXA'].unique()
    # Criar um DataFrame com todas as combinações possíveis
    combinacoes = pd.MultiIndex.from_product([todas_faixas, todos_bairros], names=['FAIXA', 'BAIRRO'])
    dados_graficos = dados_graficos.set_index(['FAIXA', 'BAIRRO']).reindex(combinacoes, fill_value=0).reset_index().sort_values(by=['BAIRRO', 'FAIXA'], ascending=[True, True])


# Exibe Gráfico Faixa de Idade e Bairro    
def exibir_grafico_faixa_idade_bairro():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras
    fig = px.bar(dados_graficos, 
                x='FAIXA', 
                y='BAIRRO', 
                color='FAIXA', 
                title='Casos de COVID-19 por Faixa de Idade e Bairro',
                labels={'FREQUENCIA': 'Número de Casos', 'FAIXA': 'Faixa de Idade'},
                text='FREQUENCIA')
                
    # Ajustar o layout
    fig.update_layout(
        xaxis_title='Faixas de Idade e Número de Casos',
        yaxis_title='Bairros',
        bargap=0.05,
        height=len(dados_graficos['BAIRRO'].unique()) * 20,  # Altura dinâmica
        yaxis=dict(
            tickangle=0,
        ),
        xaxis=dict(
            tickangle=90,
            tickmode='linear'
        )
    )

    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara Gráfico Faixa de Idade e Sexo
def preparar_grafico_faixa_idade_sexo():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de SEXO e FAIXA DE IDADE
    dados_graficos = df_dados.groupby(['FAIXA', 'SEXO'], observed=True).size().reset_index(name='FREQUENCIA')
    

# Exibe Gráfico Faixa de Idade e Sexo
def exibir_grafico_faixa_idade_sexo():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='FAIXA', 
                y='FREQUENCIA', 
                color='SEXO', 
                title='Casos de COVID-19 por Faixa de Idade e Sexo',
                labels={'FREQUENCIA': 'Número de Casos', 'FAIXA DE IDADE': 'Faixa de Idade'},
                text='FREQUENCIA',
                barmode='group')  # Barras paralelas
    # Ajustar o layout
    fig.update_layout(xaxis_title='Faixa de Idade', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara Gráfico Faixa de Idade e Encerramento
def preparar_grafico_faixa_idade_encerramento():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de FAIXA DE IDADE e ENCERRAMENTO
    dados_graficos = df_dados.groupby(['FAIXA', 'ENCERRAMENTO'], observed=True).size().reset_index(name='FREQUENCIA')
    

# Exibe Gráfico Faixa de Idade e Encerramento
def exibir_grafico_faixa_idade_encerramento():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='FAIXA', 
                y='FREQUENCIA', 
                color='ENCERRAMENTO', 
                title='Casos de COVID-19 por Faixa de Idade e Encerramento',
                labels={'FREQUENCIA': 'Número de Casos', 'FAIXA DE IDADE': 'Faixa de Idade'},
                text='FREQUENCIA',
                barmode='group')  # Barras paralelas
    # Ajustar o layout
    fig.update_layout(xaxis_title='Faixa de Idade e Encerramento', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Preparar Grafico de Evolução
def preparar_grafico_evolucao():
    global df_dados, dados_graficos
    # Contar o número de casos por dia
    dados_graficos = df_dados.groupby('DATA INCLUSÃO/ NOTIFICAÇÃO').size().reset_index(name='Número de Casos')


# Exibir o Gráfico de Evolução
def exibir_grafico_evolucao():
    global dados_graficos

    # Criar o gráfico de linhas
    fig = px.bar(dados_graficos, 
                x='DATA INCLUSÃO/ NOTIFICAÇÃO', 
                y='Número de Casos', 
                title='Casos de COVID-19 no Período',
                labels={'DATA INCLUSÃO/ NOTIFICAÇÃO': 'Data', 'Número de Casos': 'Número de Casos'},
                text='DATA INCLUSÃO/ NOTIFICAÇÃO')
    # Ajustar o layout
    fig.update_layout(xaxis_title='Data', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara gráfico Idade e Sexo
def preparar_grafico_idade_sexo():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de IDADE E SEXO
    dados_graficos = df_dados.groupby(['IDADE (anos)', 'SEXO'], observed=True).size().reset_index(name='FREQUENCIA')
    
# Exibir gráfico Idade e Sexo
def exibir__grafico_idade_sexo():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras Paralelas
    fig = px.bar(dados_graficos, 
                x='IDADE (anos)', 
                y='FREQUENCIA', 
                color='SEXO', 
                title='Casos de COVID-19 por Idade e Sexo',
                labels={'FREQUENCIA': 'Número de Casos', 'IDADE (anos)': 'Idade'},
                text='FREQUENCIA',
                barmode='group')  # Barras paralelas
    # Ajustar o layout
    fig.update_layout(xaxis_title='Idade', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara gráfico Sexo e Bairro
def preparar_grafico_sexo_bairro():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de SEXO e BAIRRO
    dados_graficos = (df_dados.groupby(['SEXO', 'BAIRRO'], observed=True)
                      .size()
                      .reset_index(name='FREQUENCIA')
                      .sort_values(by='BAIRRO', ascending=True))
   

# Exibe Gráfico Sexo e Bairro    
def exibir_grafico_sexo_bairro():
    global df_dados, dados_graficos
    # Cria Gráfico de Barras
    fig = px.bar(dados_graficos, 
                  y='BAIRRO',  # Bairros no eixo Y
                  x='FREQUENCIA',  # Frequência no eixo X
                  color='SEXO', 
                  title='Casos de COVID-19 por Sexo e Bairro',
                  labels={'FREQUENCIA': 'Número de Casos', 'SEXO': 'Sexo'},
                  text='FREQUENCIA',
                  barmode='stack')

    # Ajustar o layout
    fig.update_layout(
        yaxis_title='Bairros',  # Atualizado
        xaxis_title='Número de Casos',  # Atualizado
        bargap=0.6,
        height=2800,  # Aumenta a altura do gráfico
        width=800,  # Aumenta a largura do gráfico
        yaxis=dict(
            tickmode='linear',  # Define o modo de tick para linear
            tickangle=0,  # Rotaciona os rótulos dos bairros
            automargin=True  # Adiciona margens automáticas
        ),
        xaxis=dict(
            automargin=True  # Para que os rótulos do eixo X não sejam cortados
        )
    )

    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig, use_container_width=True)  # Ajusta o gráfico para usar a largura do container


# Prepara Gráfico Sexo e Encerramento
def preparar_grafico_sexo_encerramento():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de SEXO e ENCERRAMENTO
    dados_graficos = df_dados.groupby(['SEXO', 'ENCERRAMENTO'], observed=True).size().reset_index(name='FREQUENCIA')
    

# Exibe Gráfico Sexo e Encerramento
def exibir_grafico_sexo_encerramento():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='SEXO', 
                y='FREQUENCIA', 
                color='ENCERRAMENTO', 
                title='Casos de COVID-19 por Sexo e Encerramento',
                labels={'FREQUENCIA': 'Número de Casos', 'SEXO': 'Sexo'},
                text='FREQUENCIA',
                barmode='group')  # Barras paralelas
    # Ajustar o layout
    fig.update_layout(xaxis_title='Sexo e Encerramento', yaxis_title='Número de Casos')
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Prepara Gráfico Bairro e Encerramento
def preparar_grafico_bairro_encerramento():
    global df_dados, dados_graficos
    # Contar a frequência de combinações de BAIRRO e ENCERRAMENTO
    dados_graficos = df_dados.groupby(['BAIRRO', 'ENCERRAMENTO'], observed=True).size().reset_index(name='FREQUENCIA')
    

# Exibe Gráfico Bairro e Encerramento
def exibir_grafico_bairro_encerramento():
    global df_dados, dados_graficos
    # Criar o gráfico de barras paralelas
    fig = px.bar(dados_graficos, 
                x='BAIRRO', 
                y='FREQUENCIA', 
                color='ENCERRAMENTO', 
                title='Casos de COVID-19 por Bairro e Encerramento',
                labels={'FREQUENCIA': 'Número de Casos', 'BAIRRO': 'Bairro'},
                text='FREQUENCIA',
                barmode='group')  # Barras paralelas
    # Ajustar o layout
    fig.update_layout(
        xaxis_title='Bairro e Encerramento',
        yaxis_title='Número de Casos',
        xaxis=dict(
            tickangle=90,
            tickmode='linear')
    )
    # Configurar a aplicação Streamlit
    st.title("Gráfico de Casos de COVID-19")
    st.plotly_chart(fig)


# Carregar Dados da Sessão
def carregar_dados_sessao():
    global df_dados
    if 'df' not in st.session_state:
      st.session_state.page = 'COVID-19'
      st.switch_page('COVID-19.py')
    else:
        df_dados = st.session_state.df


# Executa as Funções correspondentes ao botão clicado
def executar():

    global opcao_escolhida

    exibido = False
    opcao_escolhida = ''
    
    # Montagem e Exibição dos Botões
  
    st.sidebar.markdown ('**SELECIONE UMA INFORMAÇÃO**')
    
    if st.sidebar.button('Idade',  use_container_width=True):
        preparar_grafico_idade()
        exibir__grafico_idade()
        exibido = True

    if st.sidebar.button('Faixa Idade',  use_container_width=True):
        preparar_grafico_faixa_idade()
        exibir_grafico_faixa_idade()
        exibido = True
        
    if st.sidebar.button('Sexo',  use_container_width=True):
        preparar_grafico_sexo()
        exibir_grafico_sexo()
        exibido = True
        
    if st.sidebar.button('Bairro',  use_container_width=True):
        preparar_grafico_bairro()
        exibir_grafico_bairro()
        exibido = True

    if st.sidebar.button('Encerramento',  use_container_width=True):
        preparar_grafico_encerramento()
        exibir_grafico_encerramento()
        exibido = True

    if st.sidebar.button('Idade e Sexo',  use_container_width=True):
        preparar_grafico_idade_sexo()
        exibir__grafico_idade_sexo()
        exibido = True

    if st.sidebar.button('Idade e Bairro',  use_container_width=True):
        preparar_grafico_idade_bairro()
        exibir_grafico_idade_bairro()
        exibido = True

    if st.sidebar.button('Idade e Encerramento',  use_container_width=True):
        preparar_grafico_idade_encerramento()
        exibir__grafico_idade_encerramento()
        exibido = True
                   
    if st.sidebar.button('Faixa Idade e Sexo',  use_container_width=True):
        preparar_grafico_faixa_idade_sexo()
        exibir_grafico_faixa_idade_sexo()
        exibido = True
        
    if st.sidebar.button('Faixa de Idade e Bairro',  use_container_width=True):
        preparar_grafico_faixa_idade_bairro()
        exibir_grafico_faixa_idade_bairro()
        exibido = True

    if st.sidebar.button('Faixa Idade e Encerramento',  use_container_width=True):
        preparar_grafico_faixa_idade_encerramento()
        exibir_grafico_faixa_idade_encerramento()
        exibido = True

    if st.sidebar.button('Sexo e Bairro',  use_container_width=True):
        preparar_grafico_sexo_bairro()
        exibir_grafico_sexo_bairro()
        exibido = True

    if st.sidebar.button('Sexo e Encerramento',  use_container_width=True):
        preparar_grafico_sexo_encerramento()
        exibir_grafico_sexo_encerramento()
        exibido = True

    if st.sidebar.button('Bairro e Encerramento',  use_container_width=True):
        preparar_grafico_bairro_encerramento()
        exibir_grafico_bairro_encerramento()
        exibido = True
        
    if st.sidebar.button('Evolução no Tempo',  use_container_width=True):
        preparar_grafico_evolucao()
        exibir_grafico_evolucao()
        exibido = True
    else:
        if not exibido:
            st.write ('Esta página fornece os gráficos das principais informações.')
            st.write ('Selecione através dos botões laterais a informação para construção dos gráficos.')
      
#=====================================#
#        Programa Principal           #
#=====================================#

def main():

    configurar_st()
    exibir_logotipo()
    carregar_dados_sessao()
    executar()
        
if __name__ == '__main__':
    main()
