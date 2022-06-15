from flask import *
import os
import aminofix
import random
os.system('set FLASK_ENV=development')
app = Flask(__name__)


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

if __name__ == '__main__':
  app.run("0.0.0.0", random.randint(2000, 9000))
