# Project Name

Describe your project here. Provide an overview of what the project does and its purpose.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

What things you need to install the software and how to install them

Python 3.x
pip

### Installing

A step by step series of examples that tell you how to get a development environment running

First, clone the repository:

```bash
git clone https://github.com/IBobko/historyChart.git
cd historyChart
python -m venv venv        # Creates virtual environment
source venv/bin/activate   # Activates the virtual environment on Unix/Linux/MacOS
````

```shell
pip install -r requirements.txt
```

### Running the Application

```
export FLASK_APP=run.py      # Unix/Linux/MacOS
flask run
```

### Running the tests

```
python -m unittest discover
```