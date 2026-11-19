# Bitácora — Introducción a la Ciencia de Datos

Bitácora individual de Joaquín López Cayaffa para el curso **Introducción a la Ciencia de Datos** (UM, 2do semestre 2026, profesora Joselina Davyt).

## Estructura

```
.
├── README.md                este archivo
├── bitacora.md              entradas por clase con los temas trabajados
├── codigo/                  scripts de las clases y ejercicios
│   ├── _comun.py            utilidades compartidas (rutas, semilla, guardado de figuras)
│   ├── clase_01 … clase_15  scripts temáticos del curso
│   ├── carga de datos …     ejercicios propios de carga de datos
│   └── datos/
│       └── generador.py     generador de datos sintéticos usado por los scripts temáticos
├── data/                    datasets reales usados en ejercicios
├── imagenes/                figuras generadas al correr los scripts
├── salidas/                 CSVs intermedios generados al correr los scripts
└── clase2.py                ejercicio inicial
```

## Cómo correr los scripts

Desde la carpeta `codigo/`:

```bash
python clase_01_flujo_reproducible.py
```

Cada script imprime resultados por consola y guarda su figura en `imagenes/`.

## Dependencias

```bash
pip install pandas numpy matplotlib scipy statsmodels
```

## Reproducibilidad

Todos los scripts usan la misma semilla (`SEMILLA = 2026` en `codigo/_comun.py`) para que los resultados sean reproducibles.
