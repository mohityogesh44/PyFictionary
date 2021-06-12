from flask import Flask, render_template, request
from dictionary import get_meaning
import sqlite3 as sql

app = Flask(__name__)
db = sql.connect('words.db', check_same_thread=False)

@app.route('/', methods = ['GET', 'POST'])
def home():
	#This if statement will run when the user will hit search button.
	if request.method == 'POST':
		# form_data = request.form
		#The key of dictionary form_data is same as the name parameter defined in the input field in the html template.
		# word = form_data['word']
		word = request.form['word']

		try:
			#By the fetchall returns a list and since we want the tuple inside of it we use indexing.
			pos, meaning = db.execute("select pos, meaning from words where word = ?;", (word,)).fetchall()[0]

		except:
			pos, meaning = get_meaning(word)
			db.execute('insert into words values (?, ?, ?);', (word, pos, meaning))
			db.commit()
		
		data = {"word": word, 'pos': pos, 'meaning': meaning}
		return render_template('index.html', data = data)

	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)