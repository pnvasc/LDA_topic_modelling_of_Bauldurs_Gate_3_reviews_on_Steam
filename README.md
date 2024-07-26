# Topic Modelling of Baldur's Gate 3 Reviews on Steam

This project performs LDA-based topic modelling on a sample of 500 Steam reviews of the game Baldur's Gate 3.

## Fetch Reviews

First, we run the script Scraping_Baldurs_Gate.py to fetch 500 reviews from Steam.

1. Open a terminal or command prompt.

2. Navigate to your project directory:
   ```
   cd path/to/your/project
   ``` 

3. Run the scraping script:
   ```
   python Scraping_Baldurs_Gate.py
   ```

## Setting up a Python Virtual Environment

This guide explains how to set up a Python virtual environment using a `requirements.txt` file.

### Prerequisites

- Python 3.x installed on your system
- `pip` (Python package installer)

### Steps

1. Open a terminal or command prompt.

2. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. You're now ready to work in your virtual environment!

## Running the Jupyter Notebook

After setting up the virtual environment, follow these steps to run the analysis notebook:

1. Ensure your virtual environment is activated (see step 4 above).

2. If not already installed, install Jupyter:
   ```
   pip install jupyter
   ```

3. Register your virtual environment as a Jupyter kernel:
   ```
   pip install ipykernel
   python -m ipykernel install --user --name=baldurs_gate_3_reviews
   ```

4. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

5. In the Jupyter interface, click on 'LDA_topic_modelling_of_Bauldurs_Gate_3_reviews_on_Steam.ipynb' to open it.

6. In the notebook, select Kernel > Change kernel > baldurs_gate_3_reviews

7. You can now run the Baldur's Gate 3 reviews analysis notebook using the virtual environment's kernel.

To stop Jupyter, press Ctrl+C in the terminal and confirm.

## Notes

- Ensure your `requirements.txt` file is up to date with all necessary dependencies for your project.
- To deactivate the virtual environment when you're done, simply run:
  ```
  deactivate
  ```
- Ensure all required libraries for the LDA topic modeling are included in your `requirements.txt` file.
