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

# mostrar os dados exigidos
print(base_de_credito.loc[base_de_credito["age"]<0])

# outra forma mostrar de mostrar os dados exigidos
print(base_de_credito[base_de_credito["age"]<0])

# excluir os dados da tabela
base_de_credito2 = base_de_credito.drop("age", axis=1)
print(base_de_credito2)

# outra forma de excluir os dados da tabela
base_de_credito3 = base_de_credito.drop(base_de_credito[base_de_credito["age"]<0].index)
print(base_de_credito3)

# acessar os locais na base de créditos, com os dados excluídos, para verificar se, realmente, foram apagados
print(base_de_credito3.loc[base_de_credito3["age"]<0])

# mostrar as médias como base para fazer operações necessárias
print(base_de_credito.mean())

# mostrar a médias dos dados que respeitam a condição de idade maior que 0
print(base_de_credito["age"][base_de_credito["age"]>0].mean())

# fazer os créditos receberem determinado resultado, mas, ocorre um erro que faz toda a linha receber o mesmo valor
base_de_credito.loc[base_de_credito["age"]<0] = 40.9
print(base_de_credito.loc[base_de_credito["age"]<0])
# mostrar um histograma da idade das pessoas
print(plot.hist(x=base_de_credito['age']))

# mostrar um histograma da renda anual das pessoas
print(plot.hist(x=base_de_credito["income"]))

# mostrar um histograma dos pedidos de empréstimo
print(plot.hist(x=base_de_credito["loan"]))

# mostrar vários gráficos, com ligações entre si em formato matricial, e com as cores representando quem pagou e quem não pagou
grafico = px.scatter_matrix(base_de_credito, dimensions=["age", "income", "loan"], color="default")
grafico.show()
