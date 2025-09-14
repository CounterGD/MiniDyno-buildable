project('MiniDyno', 'python',
  version : '1.0.0',
  license : 'MIT'
)

py_mod = import('python')
py = py_mod.find_installation('python3')

run_target('run_bot',
  command : [py, 'bot.py']
)

run_target('run_api',
  command : [py, '-m', 'uvicorn', 'api.server:app', '--reload']
)

run_target('lint',
  command : [py, '-m', 'flake8', '.']
)

run_target('docker_build',
  command : ['docker', 'build', '-t', 'minidyno', '.']
)

run_target('docker_run',
  command : ['docker', 'run', '-it', '--rm', '-p', '8000:8000', 'minidyno']
)
