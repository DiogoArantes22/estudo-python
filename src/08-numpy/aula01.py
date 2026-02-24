import numpy as np

#array numpy: uma estrutura de dados que armazena elementos do mesmo tipo, organizados em uma grade multidimensional.

#ndarray: é a estrutura de dados fundamental do NumPy, que representa um array multidimensional. Ele é eficiente em termos de memória e desempenho, permitindo operações rápidas em grandes conjuntos de dados.

#1-D-arrays: são arrays de uma dimensão, ou seja, vetores. Eles podem ser usados para armazenar sequências de números, como uma lista de temperaturas ou uma série temporal.
#2-D-arrays: são arrays de duas dimensões, ou seja, matrizes. Eles podem ser usados para representar tabelas de dados, imagens ou qualquer outra 
# estrutura bidimensional.
#3-D-arrays: são arrays de três dimensões, ou seja, tensores. Eles podem ser usados para representar dados volumétricos, como imagens 3D ou séries temporais com múltiplas variáveis.

# %%
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print(type(a))

# %%
#np.zeros: é uma função do NumPy que cria um array preenchido com zeros. Ela é útil para inicializar arrays antes de preenchê-los com dados reais. O parâmetro "shape" define as dimensões do array, e o resultado é um array de zeros com as dimensões especificadas.
import numpy as np
zero_array = np.zeros(shape = (5,3,6))
print(zero_array)

# %%

# np.ones: é uma função do NumPy que cria um array preenchido com uns. Assim como np.zeros, ela é útil para inicializar arrays antes de preenchê-los com dados reais. O parâmetro "shape" define as dimensões do array, e o resultado é um array de uns com as dimensões especificadas.
import numpy as np
um_array = np.ones((2,4))
print(um_array)

# %%

# np.empty: é uma função do NumPy que cria um array sem inicializar seus valores. Isso significa que os elementos do array podem conter valores aleatórios ou lixo de memória. O parâmetro "shape" define as dimensões do array, e o resultado é um array vazio com as dimensões especificadas. É importante notar que os valores contidos em um array criado com np.empty não são definidos e podem variar a cada execução.
import numpy as np
vazio_array = np.empty((3))
print(vazio_array)

# %% 

 #np.arange: é uma função do NumPy que cria um array com uma sequência de números. Ela é semelhante à função range do Python, mas retorna um array em vez de uma lista. O parâmetro "start" define o valor inicial da sequência, "stop" define o valor final (exclusivo) e "step" define o intervalo entre os valores. O resultado é um array contendo a sequência de números especificada.
import numpy as np
arr = np.arange(50,200,30)
print(arr)

# %%

#np.linspace: é uma função do NumPy que cria um array com uma sequência de números igualmente espaçados entre um valor inicial e um valor final. O parâmetro "start" define o valor inicial da sequência, "stop" define o valor final (inclusivo) e "num" define o número de elementos na sequência. O resultado é um array contendo a sequência de números igualmente espaçados.
import numpy as np
array_linear = np.linspace(0, 100 , num = 20, endpoint = False, retstep = True)
print(array_linear)

# %%
import numpy as np

#Descobrindo o tamanho do array 

zero_array = np.zeros(shape = (5,3,6))
print(zero_array)

#shape: é um atributo do NumPy que retorna as dimensões de um array. Ele é representado como uma tupla, onde cada elemento da tupla corresponde ao tamanho de uma dimensão do array. Por exemplo, se um array tem a forma (5, 3, 6), isso significa que ele tem 5 elementos na primeira dimensão, 3 elementos na segunda dimensão e 6 elementos na terceira dimensão.
print(zero_array.shape)

#size: é um atributo do NumPy que retorna o número total de elementos em um array. Ele é calculado multiplicando-se as dimensões do array. Por exemplo, se um array tem a forma (5, 3, 6), o tamanho seria 5 * 3 * 6 = 90, indicando que o array contém um total de 90 elementos.
print(zero_array.size)

#ndim: é um atributo do NumPy que retorna o número de dimensões de um array. Ele indica quantas dimensões o array possui. Por exemplo, se um array tem a forma (5, 3, 6), ele tem 3 dimensões, e o valor de ndim seria 3.
print(zero_array.ndim)

# %%
import numpy as np

