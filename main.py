from flask import *
import os
import aminofix
import random
import time
import heroku3


os.system('set FLASK_ENV=development')
app = Flask(__name__)



@app.route('/api/login',  methods = ['POST'])
def get_timezone():
  data = request.form
  login = data.get("login")
  password = data.get("password")
  device = data.get("device")
  client = aminofix.Client(device)
  hkey = data.get("hkey")
  app_name = data.get("app_name")
  def restart():
    heroku_conn = heroku3.from_key(hkey)
    botapp = heroku_conn.apps()[app_name]
    botapp.restart()
  try:
    client.login(email = login, password = password)
    return f"{client.sid}"
  except Exception as g:
        print(f"Não foi possivel realizar o login, pelo erro: {g}")
        restart()
        return "Ocorreu um erro na api, a aplicação foi restartada"

if __name__ == '__main__':
  app.run("0.0.0.0", random.randint(2000, 9000))
