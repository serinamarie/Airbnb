from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'airbnb predictive project'

    @app.route('/predict', methods=['POST'])
    def predict(name=None, message=""):
        try:
            content = request.get_json(force=True)
            # prediction = get_predicted_price(content)
        except Exception as identifier:
            message = f'error: {identifier}'
        return message
    
    return app

# def tokenize(text):
#     return [
#         token for token in simple_preprocess(text) if token not in STOPWORDS
#         ]
# @app.route('/', methods=['POST', 'GET'])
# def responses():
#     response = requests.get(
#         'backendurlhere')
#     return str(response.text)
# @app.route('/api', methods=['POST', 'GET'])
# def predict():
#     data = request.get_json(force=True)
#     desc = data['feature'][0]['description']
#     description_length = len(tokenize(desc))
