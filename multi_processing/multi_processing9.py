import subprocess

subprocess.run('find ./ -name "*.html"|xargs grep "python"', shell=True)
