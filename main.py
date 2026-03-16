import os


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class KeyValueStore:
    def __init__(self):
        self.index = {}

    # Find the index of a key in the store. Return -1 if the key is not found.
    def find_key(self, key):
        for i in range(len(self.index)):
            if self.index[i].key == key:
                return i
            return -1
     
    # Set a key-value pair in the store. If the key already exists, update its value.    
    def set (self, key, value):
        idx = self.find_key(key)
        if idx == -1:
            self.index.append(Entry(key, value))
        else:
            self.index[idx].value = value
    
    # Get the value associated with a key. Return None if the key is not found.
    def get(self, key):
        idx = self.find_key(key)
        if idx == -1:
            return None
        return self.index[idx].value
            
            
def run_cli():
    while True:
        try: 
            command = input().strip() # Read user input and remove leading/trailing whitespace
        except EOFError:
            break
        if command == "exit":
            break
        
        if command.startswith("SET"):
            parts = command.split()
            if len(parts) == 3:
                print("OK")
            else:
                print("ERROR")
        
        elif command.startswith("GET"):
            parts = command.split(" ", 1) # Split into at most 2 parts
            if len(parts) == 2:
                print("NULL")
            else:
                print("ERROR")
        else:
            print("ERROR")

if __name__ == "__main__":
    run_cli()
    