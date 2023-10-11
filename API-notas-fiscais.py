from flask import Flask, request, jsonify
import notas

app = Flask(__name__)

@app.route("/notas/fiscais", methods=['POST'])
def inclui_nota():
    nota = request.json
    try:
        notas.insert_nota(nota)
        return nota, 201
    except Exception as erro:
        print(erro)
        info = {"msg": "Nota nao cadastrada"}
        return info, 404
    

@app.route("/notas/fiscais", methods=['GET'])
def lista_notas():
    try:
        nota = notas.get_notas()
        lista = []
        for reg in nota:
            NotaFiscal = {}
            NotaFiscal['id'] = reg[0]
            NotaFiscal['NumeroNota'] = reg[1]
            NotaFiscal['DataEmissao'] = reg[2]
            NotaFiscal['NomeEmitente'] = reg[3]
            NotaFiscal['CNPJCPF_Emitente'] = reg[4]
            NotaFiscal['NomeDestinatario'] = reg[5]
            NotaFiscal['CNPJCPF_Destinatario'] = reg[6]
            NotaFiscal['ValorTotal'] = reg[7]
            NotaFiscal['FormaPagamento'] = reg[8]
            NotaFiscal['Observacoes'] = reg[9]
            NotaFiscal['ChaveAcesso'] = reg[10]
            lista.append(NotaFiscal)
        return lista, 200
    except Exception as erro:
        print(erro)
        info = {"msg": "Nao foi possivel obter a lista de notas fiscais"}
        return info, 500
    

@app.route("/notas/fiscais/<int:nota_id>", methods=['GET'])
def lista_nota_por_id(nota_id):
    try:
        nota = notas.get_nota_by_id(nota_id)
        if nota is not None:
            NotaFiscal = {
                'id': nota[0],
                'NumeroNota': nota[1],
                'DataEmissao': nota[2],
                'NomeEmitente': nota[3],
                'CNPJCPF_Emitente': nota[4],
                'NomeDestinatario': nota[5],
                'CNPJCPF_Destinatario': nota[6],
                'ValorTotal': nota[7],
                'FormaPagamento': nota[8],
                'Observacoes': nota[9],
                'ChaveAcesso': nota[10]
            }
            return NotaFiscal, 200
        else:
            return {"msg": "Nota fiscal não encontrada"}, 404
    except Exception as erro:
        print(erro)
        info = {"msg": "Não foi possível obter a nota fiscal"}
        return info, 500



@app.route("/notas/fiscais/<int:nota_id>", methods=['PUT'])
def atualiza_nota(nota_id):
    nota_data = request.json
    try:
        notas.update_nota(nota_id, nota_data)
        return {"msg": "Nota fiscal atualizada com sucesso"}, 200
    except Exception as erro:
        print(erro)
        info = {"msg": "Nao foi possivel atualizar a nota fiscal"}
        return info, 500



@app.route("/notas/fiscais/<int:nota_id>", methods=['DELETE'])
def deleta_nota(nota_id):
    try:
        notas.delete_nota(nota_id)
        return {"msg": "Nota fiscal excluída com sucesso"}, 200
    except Exception as erro:
        print(erro)
        info = {"msg": "Nao foi possivel excluir a nota fiscal"}
        return info, 500


app.run(debug=True)