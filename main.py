from flask import Flask, render_template, url_for, request, redirect
from services.shrink_service import shrink_url
from services.redirectservice import redirect_service
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('index.html')


@app.route('/getURL', methods=['POST', 'GET'])
def shortURL():
    url = request.form['url']
    if url == "":
        return
    # print(request.form['url'])
    return render_template('index.html', result_display='style=display:block', short_url=shrink_url(url), original_url=url)


@app.route('/<key>', methods=['POST', 'GET'])
def redirect_url(key):
    url = redirect_service(key)
    if url == "Error":
        return render_template('error.html')
    else:
        return redirect(url)


if __name__ == '__main__':
    app.run(debug=True)
