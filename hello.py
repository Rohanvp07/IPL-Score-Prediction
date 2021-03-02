from flask import Flask, redirect, url_for, request, render_template
import pickle

import numpy as np
app = Flask(__name__)

s='ipl_model.pkl'
model = pickle.load(open(s,'rb'))

@app.route('/')
def index():
   return render_template('input.html')

@app.route('/prediction/<int:score>')
def final_score(score):
   return 'Predicted score is : %d' % score


@app.route('/predict',methods=['POST'])
def pred():
   tp=[]
   if request.method == 'POST':

      if request.form['batting-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['batting-team']=='Delhi Daredevils':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
      elif request.form['batting-team']=='Kings XI Punjab':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
      elif request.form['batting-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
      elif request.form['batting-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
      elif request.form['batting-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
      elif request.form['batting-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
      elif request.form['batting-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]


      if request.form['bowling-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['bowling-team']=='Delhi Daredevils':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
      elif request.form['bowling-team']=='Kings XI Punjab':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
      elif request.form['bowling-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
      elif request.form['bowling-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
      elif request.form['bowling-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
      elif request.form['bowling-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
      elif request.form['bowling-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]

      runs=int(request.form['runs'])
      wickets=int(request.form['wickets'])
      overs=float(request.form['overs'])
      runs_last_5=int(request.form['runs_in_prev_5'])
      wickets_last_5 = int(request.form['wickets_in_prev_5'])

      tp= tp + [runs, wickets, overs, runs_last_5, wickets_last_5]

      p=np.array([tp])
      print(p)

      score=(int(model.predict(p)[0]))

      #return redirect(url_for('final_score',score=score))

      return render_template('input.html',score="Expected score is {}".format(score))
if __name__ == '__main__':
   app.run(debug = True)

