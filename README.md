## Installation

#### 1. Clone this repository, activate a virtual environment and install the requirements.

```bash
pip install langchain openai chromadb tiktoken unstructured flask waitress atlassian-python-api beautifulsoup4
```

> Note: the project requires Python 3.11. It can work with Python 3.10 with some minor changes to the code.

#### 2. Installing Microsoft Visual C++ 14.0 or greater.

If step 1 succeeds, you can skip this step. Otherwise, you may get the following error:

```bash
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

If this happens, please install the Microsoft C++ Build Tools. You can get them [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Once installed, please try installing the requirements again.

#### 3. Copy the `.env.example` file to `.env` and fill in the values.

#### 4. Run the starter bot's flask server.

```bash
waitress-serve --listen=0.0.0.0:8000 main:app
```

You can use another server instead of `waitress` and another port instead of 8000. The script should then go through three steps to test the ability:

- to access the Confluence API
- to save documents
- to access the OpenAI API (it will ask you for permission) and create a vector database

#### 5. Set up a new Google Cloud Project.

Please create a new project and set up Firestore in it, in Native Mode. I have named my chatbot DocDocGo, so you can use this (or some variation) as the project name.

#### 6. Create a starter Google Chat App.

1. Follow the instructions outlined in this [Google Chat Quickstart Guide](https://developers.google.com/chat/quickstart/gcf-app).
2. In the section "Create and Deploy a Cloud Function", name the function "docdocgo".
3. In step 7 of the "Create and deploy a Cloud Function" section, please use the code in `./cloud-function/main.py` as the function's source code.
4. In that code, set the correct value for the `BUSINESS_LOGIC_API_URL` variable.
5. Please replace the cloud function's `requirements.txt` with the one in `./cloud-function/requirements.txt`.
6. In step 7 of the "Publish the app to Google Chat" section, enter:
   - App name: DocDocGo
   - Avatar URL: https://i.imgur.com/66tcUZL.png
   - Description: PoC chatbot to interact with Confluence
   - Under the "Slash commands" section, add the following commands:
     - /new "Start a new conversation", id = 1
     - /details "Summarize all info retrieved in response to query", id = 2
     - /quotes "Display direct quotes relevant to query", id = 3
     - /retry "Resend last generated answer (for time-outs)", id = 4
     - /help "Get help on using DocDocGo", id = 5
     - /tip "Get a random tip on using DocDocGo", id = 6


#### 7. Test the Chat App's ability to communicate with the business logic flask server.
1. Start a conversation with the Chat App.
2. Enter any message.
3. If you receive a response containing a chunk of one of the Confluence documents then all components are working!

## Running Remotely

### 1. Remote Server Access

To log into the server, use the following SSH command:

```
ssh ubuntu@35.90.110.30
```

### 2. Service Endpoints

- **Chat API Endpoint**: https://docdocgo.playground.carbon3d.com/chat
  > Note: This URL passes through a load balancer which handles SSL and port remapping.

- **Google Cloud Function URL**: [Link to GCP Function](https://console.cloud.google.com/functions/details/us-west1/docdocgo?env=gen1&project=docdocgo-394222&tab=source)

### 3. Docker Setup

The service is containerized using Docker and can be found in the following directory on the server:

```
~/docdocgo-prerequisites
```

#### Building the Docker Image:

Navigate to the directory and build the Docker image using:

```bash
cd ~/docdocgo-prerequisites
docker build -t docdocgo:latest .
```

#### Running the Docker Container:

To run the Docker container and expose port 8000:

```bash
docker run --name docdocgo -p 8000:8000 -d -i -t docdocgo:latest /bin/bash
```

#### Starting the Application:

To start the application inside the Docker container:

```bash
docker exec -it docdocgo /bin/bash
waitress-serve --listen=0.0.0.0:8000 main:app
```

> Note: Currently, this step is performed manually due to a prompt during startup.

#### Restarting the Docker Container:

If you need to restart an existing Docker container:

   ```bash
   docker stop docdocgo
   docker rm docdocgo
   ```

#### Saving Generated Data:

If you need to the jsonl documents and the Chroma vector database generated inside the container:

   ```bash
   docker cp docdocgo:/test-docs test-docs
   docker cp docdocgo:/test-dbs test-dbs
   ```
