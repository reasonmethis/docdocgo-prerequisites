FROM python:3.11-bookworm

# Install python package dependencies
RUN pip install langchain openai chromadb tiktoken unstructured flask waitress atlassian-python-api beautifulsoup4

# Copy all application files into the container
COPY . .

RUN mkdir /test-docs
RUN mkdir /test-dbs


