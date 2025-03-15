from flask import Flask, request, jsonify

app = Flask(__name__)

dici = {
  "teacher": [],
  "student": []
}

@app.route("/teacher", methods=["GET"])
def getAllTeachers():
  #Retornando objeto teacher do dicionário e "Jsonificando"(transformar em json) antes de retornar
  return jsonify(dici["teacher"])

@app.route("/teacher", methods=["POST"])
def createTeacher():
  #Capturando teacher vindo da requisição
  teacher = request.json
  # Validando se campo name do objeto teacher está preenchido
  if teacher['name'] is not None:
    #Adicionando teacher na lista de teachers
    dici["teacher"].append(teacher)
    return teacher
  
  return "There's an invalid field", 400

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)