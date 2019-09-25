from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect("dbname=ppd_aula6 password=SenhaComplexa user=user host=db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mensagens ORDER BY id desc;")
    msg="<html>"
    msg+="<head> <meta http-equiv=\"refresh\" content=\"5\"></head>"
    msg+="<body>"
    msg+="<h1>Últimas Mensagens</h1>"
    for t in cur:
        print(t)
        msg+="<p>{}</p>".format(t)
    msg+="</body>"
    return msg

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')