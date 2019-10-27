
#A função consiste de 3 entradas, 2 obrigatórias e 1 opcional
#references é a lista conforme a entrada, com os números dos processos dentro de uma lista
#N é o número de quadros que podem ser ocupados
#should_print é uma variável não obrigatória. Se sua entrada for 1, a função ao ser executada irá printar o número de cada iteração, como os quadros estão e o número de falhas a cada iteração
#Caso nada seja colocado na entrada, ela não printará nada
#A saída da função é o número de falhas que acontecem
def algoritmo_fifo(references, N, should_print=0):
  locais_RAM = []
  falhas = 0
  
  for i in range(0,len(references)):
    if references[i] not in locais_RAM:
      falhas+=1
      locais_RAM.append(references[i])
      if len(locais_RAM)>N:
        locais_RAM.remove(locais_RAM[0])
    
    if should_print==1:
      print('iteração ' + str(i))
      print('entrada: ' + str(references[i]))
      print('Quadros: ' + str(locais_RAM))
      print('Numero de falhas: ' + str(falhas))
      print('')
  
  return falhas


#A função consiste de 3 entradas, 2 obrigatórias e 1 opcional
#references é a lista conforme a entrada, com os números dos processos dentro de uma lista
#N é o número de quadros que podem ser ocupados
#should_print é uma variável não obrigatória. Se sua entrada for 1, a função ao ser executada irá printar o número de cada iteração, como os quadros estão e o número de falhas a cada iteração.
#Caso nada seja colocado na entrada, ela não printará nada
#A saída da função é o número de falhas que acontecem
def algoritmo_lru(references, N, should_print=0):
  locais_RAM = []
  falhas = 0
  
  for i in range(0,len(references)):
    if references[i] not in locais_RAM:
      falhas+=1
      locais_RAM.append(references[i])
      if len(locais_RAM)>N:
        locais_RAM.remove(locais_RAM[0])
    if references[i] in locais_RAM:
      locais_RAM.remove(references[i])
      locais_RAM.append(references[i])
    
    if should_print==1:
      print('iteração ' + str(i))
      print('entrada: ' + str(references[i]))
      print('Quadros: ' + str(locais_RAM))
      print('Numero de falhas: ' + str(falhas))
      print('')
  
  return falhas


#Função necessária para o algoritmo Otimo
def procura_ultimo_elemento(references, locais_RAM):
  posicao_processo=[-1]*len(locais_RAM)
  
  #confere se algum elemento da lista não se repete mais no resto do processo
  #caso algum não se repita, ele é o elemento retirado
  for i in locais_RAM:
    try:
      references.index(i)
    except ValueError:
      return i
    
  #caso todos os elementos vão se repetir em algum momento, procura o último a se repetir
  for i in range(0,len(locais_RAM)):
    posicao_processo[i]=references.index(locais_RAM[i])
  return locais_RAM[posicao_processo.index(max(posicao_processo))]

#A função consiste de 3 entradas, 2 obrigatórias e 1 opcional
#references é a lista conforme a entrada, com os números dos processos dentro de uma lista
#N é o número de quadros que podem ser ocupados
#should_print é uma variável não obrigatória. Se sua entrada for 1, a função ao ser executada irá printar o número de cada iteração, como os quadros estão e o número de falhas a cada iteração.
#Caso nada seja colocado na entrada, ela não printará nada
#A saída da função é o número de falhas que acontecem
def algoritmo_otimo(references, N, should_print=0):
  locais_RAM = []
  falhas = 0
  
  for i in range(0,len(references)):
    if references[i] not in locais_RAM:
      falhas+=1
      locais_RAM.append(references[i])
      if len(locais_RAM)>N:
        locais_RAM.remove(procura_ultimo_elemento(references[i:],locais_RAM[:N]))
    
    if should_print==1:
      print('iteração ' + str(i))
      print('entrada: ' + str(references[i]))
      print('Quadros: ' + str(locais_RAM))
      print('Numero de falhas: ' + str(falhas))
      print('')
  
  return falhas

in_list=[]
f = open("simulacao.txt", "r")
in_lines=f.readlines()
for i in in_lines:
    in_list.append(int(i))
f.close()

N=in_list[0]
references=in_list[1:]

falhas_fifo=str(algoritmo_fifo(references,N))
falhas_lru=str(algoritmo_lru(references,N))
falhas_otimo=str(algoritmo_otimo(references,N))

file_results=open('out.txt','w')
file_results.write(str(N) + ' quadros,    ' + str(len(references)) + ' refs:\n')
file_results.write('FIFO: ' + falhas_fifo + '\n')
file_results.write('LRU: ' + falhas_lru + '\n')
file_results.write('OTIMO: ' + falhas_otimo + '\n')
