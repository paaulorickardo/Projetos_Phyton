from flask import Flask, request

from main import insertUsuario

app = Flask("Youtube")


@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}


@app.route("/cadastrar/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()

    if ("nome" not in body):
        return {"status": 400, "mensagem": "O parametro é obrigatorio"}

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "Usuário criado com sucesso", "user", usuario)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
        return response


app.run()
