from flask import Flask, jsonify, request
import galaxias_BD

app = Flask(__name__)

##Rota para retornar todas as galaxias
@app.route("/galaxias", methods =["GET"])
def get_galaxias():
    lista_galaxias = galaxias_BD.listar_galaxias()
    return jsonify(lista_galaxias)

##Rota para retornar uma galaxia
@app.route("/galaxia/<int:id>", methods=["GET"])
def obter_galaxia_route(id): 
    galaxia = galaxias_BD.retornar_galaxia(id)
    if galaxia:
        return jsonify(galaxia)
    else:
        return jsonify({"message": "Galaxia não encontrada"}), 404
    
## Rota para adicionar uma nova galaxia
@app.route("/galaxia", methods=["POST"])
def adicionar_galaxia_route():
    dados = request.json
    if not dados or 'nome' not in dados or 'estrelaPrincipal' not in dados or 'distancia' not in dados or 'imagem' not in dados:
        return jsonify({"message": "Dados incompletos"}), 400

    galaxia_adicionada = galaxias_BD.inserir_galaxia(dados['nome'], dados['estrelaPrincipal'], dados['distancia'], dados['imagem'])
    return jsonify({"message": "Galaxia adicionada com sucesso", "id": galaxia_adicionada}), 201


#Rota para atualizar todos os dados uma galaxia
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
    
    
#Rota para excluir  uma galaxia do banco de dados a partir de um id especifico. 
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
