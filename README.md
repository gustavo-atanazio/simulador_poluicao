# Simulador de Impacto Ambiental

Este projeto é um simulador de impacto ambiental que permite visualizar o efeito de diferentes níveis de poluição nos oceanos. Usando o Streamlit, a aplicação fornece uma interface interativa para ajustar variáveis como o nível de plástico, oxigênio e petróleo, e calcula o risco total para o ambiente.

## Funcionalidades

- **Ajuste de Variáveis**: Ajuste os níveis de plástico, oxigênio e petróleo no ambiente usando sliders interativos.
- **Visualização Gráfica**: Visualize os níveis de poluição em um gráfico de barras.
- **Indicador de Risco**: O simulador calcula o risco total para o ambiente e muda a cor de fundo da interface para indicar o nível de alerta:
  - **Alta**: Vermelho
  - **Média**: Amarelo
  - **Baixa**: Verde

## Como executar o projeto

### Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/gustavo-atanazio/simulador_poluicao.git
cd simulador_poluicao
```

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv myenv

# Linux / Mac
source myenv/bin/activate

# Windows
myenv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando a Aplicação

Para iniciar o simulador, execute:

```bash
streamlit run app.py
```

## Estrutura do Projeto

- `app.py`: Contém o código principal do simulador.
- `requirements.txt`: Lista de dependências do projeto.

## Cálculo do Risco

A função `calc_risk` realiza o cálculo do risco total com base nos níveis de poluição fornecidos. Cada variável tem um peso específico que influencia o cálculo do risco. O risco total é normalizado para estar entre 0 e 100.

```python
def calc_risk(values: list[int]):
    if len(values) != len(pounds):
        raise ValueError('O número de valores deve corresponder ao número de variáveis (pesos).')

    normalized_values = [value / 100 for value in values]
    risk = sum(normalized_values[i] * pounds[key] for i, key in enumerate(pounds))
    risk *= 100
    return risk
```

## Integrantes

- [Gustavo Atanazio](https://github.com/gustavo-atanazio), 1ESA, 559098
- [Lucca Cardinale](https://github.com/luccacardinale), 1ESA, 556668