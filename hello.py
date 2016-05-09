from flask import Flask
from flask import render_template
from flask import request
import copula

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DELETE'])

def hello():
	print request.form.getlist('check')
	if request.method == 'POST':
		if (request.form['copula-input']):

			copulaform = request.form['copula-input']
			copulaform.replace('\n', '<br />')
			# Call the backend
			printMe = copula.copulaCalc(copulaform)
			printMe = printMe.replace('\n', '<br />')

			get_sentences = copula.print_sentences(copulaform)
			get_sentences = get_sentences.replace('\n', '<br />')

		else:
			print request.args
			print request.args[0]
			return render_template('form.html', error=error)


		return render_template('hello.html', input=printMe, sentences = get_sentences)

	else:
		return render_template('form.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/example')
def example():
	return render_template('example.html')

if __name__ == '__main__':
	app.run()

