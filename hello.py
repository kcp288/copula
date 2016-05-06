from flask import Flask
from flask import render_template
from flask import request
import copula

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])

def hello():
	if request.method == 'POST':
		if (request.form['copula-input']):

			copulaform = request.form['copula-input']
			copulaform.replace('\n', '<br />')
			# Call the backend
			printMe = copula.copulaCalc(copulaform)
			printMe = printMe.replace('\n', '<br />')

			get_sentences = copula.print_sentences(copulaform)
			print "Sentences"
			print get_sentences
			print printMe

		else:
			return render_template('form.html', error=error)

		return render_template('hello.html', input=printMe, sentences = get_sentences)
	else:
		return render_template('form.html')



if __name__ == '__main__':
	app.run(debug=True)

