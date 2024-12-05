
# AI Text Generator

This project implements an AI-powered text generation application using `transformers`, `torch`, and `streamlit`. Below is a detailed guide on how to set up, run, and use this project.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
3. [Running the Project](#running-the-project)
4. [Commands Used](#commands-used)
5. [Usage](#usage)

---

## Requirements

Ensure you have the following installed before proceeding:
- **Python 3.10 or 3.11** (recommended for compatibility with `torch` and `transformers`)
- **pip** (Python's package manager)
- **Git** (for version control, if cloning the repository)

---

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository using the following command:
```bash
git clone <repository-url>
cd AI_Text_Generator
```

### Step 2: Create a Virtual Environment
Set up a Python virtual environment to manage dependencies:
```bash
python3.10 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies
Install the required Python libraries:
```bash
pip install --upgrade pip
pip install transformers torch streamlit
```

---

## Running the Project

### Step 1: Start the Streamlit Application
Run the Streamlit app using the following command:
```bash
streamlit run app.py
```

### Step 2: Access the Web Application
After running the above command, you will see a local URL (e.g., `http://localhost:8501/`) in the terminal. Open this link in your browser to use the application.

---

## Commands Used

### Setting Up the Environment
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI_Text_Generator
   ```
2. **Create a virtual environment:**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   ```
3. **Install required dependencies:**
   ```bash
   pip install --upgrade pip
   pip install transformers torch streamlit
   ```

### Running the Application
4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

### Optional: Managing Git (if contributing)
5. **Check the status of your Git repository:**
   ```bash
   git status
   ```
6. **Push changes to the remote repository:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

---

## Usage

The application allows you to:
- Enter a text prompt.
- Generate AI-powered responses or continue text based on the prompt.

Once the application is running, follow the instructions on the web interface to generate AI-generated text. You can tweak the parameters (if available) for better customization.

---

## Troubleshooting

- **Error: "Could not find a version that satisfies the requirement torch"**
  - Ensure you're using Python 3.10 or 3.11, as later versions might not be supported.
  
- **Error: "Streamlit not found"**
  - Ensure you have activated your virtual environment and installed all dependencies.

---

Feel free to open issues or contribute to the project if you have any suggestions!
