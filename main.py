from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/save_map_info', methods=['POST'])
def save_map_info():
    new_map_info_list = request.get_json()

    old_map_info = {}

    # 检查 map_info.json 文件是否存在
    if os.path.exists('map_info.json'):
        # 如果文件存在，检查文件是否为空
        if os.stat('map_info.json').st_size > 0:
            # 如果文件不为空，读取文件中的旧数据
            with open('map_info.json', 'r') as f:
                old_map_info = json.load(f)

        # 检查新提交的数据中的 map_name 是否在旧数据中
        for new_map_info in new_map_info_list:
            for new_map_name, new_map_details in new_map_info.items():
                if new_map_name in old_map_info:
                    # 如果有重复的数据，返回一个错误消息和重复的数据
                    return jsonify({'message': f'重复的地图名: {new_map_name}', 'duplicate': new_map_name}), 400
                else:
                    # 将新的数据添加到 old_map_info 的后面
                    old_map_info[new_map_name] = new_map_details

    # 将 old_map_info 写入文件
    with open('map_info.json', 'w') as f:
        json.dump(old_map_info, f)

    return jsonify({'message': 'Success'}), 200

if __name__ == '__main__':
    app.run(port=5000)