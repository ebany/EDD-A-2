import os
cmd = "dot -Tpng arbolB.dot -o arbolB.png"

class Nodo:
    def __init__(self, clave, valor, tamanio=0):
        self.clave = clave
        self.valor = valor
        self.tamanio = tamanio

class NodoArbolB:
    def __init__(self, esHoja=False):
        self.esHoja = esHoja
        self.clavesValores = []
        self.hijos = []

class ArbolB:
    def __init__(self):
        self.raiz = NodoArbolB(True)
        self.grado = 3

    def insertar(self, nuevoNodo):
        raiz = self.raiz
        if len(raiz.clavesValores) == (2 * self.grado) - 1:
            temporal = NodoArbolB()
            self.raiz = temporal
            temporal.hijos.insert(0, raiz)
            self.dividir_hijos(temporal, 0)
            self.insertar_con_espacio(temporal, nuevoNodo)
        else:
            self.insertar_con_espacio(raiz, nuevoNodo)

    def insertar_con_espacio(self, nodo, nuevoNodo):
        posicionActual = len(nodo.clavesValores) - 1
        if nodo.esHoja:
            nodo.clavesValores.append(Nodo(None, None))
            while posicionActual >= 0 and nuevoNodo.clave < nodo.clavesValores[posicionActual].clave:
                nodo.clavesValores[posicionActual +
                                   1] = nodo.clavesValores[posicionActual]
                posicionActual -= 1
            nodo.clavesValores[posicionActual + 1] = nuevoNodo
        else:
            while posicionActual >= 0 and nuevoNodo.clave < nodo.clavesValores[posicionActual].clave:
                posicionActual -= 1
            posicionActual += 1
            if len(nodo.hijos[posicionActual].clavesValores) == (2 * self.grado) - 1:
                self.dividir_hijos(nodo, posicionActual)
                if nuevoNodo.clave > nodo.clavesValores[posicionActual].clave:
                    posicionActual += 1
            self.insertar_con_espacio(nodo.hijos[posicionActual], nuevoNodo)

    def dividir_hijos(self, nodo, posicionActual):
        grado = self.grado
        y = nodo.hijos[posicionActual]
        z = NodoArbolB(y.esHoja)
        nodo.hijos.insert(posicionActual + 1, z)
        nodo.clavesValores.insert(posicionActual, y.clavesValores[grado - 1])
        z.clavesValores = y.clavesValores[grado: (2 * grado) - 1]
        y.clavesValores = y.clavesValores[0: grado - 1]
        if not y.esHoja:
            z.hijos = y.hijos[grado: 2 * grado]
            y.hijos = y.hijos[0: grado - 1]

    def buscar(self, clave, valor, nodo=None):
        if nodo is not None:
            i = 0
            while i < len(nodo.clavesValores) and clave > nodo.clavesValores[i].clave:
                i += 1
            if i < len(nodo.clavesValores) and clave == nodo.clavesValores[i].clave:
                return nodo.clavesValores[i].valor
            elif nodo.esHoja:
                return None
            else:
                return self.buscar(clave, valor, nodo.hijos[i])
        else:
            return self.buscar(clave, valor, self.raiz)

    def generate_dot_b_tree(self, x):
        dotContent = "digraph G {\n node [shape=record]" + \
            self.aux_export_graphviz(x) + "}"
        f = open("arbolB.dot", "w")
        f.write(dotContent)
        f.close()
        os.system(cmd)

    def aux_export_graphviz(self, x, l=0):
        dotContent = ""
        dotContent += "node" + str(x.clavesValores[0].clave) + " [label=\""
        dotContent += '|'.join([str(i.clave) + "\\n" + i.valor for i in x.clavesValores])
        dotContent += "\"];\n"
        l += 1
        if len(x.hijos) > 0:
            for i in x.hijos:
                dotContent += "node" + \
                    str(x.clavesValores[0].clave) + "->" + "node" + \
                    str(i.clavesValores[0].clave) + "\n"
                dotContent += self.aux_export_graphviz(i, l)
        return dotContent

def toInt(name):
    value = 0
    for character in name:
        value += ord(character)
    return value

def main():
    B = ArbolB()

    B.insertar(Nodo(toInt("hola"),"hola"))
    B.insertar(Nodo(toInt("adios amor"),"adios amor"))
    B.insertar(Nodo(toInt("casa"),"casa"))
    B.insertar(Nodo(toInt("perro"),"perro"))
    B.insertar(Nodo(toInt("gato"),"gato"))
    B.insertar(Nodo(toInt("casa1"),"casa1"))
    B.insertar(Nodo(toInt("casa2"),"casa2"))
    B.insertar(Nodo(toInt("casa3"),"casa3"))
    B.insertar(Nodo(toInt("mas"),"mas"))
    B.insertar(Nodo(toInt("menos"),"menos"))
    B.insertar(Nodo(toInt("casa4"),"casa4"))
    B.insertar(Nodo(toInt("texto de prueba"),"texto de prueba"))
    B.insertar(Nodo(toInt("Hola Mundo"),"Hola Mundo"))
    B.insertar(Nodo(toInt("Hogar Dulce Hogar"),"Hogar Dulce Hogar"))
    B.insertar(Nodo(toInt("ali baba y los 40 ladrones"),"ali baba y los 40 ladrones"))
    B.insertar(Nodo(toInt("jorge el curioso"),"jorge el curioso"))
    B.insertar(Nodo(toInt("don quijote de la mancha"),"don quijote de la mancha"))
    B.insertar(Nodo(toInt("el principito"),"el principito"))
    B.insertar(Nodo(toInt("el arte de la guerra"),"el arte de la guerra"))
    B.insertar(Nodo(toInt("amor y paz"),"amor y paz"))
    B.insertar(Nodo(toInt("la biblia"),"la biblia"))
    B.insertar(Nodo(toInt("el coran"),"el coran"))
    B.insertar(Nodo(toInt("el libro de los muertos"),"el libro de los muertos"))
    B.insertar(Nodo(toInt("el libro de la selva"),"el libro de la selva"))
    B.insertar(Nodo(toInt("el libro de la vida"),"el libro de la vida"))
    B.insertar(Nodo(toInt("el libro de la muerte"),"el libro de la muerte"))
    B.insertar(Nodo(toInt("el libro de la luz"),"el libro de la luz"))
    B.insertar(Nodo(toInt("el libro de la oscuridad"),"el libro de la oscuridad"))
    B.insertar(Nodo(toInt("el libro de la sabiduria"),"el libro de la sabiduria"))
    B.insertar(Nodo(toInt("el libro de la ignorancia"),"el libro de la ignorancia"))
    B.insertar(Nodo(toInt("el libro de la verdad"),"el libro de la verdad"))
    B.insertar(Nodo(toInt("el libro de la mentira"),"el libro de la mentira"))
    B.insertar(Nodo(toInt("el libro de la vida y la muerte"),"el libro de la vida y la muerte"))
    B.insertar(Nodo(toInt("el libro de la vida eterna"),"el libro de la vida eterna"))
    B.insertar(Nodo(toInt("el libro de la vida mortal"),"el libro de la vida mortal"))
    B.insertar(Nodo(toInt("el libro de la vida inmortal"),"el libro de la vida inmortal"))
    B.insertar(Nodo(toInt("el libro de la vida infinita"),"el libro de la vida infinita"))

    #TODO: Corregir index out
    search = B.buscar(toInt("texto de pruebas"),"texto de prueba")
    if search is not None:
        print(search)
    else:
        print("\nNot Found")

    B.generate_dot_b_tree(B.raiz)

if __name__ == '__main__':
    main()