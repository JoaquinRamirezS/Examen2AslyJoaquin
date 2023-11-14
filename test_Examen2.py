import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    miObjeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])

#Pruebas Unitarias (Asly)

#Método 1
    def test_init_AsignacionCorrecta(self):
        # Verifica que los valores de los atributos se asignancorrectamente
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.Valencia, 1)
        self.assertEqual(objeto.Tempo, 120)
        self.assertEqual(objeto.Tonos, 3)
        self.assertEqual(objeto.listaCanciones, ["Cancion1", "Cancion2"])
        self.assertEqual(objeto.listaBailabilidad, [0.8, 0.9, 0.7])

    def test_init_AtributosTiposCorrectos(self):
        # Verifica que los atributos se asignan según el tipo de dato correcto
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        self.assertIsInstance(objeto.Valencia, int)
        self.assertIsInstance(objeto.Tempo, int)
        self.assertIsInstance(objeto.Tonos, int)
        self.assertIsInstance(objeto.listaCanciones, list)
        self.assertIsInstance(objeto.listaBailabilidad, list)

#Método 2 

    def testObtieneValenciaNumCombinado(self):
        # Verifica que ObtieneValencia funcione bien con un número con cifras pares e impares
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneValencia(123456789)
        self.assertEqual(resultado, 5)

    def testObtieneValenciaNumCero(self):
        # Verifica que ObtieneValencia funcione bien con un número = 0
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneValencia(0)
        self.assertEqual(resultado, 0)
    
#Método 3

    def testDivisibleTempoNumPrimo(self):
        # Verifica que la lista de divisores de un num primo sea el mismo y 1
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])

    def testDivisibleTempoCero(self):
        # Verifica que 0 no tenga divisores
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.DivisibleTempo(0)
        self.assertEqual(resultado, [])

#Método 4

    def testObtieneMasBailableListaVacia(self):
        # Verifica que el número mayor de una lista vacia sea None
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneMasBailable([])
        self.assertEqual(resultado, None)
    
    def testObtieneMasBailableListaNumIguales(self):
        # Verifica que el número mayor de una lista con números repetidos sea ese número
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneMasBailable([2,2,2])
        self.assertEqual(resultado, 2)

#Método 5

    def testVerificaListaCanciones(self):
        # Verifica el resultado cuando la lista no contiene ningún None
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.VerificaListaCanciones(["Canción 1", "Canción 2"])
        self.assertEqual(resultado, True)

    def testVerificaListaCancionesTodoNone(self):
        # Verifica el resultado cuando la lista está formada solo por None
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.VerificaListaCanciones([None, None, None])
        self.assertEqual(resultado, False)
        

#Pruebas unitarias (Joaquín)

#Método 1

    def test_init_AtributosListasVacías(self):
        #Verifica que los atributos se manejen adecuadamente si hay listas vacías
        objeto = MiClase(1, 120, 3, [], [])
        self.assertIsInstance(objeto.Valencia, int)
        self.assertIsInstance(objeto.Tempo, int)
        self.assertIsInstance(objeto.Tonos, int)
        self.assertIsInstance(objeto.listaCanciones, list )
        self.assertIsInstance(objeto.listaBailabilidad, list)

    def test_init_AtributosNone(self):
        #Verifica que los atributos se manejen de manera adecuada si son None
        objeto = MiClase(None, None, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        self.assertIsNone(objeto.Valencia)
        self.assertIsNone(objeto.Tempo)
        self.assertEqual(objeto.Tonos, 3)
        self.assertEqual(objeto.listaCanciones, ["Cancion1", "Cancion2"])
        self.assertEqual(objeto.listaBailabilidad, [0.8, 0.9, 0.7])

#Método 2

    def testObtieneValenciaNumPar(self):
        #Verifica que ObtieneValencia funcione correctamente cuando hay únicamente número pares
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)

    def testObtieneValenciaNumIgual(self):
        #Verifica que ObtieneValencia funciones correctamente cuándo hay número iguales 
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneValencia(555)
        self.assertEqual(resultado, 3)

#Método 3
    
    def testDivisibleTempoNumComp(self):
        #Verifica la correcta obtención de los diviroes de un número compuesto
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.DivisibleTempo(12)
        self.assertEqual(resultado, [1, 2, 3, 4, 6, 12])

    def testDivisbleTempoUno(self):
        #Verifica que la función manejen correctamente los divisores de 1
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.DivisibleTempo(1)
        self.assertEqual(resultado, [1])

#Método 4

    def testObtieneMasBailableOne(self):
        #Verifica que el número mayor de una lista con un único valor, sea ese valor.
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneMasBailable([0.2])
        self.assertEqual(resultado, 0.2 )

    def testObtieneMasBailabreCorrecto(self):
        #Verifica que el número mayor de una lista sea el correcto
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.ObtieneMasBailable([0.4, 0.5, 0.6])
        self.assertEqual(resultado,0.6)

#Método 5

    def testVerificaListaCancionesVacia(self):
        #Verifica el resultado cuando la lista es vacía
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.VerificaListaCanciones([])
        self.assertEqual(resultado, True)

    def testVerificaListaCancionesUnNone(self):
        #Verifica el resultado cuando hay al menos un None en la lista
        objeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])
        resultado = objeto.VerificaListaCanciones(["Cancion1", "Cancion2", None])
        self.assertEqual(resultado,False)

# Pruebas unitarias del nuevo módulo

#Método 6
    
    def testEncuentraElementoEnLista(self):
        # Verifica que Encuentra funcione correctamente cuando el elemento está en la lista
        lista = [2, 6, 8]
        elemento = 6
        resultado = self.miObjeto.Encuentra(lista, elemento)
        self.assertEqual(resultado, elemento)

    def testEncuentraNone(self):
        # Verifica que Encuentra retorne None cuando la lista contiene elementos no enteros
        lista = [2, 0.6 , 8]
        elemento = 8
        resultado = self.miObjeto.Encuentra(lista, elemento)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
