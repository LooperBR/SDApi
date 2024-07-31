from flask import Flask,request,jsonify
import banco

app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/')
def principal():
    return "pagina principal"

#background process happening without any refreshing
@app.route('/produto/<id>',methods = ['GET'])
def getProduto(id):
    return jsonify(banco.get_id(id))

@app.route('/produto',methods = ['GET'])
def getProdutos():
    return jsonify(banco.get_all())

@app.route('/produto',methods = ['POST'])
def postProduto():
    item = request.get_json()
    return jsonify(banco.insert(item))

@app.route('/produto',methods = ['PUT'])
def putProduto():
    item = request.get_json()
    return jsonify(banco.update(item))

@app.route('/produto/<id>',methods = ['DELETE'])
def deleteProduto(id):
    return jsonify(banco.delete(id))

if __name__ == "__main__":
    banco.create_table()
    #app.route(debug=False)