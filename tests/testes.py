import unittest

import requests


class TestTeacherMethods(unittest.TestCase):
  
  def test_000_professores_retorna_lista(self):
    response = requests.get('http://localhost:5000/professores').json() #retorna o conteúdo(corpo) da resposta em formato json 
    #.json() = vai me retornar a resposta que eu fiz da requisição para a api em formtato json
    #porque eu quero que ele me retorne uma lista, e essa lista tem que estar em formato json
    print(response)
    self.assertEqual(type(response), type([]))
    
  def test_001_criar_professor_sucesso(self):
    professor = {
      "id": 1028,
      "nome": "José",
      "idade": 35,
      "materia": "SQL",
      "observacoes": "Ele disponibiliza materiais complementares, como slides, artigos e listas de exercícios, que ajudam os alunos a revisar e aprofundar o conteúdo após a aula."
    }
    
    response = requests.post("http://localhost:5000/professores",json=professor) #está enviando um corpo(professor) para requisição para criar um novo professor
    #este corpo professor eu mando em formato json, porque é o formato para comunicação com a api
    print(response)
    self.assertEqual(response.json(), professor)
    
  def_test 
  
   
  def test_002_criar_professor_erro(self):
    professores = {
      "id": None,
      "nome": "José",
      "idade": 35,
      "materia": "SQL",
      "observacoes": "Ele disponibiliza materiais complementares, como slides, artigos e listas de exercícios, que ajudam os alunos a revisar e aprofundar o conteúdo após a aula."
    }
    
    response = requests.post("http://localhost:5000/professores",json=professores)
    print(response)
    self.assertEqual(response.status_code,400)
    #assertEqual = compara se A é igual a B (lado-esq/drt), verificando se o código de status da resposta é igual a 400
    

def runTests():
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTeacherMethods)
  unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
  runTests()