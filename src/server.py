from flask import Flask, jsonify, request

app = Flask(__name__)

dici = {
    "professores": [
        {
        'id': 1023,
        'nome': 'Lucas Silva',
        'idade': 21,
        'materia': 'Programação Orientada a Objetos',
        'observacoes': 'O professor explica os conteúdos de forma clara e organizada, facilitando o entendimento dos temas abordados.'
        },
        
        {
        'id': 1024,
        'nome': 'Ana Oliveira',
        'idade': 22,
        'materia': 'Banco de Dados',
        'observacoes': 'Durante as aulas, ele incentiva a participação dos alunos, fazendo perguntas e promovendo discussões para garantir que todos acompanhem o ritmo.'
        },
        
        {
        'id': 1025,
        'nome': 'Pedro Santos',
        'idade': 20,
        'materia': 'Estrutura de Dados',
        'observacoes': 'Ele costuma apresentar exemplos do dia a dia ou casos reais para ajudar na aplicação dos conceitos.'
        },
        
        {
        'id': 1026,
        'nome': 'Mariana Costa',
        'idade': 23,
        'materia': 'Redes de Computadores',
        'observacoes': ' A aula é bem estruturada e dinâmica, o que mantém a atenção dos alunos e evita que o conteúdo fique monótono.'
        },
        
        {
        'id': 1027,
        'nome': 'Carlos Lima',
        'idade': 24,
        'materia': 'Desenvolvimento Web',
        'observacoes': 'O professor dá retorno sobre as dúvidas e os exercícios feitos em aula, reforçando os pontos fortes e ajudando a corrigir os erros de forma construtiva.'
        }
        ]
    }
   
#ler
@app.route("/professores", methods=["GET"])
def getTodosProfessors():
  return jsonify(dici["professores"])

#criar
campos_obrigatorios = ["nome","idade","materia","observacoes"]

@app.route("/professores",methods=["POST"])
def criarProfessor():
    dados = request.get_json()
    for campo in campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            return jsonify({"mensagem": f"O campo '{campo}' é obrigatório e deve estar preenchido."}), 400
    return jsonify({"mensagem": "Todos os campos obrigatórios estão preenchidos."}), 200


    
 
 
 
 
 
 
 
 
# #att
# @app.route("/professores/<int:idProfessor>", methods=['PUT'])
# def updateProfessores(idProfessor):
#     professores = dici["professores"]
#     for professor in professores:
#         if professor['id'] == idProfessor:
#             dados = request.json
#             professor["id"] = dados['id']
#             professor['nome'] = dados['nome']
#             return jsonify(dados)
#         else:
#             return jsonify("professor nao encontrado")

# #deletar
# @app.route("/professores/<int:idProfessor>",methods=['DELETE'])
# def deleteProfessor(idProfessor):
#     professores = dici["professores"]
#     for professor in professores:
#         if professor ['id'] == idProfessor:
#             professores.remove(professor)
#             return jsonify({"mensagem": "Professor removido com sucesso"})
#     return jsonify ({"mensagem": "Professor não encontrado"}), 404

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5000, debug = True)