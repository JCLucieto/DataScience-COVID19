#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 5-Mapa da COVID-19                       #
# - Apresenta Mapa dos Bairros e Casos            #
#=================================================#


import pandas as pd
import streamlit as st
import plotly.express as px


# Variáveis Globais
df_geo_bairros = None
df_ocorrencias = None
df_obitos = None
df_junto1 = None
df_final = None

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


# Exibir o Título da Página
def exibir_titulo():
    st.title('O Mapa da COVID-19 em Curitiba')


# Recebe um Inteiro e Formata Uma String
# separada por pontos de milhar, milhao, bihao
def formata_qtde(qtde):
    if qtde >= 1000000000:
        return f"{qtde:,.0f}".replace(',', '.').replace('.', ',', 1)
    elif qtde >= 1000000:
        return f"{qtde:,.0f}".replace(',', '.')
    elif qtde >= 1000:
        return f"{qtde:,.0f}".replace(',', '.')
    else:
        return str(qtde)


# Ler arquivo com a geolocalização dos Bairros de Curitiba
def ler_arquivo_geolocalizacao():
    global df_geo_bairros
    # Le Arquivo com a geolocalização dos Bairros de Curitiba e cria dataframe
    try:
        df_geo_bairros = pd.read_csv('latlong-bairros-curitiba.csv', sep=';', index_col=None)
    except FileNotFoundError as erro:
        st.error(body='Arquivo de Dados Não Encontrado!')
        st.stop()
    except Exception as erro:
        st.error(body='Erro Na Leitura do Arquivo de Geolocalização!')
        st.write(erro)
        st.stop()


# Monta e exibe o Mapa
def exibir_mapa():
    # Cria o mapa
    fig = px.scatter_mapbox(df_final, 
                             lat='LATI', 
                             lon='LONG', 
                             hover_name='BAIRRO', 
                             hover_data={
                                 'LATI': False,
                                 'LONG': False,
                                 'CASOS': True,
                                 'ÓBITOS': True
                             },
                             color_discrete_sequence=["blue"],
                             zoom=11,
                             height=600)
    # Configura o layout do mapa
    fig.update_layout(mapbox_style="open-street-map")  # Ou "carto-positron"
    fig.update_traces(marker=dict(size=10))  # Tamanho dos marcadores

    # Exibe o Mapa no Streamlit
    st.plotly_chart(fig)


# Carregar Dados da Sessão
def carregar_dados_sessao():
    if 'df' not in st.session_state:
      st.session_state.page = 'COVID-19'
      st.switch_page('COVID-19.py')


# Agrupa as Informações de Bairro, Latitude, Longitude, 
# Casos Totais e Número de Óbitos em um único data frame
def agrupar_informacoes():
    global df_ocorrencias, df_obitos, df_junto1, df_final
    # Soma as ocorrências por Bairro
    df_ocorrencias = st.session_state.df.groupby('BAIRRO').size().reset_index(name='CASOS')
    # Agrupa as Ocorrencias de Obtio Por Bairro
    df_obitos = st.session_state.df[st.session_state.df['ENCERRAMENTO'] == 'ÓBITO CONF'].groupby('BAIRRO').size().reset_index(name='ÓBITOS')
    # Junta as df_ocorrencias e df_obitos pelo Bairro
    df_junto1 = pd.merge(df_ocorrencias, df_obitos, on='BAIRRO', how='outer')
    # Junta, pelo Bairro, as coordenadas com todo o resto
    df_final = pd.merge(df_junto1, df_geo_bairros, on='BAIRRO', how='outer')



#=====================================#
#        Programa Principal           #
#=====================================#

def main():

    configurar_st()
    exibir_logotipo()
    exibir_titulo()
    carregar_dados_sessao()
    ler_arquivo_geolocalizacao()
    agrupar_informacoes()
    exibir_mapa()
    
        
if __name__ == '__main__':
    main()

