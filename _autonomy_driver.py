import subprocess, sys, time, os

# Background driver: runs the autonomy loop once every 30 minutes.
# The loop itself posts exactly ONE Moltbook draft per tick (_moltbook_post_one),
# respecting Moltbook's rate/trust limit. This is the patient drip.
REPO = r"C:\one\paperclip-company"
LOOP = os.path.join(REPO, "autonomy-loop.py")
TICK = 30 * 60  # 30 min

while True:
    try:
        subprocess.run([sys.executable, LOOP], cwd=REPO, timeout=300)
    except Exception as e:
        sys.stderr.write(f"loop error: {e}\n")
    time.sleep(TICK)
