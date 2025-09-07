# Implementing BabyAGI AI Agent

1. Clone the [BabyAGI](https://github.com/yoheinakajima/babyagi_archive) archive repository

   ```bash
   git clone https://github.com/yoheinakajima/babyagi_archive.git
   cd babyagi_archive
   ```

2. Open the folder in VSCode

   ```bash
   code .
   ```

3. Check your Python version

   ```bash
   python --version
   ```

   - If you are using Python version `3.12` or higher, edit the `requirements.txt` file to update the `tiktoken` version to `0.5.2` or higher
     - The version `0.3.3` doesn't support Python versions `3.12` or higher
       - The [wheels](https://pythonwheels.com/) for Python `3.12` were implemented in version `0.5.2`

     ```text
     tiktoken==0.5.2
     ```

4. Activate your virtual environment

   - Run `python -m venv venv/` (Linux/MacOS) or `py -m venv venv/` (Windows) to create a virtual environment on your project's folder
   - Run `source venv/bin/activate` or `. venv/bin/activate` (Linux/MacOS) or `venv/Scripts/activate` (Windows) to activate the virtual environment

5. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

6. Setup the environment variables

   ```bash
   cp .env.example .env
   ```

   - Change the `LLM_MODEL` to `gpt-4o` or `gpt-4o-mini`
   - Fill in the `OPENAI_API_KEY` with your OpenAI API key
   - Change the `OBJECTIVE` to something practical
     - For example: `"Write a short blog post about how to build AI agents"`

7. Run the script

   ```bash
   python babyagi.py
   ```

   - The agent will start creating tasks and executing them
     - Often the program will hang for a while due to rate limits in the OpenAI API
