from flask import Flask, send_from_directory,request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
    return send_from_directory('.', 'index.html')

@app.route('/login')
def login():
    return send_from_directory('.', 'login.html')

@app.route('/main')
def ffgdg():
    return send_from_directory('.', 'main.html')

@app.route('/trylogin', methods=['POST'])
def trylogin():
    try:
        data = request.get_json()
        print("Полученные данные:", data)

        existing_data = []
        with open('data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        for i in existing_data:
            if i['pass'] == data['pass'] and i['login'] == data['login']:
                return jsonify({
                    'status': 'success',
                    'message': 'Вход успешен',
                    'data': i
                }), 200
        raise Exception("Сообщение об ошибке")
    except Exception as e:
        print("Ошибка:", str(e))
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/create', methods=['POST'])
def create():
    try:
        data = request.get_json()
        print("Полученные данные:", data)

    # от сюда
        existing_data = []
        with open('data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        existing_data.append(data)

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

    # до сюда
        return jsonify({
            'status': 'success',
            'message': 'Данные сохранены',
        }), 200

    except Exception as e:
        print("Ошибка:", str(e))
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)


