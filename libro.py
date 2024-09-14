class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' por {self.autor}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)
        else:
            print(f"El libro '{libro.titulo}' ya está prestado a este usuario.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro '{libro.titulo}' no está prestado a este usuario.")

    def __repr__(self):
        libros = ', '.join([libro.titulo for libro in self.libros_prestados])
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: [{libros}]"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, user_id):
        if user_id in [usuario.user_id for usuario in self.usuarios]:
            print(f"Ya existe un usuario con ID {user_id}.")
        else:
            self.usuarios.add(Usuario(nombre, user_id))

    def dar_baja_usuario(self, user_id):
        self.usuarios = {usuario for usuario in self.usuarios if usuario.user_id != user_id}

    def prestar_libro(self, user_id, isbn):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        libro = self.libros.get(isbn)
        if usuario and libro:
            usuario.prestar_libro(libro)
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        libro = self.libros.get(isbn)
        if usuario and libro:
            usuario.devolver_libro(libro)
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        return resultados

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

    def __repr__(self):
        libros = ', '.join([str(libro) for libro in self.libros.values()])
        return f"Biblioteca con libros: [{libros}]"


# Ejemplo de uso del sistema de biblioteca
biblioteca = Biblioteca()

# Añadir libros
biblioteca.añadir_libro(Libro("1984", "George Orwell", "Distopía", "1234567890"))
biblioteca.añadir_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "0987654321"))

# Registrar usuarios
biblioteca.registrar_usuario("Alice", "user1")
biblioteca.registrar_usuario("Bob", "user2")

# Prestar y devolver libros
biblioteca.prestar_libro("user1", "1234567890")
biblioteca.devolver_libro("user1", "1234567890")

# Buscar libros
print(biblioteca.buscar_libro("titulo", "1984"))

# Listar libros prestados
print(biblioteca.listar_libros_prestados("user1"))

# Mostrar estado de la biblioteca
print(biblioteca)
