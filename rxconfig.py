import reflex as rx

config = rx.Config(
    app_name="differential_connect",
    db_url="mysql+pymysql://root:Contraseña@localhost:3306/differential_connect",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)