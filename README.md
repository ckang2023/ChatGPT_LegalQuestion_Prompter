# ChatGPT_LegalQuestion_Prompter
By Northwestern Innovation Lab Group 7

## Installation

### Prerequisites

Install git on your machine: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Install Python 3 on your machine (project default is Python 3.7): https://www.python.org/downloads/

Set up a integrated development environment (IDE) on your machine. Recommendation: PyCharm, VSCode

### Local Setup

In terminal, `cd` into `git` directory. 

Then, `git clone` the repository. (Using HTTP Link)

`cd` into the cloned project repository. 

**Check out a new branch for local testing** (Very important to avoid version control conflicts)

command line: `git checkout -b local_testing_branch_myname`.

You can use `git branch` to check your current branch.

Then, you need to setup a virtual environment for the project to be configured: 

`python3 -m venv /path/to/cloned_repository_on_your_machine`

Activate virtual environment: `source /path/to/venv/bin/activate`

Afterwards, install the project's dependencies with command: 

`pip install -r requirements.txt` (Note, you might need to install pip if error pops up)

## Usage

### Single .xml File Test on Local Web App

#### Launching Platform

After cloning the repository to your local machine, `cd` into the cloned project repository. 

The Web App is implemented in the **demo_ui** branch. To ensure you are at the current branch, do `git checkout demo_ui`.

Afterwards, do `git branch` to ensure you are at the right branch. 

Activate the virtual environment, then, do `chatgpt install`. A Firefox browser window will show up, you can log into ChatGPT and check that it is working properly. Afterwards, close that window, and exit out of the install mode by typing `!exit` in terminal.

At this point, you have logged into ChatGPT. 

Afterwards, do `python3 __init__.py`, then `python3 main.py`. 

In terminal, you will see messege `Running on http://127.0.0.1:5000/`. This means that the app is running at address http://127.0.0.1:5000/ on your local machine. 

Go to this address, you will see the homepage for the web app. Follow the instructions on the homepage to complete the testing process. 

Below is the screen record for a complete use case.



https://user-images.githubusercontent.com/56417619/232988646-f3c20a86-f8e0-4bb0-889d-51416fbc9bbb.mov




https://user-images.githubusercontent.com/56417619/232989549-6d257c94-0675-4720-b075-4ad61db2e09f.mov




https://user-images.githubusercontent.com/56417619/232989756-ba83f645-ff75-4382-bf00-2cb197f3253a.mov





https://user-images.githubusercontent.com/56417619/232990065-b02195f5-edb9-41c8-9e6f-6f2782a96704.mov

### Select Test Data

The current maximum number of prompts is around 250. Based on the size of `.xml` files we are using, it is about 4 files per test. 

Delete all existing files in the `xmlData` folder. 

Put the `.xml` files you want to focus on for your current experiment in the `xmlData` folder. (You can find untested files in `unProcessedXmlData`).

### Test Using Terminal
In terminal, process the data by running: `python3 path/to/dataProcessor.py`

Then, you can check for processed data at `processedData/processedJsonData.txt`

To get ready for automatic prompting, you need to first log into ChatGPT.

In terminal, do `chatgpt install`. A Firefox browser window will show up, you can log in to ChatGPT and check that is is working properly. Afterwards, close that window, and exit out of the install mode by typing `!exit` in terminal.

Then, start ChatGPT again by typing `chatgpt` in terminal. 

Afterwards, open a new terminal window, `cd` into the project directory, activate the virtual environment, **verify that you are at your local testing branch**. At this point, you have processed the data and started ChatGPT, start the automatic prompting process via command:

`python3 path/to/premiseHypothesisPrompter.py`

The automatic prompting will start, it will print out the total number of prompts being tested and it will also print out ChatGPT's response to each prompt. 

When the process finishes, the results will be in `results/resultsDataJson.json`.

To output result into Google sheet, copy this file into `resultsForGoogleSheet/` and put a proper name for it. 


## Data
