import json

# Create variable for log path file 
log_file = '/opt/cowrie/var/log/cowrie.json'

# Open file and process each line as JSON object
with open(log_file, "r") as f:
    for line in f:
        try:
            #Parse line as json
            log_entry = json.loads(line.strip())

            timestemp = log_entry.get("timestamp", "N/A")
            src_ip = log_entry.get('src_ip', 'N/A')
            srcport = log_entry.get('src_port', 'N/A')
            username = log_entry.get('username', 'N/A')
            password = log_entry.get('password', 'N/A')

            print(f"Timestamp: {timestemp}, Source IP: {src_ip}, Source Port: {srcport}, Username: {username}, Password: {password}")
        except json.JSONDecodeError:
            print('Could not parse line: ', line)
        

    