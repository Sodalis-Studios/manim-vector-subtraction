# Resta de vectores con Manim

Pequeña animación sobre la resta de vectores creada con [Manim Community](https://www.manim.community/).
Explica por qué **B − A** es el vector que va de la punta de **A** a la punta de **B**, primero con números y después de forma geométrica.

<p align="center">
  <img src="docs/vector_subtraction.gif" alt="Vista previa de la animación" width="720">
</p>

## Vídeo

Esta animación se ha utilizado para el siguiente vídeo de YouTube sobre el tema:

[![Ver el vídeo en YouTube](https://img.youtube.com/vi/9t3l1HUXTE8/maxresdefault.jpg)](https://www.youtube.com/watch?v=9t3l1HUXTE8)

## Qué se explica

1. **Sección numérica:** definición de `A` y `B` por componentes y cálculo de `B − A`.
2. **Sección visual:** los vectores en el plano y `R = B − A` dibujado de la punta de `A` a la punta de `B`.
3. **Forma polar:** ángulo `θ` y magnitud `‖R‖`, con el vector como vector libre.
4. **Resta como suma:** `B − A = (−A) + B`, comprobado geométricamente.
5. **Recorrido:** de `A` al origen y del origen a `B`, y el recorrido inverso que da `−R`.
6. **Conclusiones:** El sentido sigue `Destino − Origen` y los vectores son libres.

## Requisitos

- Python (versión indicada en [`.python-version`](.python-version))
- [uv](https://docs.astral.sh/uv/)
- **LaTeX** (las fórmulas usan `MathTex`), por ejemplo [TeX Live](https://tug.org/texlive/) o [MiKTeX](https://miktex.org/)
- Las dependencias del sistema de Manim (FFmpeg, Cairo, Pango). Consultar la [guía de instalación oficial](https://docs.manim.community/en/stable/installation.html).

## Uso

```bash
git clone https://github.com/joaquin-salas/manim-vector-subtraction.git
cd manim-vector-subtraction
uv sync
```

Renderizar en baja calidad (480p, 15 fps):

```bash
uv run manim -pql src/vector_subtraction.py VectorSubtraction
```

Renderizar en full HD (1080p, 60 fps):

```bash
uv run manim -pqh src/vector_subtraction.py VectorSubtraction
```

Renderizar en 2K (1440p, 60 fps):

```bash
uv run manim -pqp src/vector_subtraction.py VectorSubtraction
```

El vídeo se guarda en la carpeta `media/videos/`.

## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
