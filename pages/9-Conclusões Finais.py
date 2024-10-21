#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 5-Conclusões.py                          #
# - Apresenta as Conclusões sobre o trabalho.     #
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
    st.title('Conclusões Finais')


# Exibir as Informações da Página

def exibir_informacoes():

    st.markdown(
        '''
        <p style="color:blak;">
          <strong>As análises dos Dados sobre COVID-19 na cidade de Curitiba durante o período de 11.03.2020 até 09.10.2024 mostraram as seguintes tendências: :</strong>
        </p>

        <ul>
        
        <p style="color:blak;">
          <strong>FAIXA ETÁRIA</strong>
        </p>
        <p style="color:blak;">
          <li>A Faixas Etárias que apresentaram o maior número de infecções foram as de:  31 a 40, 41 a 50  e 21 a 30 Anos.</li>
        </p>
        <p style="color:blak;">
          <li>O fato de terem sido atingidos os indivíduos das faixas de Adultos e Adultos Jovens pode ser 
          atribuído a fatores como mobilidade, socialização e menos preocupações com comorbidades.</li>
        </p>
        <p style="color:blak;">
          <strong>IDADE</strong>
        </p>
        <p style="color:blak;">
          <li>A Idade preponderante foi de 39 Anos</li>
        </p>
        <p style="color:blak;">
          <strong>SEXO</strong>
        </p>
        <p style="color:blak;">
          <li>O sexo Feminino apresentou maior número de infecções sobre o sexo Masculino.</li>
        </p>
        <p style="color:blak;">
          <strong>MORTALIDADE</strong>
        </p>
        <p style="color:blak;">
          <li>O sexo Masculino apresentou maior número de óbitos do que o sexo Feminino, o que sugere que, 
          embora as mulheres tenham tido mais casos confirmados, os homens têm um maior risco de complicações 
          graves e morte em decorrência da doença.</li>
        </p>
        <p style="color:blak;">
          <strong>BAIRROS</strong>
        </p>
        <p style="color:blak;">
          <li>Os bairros que apresentaram maior número de infectados foram:
          <ul>
              <li>Cidade Industrial de Curitiba - 63.399 Casos</li>
              <li>Sítio Cercado - 40.269 Casos</li>
              <li>Cajuru - 32.917 Casos</li>
              <li>Uberaba - 25.899 Casos</li>
              Embora não sejam todos próximos, eles estão relativamente próximos dentro do contexto de Curitiba.
              As condições financeiras variam, mas, em geral, os moradores enfrentam desafios econômicos, e de falta de 
              infraestrutura especialmente em Sítio Cercado, Uberaba e Cajuru.
            </ul>
          </li>
        </p>
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
