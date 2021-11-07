# importar as bibliotecas
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plot
# no Google Colab, dê o comando: !pip install plotly --upgrade
import plotly.express as px

# chamar a base de crédito no programa
base_de_credito = pd.read_csv("credit_data.csv")

# mostrar os 5 primeiros e os 5 últimos elementos da base de crédito
print(base_de_credito)

# mostrar os 10 primeiros elementos da base de crédito
print(base_de_credito.head(10))

# mostrar os 10 últimos elementos da base de crédito
print(base_de_credito.tail(10))

# descrever dados referentes a base de créditos
print(base_de_credito.describe())

# mostrar dados do cliente com o menor pedido de empréstimo
print(base_de_credito[base_de_credito["loan"] <= 1.377630])

# mostrar o cliente com a maior renda anual
print(base_de_credito[base_de_credito["income"] >= 69995])

# retorna os valores possíveis de default e quantas pessoas corresponderam a cada um deles
print(np.unique(base_de_credito["default"], return_counts=True))

# retorna um gráfico que mostra quantas pessoas corresponderam aos dois valores de default
print(sb.countplot(x=base_de_credito["default"]))

# mostrar um histograma da idade das pessoas
print(plot.hist(x=base_de_credito['age']))

# mostrar um histograma da renda anual das pessoas
print(plot.hist(x=base_de_credito["income"]))

# mostrar um histograma dos pedidos de empréstimo
print(plot.hist(x=base_de_credito["loan"]))

# mostrar vários gráficos, com ligações entre si em formato matricial, e com as cores representando quem pagou e quem não pagou
grafico = px.scatter_matrix(base_de_credito, dimensions=["age", "income", "loan"], color="default")
grafico.show()