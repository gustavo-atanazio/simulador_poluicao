import streamlit as st

# Cores de cada nível de alerta (em CSS)
colors = {
    'high': 'radial-gradient(circle, rgba(176,10,10,1) 0%, rgba(2,0,36,1) 100%);',
    'medium': 'radial-gradient(circle, rgba(203,160,18,1) 0%, rgba(2,0,36,1) 100%);',
    'low': 'radial-gradient(circle, rgba(9,121,28,1) 0%, rgba(2,0,36,1) 100%);'
}

# Peso de cada variável
pounds = {
    'plastic': 0.65,
    'oxygen': 0.45,
    'oil': 0.85
}

# Função que realiza o cálculo final
def calc_risk(values: list[int]):
    # Verificando se a lista de variáveis é do mesmo tamanho da de pesos
    if len(values) != len(pounds):
        raise ValueError('O número de valores deve corresponder ao número de variáveis (pesos).')

    # Normalização dos valores das variáveis (0-1)
    normalized_values = [value / 100 for value in values]

    # Cálculo ponderado e normalizado do risco total
    risk = 0
    for i, key in enumerate(pounds):
        risk += normalized_values[i] * pounds[key]

    # Garantindo resultado entre 0 e 100
    risk *= 100
    return risk

# Função responsável por mudar a cor de fundo da interface
def change_color(color):
    st.markdown(f'''
        <style>
            .stApp {{ background: {color} }} 
        </style>
    ''', unsafe_allow_html = True)

def main():
    # INTERFACE
    st.title('Simulador de impacto ambiental')
    st.write('Para uma melhor visualização, habilite a opção de tela cheia.')
    st.divider()

    # Dividindo o layout em duas colunas
    col1, col2 = st.columns(
        spec = [0.4, 0.6], # Retorna duas colunas, uma com 40% de preenchimento, e outra com 60%
        gap = 'large' # Espaço entre as colunas
    )

    ## VARIÁVEIS
    with col1:
        st.header('Variáveis')

        plastic = st.slider(
            'Nível de plástico', # Label
            0, # Mínimo
            100, # Máximo
            0, # Valor inicial
            help = '' # Texto de apoio
        )

        oxygen = st.slider(
            'Nível de oxigênio',
            0,
            100,
            0,
            help = ''
        )

        oil = st.slider(
            'Nível de petróleo',
            0,
            100,
            0,
            help = ''
        )

    data = {
        'Valores': [plastic, oxygen, oil], # Lista de valores
        'Nomes': ['Plástico', 'Oxigênio', 'Petróleo'] # Labels
    }

    ## GRÁFICO
    with col2:
        st.header('Gráfico')

        st.bar_chart(
            data, # Valores
            x = 'Nomes', # Posição no dicionário contendo as labels
            color = '#0000FF' # Cor das barras
        )
        
    # LÓGICA
    total_risk = calc_risk([plastic, oxygen, oil])

    if total_risk > 70:
        change_color(colors['high'])
    elif total_risk > 40:
        change_color(colors['medium'])
    else:
        change_color(colors['low'])

main()