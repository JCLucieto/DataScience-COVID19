#=================================================#
# COVID-19 - PARANÁ                               #
#=================================================#
# Página 3-Estatística Descritiva.py              #
# - Apresenta Informações Estatísticas            #
#=================================================#

import streamlit as st
import pandas as pd
from collections import Counter

# Variáveis Globais

estatisticas = None
menor = None
maior = None
media = None
mediana = None
modas = None
desvio_padrao = None
total_elementos = None
freq_25 = None
freq_50 = None
freq_75 = None
frequencias = None
faixas_contagem = None
faixas_ordenadas = None
percentual_1 = None
percentual_2 = None
percentual_3 = None


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
    st.title('Estatísticas Descritivas')

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

# Monta Dados Estatisticos Descritivos - Idade
def preparar_idade():

    global estatisticas, menor, maior
    global media, mediana, modas, frequencias
    global desvio_padrao, total_elementos
    global freq_25, freq_50, freq_75, faixas_contagem

    estatisticas = st.session_state.df['IDADE (anos)'].describe()

    # Total de Linhas
    total_elementos = int(estatisticas['count'])

    # Menor Valor de Idade
    menor = estatisticas['min']

    # Maior Valor de Idade
    maior = estatisticas['max']

    # Valor Médio de Idade
    # (Média Aritimetica = Soma de Todas as Idades / Quantidades de Linhas)
    media = round(estatisticas['mean'], 2)

    # Mediana = Medida de Tendencia Central
    # Exemplo:
    #   - Conjunto Impar : [3,2,5] - Ordena [2,3,5] - Mediana é 3
    #   - Conjunto Par   : [3,2,5,1] - Ordena [1,2,3,5] - Mediana é ( (2+3)/ 2 ) = 2.5
    mediana = round(st.session_state.df['IDADE (anos)'].median(), 2)

    # Modas
    # Conta a frequência de cada número
    contador = Counter(st.session_state.df['IDADE (anos)'])
    # Encontra a(s) moda(s)
    max_freq = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == max_freq]

    # Cálculo do Desvio Padrão
    # 1 - Calcular a média (𝜇):
    #     - Soma todos os valores do conjunto e divide pelo número total de valores.
    # 2 - Calcular a diferença de cada valor em relação à média:
    #     - Para cada valor 𝑥𝑖 no conjunto, calcula-se a diferença (𝑥𝑖 − 𝜇)
    # 3 - Elevar ao quadrado:
    #     - Eleva-se ao quadrado cada uma dessas diferenças para evitar que valores negativos se anulem.
    # 4 - Calcular a média dos quadrados das diferenças:
    #     - Soma todos os quadrados das diferenças e divide pelo número total de valores
    #       (para a população) ou pelo número total de valores menos um (para a amostra).
    # 5 - Tirar a raiz quadrada:
    #     - A raiz quadrada do valor obtido na etapa anterior é o desvio padrão.
    desvio_padrao = round(estatisticas['std'],2)

    # Percentuais (Quantis)
    # Os percentuais representam a distribuição dos dados e ajudam a entender a dispersão e a centralidade.
    # 25% (1º quartil): O valor abaixo do qual 25% dos dados estão. É o primeiro quartil.
    # 50% (mediana): O valor abaixo do qual 50% dos dados estão. É a mediana.
    # 75% (3º quartil): O valor abaixo do qual 75% dos dados estão. É o terceiro quartil.
    freq_25 = estatisticas['25%']
    freq_50 = estatisticas['50%']
    freq_75 = estatisticas['75%']

    # As 4 Idades Mais Frequentes
    frequencias = st.session_state.df['IDADE (anos)'].value_counts()

    # Contando quantos registros estão em cada faixa de idade
    faixas_contagem = st.session_state.df['FAIXA'].value_counts()

    
