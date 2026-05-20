import reflex as rx
from datetime import datetime
from typing import Optional

# 1. Tabla Usuario
class Usuario(rx.Model, table=True):
    nombre: str
    apellido: str
    correo: str = rx.Field(unique=True, max_length=150)
    telefono: str
    estado: str="Activo"
    fecha_registro: str = rx.Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

# 2. Tabla Estudiante
class Estudiante(rx.Model, table=True):
    id_usuario: int = rx.Field(foreign_key="usuario.id")
    universidad: str
    carrera: str
    semestre: int

# 3. Tabla Tutor
class Tutor(rx.Model, table=True):
    id_usuario: int = rx.Field(foreign_key="usuario.id")
    especialidad: str
    experiencia_anhos: int
    tarifa_por_hora: float
    estado: str = "Activo"

# 4. Tabla Tutoría
class Tutoria(rx.Model, table=True):
    id_estudiante: int = rx.Field(foreign_key="estudiante.id")
    id_tutor: int = rx.Field(foreign_key="tutor.id")
    tema_general: str  # Ej: "Derivadas Implícitas"
    estado: str = "Activa"
    fecha_creacion: str = rx.Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

# 5. Tabla Detalle Tutoría (Temario en LaTex)
class DetalleTutoria(rx.Model, table=True):
    id_tutoria: int = rx.Field(foreign_key="tutoria.id")
    temario: str  # Soportará texto plano y formato LaTeX
    horas_programadas: int
    descripcion: str

# 6. Tabla Lugar
class Lugar(rx.Model, table=True):
    tipo: str  # "Virtual" o "Presencial"
    direccion: Optional[str] = None  # Dirección si es presencial
    enlace: Optional[str] = None     # Link de Teams/Meet si es virtual

# 7. Tabla Sesión Tutoría
class SesionTutoria(rx.Model, table=True):
    id_tutoria: int = rx.Field(foreign_key="tutoria.id")
    id_lugar: int = rx.Field(foreign_key="lugar.id")
    fecha: str
    hora_inicio: str
    hora_fin: str

########################################################################
#   Escribir código a partir de acá
#######################################################################