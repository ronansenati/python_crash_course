#Armazenando suas funções em módulos
#Importando um módulo completo

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

#Importando funções específicas

from pizza import make_pizza

make_pizza(18, 'pepperoni') 
make_pizza(15, 'mushrooms', 'green peppers','extra cheese') 


#Usando a palavra reservada as para atribuir um alias a uma função

from pizza import make_pizza as mp

mp(16, 'pepperoni') 
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Usando a palavra reservada as para atribuir um alias a um módulo

import pizza as p

p.make_pizza(16, 'pepperoni') 
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

#Importando todas as funções de um módulo

from pizza import *

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers','extra cheese') 