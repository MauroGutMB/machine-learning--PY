import pandas
import seaborn
import matplotlib.pyplot as plt
import plotly.express as px

data = pandas.read_csv("Preços_de_casas.csv")
data.info()
data = data.drop(columns = "Id")

correlacao = data.corr()


# print("\n\n\n", correlacao['preco_de_venda'])


# plt.scatter(data['area_primeiro_andar'], data['preco_de_venda'])
# plt.title("Relação entre Área e Preço")
# plt.axline(xy1 = (66, 250000), xy2 = (190, 1800000), color = "red")
# plt.xlabel("Área do primeiro andar")
# plt.ylabel("Preço de venda")

img = px.scatter(data, x = 'area_primeiro_andar', y = 'preco_de_venda', trendline_color_override="red", trendline = 'ols' )

# plt.savefig("areaXpreco-px.png")
# img.write_image("areaXpreco-px.png")
img.show()
