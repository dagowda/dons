import donut
import sys

def banner():
    print(r"""
     ____                  
    |  _ \  ___  _ __  ___ 
    | | | |/ _ \| '_ \/ __|
    | |_| | (_) | | | \__ \
    |____/ \___/|_| |_|___/
    
    Donut Shellcode Generator by dagowda
    """)

def main():
    if len(sys.argv) != 2:
        print("Invalid arguments: Usage 'python3 donut.py <windows executable>'")
        sys.exit(1)

    dll_path = sys.argv[1]
    output_file = "/tmp/shellcode.bin"

    try:
        shellcode = donut.create(file=dll_path)
        with open(output_file, "wb") as f:
            f.write(shellcode)
        print(f"Shellcode written to {output_file}")
    except Exception as e:
        print(f"Error generating shellcode: {e}")

if __name__ == "__main__":
    banner()
    main()
