# Galaxy classification using convolutional networks

[Enlace al cuaderno jupyter](https://colab.research.google.com/drive/1fEvicnUxsuY2gYEj2rAO_zAFWn50vPo4?usp=sharing)

This repository contains a set of tools and data for generating and working with galaxies images, specifically for training purposes. The project includes code for sampling images, as well as CSV files that track various galaxy-related information.

## Estructura del directorio

- `galaxy.py`: Archivo principal donde se crea el modelo y se entrena.
- `galaxies/`: Directorio que contiene las imágenes que vamos a usar en el entrenamiento. Tamaño 10 000.
- `images_sampler.py`: Un script en python que se encarga de seleccionar las imágenes que se van a usar del conjunto.
- `images_training_rev1/`: Directorio que contiene todas las imágenes de galaxias descargadas desde `kaggle`.
- `random_galaxies.csv`: Archivo CSV que contiene los datos de las galaxias que se usarán en el entrenamiento.
- `training_solutions.csv`: Archivo CSV que contiene los datos de TODAS las galaxias.

## Uso

### 1. **Samplear imágenes aleatorias de galaxias**

Puedes usar el archivo `images_sampler.py` para seleccionar imágenes aleatorias y galaxias y almacenarlas en el directorio de `galaxies/`.

Para ejecutar el script:

```bash
python images_sampler.py
```
