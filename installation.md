# How to Install Jupyter Notebooks and Miniconda

## Step 1: Install Miniconda

### **Windows:**

1. Download the Miniconda installer for Windows from the Miniconda website: [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/en/latest/miniconda.html).

2. Double-click the downloaded `.exe` file to run the installer.

3. Follow the on-screen instructions to install Miniconda. Choose the "Just Me" option for installation scope and the default installation location.

4. After installation, open the "Anaconda Prompt" or "Miniconda3" command prompt from the Start menu.

### **macOS:**

1. Open a terminal window.

2. Install Miniconda for macOS using Homebrew:

   ```bash
   brew install --cask miniconda
   ```

3. Follow the on-screen instructions to complete the installation. When prompted, press Enter to accept the license agreement and select the default installation location.

### **Linux(Ubuntu):**

1. Open a terminal window.

2. Install Miniconda for Linux using the package manager (e.g., apt on Ubuntu):

    ```bash
    sudo apt update
    sudo apt install miniconda
    ```

3. Follow the on-screen instructions to complete the installation. When prompted, press Enter to accept the license agreement and select the default installation location.

## Step 2: Create a Conda Environment

1. Open a terminal or command prompt.

2. Create a new Conda environment and install Jupyter Notebook by running the following command:

    ```bash
    conda create -n myenv python=3.x
    ```

    Replace myenv with the desired environment name and 3.x with your preferred Python version (e.g., 3.8, 3.9, etc.).

3. Activate the newly created environment:

    - On Windows:

        ```bash
        conda activate myenv
        ```

    - On macOS/Linux:

        ```bash
        source activate myenv
        ```

## Step 3: Install Jupyter Notebook

1. While the Conda environment is active, install Jupyter Notebook using the following command:

    ```bash
    conda install -c anaconda jupyter
    ```

## Step 4: Launch Jupyter Notebook

1. In the same terminal where your Conda environment is active, run the following command to start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2. This will open a new browser window or tab displaying the Jupyter Notebook interface.

Now you have successfully installed Jupyter Notebooks and Miniconda on your computer and can begin using them within your Conda environment.