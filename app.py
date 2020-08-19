from flask import Flask

app = Flask(__name__)

@app.route('/')
def action():
   return {"name:Sadiq"}

   if __name__== "__main__":
       app.run(debug=True)