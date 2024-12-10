import json

def json_to_oneliner_with_escape():
    print("Enter JSON text (end with Ctrl+D or Ctrl+Z on a new line depending on your OS, and press Enter/ return twice):")
    try:
        # Read multi-line input from the user
        json_text = "".join(iter(input, ""))
        
        # Parse and validate JSON
        json_object = json.loads(json_text)
        
        # Convert to one-liner with escaped double quotes
        oneliner_json = json.dumps(json_object, separators=(',', ':'))
        escaped_json = oneliner_json.replace('"', '\\"')
        
        print("Escaped and formatted JSON (one-liner):")
        print(escaped_json)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON input: {e}")

def oneliner_to_formatted_json():
    print("Enter escaped and one-liner JSON text (end with Ctrl+D or Ctrl+Z on a new line depending on your OS, and press Enter/ return twice):")
    try:
        # Read multi-line input from the user
        escaped_json = "".join(iter(input, ""))
        
        # Remove escape characters
        unescaped_json = escaped_json.replace('\\"', '"')
        
        # Parse and validate JSON
        json_object = json.loads(unescaped_json)
        
        # Convert to pretty-formatted JSON
        formatted_json = json.dumps(json_object, indent=2)
        
        print("Formatted JSON text:")
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON input: {e}")

def main():
    print("Choose an option:")
    print("1. Convert JSON to one-liner with escaped characters")
    print("2. Convert one-liner JSON to formatted JSON without escape characters")
    
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        json_to_oneliner_with_escape()
    elif choice == '2':
        oneliner_to_formatted_json()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()