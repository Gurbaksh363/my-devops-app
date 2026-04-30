from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return "<h1>Gurbaksh Kaur: Devops Successfull!</h1><p>Python+ Docker + Git + AWS running</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

# adding comment
