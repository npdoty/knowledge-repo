# Using official python runtime base image
FROM python:2.7

# Set the application directory
WORKDIR /app

# Copy our code from the current folder to /app inside the container
ADD . /app

# install the knowledge-repo toolkit, including dependencies
RUN pip install  --upgrade knowledge-repo

# load the Knowledge Repository
RUN git clone https://github.com/npdoty/knowledge-repo-patterns.git

EXPOSE 7000

# Define our command to be run when launching the container
# (customize the name of your knowledge repository here)
CMD ["knowledge_repo", "--repo", "knowledge-repo-patterns", "deploy"]