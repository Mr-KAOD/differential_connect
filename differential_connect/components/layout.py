import reflex as rx

def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    # Componente auxiliar para los botones del menú lateral
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon, size=18, color="#94a3b8"),
            rx.text(text, font_size="16px", font_weight="500", color="#cbd5e1"),
            spacing="3",
            padding="10px 15px",
            border_radius="8px",
            _hover={"background_color": "#1e293b", "color": "#22d3ee"},
            transition="all 0.2s ease"
        ),
        href=url,
        text_decoration="none",
        width="100%"
    )

def base_layout(content: rx.Component) -> rx.Component:
    #Contenedor principal que envolverá todas las páginas del proyecto
    return rx.hstack(
        # SIDEBAR (Menú Izquierdo Permanente)
        rx.vstack(
            rx.heading("Differential Connect", font_size="22px", color="#22d3ee", margin_bottom="20px"),
            sidebar_item("Inicio", "home", "/"),
            sidebar_item("Estudiantes", "users", "/estudiantes"),
            sidebar_item("Tutores", "graduation-cap", "/tutores"),
            sidebar_item("Tutorías", "book-open", "/tutorias"),
            sidebar_item("Sesiones / Lugares", "calendar", "/sesiones"),
            sidebar_item("Pagos", "credit-card", "/pagos"),
            spacing="2",
            padding="30px 20px",
            width="260px",
            height="100vh",
            background_color="#0f172a",
            border_right="1px solid #1e293b",
            align_items="start"
        ),
        # CUERPO PRINCIPAL DE LA PÁGINA
        rx.vstack(
            # Navbar Superior Informativa
            rx.hstack(
                rx.text("Panel de Control", font_weight="600", color="#f8fafc"),
                rx.spacer(),
                rx.badge("Conectado a DB Local", color_scheme="green", variant="surface"),
                width="100%",
                padding="15px 40px",
                background_color="#0f172a",
                border_bottom="1px solid #1e293b"
            ),
            # El contenido dinámico que haga cada compañero se renderizará aquí:
            rx.box(
                content,
                padding="40px",
                width="100%",
                height="calc(100vh - 60px)",
                overflow_y="auto",
                background_color="#0b0f19"
            ),
            width="calc(100% - 260px)",
            spacing="0"
        ),
        background_color="#0f172a",
        width="100vw",
        height="100vh",
        spacing="0"
    )