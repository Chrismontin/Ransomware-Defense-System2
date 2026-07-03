import os

folder = r"C:\test-folder"  # same folder your agent is monitoring

for i in range(50):
    with open(f"{folder}\\file_{i}.txt", "w") as f:
        f.write("ransomware simulation")

print("✅ Test files created")