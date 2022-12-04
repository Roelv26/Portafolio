#Equipo 5:
#Edgar Castillo Ramírez A00827826
#Roel De la Rosa Castillo	A01197595
#Rodrigo Montelongo Pinales A00827757
#Juan Pablo Yáñez González A00829598		
#Héctor San Román Caraza A01422876
#Miguel Alejandro Salas Reyna A00827219

#CKY Algorithm implementation

#Paso 1. Implementar en Python la estructura de la matriz de análisis sintáctico (CKY).

from collections import OrderedDict

phrase = "time flies like an arrow".split()

n = len(phrase)

matrixCKY = [[OrderedDict() for j in range(n)] for i in range(n)]

fullSentence = set()

#Paso 2. Implementar en Python la representación de la gramática proporcionada.
non_terminals = ["S", "NP", "VP", "PP", "Det", "Nominal", "Verb", "Preposition", "Noun"]

terminals = ["time", "flies", "arrow", "an", "like",]
 
# Reglas y probabilidad
R = {
    "S": [["NP", "VP", 0.800]],
    "NP": [["time", 0.002], ["flies", 0.002], ["arrow", 0.002], ["Det","Nominal", 0.300], ["Nominal", "Nominal", 0.200]],
    "Nominal": [["time", 0.002],["flies", 0.002],["arrow", 0.002],["Nominal","Noun", 0.100],["Nominal","PP", 0.200]],
    "VP": [["time", 0.004],["flies", 0.008],["like", 0.008],["Verb","NP", 0.300],["Verb","PP", 0.200]],
    "PP": [["Preposition", "NP", 0.100]],
    "Verb": [["time", 0.010], ["flies", 0.020], ["like", 0.020]],
    "Noun": [["time", 0.010],["flies", 0.010],["arrow", 0.010]],
    "Det": [["an", 0.050]],
    "Preposition": [["like", 0.050]]
    }

#Paso 3. Implementar en Python el algoritmo CKY probabilístico.
#Paso 4. Aplicar el algoritmo a la frase que se quiere analizar usando la matriz tabla, operando por columnas de abajo arriba y de izquierda a derecha. Para cada celda se deben determinar los constituyentes sintácticos posibles y calcular sus probabilidades.
for j in range (0,n):
    for lhs, rule in R.items(): 
        for rhs in rule:
            if len(rhs) == 2 and rhs[0] == phrase[j]:
                matrixCKY[j][j][lhs] = rhs[1]

        for i in range(j, -1, -1):  
              
            for k in range(i, j + 1):    
 
                for lhs, rule in R.items():
                    for rhs in rule:
                         
                        if(k + 1 < n):
                            if len(rhs) == 3 and rhs[0] in matrixCKY[i][k] and rhs[1] in matrixCKY[k + 1][j]:
                                matrixCKY[i][j][lhs]= rhs[2]*matrixCKY[i][k][rhs[0]]*matrixCKY[k + 1][j][rhs[1]]
                                if lhs == "S" and i == 0 and j == n-1:
                                    fullSentence.add(matrixCKY[i][j][lhs])

#Paso 5. Implementar el algoritmo para el cálculo de la ruta de Viterbi más probable. Como resultado se debe obtener el árbol de análisis sintáctico más probable.
for j in range (0,n):
    #Se imprime la matriz, no es muy visual
    print(matrixCKY[j])
    print()

#Aquí se imprimen todas las S finales que se encontraron en la casilla de la esquina superior derecha. Se hace de esta manera pues la manera en la que se almacenan los datos no permite que existan duplicados, ya que sobreescribe. Sin embargo, las S encontradas
#se almacenan en este set para ser presentadas finalmente.
print("S encontradas: ", fullSentence)
print()

#Paso 6. Proponer una forma de representación del árbol.
#Según los resultados encontrados la estructura del árbol para la S con mayor probabilidad (9.600000000000004e-13) sería:
print("S -> NP(0,0) & VP(1,4)")
print("NP -> Verb(0,1) & PP(2,4)")
print("PP -> Prep(2,2) & NP(3,4)")
print("NP -> Det(3,3) & Nominal(4,4)")

#Por lo tanto se tiene que:
print("NP: Time, Verb: Flies, Prep: Like, Det: An, Nominal: Arrow")