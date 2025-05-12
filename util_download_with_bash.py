import subprocess
import shlex

def perform_download_with_bash(url):
  # command = f"gallery-dl --get-url {shlex.quote(url)}"
  command = f"gallery-dl --resolve-urls {shlex.quote(url)}"
  process = subprocess.Popen(
    shlex.split(command),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
  )
  stdout, stderr = process.communicate()

  output = stdout.decode()
  error = stderr.decode()

  return output, error
