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
     - /new "Start a new conversation"
     - /details "Summarize all info retrieved in response to query"
     - /quotes "Display direct quotes relevant to query"
