# FROM baseImage:tag
FROM python:latest

# WORKDIR /the/workdir/path, it's like doing 1.mkdir /app 2. cd /app
# Set the working directory for any subsequent ADD, COPY, CMD, ENTRYPOINT, or RUN instructions that follow it in the Dockerfile.
# WORKDIR /path/to/workdir
# WORKDIR relative/path
WORKDIR /app

# COPY [flags] source ... dest
# The name of the destination file or folder.
# Copy new files and directories to the image's filesystem.
# . is the current directory which is /app
COPY requirements.txt .


# RUN command parameter ...
# The command to run.
# Execute commands inside a shell.
RUN pip install -r requirements.txt


COPY hello.py .

# Instruction has no argumentsdockerfile-utils(2)
# Define the network ports that this container will listen on at runtime.
EXPOSE 5000


# CMD [ "executable" ]
# Provide defaults for an executing container. If an executable is not specified, then ENTRYPOINT must be specified as well. There can only be one CMD instruction in a Dockerfile.
# CMD [ "/bin/ls", "-l" ]

# Configures the container to be run as an executable.
# ENTRYPOINT [ "/opt/app/run.sh", "--port", "8080" ]
ENTRYPOINT ["/bin/bash", "-c"]

# CMD [ "parameter", "parameter2", ... ]
# A parameter to the entrypoint executable.
# Set the default parameters for this executing container. An ENTRYPOINT instruction must also be specified.
# Executed at the container run time
# this doesn't work with the entry point since it get executed in the exec mode which run in the standard shell sh
# works without entrypoint command
# CMD [ "python", "hello.py" ] 
# CMD ["python hello.py"]
# this works with the entrypoint instruction
# CMD ["echo 'Running some setup...' && python hello.py"] 
# this works with the entrypoint instruction
CMD ["python hello.py"]  

