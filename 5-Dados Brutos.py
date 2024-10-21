#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 9-Dados Brutos.py                        #
# - Apresenta tabela com os dados brutos.         #
# - Possibilita seleção de colunas.               #
# - Oferece filtros.                              #
# - Permite o download do arquivo CSV gerado      #
#   de acordo com a seleção de colunas e filtros  #
#   aplicados sobre os dados brutos.              #
#=================================================#

import time
import chardet
import datetime
import pandas as pd
import streamlit as st


# Variáveis Globais
nome_arquivo = None
dados_filtrados = None

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
    st.title('Dados Brutos')

   
# Converte o DataFrame para Arquivo CSV
@st.cache_data
def converte_csv(df):
    global nome_arquivo
    return df.to_csv(sep=';', index = False).encode('utf-8')


# Mensagem de Sucesso
def mensagem_sucesso():
    sucesso = st.success('Arquivo Baixado Com Sucesso!', icon = '✅')
    time.sleep(5)
    sucesso.empty()


# Carregar Dados da Sessão
def carregar_dados_sessao():
    if 'df' not in st.session_state:
      st.session_state.page = 'COVID-19'
      st.switch_page('COVID-19.py')


# Exibir Informações da Página
def exibir_informacoes():

    global nome_arquivo, dados_filtrados

    informacao = '''
                <span style="color:black;">
                    <strong>
                        Esta página lhe oferece a possibilidade de montar infinitas pesquisas através
                        da seleção das colunas de interesse e também a aplicação de filtros sobre
                        os dados das colunas selecionadas.<br>
                        No final da sua pesquisa você tem a possibilidade de gerar um arquivo .CSV e
                        fazer o download desse arquivo para o seu computador.
                    </strong>
                </span>
                <span style="color:blue;">
                    <strong>
                        Explore as possibilidades!
                    </strong>
                    <br>
                </span>
    '''
    st.markdown(informacao, unsafe_allow_html=True)

    with st.expander('CLIQUE AQUI PARA SELECIONAR AS COLUNAS DESEJADAS'):
        colunas = st.multiselect('COLUNAS', list(st.session_state.df.columns), list(st.session_state.df.columns))

    st.sidebar.title('Filtros')

    with st.sidebar.expander('Data Notificação'):
        col1, col2 = st.columns(2)
        with col1:
            data_notificacao_inicial = st.date_input('Inícial', (st.session_state.df['DATA INCLUSÃO/ NOTIFICAÇÃO'].min()))
        with col2:
            data_notificacao_final = st.date_input('Final', (st.session_state.df['DATA INCLUSÃO/ NOTIFICAÇÃO'].max()))

    with st.sidebar.expander('Classificação Final'):
        classificacao_final = st.multiselect('Selecione Classificação Final', sorted(st.session_state.df['CLASSIFICAÇÃO FINAL'].unique()), sorted(st.session_state.df['CLASSIFICAÇÃO FINAL'].unique()))

    with st.sidebar.expander('Idade (Anos)'):
        idade = st.slider('Selecione Idade', 0,120, (0,120))

    with st.sidebar.expander('Faixa Idade (Anos)'):
        faixa = st.multiselect('Selecione Faixas', sorted(st.session_state.df['FAIXA'].unique()), sorted(st.session_state.df['FAIXA'].unique()))
        
    with st.sidebar.expander('Sexo'):
        sexo = st.multiselect('Selecione Sexo', sorted(st.session_state.df['SEXO'].unique()), sorted(st.session_state.df['SEXO'].unique()))

    with st.sidebar.expander('Bairro'):
        bairro = st.multiselect('Selecione Bairros', sorted(st.session_state.df['BAIRRO'].unique()), sorted(st.session_state.df['BAIRRO'].unique()))

    with st.sidebar.expander('Distrito'):
        distrito = st.multiselect('Selecione Distritos', sorted(st.session_state.df['DISTRITO RESIDÊNCIA'].unique()), sorted(st.session_state.df['DISTRITO RESIDÊNCIA'].unique()))

    with st.sidebar.expander('Internado'):
        internado = st.multiselect('Selecione Internado', sorted(st.session_state.df['INTERNADO (SIM/NÃO)'].unique()), sorted(st.session_state.df['INTERNADO (SIM/NÃO)'].unique()))

    with st.sidebar.expander('Data do Exame'):
        col1, col2 = st.columns(2)
        with col1:
            data_coleta_inicial = st.date_input('Inicial', (st.session_state.df['DATA COLETA EXAME'].min()))
        with col2:
            data_coleta_final = st.date_input('Final', (st.session_state.df['DATA COLETA EXAME'].max()))

    with st.sidebar.expander('Encerramento'):
        encerramento = st.multiselect('Selecione Encerramento', sorted(st.session_state.df['ENCERRAMENTO'].unique()), sorted(st.session_state.df['ENCERRAMENTO'].unique()))

    # Monta uma única query do Pandas para fazer
    # todas as condições de filtragem simultaneamente
    
    query = '''
        @data_notificacao_inicial <= `DATA INCLUSÃO/ NOTIFICAÇÃO` <= @data_notificacao_final and \
        `CLASSIFICAÇÃO FINAL` in @classificacao_final and \
        @idade[0] <= `IDADE (anos)` <= @idade[1] and \
        FAIXA in @faixa and \
        SEXO in @sexo and \
        BAIRRO in @bairro and \
        `DISTRITO RESIDÊNCIA` in @distrito and \
        `INTERNADO (SIM/NÃO)` in @internado and \
        @data_coleta_inicial <= `DATA COLETA EXAME` <= @data_coleta_final and \
        ENCERRAMENTO in @encerramento
        '''

          
    # Aplica o Filtro das Seleções Laterais
    dados_filtrados = st.session_state.df.query(query)

    # Aplica o Filtro de Colunas do Incio da Página
    with st.spinner('Prcessando ! - Aguarde....'):
        dados_filtrados = dados_filtrados[colunas]

    st.dataframe(dados_filtrados)

    st.markdown(f'A tabela possui  :blue[{dados_filtrados.shape[0]}] linhas e  :blue[{dados_filtrados.shape[1]}] colunas')

    st.markdown('Digite um Nome Para o Arquivo :')

    coluna1, coluna2 = st.columns(2)
    with coluna1:
        nome_arquivo = st.text_input('Nome', label_visibility = 'collapsed', value = 'dados')
        nome_arquivo += '.csv'
    with coluna2:
        st.download_button('Download da Tabela em Formato CSV', data = converte_csv(dados_filtrados), file_name = nome_arquivo, mime = 'text/csv', on_click = mensagem_sucesso)



#=====================================#
#        Programa Principal           #
#=====================================#

def main():

    configurar_st()
    exibir_logotipo()
    exibir_titulo()
    with st.spinner('Aguarde - Carregando Dados...'):
        carregar_dados_sessao()
        exibir_informacoes()
    
        
if __name__ == '__main__':
    main()

