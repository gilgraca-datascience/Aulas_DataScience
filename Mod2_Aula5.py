# Git (Csistema de ontrole de versão de arquivos) e GitHub Controle de versão parte 1. Ex: tem uma função que não se usa mais, mas o chefe pediu pra usar novamente. Como recuperar essa versão pra usar a função?

# O Git é um software que precisa ser instalado no computador. e depois criar o repositório num diretório para salvamento das versões. Isso se faz abrindo o proprio terminal do Git 

# No controle de versão para poder salvar na núvem, o que é que faz de fato, precisa usar o terminal para tanto:

# usar esse código para salvar uma versão, toda vez que houver uma mudança:
## git add Mod2_Aula5.py  # Esse serve para adicionar o arquivo
## git commit -m "my first commit"
# Agora com o github já aberto e com a conta criada, criar um repositório lá e vincular o nosso arvuivo aqui.
## usar então no terminal assim: De acordo com o que foi feito. git remote add origin https://github.com/gilgraca-datascience/Aulas_DataScience.git
# toda vez que precisar salvar uma versão do código (Salvar o codigo antes disso), usar o terminal nos seguintes passos:
##git add Mod2_Aula5.py
##git commit -m "Mensagem descritiva da mudança"
##git push # para enviar o arquivo pra nuvem github

import pandas as pd
import matplotlib.pylab as plt
import numpy as np


