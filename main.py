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
    