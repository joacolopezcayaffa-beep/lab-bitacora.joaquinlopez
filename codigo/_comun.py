"""
Utilidades compartidas por los scripts de clase.

Resuelve la ruta del proyecto para que los scripts corran igual desde
cualquier carpeta, y centraliza el guardado de figuras.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")          # sin ventana: funciona en cualquier máquina
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]
SALIDAS = RAIZ / "salidas"
IMAGENES = RAIZ / "imagenes"
SALIDAS.mkdir(exist_ok=True)
IMAGENES.mkdir(exist_ok=True)
sys.path.insert(0, str(RAIZ))

SEMILLA = 2026


def guardar(nombre):
    """Guarda la figura actual en imagenes/ y la cierra."""
    ruta = IMAGENES / nombre
    plt.tight_layout()
    plt.savefig(ruta, dpi=110)
    plt.close()
    print(f"  [figura guardada] imagenes/{nombre}")


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)
