from flask import Blueprint, request, jsonify
from .system_module.psutile_module import take_cpu_info, take_disk_partision, check_network_interfaces, take_ram, take_general_info

data_api = Blueprint('data_api', __name__, url_prefix='/API')

@data_api.route('/cpu')
def take_cpu_data():
    data = take_cpu_info()
    return jsonify(data)

@data_api.route('/disk')
def take_disk_data():
    data = take_disk_partision
    return jsonify(data)

@data_api.route('/network')
def take_network_data():
    data = check_network_interfaces()
    return jsonify(data)

@data_api.route('/ram')
def take_ram_data():
    data = take_ram()
    return jsonify(data)

@data_api.route("/general-data")
def general_data():
    data = take_general_info()
    return data