# Exibir Estatisticas Idade
def exibir_idade():

    global estatisticas, menor, maior
    global media, mediana, modas, frequencias
    global desvio_padrao, total_elementos
    global freq_25, freq_50, freq_75, faixas_contagem

    conteudo_html = f'''
    <p style="color:black;">
        <strong>Principais Características da Informação :  [ IDADE EM (ANOS) ]</strong><br>
    </p>
    <table style="border-collapse:collapse;">
        <tr>
            <th style="border:1px solid black; padding:8px; width:280px; background-color:#B6B6B6;">MEDIDAS</th>
            <th style="border:1px solid black; padding:8px; width:300px; background-color:#B6B6B6;">VALORES</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Quantidade de Elementos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(total_elementos)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Menor Idade</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{int(menor)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Maior Idade</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{int(maior)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Média</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{media}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Mediana</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{mediana}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Modas</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{modas}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Desvio Padrão</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{desvio_padrao}</td>
        </tr>    
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>Percentuais (Quantis)</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">25%</td>
            <td style="border:1px solid black; padding:8px; color:blue;">Abaixo de {int(freq_25)} Anos</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">50%</td>
                <td style="border:1px solid black; padding:8px; color:blue;">Menor ou Igual a {int(freq_50)} Anos</td>
            </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">75%</td>
            <td style="border:1px solid black; padding:8px; color:blue;">Abaixo de {int(freq_75)} Anos</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>As (5) Idades Mais Frequentes</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
    '''

    for i in range(5):
        conteudo_html += '<tr>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[i]}</td>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[i])}</td>'
        conteudo_html += '</tr>'

    conteudo_html += f'''
        <tr>
            <td style="border:1px solid black; padding:8px; color:black; background-color:#C6C6C6;"><strong>As Faixas de Idade Por Ocorrência</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
    '''
    for i in range(len(faixas_contagem)):
        conteudo_html += '<tr>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:black;">{faixas_contagem.index[i]}</td>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(faixas_contagem.values[i])}</td>'
        conteudo_html += '</tr>'
    conteudo_html += '</table>'
    
    st.markdown(conteudo_html, unsafe_allow_html=True)


# Monta Dados Estatisticos Descritivos - Faixa de Idade
def preparar_faixa_idade():

    global estatisticas, total_elementos, frequencias, faixas_contagem, faixas_ordenadas

    estatisticas = st.session_state.df['FAIXA'].describe()

    # Total de Linhas
    total_elementos = int(estatisticas['count'])

    # As 4 Faixas Mais Frequentes
    frequencias = st.session_state.df['FAIXA'].value_counts().nlargest(4)

    # Contando quantos registros estão em cada faixa de idade
    faixas_contagem = st.session_state.df['FAIXA'].value_counts()

    #Ordenar pelas faixas (índices)
    resultado = sorted(faixas_contagem.items(), key=lambda x: (int(x[0].split('-')[0]), int(x[0].split('-')[1])))
    
    # Separando em duas listas
    indices = [item[0] for item in resultado]
    valores = [item[1] for item in resultado]
    faixas_ordenadas = pd.DataFrame({'faixa': indices, 'valor': valores}).reset_index()


# Exibir Estatisticas Faixa Idade
def exibir_faixa_idade():

    global total_elementos, frequencias, faixas_ordenadas

    conteudo_html = f'''
    <p style="color:black;">
        <strong>Principais Características da Informação :  [ FAIXA DE IDADE ]</strong><br>
    </p>
    <table style="border-collapse:collapse;">
        <tr>
            <th style="border:1px solid black; padding:8px; width:280px; background-color:#B6B6B6;">MEDIDAS</th>
            <th style="border:1px solid black; padding:8px; width:300px; background-color:#B6B6B6;">VALORES</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Quantidade de Elementos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(total_elementos)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>As (4) Faixas Mais Frequentes</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[0]} Anos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[0])}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[1]} Anos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[1])}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[2]} Anos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[2])}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[3]} Anos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[3])}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black; background-color:#C6C6C6;"><strong>Todas Faixas de Idade</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
    '''
    for index, row in faixas_ordenadas.iterrows():
        conteudo_html += '<tr>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:black;">{row['faixa']} Anos</td>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(row['valor'])}</td>'
        conteudo_html += '</tr>'
    conteudo_html += '</table>'
    
    st.markdown(conteudo_html, unsafe_allow_html=True)


