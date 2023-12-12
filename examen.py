from colorama import Fore, Style

class Curso:
    def __init__(self, curso_id, nombre, creditos, anios_de_estudio):
        self.curso_id = curso_id
        self.nombre = nombre
        self.creditos = creditos
        self.anios_de_estudio = anios_de_estudio

    def mostrar_ficha(self):
        print(f"{Fore.LIGHTCYAN_EX}Ficha del Curso {self.nombre} (ID: {self.curso_id}){Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}Créditos: {self.creditos}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}Años de Estudio: {self.anios_de_estudio}{Style.RESET_ALL}")
        print()

class Alumno:
    def __init__(self, alumno_id, nombre, email):
        self.alumno_id = alumno_id
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"{Fore.LIGHTMAGENTA_EX}Ficha del Alumno {self.nombre} (ID: {self.alumno_id}){Style.RESET_ALL}")
        print(f"{Fore.LIGHTMAGENTA_EX}Email: {self.email}{Style.RESET_ALL}")
        print()

class Matricula:
    def __init__(self, matricula_id, fecha_matricula, alumno_id, curso_id):
        self.matricula_id = matricula_id
        self.fecha_matricula = fecha_matricula
        self.alumno_id = alumno_id
        self.curso_id = curso_id

    def mostrar_datos_matricula(self):
        print(f"{Fore.LIGHTRED_EX}Datos de Matrícula (ID: {self.matricula_id}){Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}Fecha de Matrícula: {self.fecha_matricula}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}ID del Alumno: {self.alumno_id}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}ID del Curso: {self.curso_id}{Style.RESET_ALL}")
        print()
def main():
    # Crear instancias de cursos
    curso1 = Curso(1, "Programación en Python", 5, 2)
    curso2 = Curso(2, "Diseño de Interfaces", 4, 2)

    # Mostrar ficha de cursos
    curso1.mostrar_ficha()
    curso2.mostrar_ficha()

    alumno1 = Alumno(1, "Juan Pérez", "juan@example.com")
    alumno2 = Alumno(2, "María López", "maria@example.com")

    alumno1.mostrar_ficha()
    alumno2.mostrar_ficha()

    matricula1 = Matricula(1, "2023-01-15", alumno1.alumno_id, curso1.curso_id)
    matricula2 = Matricula(2, "2023-01-20", alumno2.alumno_id, curso1.curso_id)
    matricula3 = Matricula(3, "2023-01-25", alumno2.alumno_id, curso2.curso_id)

    matricula1.mostrar_datos_matricula()
    matricula2.mostrar_datos_matricula()
    matricula3.mostrar_datos_matricula()