# Git e GitHub controle de versão parte 2

# pra que uma pessoa não atrapalhe outra por ser mesmo códito e funçoes diferentes na atuação..
# temos o conceito de ramificações de branchs. Para que haja uma ramificação pra que um outro código não seja inserido de imediato no codigo principal

# no canto esquerdo, em baixo do VS indica onde estou trablhando. A princípio é master, código principal

# agora vou criar um outro local que será a cópia do master pra que eu possa criar um código pra ser verificado

# no terminal usamos: git checkout -b "develop"  # dessa forma passamos do master para o branch develop
# para voltar para a branch master novamente é só usar no terminal assim: git checkout master
# no proprio VS dar para alternar entre as branch criadas.
# no caso de enviar para o github a versão atual, as mudanças, no caso do branch develop, o terminal vai pedir algumas coisas diferentes divdo mudança de branch. Ver os procedimentos na aula depois. 


import  pandas as pd
import matplotlib.pylab as plt
import numpy as np


# no site github (ondte o terminal indica pra executar algo) teremos  opções de verificar no master ou no develop, no caso aqui criado.
# TAmbém é possivel fazer a confirm merge, que é a mesclagem do código, daí passa a fazer parte também do código em master



