# https://youtu.be/K2ejI4z8Mbg?list=PLMhVDSpAv9uXl6anUogvCnHha-K1x6sm1
# pip install Flask
# pip install gunicorn
# pip freeze > requirements.txt
# git init
# heroku git:remote -a escoladigitalfac
# git add .
# git commit -am "Primeira versão!"
# git push heroku master

from flask import Flask, render_template

app = Flask(__name__)

# Criando a primeira página do site
# route -> escola_digital.com/
# função -> o que vai ser exibido na página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #Colocar dentro do if mais tarde para o deploy

# servidor do heroku







