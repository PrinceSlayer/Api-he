from flask import *
import os
import aminofix
import random
import time
os.system('set FLASK_ENV=development')
app = Flask(__name__)
@app.route('/api/login')
def get_timezone():
  data = request.args
  login = data.get("email")
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
