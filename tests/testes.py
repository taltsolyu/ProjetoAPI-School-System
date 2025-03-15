import unittest
import requests


class TestTeacherMethods(unittest.TestCase):
  
  def test_000_professores_retorna_lista(self):
    response = requests.get('http://localhost:5000/professores').json()
    print(response)
    self.assertEqual(type(response), type([]))
    
  def test_001_criar_professor_sucesso(self):
    professores = {
      "id": 1028,
      "nome": "José",
      "idade": 35,
      "materia": "SQL",
      "observacoe": "Ele disponibiliza materiais complementares, como slides, artigos e listas de exercícios, que ajudam os alunos a revisar e aprofundar o conteúdo após a aula."
    }
    
    response = requests.post("http://localhost:5000/professores",json=professores)
    print(response)
    self.assertIsNotNone(response.json())

def runTests():
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTeacherMethods)
  unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
  runTests()