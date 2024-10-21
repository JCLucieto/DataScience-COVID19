#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página Informações da Base de Dados.py          #
# - Apresenta Informações Gerais da Base          #
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
    st.title('Informações da Base de Dados (Inicial)')


# Exibir as Informações da Página

def exibir_informacoes():

    st.markdown(
        '''
        <p style="color:black;">
        <strong>Tipo de Arquivo Original</strong>
        </p>
        <p style="color:blue;">
        Planilha no formato CSV (comma-separated-values)
        </p>
        <p style="color:black;">
        <strong>Volume dos Dados</strong>
        </p>
        <p style="color:blue;">
        645.680 Linhas x  10 Colunas
        </p>
        <p style="color:black;">
        <strong>Informações das Colunas</strong>
        </p>
        <table border="1">
            <thead>
                <tr>
                    <th style="width: 250px;">Colunas</th>                    
                    <th style="width: 490px;">Valores Encontrados</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>DATA INCLUSÃO/ NOTIFICAÇÃO</td>
                    <td style="color:blue;">De: 11/03/2020  Até: 09/10/2024</td>
                </tr>
                <tr>
                    <td>CLASSIFICAÇÃO FINAL</td>
                    <td style="color:blue;">CONFIRMADO</td>
                </tr>
                <tr>
                    <td>IDADE (anos)</td>
                    <td style="color:blue;">De: 0  Até: 107 anos</td>
                </tr>
                <tr>
                    <td>SEXO</td>
                    <td style="color:blue;">M e F</td>
                </tr>
                <tr>
                    <td>BAIRRO</td>
                    <td style="color:blue;">
                      ABRANCHES, ÁGUA VERDE, AHÚ, ALTO BOQUEIRÃO, ALTO DA GLÓRIA, ALTO DA RUA XV,
                      ATUBA, AUGUSTA, BACACHERI, BAIRRO ALTO, BARREIRINHA, BATEL,
                      BIGORRILHO, BOA VISTA, BOM RETIRO, BOQUEIRÃO, BUTIATUVINHA, CABRAL,
                      CACHOEIRA, CAJURU, CAMPINA DO SIQUEIRA, CAMPO COMPRIDO,
                      CAMPO DE SANTANA, CAPÃO DA IMBUIA, CAPÃO RASO, CASCATINHA, CAXIMBA,
                      CENTRO, CENTRO CÍVICO, CIDADE INDUSTRIAL DE CURITIBA, CRISTO REI,
                      DESCONHECIDO, FANNY, FAZENDINHA, GANCHINHO, GUABIROTUBA, GUAÍRA,
                      HAUER, HUGO LANGE, JARDIM BOTÂNICO, JARDIM DAS AMÉRICAS,
                      JARDIM SOCIAL, JUVEVÊ, LAMENHA PEQUENA, LINDÓIA, MERCÊS, MOSSUNGUÊ,
                      NOVO MUNDO, ORLEANS, PAROLIN, PILARZINHO, PINHEIRINHO, PORTÃO,
                      PRADO VELHO, REBOUÇAS, RIVIERA, SANTA CÂNDIDA, SANTA FELICIDADE,
                      SANTA QUITÉRIA, SANTO INÁCIO, SEMINÁRIO, SÃO BRAZ, SÃO FRANCISCO,
                      SÃO JOÃO, SÃO LOURENÇO, SÃO MIGUEL, SÍTIO CERCADO, TABOÃO, TARUMÃ,
                      TATUQUARA, TINGUI, UBERABA, UMBARÁ, VILA IZABEL, VISTA ALEGRE,
                      XAXIM
                    </td>
                </tr>
                <tr>
                    <td>DISTRITO RESIDÊNCIA</td>
                    <td style="color:blue;">DSMZ, DSBQ, DSPR, DSBV, DSSF, DSCJ, DSPN, DSCIC, DSBN, DSTQ</td>
                </tr>
                <tr>
                    <td>INTERNADO (SIM / NÃO)</td>
                    <td style="color:blue;">SIM ou NÃO</td>
                </tr>
                <tr>
                    <td>DATA COLETA EXAME</td>
                    <td style="color:blue;">De 01/01/2021  até  31/12/2023</td>
                </tr>
                <tr>
                    <td>DATA ÓBITO</td>
                    <td style="color:blue;">De 18/04/2020  até  03/10/2024</td>
                </tr>
                <tr>
                    <td>ENCERRAMENTO</td>
                    <td style="color:blue;">ATIVO, RECUPERADO, ÓBITO CONF</td>
                </tr>
            </tbody>
        </table>
            
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