# Monta Dados Estatisticos Descritivos - Sexo
def preparar_sexo():

    global estatisticas, total_elementos, frequencias
    global percentual_1, percentual_2

    estatisticas = st.session_state.df['SEXO'].describe()

    # Total de Linhas
    total_elementos = int(estatisticas['count'])

    # Os 2 Valores Mais Frequentes
    frequencias = st.session_state.df['SEXO'].value_counts().nlargest(2)

    percentual_1 = round(float(frequencias.values[0] / total_elementos) * 100, 2)
    percentual_2 = round(float(frequencias.values[1] / total_elementos) * 100, 2)


# Exibir Estatisticas Sexo
def exibir_sexo():

    global total_elementos, frequencias
    global percentual_1, percentual_2

    info = f'''
    <p style="color:black;">
        <strong>Principais Características da Informação :  [ SEXO ]</strong><br>
    </p>
    <table style="border-collapse:collapse;">
        <tr>
            <th style="border:1px solid black; padding:8px; width:280px; background-color:#B6B6B6";>MEDIDAS</th>
            <th style="border:1px solid black; padding:8px; width:300px; background-color:#B6B6B6";">VALORES</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Quantidade de Elementos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(total_elementos)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>Valores Mais Frequentes</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;"><strong>{frequencias.index[0]}</strong> - (Quantidade e Percentual)</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[0])}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;({percentual_1} %)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;"><strong>{frequencias.index[1]}</strong> - (Quantidade e Percentual)</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[1])}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;({percentual_2} %)</td>
        </tr>
    </table>
    '''
    st.markdown(info, unsafe_allow_html=True)

# Monta Dados Estatisticos Descritivos - Bairro
def preparar_bairro():

    global estatisticas, total_elementos, frequencias, faixas_contagem

    estatisticas = st.session_state.df['BAIRRO'].describe()

    # Total de Linhas
    total_elementos = int(estatisticas['count'])

    # Os Bairros Mais Frequentes
    frequencias = st.session_state.df['BAIRRO'].value_counts()

    # Contando quantos registros estão em cada Bairro
    faixas_contagem = st.session_state.df['BAIRRO'].value_counts()

    # Ordena os Bairros pelo Nome
    faixas_contagem = faixas_contagem.sort_index()


# Exibir Estatisticas Bairro
def exibir_bairro():

    global total_elementos, frequencias, faixas_ordenadas

    conteudo_html = f'''
    <p style="color:black;">
        <strong>Principais Características da Informação :  [ BAIRRO ]</strong><br>
    </p>
    <table style="border-collapse:collapse;">
        <tr>
            <th style="border:1px solid black; padding:8px; width:280px; background-color:#B6B6B6;">MEDIDAS</th>
            <th style="border:1px solid black; padding:8px; width:300px; background-color:#B6B6B6;">VALORES</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Quantidade de Elementos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(total_elementos)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>Os (4) Bairros Mais Frequentes</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
    '''
    for i in range(4):
        conteudo_html += '<tr>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:black;">{frequencias.index[i]}</td>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[i])}</td>'
        conteudo_html += '</tr>'

    conteudo_html += f'''    
        <tr>
            <td style="border:1px solid black; padding:8px; color:black; background-color:#C6C6C6;"><strong>Bairros em Ordem Alfabética</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>        
    '''
    for i in range(len(faixas_contagem)):
        conteudo_html += '<tr>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:black;">{faixas_contagem.index[i]}</td>'
        conteudo_html += f'<td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(faixas_contagem.values[i])}</td>'
        conteudo_html += '</tr>'
    conteudo_html += '</table>'
    
    st.markdown(conteudo_html, unsafe_allow_html=True)


