from chalice import Chalice, Response
from chalicelib import URL
app = Chalice(app_name='aws-chalice-echosvc')

@app.route('/')
def index():
    return { 'hello': 'world'}

@app.route('/echo')
def echo():
    ctx = app.current_request.to_dict()
    return { 'source' : (ctx['context']['identity']['sourceIp']) }

@app.route('/hello/{name}')
def hello(name):
    return { 'hello' : name }

@app.route('/rick')
def rick():
    return Response(body='',
                    status_code=301,
                    headers={'Location': URL })
