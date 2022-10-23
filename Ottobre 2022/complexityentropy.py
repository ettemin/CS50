from math import log2, factorial
import csv
import numpy as np

# Creazione dell'array dove inserire la serie temporale

arr0=[]

# Importazione della serie temporale da un file csv

with open('csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='¿')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            arr0=(row[1].replace(";"," ")).split()
            line_count += 1
        else:
            line_count += 1

# Conversione della serie temporale da string a float

arr0 = list(map(float, arr0))

# Scelta della embedding dimension

dimensione=5

# Creazione della matrice composta da (arr0 - embedding dimension + 1) elementi

obj={}
obj2={}
listacopiata=[]
for i in range(len(arr0)-(dimensione)+1):
    lista=[]
    listadatenere=[]
    for j in range((dimensione)):
        lista.append(arr0[i+j])
    listacopiata=lista.copy()
    listadatenere=lista.copy()
    listacopiata.sort()
    for j in range(len(listacopiata)):
        for k in range(len(lista)):
            if lista[k]==listacopiata[j]:
                lista[k]=j
    obj[i]=listadatenere
    obj2[i]=lista

permutazionebase=[]
for i in range(dimensione):
    permutazionebase.append(i)

# Mappatura della permutazione

p=[]
oggettofinale={}
def permute(lst, f=0):
    if f>=len(lst):
        n=0
        for i in range(len(obj2)):
            if lst==obj2[i]:
                n=n+1
        oggettofinale[str(lst)]=n
        return
    for s in range (f, len(lst)):
        lst[f], lst[s] = lst[s], lst[f]
        permute(lst, f+1)
        lst[f], lst[s] = lst[s], lst[f]
permute(permutazionebase)

sommatoria=0
distribuzioneprobabilita=[]

# Calcolo della permutazione finale

for i in (oggettofinale):
    if oggettofinale[i]!=0:
        divisione=float(oggettofinale[i]/len(obj2))
        distribuzioneprobabilita.append(divisione)
        logaritmo=log2(divisione)
        sommatoria=sommatoria+(divisione)*logaritmo
permutationentropy = (-1*sommatoria)*(1/(log2(factorial(dimensione))))

data_1=[]
data_1 = distribuzioneprobabilita.copy()
data_2=[]
N=1/len(distribuzioneprobabilita)
for i in range(len(distribuzioneprobabilita)):
    data_2.append(N)

# Computazione della divergenza di Kullback–Leibler

"""KL Divergence(P|Q)"""
def KLD(p_probs, q_probs):    
    KLD = p_probs * np.log(p_probs / q_probs)
    return np.sum(KLD)
    
# Computazione della divergenza di Jensen-Shannon

def JSD(p, q):
    p = np.asarray(p)
    q = np.asarray(q)
    # Normalizzazione
    p /= p.sum()
    q /= q.sum()
    m = (p + q) / 2
    return (KLD(p, m) + KLD(q, m)) / 2
    
# Risultati
'''data_1 e data_2 sono le distribuzioni di probabilità rispettivamente del sistema e della distribuzione equiprobabile'''

result_JSD12= JSD(data_1, data_2)
print("The permutation entropy is ",permutationentropy)
print("The JS Divergence between data_1 and data_2",result_JSD12)
print("The complexity measure is ", result_JSD12*permutationentropy)