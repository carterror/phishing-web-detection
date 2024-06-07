# Proyecto: Detección de Sitios Web de Phishing usando Aprendizaje Automático
 
## Dataset Seleccionado
Mohammad,Rami and McCluskey,Lee. (2015). Phishing Websites. UCI Machine Learning Repository. https://doi.org/10.24432/C51W2X.

## Descripción

Este proyecto tiene como objetivo detectar sitios web de phishing utilizando técnicas de aprendizaje automático. Utiliza el dataset "Phishing Websites" del repositorio UCI Machine Learning, que contiene 30 características y 11,055 instancias.

## Estructura del Proyecto

1. **Instalación de Bibliotecas**: Instalación de las bibliotecas necesarias (`scipy`, `pandas`, `scikit-learn`).
2. **Carga y Preprocesamiento del Dataset**: Carga del archivo `.arff` y conversión a un DataFrame de pandas.
3. **Decodificación de Columnas**: Conversión de columnas categóricas de bytes a strings.
4. **Separación de Características y Etiquetas**: División del dataset en características (`X`) y etiquetas (`y`).
5. **División del Conjunto de Datos**: División en conjuntos de entrenamiento y prueba.
6. **Entrenamiento del Modelo**: Entrenamiento de un modelo de Random Forest [Explicación RandomForest](./RandomForest.md).
7. **Predicción y Evaluación**: Predicción con el conjunto de prueba y evaluación del modelo.

## Requisitos

- [Python 3.x](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
    - [numpy](https://numpy.org/)
- [scipy](https://scipy.org/)
- [scikit-learn](https://scikit-learn.org/)

### Las extensiones VSCode utilizadas son: `ms-toolsai.jupyter`
- Name: Jupyter
- Id: ms-toolsai.jupyter
- Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.
- Version: 2024.4.0
- Publisher: Microsoft
- VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

## Instalación

Instala las bibliotecas necesarias ejecutando:
```bash
# crear entorno virtual con python
python -m venv venv

## instalar dependencias
pip install requirements.txt
```

## Uso
Esta explicado en cada paso del main.ipynb

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un issue para discutir lo que te gustaría cambiar.

## Licencia

Este proyecto está bajo la licencia MIT. 