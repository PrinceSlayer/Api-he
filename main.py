from flask import *
import os
import aminofix
import random
import time
import heroku3


os.system('set FLASK_ENV=development')
app = Flask(__name__)

def restart():
    heroku_conn = heroku3.from_key("b0fce155-8839-436a-b0e2-e6e02699208d")
    botapp = heroku_conn.apps()["sid-amino"]
    botapp.restart()

@app.route('/api/login',  methods = ['POST'])
def get_timezone():
  data = request.form
  login = data.get("login")
  password = data.get("password")
  device = data.get("device")
  client = aminofix.Client(device)
  try:
    client.login(email = login, password = password)
    return f"{client.sid}"
  except:
    try:
      client.login(email = login, password = password)
      return f"{client.sid}"
    except:
      try:
        client.login(email = login, password = password)
        return f"{client.sid}"
      except:
        try:
          client.login(email = login, password = password)
          return f"{client.sid}"
        except Exception as g:
          print(f"Não foi possivel realizar o login, pelo erro: {g}")
          restart()

if __name__ == '__main__':
  app.run("0.0.0.0", random.randint(2000, 9000))
