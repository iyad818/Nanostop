import subprocess
import time
import shutil

bot_file = "bot.py"
python_cmd = shutil.which("python3") or shutil.which("python") or "python3"

print(f"🔍 Using Python command: {python_cmd}")

while True:
    try:
        print("\n🚀 Running bot... (Railway Active)")
        process = subprocess.Popen(
            [python_cmd, bot_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while True:
            output = process.stdout.readline()
            error_output = process.stderr.readline()

            if output:
                print(f"✅ Bot Active: {output.strip()}")
            if error_output:
                print(f"⚠️ Error: {error_output.strip()}")

            if process.poll() is not None:
                break

    except Exception as e:
        print(f"🔥 Critical Error: {e}")

    print("♻️ Restarting in 3 seconds...\n")
    time.sleep(3)
