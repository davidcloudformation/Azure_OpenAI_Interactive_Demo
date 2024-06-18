# Azure OpenAI Interactive Demo

This repository contains a demo of using Azure OpenAI for various tasks, including data preparation, model training, and model inference. 
The demo is structured into Jupyter notebooks and Python scripts for ease of use and reproducibility.

## Repository Structure

- `notebooks/`: Contains Jupyter notebooks for interactive exploration and demonstration.
    - `01_data_preparation.ipynb`: Notebook for data preparation.
    - `02_model_training.ipynb`: Notebook for model training.
    - `03_model_inference.ipynb`: Notebook for model inference.

- `scripts/`: Contains Python scripts for automated execution.
    - `data_preparation.py`: Script for data preparation.
    - `model_training.py`: Script for model training.
    - `model_inference.py`: Script for model inference.

- `data/`: Contains sample data used in the demo.
    - `sample_data.csv`: Sample data file.

- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.
- `.gitignore`: Git ignore file.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Azure subscription
- Azure OpenAI resource

### Installation

1. Clone the repository:
   ```bash
   git clone https://davidcloudformation/Azure_OpenAI_Interactive_Demo.git
   cd Azure_OpenAI_Interactive_Demo
   
2. Install the required Python packages
	```bash
   pip install -r requirements.txt
3. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
### Usage
4.Jupyter Notebooks 
#### Start Jupyter Notebook: 
   
     jupyter notebook
##### Open and run the notebooks in the notebooks/ directory.

5.Python Scripts
#### Run the data preparation script:
   ```bash
   python scripts/data_preparation.py
   ```
##### Run the model training script:
   ```
   python scripts/model_training.py
   ```

##### Run the model inference script:
   ```
	python scripts/model_inference.py
   ```
   



