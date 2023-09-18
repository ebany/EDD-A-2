class Empleado:
    def __init__(self, id, nombre, contrasenia):
        self.id = id
        self.nombre = nombre
        self.contrasenia = contrasenia

    def __str__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Contraseña: {self.contrasenia}"

class TablaHash:
    def __init__(self, tamanio):
        self.tabla = [None] * tamanio
        self.factorCarga = 0

    def __str__(self):
        data = ""
        for i in range(len(self.tabla)):
            if self.tabla[i] != None:
                data += f"{i} - {self.tabla[i]}\n"
            else:
                data += f"{i} - {self.tabla[i]}\n"
        return data

    def toInt(self, name):
        value = 0
        for character in name:
            value += ord(character)
        return value

    def getNextFibonacci(self, n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b

    def funcionHash(self, clave, busqueda=False):
        hash = self.toInt(clave) % len(self.tabla)

        if busqueda:
            if self.tabla[hash] and self.tabla[hash].nombre == clave:
                return hash

        if self.tabla[hash] != None:
            hash = self.colisionHash(hash, busqueda, clave)

        return hash

    def colisionHash(self, hash, busqueda, clave, extra=0):
        nuevoHash = hash
        cuadratico = 0
        while nuevoHash < len(self.tabla) and self.tabla[nuevoHash] != None:
            nuevoHash = nuevoHash + pow(cuadratico, 2) + extra
            if busqueda and nuevoHash < len(self.tabla):
                if self.tabla[nuevoHash] and self.tabla[nuevoHash].nombre == clave:
                    return nuevoHash

            cuadratico += 1

        if nuevoHash >= len(self.tabla):
            nuevoHash = self.colisionHash(0, busqueda, clave, 1)

        return nuevoHash

    def rehashing(self):
        nuevaTabla = TablaHash(self.getNextFibonacci(len(self.tabla) + 1))
        for i in range(len(self.tabla)):
            if self.tabla[i] != None:
                nuevaTabla.set(self.tabla[i].nombre, self.tabla[i])
        self.tabla = nuevaTabla.tabla

    def set(self, clave, valor):
        while self.factorCarga / len(self.tabla) > 0.7:
            self.rehashing()

        direccion = self.funcionHash(clave)

        self.tabla[direccion] = valor
        self.factorCarga += 1

    def get(self, clave):
        direccion = self.funcionHash(clave, True)
        return self.tabla[direccion]

def main():
    usuarios = TablaHash(5)

    usuarios.set("admin", Empleado(1, "admin", "admin"))
    usuarios.set("user", Empleado(2, "user", "user"))
    usuarios.set("root", Empleado(3, "root", "root"))
    usuarios.set("guest", Empleado(4, "guest", "guest"))
    usuarios.set("test", Empleado(5, "test", "test"))
    usuarios.set("prueba", Empleado(6, "prueba", "prueba"))
    usuarios.set("prueba2", Empleado(7, "prueba2", "prueba2"))
    usuarios.set("prueba3", Empleado(8, "prueba3", "prueba3"))
    usuarios.set("prueba4", Empleado(9, "prueba4", "prueba4"))
    usuarios.set("prueba5", Empleado(10, "prueba5", "prueba5"))
    usuarios.set("prueba6", Empleado(11, "prueba6", "prueba6"))
    usuarios.set("jorge luis", Empleado(12, "jorge luis", "jorge luis"))
    usuarios.set("jorge luis2", Empleado(13, "jorge luis2", "jorge luis2"))
    usuarios.set("oscar rodriguez", Empleado(14, "oscar rodriguez", "oscar rodriguez"))
    usuarios.set("omar rodriguez", Empleado(15, "omar rodriguez", "omar rodriguez"))
    usuarios.set("fernando sanchez", Empleado(16, "fernando sanchez", "fernando sanchez"))
    usuarios.set("cris sanchez", Empleado(17, "cris sanchez", "cris sanchez"))
    usuarios.set("jose sanchez", Empleado(18, "jose sanchez", "jose sanchez"))
    usuarios.set("isabel rodriguez", Empleado(19, "isabel rodriguez", "isabel rodriguez"))
    usuarios.set("maria sanchez", Empleado(20, "maria sanchez", "maria sanchez"))
    usuarios.set("maria rodriguez", Empleado(21, "maria rodriguez", "maria rodriguez"))
    usuarios.set("maria luisa", Empleado(22, "maria luisa", "maria luisa"))
    usuarios.set("maria elena", Empleado(23, "maria elena", "maria elena"))
    usuarios.set("maria jose", Empleado(24, "maria jose", "maria jose"))
    usuarios.set("maria isabel", Empleado(25, "maria isabel", "maria isabel"))

    print(usuarios)
    print("----------------")
    print(usuarios.get("user"))

if __name__ == "__main__":
    main()