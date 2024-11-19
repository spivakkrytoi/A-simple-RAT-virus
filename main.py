from flask import Flask, request, jsonify, render_template
import psutil
import os
import subprocess

app = Flask(__name__)

# Отримати список запущених процесів
def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append({'pid': proc.info['pid'], 'name': proc.info['name']})
        except psutil.NoSuchProcess:
            continue
    return processes

# Закрити процес за PID
def kill_process(pid):
    try:
        os.kill(pid, 9)  # SIGKILL
        return True
    except Exception as e:
        return str(e)

# Запустити новий процес
def start_process(command):
    try:
        subprocess.Popen(command, shell=True)
        return True
    except Exception as e:
        return str(e)

# Головна сторінка
@app.route('/')
def index():
    processes = get_processes()
    return render_template('index.html', processes=processes)

# API для закриття процесу
@app.route('/kill', methods=['POST'])
def api_kill():
    data = request.json
    pid = data.get('pid')
    if not pid:
        return jsonify({'error': 'PID is required'}), 400
    result = kill_process(int(pid))
    if result is True:
        return jsonify({'message': 'Process killed successfully'})
    return jsonify({'error': result}), 500

# API для запуску нового процесу
@app.route('/start', methods=['POST'])
def api_start():
    data = request.json
    command = data.get('command')
    if not command:
        return jsonify({'error': 'Command is required'}), 400
    result = start_process(command)
    if result is True:
        return jsonify({'message': 'Process started successfully'})
    return jsonify({'error': result}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