#Transformando um vetor em matriz
# newaxis: é um objeto do NumPy que é usado para adicionar uma nova dimensão a um array. Ele é frequentemente utilizado para transformar um vetor unidimensional em uma matriz bidimensional ou para adicionar uma dimensão extra a um array existente. Por exemplo, se você tem um vetor de forma (3,) e deseja transformá-lo em uma matriz de forma (3, 1), você pode usar newaxis para adicionar uma nova dimensão.
a = np.array( [ 1, 2, 3])
print(a.shape, a.ndim)

a21 = a[np.newaxis,:]
print(a21.shape)
print(a21.ndim)
print(a21)

a22 = a[:, np.newaxis]
print(a22.shape)
print(a22.ndim)
print(a22)

#Acessando dado específico de um array
print(a22[0][0])

# %%
import numpy as np

#Concatenando arrays
# np.concatenate: é uma função do NumPy que é usada para concatenar ou juntar arrays ao longo de um eixo específico. Ela permite combinar arrays de forma eficiente, criando um novo array que contém os elementos dos arrays originais. O parâmetro "axis" define o eixo ao longo do qual os arrays serão concatenados. Por exemplo, se você tem dois arrays de forma (2, 3) e deseja concatená-los ao longo do eixo 0, o resultado será um array de forma (4, 3), onde os elementos dos dois arrays originais são combinados verticalmente.

a = np.array( [1, 2, 3])
b = np.array( [4, 5, 6])

c=np.concatenate((a,b))
d=np.concatenate((b,a))

print(c)
print(d)

# %%
import numpy as np

# Consultando itens específicos de um array

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print('------------')
print(a[a<8])

# %%
import numpy as np

#Operações aritméticas em arrays

a = np.array( [1, 2, 3])

print(a.max())
print(a.min())
print(a.mean())
print(a.sum())
# %%
import numpy as np
from numpy.random import default_rng

#Gerando números aleatórios
# np.random: é um módulo do NumPy que fornece funções para gerar números aleatórios. Ele inclui uma variedade de funções para criar arrays de números aleatórios, como np.random.rand para gerar números aleatórios entre 0 e 1, np.random.randint para gerar números inteiros aleatórios dentro de um intervalo específico, e np.random.normal para gerar números aleatórios seguindo uma distribuição normal. Essas funções são úteis para simulações, amostragem e outras aplicações que requerem a geração de dados aleatórios.

rng= default_rng()
aleatorio = rng.integers(10, size=(2,4))
print(aleatorio)

# %%
import numpy as np
#Diferença entre Arrys e Listas
# Arrays do NumPy são mais eficientes em termos de memória e desempenho do que as listas do Python, especialmente para operações matemáticas e manipulação de grandes conjuntos de dados. Eles também oferecem uma ampla gama de funções e métodos para realizar operações complexas em arrays, como operações aritméticas, estatísticas e de álgebra linear. Por outro lado, as listas do Python são mais flexíveis e podem conter elementos de diferentes tipos, mas não são otimizadas para operações matemáticas ou manipulação de grandes conjuntos de dados.

a = np.array([1,3,4,5,6,5,7,8])
print("Essa é o array 'a':",a)
print("Esse é tipo de 'a':",type(a))
print('-------------------------------------')
lista_a=[1,3,4,5,6,5,7,8]
print("Essa é a 'lista_a':", lista_a)
print("Esse é tipo de 'lista_a':",type(lista_a))

#arrays não permitem tipos de dados distintos:
a = np.array([1,'Daniel',2,3,4,5,6,7,8])
print(a)
print(type(a[0]))

#já as listas sim:
lista_a = [1,'Daniel',2,3,4,5,6,7,8]
print(a)
print(type(lista_a[0]))

# %%

import numpy as np

from time import process_time
lista_a = list(rng.integers(10, 100, 10000000))
print(type(lista_a))
lista_b = list(rng.integers(10, 100, 10000000))
c = lista_a*lista_b 

print(type(lista_a))
print(len(lista_a))

c=[]
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i] * lista_b[i])
t2 = process_time()

print(t2-t1)

a = rng.integers(10, 100, 10000000)
b = rng.integers(10, 100, 10000000)
print(type(a))
print(a)
t1a=process_time()
c=a*b
t2a=process_time()
print(t2a-t1a)

# %%
import matplotlib.pyplot as plt
import numpy as np

dados_x = rng.integers(20, size = 30)
dados_y = rng.integers(12, size = 30)

plt.scatter(x = dados_x, y = dados_y)
plt.show()