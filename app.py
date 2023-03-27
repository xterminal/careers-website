from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bangalore, India',
  'salary': '45000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': '115000'
}, {
  'id': 3,
  'title': 'Helpdesk',
  'location': 'San Francisco, USA',
  'salary': '32000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Dallas, USA',
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  print("I'm inside the if now.")
  app.run(host='0.0.0.0', debug=True)
