import os


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class KeyValueStore:
    def __init__(self, filename="data.db"):
        self.filename = filename
        self.index = []
        self.load_from_disk()

    # Find the index of a key in the store. Return -1 if the key is not found.
    def find_key(self, key):
        for i in range(len(self.index)):
            if self.index[i].key == key:
                return i
        return -1

    # Set a key-value pair in memory. This updates the in-memory index but does not persist to disk.
    def set_memory(self, key, value):
        idx = self.find_key(key)
        if idx == -1:
            self.index.append(Entry(key, value))
        else:
            self.index[idx].value = value
            
    # Append a key-value pair to the disk file. This is used to persist changes to the store.
    def append_disk(self, key, value):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"SET\t{key}\t{value}\n")
            file.flush()
            os.fsync(file.fileno())
            
    # Set a key-value pair in the store. If the key already exists, update its value.
    def set(self, key, value):
        self.append_disk(key, value)
        self.set_memory(key, value)

    # Get the value associated with a key. Return None if the key is not found.
    def get(self, key):
        idx = self.find_key(key)
        if idx == -1:
            return None
        return self.index[idx].value

    # Save the current state of the store to disk. This is used to persist the store across sessions.
    def load_from_disk(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n")
                parts = line.split("\t", 2)

                if len(parts) != 3:
                    continue

                command, key, value = parts

                if command == "SET":
                    self.set_memory(key, value)


# Command-line interface for the key-value store. This allows users to interact with the store using simple commands.
def run_cli():
    store = KeyValueStore()

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if not command:
            continue

        if command == "EXIT":
            break

        if command.startswith("SET "):
            parts = command.split(" ", 2)

            if len(parts) != 3:
                print("ERROR", flush=True)
                continue

            _, key, value = parts
            store.set(key, value)
            print("OK", flush=True)

        elif command.startswith("GET "):
            parts = command.split(" ", 1)
            if len(parts) != 2:
                print("ERROR", flush=True)
                continue
            
            _, key = parts
            value = store.get(key)

            if value is None:
                print(flush=True)
            else:
                print(value, flush=True)
        else:
            print("ERROR", flush=True)

if __name__ == "__main__":
    run_cli()