# Monta Dados Estatisticos Descritivos - Encerramento
def preparar_encerramento():
    
    global estatisticas, total_elementos, frequencias
    global percentual_1, percentual_2, percentual_3
    
    estatisticas = st.session_state.df['ENCERRAMENTO'].describe()

    # Total de Linhas
    total_elementos = int(estatisticas['count'])

    # Os 4 Valores Mais Frequentes
    frequencias = st.session_state.df['ENCERRAMENTO'].value_counts().nlargest(4)

    percentual_1 = round(float(frequencias.values[0] / total_elementos) * 100, 2)
    percentual_2 = round(float(frequencias.values[1] / total_elementos) * 100, 2)
    percentual_3 = round(float(frequencias.values[2] / total_elementos) * 100, 2)

# Exibir Estatisticas Encerramento
def exibir_encerramento():

    global total_elementos, frequencias
    global percentual_1, percentual_2, percentual_3
    
    info = f'''
    <p style="color:black;">
        <strong>Principais Características da Informação :  [ ENCERRAMENTO ]</strong><br>
    </p>
    <table style="border-collapse:collapse;">
        <tr>
            <th style="border:1px solid black; padding:8px; width:320px; background-color:#B6B6B6;">MEDIDAS</th>
            <th style="border:1px solid black; padding:8px; width:300px; background-color:#B6B6B6;">VALORES</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px;">Quantidade de Elementos</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(total_elementos)}</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"><strong>Frequencia dos Valores</strong></td>
            <td style="border:1px solid black; padding:8px; background-color:#C6C6C6;"></td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;"><strong>{frequencias.index[0]}</strong> - (Quantidade e Percentual)</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[0])}&nbsp;&nbsp;&nbsp&nbsp;&nbsp({percentual_1} %)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;"><strong>{frequencias.index[1]}</strong> - (Quantidade e Percentual)</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[1])}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp({percentual_2} %)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:8px; color:black;"><strong>{frequencias.index[2]}</strong> - (Quantidade e Percentual)</td>
            <td style="border:1px solid black; padding:8px; color:blue;">{formata_qtde(frequencias.values[2])}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp({percentual_3} %)</td>
        </tr>
    </table>
    '''
    st.markdown(info, unsafe_allow_html=True)


# Carregar Dados da Sessão
def carregar_dados_sessao():
    if 'df' not in st.session_state:
      st.session_state.page = 'COVID-19'
      st.switch_page('COVID-19.py')


# Executa as Funções correspondentes ao botão clicado
def executar():

    global opcao_escolhida

    exibido = False
    opcao_escolhida = ''
    
    # Montagem e Exibição dos Botões
  
    st.sidebar.markdown ('**SELECIONE UMA INFORMAÇÃO**')
    
    if st.sidebar.button('Idade',  use_container_width=True):
        preparar_idade()
        exibir_idade()
        exibido = True

    if st.sidebar.button('Faixa Idade',  use_container_width=True):
        preparar_faixa_idade()
        exibir_faixa_idade()
        exibido = True
        
    if st.sidebar.button('Sexo',  use_container_width=True):
        preparar_sexo()
        exibir_sexo()
        exibido = True
        
    if st.sidebar.button('Bairro',  use_container_width=True):
        preparar_bairro()
        exibir_bairro()
        exibido = True

    if st.sidebar.button('Encerramento',  use_container_width=True):
        preparar_encerramento()
        exibir_encerramento()
        exibido = True
    else:
        if not exibido:
            st.write ('Esta página fornece Estatística Descritiva das principais informações.')
            st.write ('Selecione através dos botões laterais a informação sobre a qual quer as estatísticas.')
      
#=====================================#
#        Programa Principal           #
#=====================================#

def main():

    configurar_st()
    exibir_logotipo()
    exibir_titulo()
    carregar_dados_sessao()
    executar()
        
if __name__ == '__main__':
    main()
