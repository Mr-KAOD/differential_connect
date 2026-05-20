import reflex as rx
from differential_connect.components.layout import base_layout

def index() -> rx.Component:
    # Contenido específico de la página de bienvenida
    page_content = rx.vstack(
        rx.heading("¡Bienvenidos a Differential Connect!", size="8", color="#f8fafc", margin_bottom="10px"),
        rx.text(
            "La mejor plataforma de tutorías en Cálculo diferencial.",
            color="#94a3b8",
            font_size="18px"
        ),
        
        # USO DE LATEX
        rx.box(
            rx.vstack(
                rx.badge("Límites", color_scheme="blue", margin_bottom="10px"),
                rx.heading("Temario", size="4", color="#22d3ee"),
                rx.text(
                    "En análisis real y complejo, la teoría de límite es la clave de toque que formaliza la noción intuitiva de aproximación hacia un punto concreto de una sucesión o una función, a medida que los parámetros de esa sucesión o función se acercan a un determinado valor. En el análisis los conceptos de series convergentes, derivada e integral definida se fundamentan mediante el concepto de límite.",
                    color="#cbd5e1"
                ),
                # El componente rx.markdown procesa LaTeX encerrándolo entre signos de $
                rx.markdown(
                    "Sea $$ A = \{a_1, a_2\},\\dots  = \{a_n\}$$ una sucesión de elementos en un espacio métrico $$( X , d )$$. Se dice que $$L ∈ X$$ es el límite de la sucesión $$ \{ A \}$$ y se denota como:"
                    " $$\\lim_{h \\to \infty} = L$$",
                    color="#f8fafc",
                    font_size="18px",
                    padding="15px",
                    background_color="#0f172a",
                    border_radius="6px",
                    width="100%"
                ),
                align_items="start",
                spacing="3"
            ),
            margin_top="30px",
            padding="25px",
            background_color="#1e293b",
            border_radius="12px",
            border="1px solid #334155",
            width="100%"
        ),
        align_items="start",
        spacing="4"
    )
    
    return base_layout(page_content)