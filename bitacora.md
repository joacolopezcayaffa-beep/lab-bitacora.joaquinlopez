# Bitácora — Introducción a la Ciencia de Datos

Registro de las clases, con el script correspondiente y los temas trabajados.

---

## Clase 01 — Flujo reproducible
**Script:** `codigo/clase_01_flujo_reproducible.py`
Tres pilares de reproducibilidad: semillas aleatorias, rutas relativas y análisis de punta a punta. Si no fijás la semilla, dos corridas de un `random` dan distinto; con `SEMILLA = 2026` quedan idénticas. Las rutas absolutas rompen en otra máquina, por eso todo arranca desde `RAIZ`. Salida: `imagenes/clase01_ventas.png`.

---

## Clase 02 — Medición y muestreo
**Script:** `codigo/clase_02_medicion_muestreo.py`
Diferencia entre sesgo y varianza. Una muestra sesgada puede ser muy precisa y aun así estar sistemáticamente equivocada — el sesgo no se ve en la dispersión. Salida: `imagenes/clase02_muestreo.png`.

---

## Clase 03 — Calidad y estructura de datos
**Script:** `codigo/clase_03_calidad_estructura.py`
Limpieza de transacciones sucias: tipos mal cargados, duplicados, agregaciones. Salida: `salidas/clase03_transacciones_limpias.csv`.

---

## Clase 04 — Exploración y valores faltantes
**Script:** `codigo/clase_04_exploracion_faltantes.py`
Diagnóstico de NAs: cuántos faltan, dónde faltan, si el faltante correlaciona con otras variables. Mapa de faltantes. Salida: `imagenes/clase04_faltantes.png`.

---

## Clase 05 — Comparar grupos
**Script:** `codigo/clase_05_comparar_grupos.py`
Comparación entre grupos con test de permutación. Correcciones por múltiples pruebas: Bonferroni (conservador, controla el error familiar) vs Benjamini-Hochberg (controla la tasa de falsos descubrimientos). BH es el estándar cuando hay muchas pruebas. Salida: `imagenes/clase05_permutacion.png`.

---

## Clase 06 — Relaciones y reducción de dimensiones
**Script:** `codigo/clase_06_relacion_dimensiones.py`
PCA sobre un cuestionario. Los ítems se agrupan en dos bloques → el cuestionario mide dos cosas, no una. Útil para detectar cuando un índice supuestamente único en realidad esconde dimensiones distintas. Salida: `imagenes/clase06_pca.png`.

---

## Clase 07 — Series de tiempo, estructura
**Script:** `codigo/clase_07_series_estructura.py`
Descomposición de una serie en tendencia, estacionalidad y residuo. Medias móviles, autocorrelación (ACF). Salidas: `imagenes/clase07_movil.png`, `clase07_descomposicion.png`, `clase07_acf.png`.

---

## Clase 08 — Pronóstico y validación
**Script:** `codigo/clase_08_pronostico_validacion.py`
Validación de pronósticos. MAE vs sesgo medio: un sesgo medio alejado de cero es peor que un MAE alto porque indica error sistemático. Salida: `imagenes/clase08_pronostico.png`.

---

## Clase 09 — Estacionariedad y correlaciones espurias
**Script:** `codigo/clase_09_estacionariedad_espuria.py`
Dos series no estacionarias independientes generan correlaciones "significativas" el 79% de las veces en vez del 5% esperado. Es un problema estructural: hay que testear estacionariedad antes de correlacionar. Salida: `imagenes/clase09_espuria.png`.

---

## Clase 10 — Datos de panel
**Script:** `codigo/clase_10_panel_estructura.py`
Paradoja de Simpson aplicada a panel: la correlación dentro de cada unidad puede ser positiva y al agregar ser negativa. Siempre verificar la relación dentro de las unidades antes de agregar. Salida: `imagenes/clase10_panel.png`.

---

## Clase 12 — Cohortes y análisis de supervivencia
**Script:** `codigo/clase_12_cohortes_comparacion.py`
Comparación de cohortes con Kaplan-Meier. Las cohortes tardías tienen menos seguimiento → sus celdas lejanas están estimadas con pocos datos y no se pueden comparar directamente con las tempranas. Salidas: `imagenes/clase12_cohortes.png`, `clase12_km_planes.png`.

---

## Clase 13 — Experimentos A/B
**Script:** `codigo/clase_13_experimento_ab.py`
Diseño y análisis de A/B tests. Problema de los subgrupos: con suficientes subgrupos aparece uno "significativo" por azar. Regla: los subgrupos se declaran ANTES, o se corrigen por pruebas múltiples.

---

## Clase 14 — Diferencias en diferencias (DiD)
**Script:** `codigo/clase_14_did_evento.py`
Evaluación causal con DiD. Supuesto crítico: tendencias paralelas antes del evento. Si las brechas ya venían creciendo, lo que se mide no es el efecto de la intervención. Salidas: `imagenes/clase14_evento.png`, `clase14_did.png`.

---

## Clase 15 — Incertidumbre y comunicación
**Script:** `codigo/clase_15_incertidumbre_comunicacion.py`
Bootstrap para intervalos de confianza no paramétricos. Checklist de comunicación de resultados: qué tendría que ser cierto para que esté equivocado, y declarar dónde se usó asistencia de IA y cómo se verificó la salida. Salida: `imagenes/clase15_bootstrap.png`.

---

## Ejercicios propios de carga de datos

En `codigo/` también quedan los tres scripts de los primeros ejercicios de carga de datos con pandas:
- `carga de datos en python 2.py` — carga de `autoscope_01_2021_velocidad.csv`
- `carga de datos en python 22.py` — carga del CSV de residuos de la estación de transferencia
- `carga de datos en python velocidad.py` — segundo pase sobre el dataset de velocidad

Todos hacen la misma inspección básica: `info()`, `shape`, `nunique()`, `isnull()`, `duplicated()`.
