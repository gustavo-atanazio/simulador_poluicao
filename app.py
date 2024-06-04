import streamlit as st

colors = {
    'high': 'radial-gradient(circle, rgba(176,10,10,1) 0%, rgba(2,0,36,1) 100%);',
    'medium': 'radial-gradient(circle, rgba(203,160,18,1) 0%, rgba(2,0,36,1) 100%);',
    'low': 'radial-gradient(circle, rgba(9,121,28,1) 0%, rgba(2,0,36,1) 100%);'
}

pounds = {
    'plastic': 0.5,
    'oxygen': 0.3,
    'oil': 0.7
}

def calc_risk(plastic, oxygen, oil):
    risk = (
        plastic * pounds['plastic']
        + oxygen * pounds['oxygen']
        + oil * pounds['oil']
    )

    return risk

def change_color(color):
    st.markdown(f'''
        <style>
            .stApp {{ background: {color} }} 
        </style>
    ''', unsafe_allow_html = True)

def main():
    # Interface
    st.title('Simulador de impacto ambiental')
    st.divider()

    col1, col2 = st.columns(spec = [0.4, 0.6], gap = 'large')

    ## Variáveis
    with col1:
        st.header('Variáveis')

        plastic = st.slider('Nível de plástico', 0, 100, 0)
        oxygen = st.slider('Nível de oxigênio', 0, 100, 0)
        oil = st.slider('Nível de petróleo', 0, 100, 0)

    data = {
        'Valores': [plastic, oxygen, oil],
        'Nomes': ['Plástico', 'Oxigênio', 'Petróleo']
    }

    ## Gráfico
    with col2:
        st.header('Gráfico')

        st.bar_chart(
            data, 
            x = 'Nomes', 
            color = '#0000FF'
        )
        
    # Lógica
    total_risk = calc_risk(plastic, oxygen, oil)

    if total_risk > 70:
        change_color(colors['high'])
    elif total_risk > 40:
        change_color(colors['medium'])
    else:
        change_color(colors['low'])

main()