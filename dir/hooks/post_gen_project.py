import subprocess

# Create git repo.
subprocess.call(['git', 'init'])
subprocess.call(["git", "config", "user.name", "{{ cookiecutter.author_name }}"])
subprocess.call(["git", "config", "user.email", "{{ cookiecutter.author_email }}"])
subprocess.call(['git', 'add', '--all'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
