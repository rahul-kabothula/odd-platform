import json

from flask import Flask, request, jsonify
import subprocess
import sys
import yaml
import os

app = Flask(__name__)


@app.route('/run_collector', methods=['GET'])
def run_main():
    # todo
    # Get the collector_config.yaml file from odd_platform

    # Define the path to Project A's __main__.py script
    script_path = "/Users/rahulkabothula/Desktop/RK/odd-collectors-main/odd-collector/odd_collector/__main__.py"

    # Use subprocess to execute the script
    try:
        # Run the script with Python interpreter
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)

        # Check the return code for success
        if result.returncode == 0:
            # Return the output from the script
            return jsonify({"output": result.stdout})
        else:
            # Return an error message if the script failed
            return jsonify({"error": f"Script failed with return code {result.returncode}"}), 500

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({"error": str(e)}), 500


@app.route('/save_collector_config_details', methods=['POST'])
def save_details():
    data = request.json  # Assuming the client sends JSON data

    project_folder = '/Users/rahulkabothula/Desktop/RK/DataPal/odd-collectors/odd-collector'  # Specify the path to the other project folder
    config_path = os.path.join(project_folder, 'collector_config.yaml')

    try:
        # Check if config.yaml file exists
        if not os.path.exists(config_path):
            # Create config.yaml file with an empty dictionary
            with open(config_path, 'w') as file:
                yaml.dump({}, file)

        # Load existing config.yaml file
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        # Update config with received details
        config.update(data)

        # Write updated config to config.yaml file
        with open(config_path, 'w') as file:
            yaml.dump(config, file)

        return jsonify({'message': f'Details saved successfully. {data}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
