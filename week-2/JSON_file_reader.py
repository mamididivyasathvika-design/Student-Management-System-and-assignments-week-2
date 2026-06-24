import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check if the file format is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_name = 'data.json'
read_json_file(file_name)