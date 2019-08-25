from flask import Flask, send_file, request, jsonify, render_template
from flask_cors import CORS
from comment import Comment
import os

def create_app(test_config=None):
    
    app = Flask(__name__,
        static_folder='./dist/static',
        template_folder='./dist',
        instance_relative_config=True)

    CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    comment = Comment()

    @app.route('/', defaults={'path': ''})
    def index(path):
        return render_template('index.html')


    @app.route('/create', methods=['POST'])
    def create():

        json = request.get_json()
        title = json['title']
        category = json['category']
        content = json['content']

        index = comment.insert(title, category, content)
        result = comment.select(index)

        return jsonify(results=result)

    @app.route('/read', methods=['GET'])
    def read_all():

        result = comment.select_all()
        return jsonify(results=result)

    @app.route('/read/<index>', methods=['GET'])
    def read(index):

        result = comment.select(index)
        return jsonify(results=result)

    @app.route('/update', methods=['POST'])
    def update():

        json = request.get_json()
        index = json['index']
        title = json['title']
        category = json['category']
        content = json['content']

        index = comment.update(index, title, category, content)
        result = comment.select(index)

        return jsonify(results=result)

    @app.route('/delete', methods=['POST'])
    def delete():

        json = request.get_json()
        index = json['index']

        index = comment.delete(index)
        result = len(comment.select(index)) == 0

        return jsonify(results=result)

    return app

