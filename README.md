# Tarea2RedesNeuronales

## Como correr la tarea?

1) crear un ambiente virtual (virtualenv venv) y activarlo (source venv/bin/activate )
2) instalar los requiriments.txt (pip install -r requirements)
3) correr el archivo graphFitness.py con python3 (python3 graphFitness.py)
4) correr el archivo heatMap.py con python3 (python3 heatMap.py)
5) ver resultados

## Que hay en este repositorio?

1)analisisFindWord.py: archivo que corre el analisis de el algoritmo que encuentra una palabra
2) carpeta algoritmosGeneticos, la cual contiene 3 carpetas:

    -boundknapsack: algoritmo con su suite de funciones que resuelve
        el problema de la mochila con restricciones.
        
    -findingWords: algoritmo que encuentra una palabra.
    
    -tests.

## que hay en la carpeta boundKanpsack?
1) knapsuite.py: es un archivo python que contiene la clase knapsack:
    esta recibe un arreglo de valores, un arreglo de pesos y un peso maximo.
    tambien esta clase posee un mascara de bits (este es el gen), la cual es un arreglo del mismo largo 
    de los otros dos arreglos donde en la posicion i, un 1 indica que la mochila contiene el articulo i.
    (un 0 indica que no lo contiene).
    
    la clase ademas contiene funciones importantes como la funcion fitness, la cual calcula el fitness de 
    un knapsack como la multiplicacion punto a punto entre el arreglo de valores por la mascara de bits, luego suma en la
    dimension 0. se hace lo mismo para el peso y si se excede el peso maximo entonces se aplica un castigo
    que es dividir el valor por la mitad (asi se controla a la poblacion).
    
    otras funcion importante es la mutacion, que lo que hace es prender o apagar bits de la mascara de bits.
    por ultimo la funcion crossOver que mescla 2 mascaras de dos knapsacs.
    
2) geneticEngine.py: es el motor de el algoritmo genetico el cual posee la funcion find, que es la que se encarga de
    crear las poblaciones, poner a competir a los individuos y reproducirlos.




## analisis

Para este analisis, se decidio que se analizaria el ejercicio 2, de encontrar palabras. Se realizan una serie de experimentos que analizaremos a continuacion.


### grafico fitness para oración grande:

Reference-style: 
![alt text][porcentaje]

[porcentaje]: src/findWordFitness.png

El color rojo representa el fitness de el mejor individuo a travez de el tiempo, el color amarillo representa
el fitness de el promedio de la poblacion, mientras que el azul representa el fitness de el peor individuo

se puede observar que en general todos los individuos tienden al fitness maximo, esto puede deverse a que 
el algoritmo genetico está funcionando bien.

(si la foto no se ve, ver src/findWordFitness.png)

### heatMap poblacion v/s mutabilidad.

Reference-style: 
![alt text][heatMap]

[heatMap]: src/findWordHeatMap.png


en el siguiente heatMap, en el eje Y se encuentra la cantidad de población (donde en la parte de abajo hay mas poblacion=9*50 individuos)
en el eje x se encuentra la probabilidad de mutabilidad (donde en la parte derecha esta el 100% de probabilidad)

en cuanto a los colores, colores frios (azul) representa que se encontro rapidamente la palabra, mientras que colores calidos
(rojo) representa que se demoro mas. Observamos que mientras mas poblacion y mas probabilidad de mutabilidad, es mas rapido encontrar al individuo
sin embargo lo que da mas peso es la población.


(si la foto no se ve, ver src/heatMap.png)


##Extra

- si las fotos no se pueden ver, estan en la carpeta src

