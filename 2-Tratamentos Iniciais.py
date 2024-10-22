#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 2-Tratamentos Iniciais.py                #
# - Apresenta Informações sobre os Tratamentos    #
#   feitos sobre a base de dados.                 #
#=================================================#

import streamlit as st

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
    st.title('Tratamentos Iniciais')


# Exibir as Informações da Página

def exibir_informacoes():

    st.markdown(
        '''
        <p style="color:black;">
        <strong>Coleta, Armazenamento, Análise, Preparação e Limpeza dos Dados</strong>
        </p>
        <p style="color:blak;">
          <strong>Durante a etapa de Preparação e Limpeza dos Dados foram aplicadas as seguites ações :</strong>
        </p>
        <ul>
            <li>Retirada da coluna <strong>CLASSIFICAÇÃO FINAL</strong> pois só existe um único valor para todos os registros (<strong style="color: blue;">CONFIRMADO</strong>)</li>
            <li>Unificação dos valores da coluna <strong>SEXO</strong> para apenas letras maiúsculas (<strong style="color: blue;">F</strong> ou <strong style="color: blue;">M</strong>)</li>
            <li>Unificação dos valores da coluna <strong>INTERNADO</strong> para apenas as palavras (<strong style="color: blue;">SIM</strong> ou <strong style="color: blue;">NÃO</strong>)</li>
            <li><strong>Eliminação de Valores Nulos das Colunas:</strong>
                <ul>
                    <li> <strong>BAIRRO</strong> :  10.911 Ocorrências - Atribuição :  (<strong style="color: blue;">Desconhecido</strong>)</li>
                    <li> <strong>DISTRITO RESIDÊNCIA</strong> : 10.915 Ocorrências - Atribuição :  (<strong style="color: blue;">DS**</strong>)</li>
                    <li> <strong>DATA ÓBITO</strong> : 636.747 Ocorrências - Atribuição :  (<strong style="color: blue;">00/00/0000</strong>)</li>
                </ul>
            </li>
            <li>Criação de coluna FAIXA (Faixa de Idade) e classificação dos registros com base na Idade (Anos)</li>
            <li><strong>Alteração do Formato das Colunas:</strong>
                <ul>
                    <li> <strong>DATA INCLUSÃO/ NOTIFICAÇÃO</strong> : Formato alterado para (<strong style="color: blue;">DateTime</strong>)</li>
                    <li> <strong>DATA COLETA EXAME</strong> : Formato alterado para (<strong style="color: blue;">DateTime</strong>)</li>
                    <li> <strong>DATA ÓBITO</strong> : Formato alterado para <strong style="color: blue;">DateTime</strong>)</li>
                </ul>
            </li>
            <li><strong>Criação das Colunas :</strong>
                <ul>
                    <li> <strong>DATA_INCLUSAO_FORMATADA</strong> : Formato (<strong style="color: blue;">dd/mm/aaaa</strong>)</li>
                    <li> <strong>DATA_COLETA_FORMATADA</strong> : Formato (<strong style="color: blue;">dd/mm/aaaa</strong>)</li>
                    <li> <strong>DATA_OBITO_FORMATADA</strong> : Formato <strong style="color: blue;">dd/mm/aaaa</strong>)</li>
                </ul>
            </li>
        </ul>
        ''', unsafe_allow_html=True)


#=====================================#
#        Programa Principal           #
#=====================================#

def main():

    configurar_st()
    exibir_logotipo()
    exibir_titulo()
    exibir_informacoes()
    
        
if __name__ == '__main__':
    main()
