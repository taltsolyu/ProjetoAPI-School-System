# Importando módulos unittes e requests
import unittest
import requests

# Declarando classe test_teacher e herdando da classe TestCase do módulo unitest
class test_teacher_methods(unittest.TestCase):
  #Criando caso de teste
  def test_000_teacher_list (self):
    #Realizando chamada para a API e retornando resposta como json com o método .json()
    response = requests.get('http://localhost:5000/teacher').json()
    print(response)
    #Fazendo asserção(verificação) do objeto da esquerda com objeto da direita se igual.
    self.assertEqual(type(response), type([]))
    #Comparando se tipo do objeto a esquerda (resposta) é igual ao tipo do objeto a direita (tipo lista)
    
  def test_001_create_teacher(self):
    #Criando objeto teacher para enviar no corpo da requisição
    teacher = {
      "id": 1023,
      "name": "José",
      "age": 40,
      "class": "SQL",
    }
    #Enviando requisiação para o endpoint teacher com o json sendo o objeto teacher
    response = requests.post("http://localhost:5000/teacher", json=teacher)
    #Verificando se objeto de resposta não é nullo ou vazio
    print(response)
    self.assertIsNotNone(response.json())
  
  def test_002_create_teacher_error_name_none(self):
    teacher = {
      "id": 1024,
      "name": None,
      "age": 32,
      "class": "Data structure and algorithms"
    }
    
    response = requests.post("http://localhost:5000/teacher", json=teacher)
    print(response)
    self.assertEqual(response.status_code, 400)
    
def runTests():
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_teacher_methods)
  unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
if __name__ == '__main__':
  runTests()