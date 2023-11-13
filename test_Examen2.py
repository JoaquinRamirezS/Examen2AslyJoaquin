import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    miObjeto = MiClase(1, 120, 3, ["Cancion1", "Cancion2"], [0.8, 0.9, 0.7])

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

if __name__ == '__main__':
    unittest.main()
