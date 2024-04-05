<?php
// 设置文件路径
$file_path = '../storage/map_info.json';

// 检查文件是否存在
if (!file_exists($file_path)) {
    http_response_code(404);
    echo json_encode(['message' => 'File not found']);
    exit();
}

// 获取文件名
$file_name = basename($file_path);

// 获取文件大小
$file_size = filesize($file_path);

// 读取文件内容
$file_content = file_get_contents($file_path);

// 解码 JSON 文件的内容
$json_content = json_decode($file_content, true);

// 计算内容项的总数
$item_count = count($json_content);

// 返回信息
echo json_encode(['file_name' => $file_name, 'file_size' => $file_size, 'item_count' => $item_count]);
?>