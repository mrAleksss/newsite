from flask import Flask, request


mirror = Flask(__name__)


@mirror.route('/', methods=['POST', 'GET'])
def example():
    if request.method == 'POST':
        answer = request.form.get('answer')
        return f'<h1>{answer}</h1>'
    return '''
          <form method="POST">
             <div><label>Type here: <input type="text" name='answer'></label></div>
             <input type="submit" value="Submit">
          </form>'''



if __name__ == '__main__':
    mirror.run(debug=True, port=5000)