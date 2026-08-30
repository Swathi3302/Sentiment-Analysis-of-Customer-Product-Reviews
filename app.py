import os
import sys
import subprocess

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    venv_python = os.path.join(base_dir, "venv", "Scripts", "python.exe")
    python_exe = venv_python if os.path.exists(venv_python) else sys.executable
    server_script = os.path.join(base_dir, "server.py")

    print("=" * 60)
    print("  Starting Sentiment AI Web Application")
    print("  URL: http://localhost:8000")
    print("=" * 60)

    try:
        subprocess.run([python_exe, server_script])
    except KeyboardInterrupt:
        print("\nSentiment AI server stopped.")

if __name__ == "__main__":
    main()
