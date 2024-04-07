from flask import Flask, jsonify, request
import galaxias_BD

app = Flask(__name__)

##Rota para retornar todas as galaxias
@app.route("/galaxias", methods =["GET"])
def get_galaxias():
    lista_galaxias = galaxias_BD.listar_galaxias()
    return jsonify(lista_galaxias)

##Rota para retornar um personagem
@app.route("/galaxia/<int:id>", methods=["GET"])
def obter_galaxia_route(id): 
    galaxia = galaxias_BD.retornar_galaxia(id)
    if galaxia:
        return jsonify(galaxia)
    else:
        return jsonify({"message": "Galaxia não encontrada"}), 404

#Rota para atualizar um personagem
@app.route("/atualizar/<int:id>", methods = ["PUT"])
def put_galaxia(id):
    galaxia_id = galaxias_BD.retornar_galaxia(id)
    if galaxia_id:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        galaxias_BD.atualizar_galaxia(**dados_atualizados)
        return jsonify(dados_atualizados)
    else:
        return jsonify({"message": "Personagem não encontrado"}),404

@app.route("/delete/<int:id>", methods=["DELETE"])
def deletar_galaxia_route(id): 
    galaxia = galaxias_BD.retornar_galaxia(id)
    if galaxia:
       galaxias_BD.deletar_galaxia(id)
       return jsonify({"message":"Galaxia removida com sucesso"})
    else:
       return jsonify({"message":"Galaxia não encontrada"}), 404



if __name__ == '__main__':
    galaxias_BD.criar_tabela()
    app.run(debug=True)
