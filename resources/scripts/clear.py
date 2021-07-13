dirPath = 'temp'

try:
    shutil.rmtree(dirPath)
except OSError as e:
    print(f"Error:{e.strerror}")

try:
    os.mkdir(dirPath)

except OSError as e:
    print(f"Error:{e.strerror}")
