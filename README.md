# Seatable OpenAI Integration
<img src="assets/seatable.png" alt="Seatable logo" width="48"/><img src="assets/bidirectional.png" alt="Bidirectional" width="48"/><img src="assets/openai.svg" alt="OpenAI logo" width="48"/>

## Overview
This repository demonstrates the seamless integration of the OpenAI API within Seatable, enabling the exchange of prompts with ChatGPT.

Key features:
- Python script tailored for Seatable Cloud usage
- OpenAI API interaction via HTTP requests

## Example Usage
Consider a table with three essential columns:

| Name | Meaning | Action  |
|------|---------|---------|
| Bob  |         | [Button] |
| Anna |         | [Button] |
| Joe  |         | [Button] |


Each row contains a unique **name** entry. The **Action** column houses a button. When activated, a Python script is executed. This script retrieves the name from the corresponding row, transmits a predefined prompt to OpenAI with the name, and finally stores the response in the designated **meaning** field.


## Prerequisites
- An active OpenAI account with an associated billing plan
- An OpenAI API Key, see [Account settings](https://platform.openai.com/account/api-keys)
- An account with seatable.io 

   (Pleasebe aware of potential rate limits depending on your billing plan)

## Getting Started
1. Create a new Base on Seatable.io.
2. Add a Python script and paste the code from `script.py`.
3. The script requires some customizations for seamless operation. Refer to the provided instructions.
4. Introduce the following columns:
   - **Name** (type: text)
   - **Meaning** (type: formatted text)
   - **Action** (type: button, action: Execute the Python script)
5. Press a button to automatically receive the meaning of the corresponding name.

## Limitations
The execution of python scripts within seatable.io has a time constraint. Because of that, more complex queries can cause a timeout. 
## Attribution
- `bidirectional.png` by DinosoftLabs

