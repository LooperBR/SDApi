from flask import Flask,render_template,request
import requests

app = Flask('testapp')

@app.route('/')
def index():
    r = requests.get('http://127.0.0.1:5000/produto')
    print(r.json())
    compras = r.json()["compras"]
    return render_template('index.html', compras=compras)

@app.route('/criar',methods =["POST"])
def criar():
    item = {}
    item['id']=request.form['id']
    item['produto']=request.form['produto']
    item['valor']=request.form['valor']
    item['vencimento']=request.form['vencimento']
    print(item)
    if(request.form['tipo']=='inserir'):
        print('inserir')
        r = requests.post('http://127.0.0.1:5000/produto',json=item)
        print(r.json())
    elif(request.form['tipo']=='atualizar'):
        print('atualizar')
        r = requests.put('http://127.0.0.1:5000/produto',json=item)
        print(r.json())
    return index()

@app.route('/delete/<id>')
def delete(id):
    r = requests.delete('http://127.0.0.1:5000/produto/'+id)
    print(r.json())
    return index()

if __name__ == '__main__':
    app.run()