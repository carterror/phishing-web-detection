## Random Forest o Bosques aleatorios

En los bosques aleatorios (consulte las clases RandomForestClassifier y RandomForestRegressor), cada árbol del conjunto se construye a partir de una muestra extraída con reemplazo (es decir, una muestra de arranque) del conjunto de entrenamiento.

Además, al dividir cada nodo durante la construcción de un árbol, la mejor división se encuentra mediante una búsqueda exhaustiva de los valores de las características de todas las características de entrada o de un subconjunto aleatorio de tamaño max_features. (Consulte las pautas de ajuste de parámetros para obtener más detalles).

El propósito de estas dos fuentes de aleatoriedad es disminuir la varianza del estimador forestal. De hecho, los árboles de decisión individuales suelen presentar una gran variación y tienden a sobreajustarse. La aleatoriedad inyectada en los bosques produce árboles de decisión con errores de predicción algo desacoplados. Al tomar un promedio de esas predicciones, algunos errores pueden anularse. Los bosques aleatorios logran una variación reducida al combinar diversos árboles, a veces a costa de un ligero aumento en el sesgo. En la práctica, la reducción de la varianza suele ser significativa, por lo que se obtiene un mejor modelo en general.

A diferencia de la publicación original [B2001], la implementación de scikit-learn combina clasificadores promediando su predicción probabilística, en lugar de permitir que cada clasificador vote por una sola clase.

Una alternativa competitiva a los bosques aleatorios son los modelos de aumento de gradiente basado en histogramas (HGBT):

Construcción de árboles: los bosques aleatorios generalmente dependen de árboles profundos (que se adaptan individualmente) que utilizan muchos recursos computacionales, ya que requieren varias divisiones y evaluaciones de divisiones candidatas. Los modelos de impulso construyen árboles poco profundos (que no se ajustan individualmente) que son más rápidos de ajustar y predecir.

Impulso secuencial: En HGBT, los árboles de decisión se construyen de forma secuencial, donde cada árbol es entrenado para corregir los errores cometidos por los anteriores. Esto les permite mejorar iterativamente el rendimiento del modelo utilizando relativamente pocos árboles. Por el contrario, los bosques aleatorios utilizan una votación mayoritaria para predecir el resultado, lo que puede requerir una mayor cantidad de árboles para lograr el mismo nivel de precisión.

Agrupación eficiente: HGBT utiliza un algoritmo de agrupación eficiente que puede manejar grandes conjuntos de datos con una gran cantidad de funciones. El algoritmo de agrupación puede preprocesar los datos para acelerar la construcción posterior del árbol (consulte Por qué es más rápido). Por el contrario, la implementación scikit-learn de bosques aleatorios no utiliza agrupación y se basa en una división exacta, lo que puede resultar costoso desde el punto de vista computacional.

En general, el costo computacional de HGBT versus RF depende de las características específicas del conjunto de datos y la tarea de modelado. Es una buena idea probar ambos modelos y comparar su rendimiento y eficiencia computacional en su problema específico para determinar qué modelo se adapta mejor.