from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/save_map_info', methods=['POST'])
def save_map_info():
    new_map_info = request.get_json()

    # 检查 map_info.json 文件是否存在
    if os.path.exists('map_info.json'):
        # 如果文件存在，读取文件中的旧数据
        with open('map_info.json', 'r') as f:
            old_map_info = json.load(f)

        # 检查新提交的数据中的 map_name 是否在旧数据中
        for new_info in new_map_info:
            for old_info in old_map_info:
                if list(new_info.keys())[0] == list(old_info.keys())[0]:
                    # 如果有重复的数据，返回一个错误消息和重复的数据
                    return jsonify({'message': '重复的地图名', 'duplicate': list(new_info.keys())[0]}), 400

    # 如果没有重复的数据，将新的数据写入文件
    with open('map_info.json', 'w') as f:
        json.dump(new_map_info, f)

    return jsonify({'message': 'Success'}), 200

if __name__ == '__main__':
    app.run(port=5000)