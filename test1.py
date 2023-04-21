import os

pipe_name = 'named_pipe_test'

pipe = os.open(pipe_name, os.O_RDONLY)

data = os.read(pipe, 1024)
print(data.decode())

os.close(pipe)
