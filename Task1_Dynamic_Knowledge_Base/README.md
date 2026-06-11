# Dynamic Knowledge Base Chatbot

## Overview

This project implements a chatbot with a dynamically expanding knowledge base. The chatbot can periodically update its knowledge repository by incorporating new information from predefined sources and making that information available during conversations.

## Features

* Dynamic knowledge base expansion
* Automatic ingestion of new information from source files
* Periodic updates to the knowledge repository
* Semantic search for relevant information retrieval
* AI-powered chatbot interface
* Fast response generation using vector-based retrieval

## Technologies Used

* Python
* Pandas
* Sentence Transformers
* FAISS
* Streamlit

## Project Objective

Implement a system for dynamically expanding the chatbot's knowledge base. Create a mechanism to periodically update the vector database with new information from specified sources.

### Expected Outcome

A chatbot that can automatically incorporate new information into its responses over time without requiring manual retraining.

## Project Structure

Task1_Dynamic_Knowledge_Base
├── AI.txt
├── DataScience.txt
├── MachineLearning.txt
├── Python.txt
└── chatbot.py

## File Description

### AI.txt

Contains introductory information about Artificial Intelligence.

### DataScience.txt

Contains information related to Data Science concepts and applications.

### MachineLearning.txt

Contains basic Machine Learning concepts and learning mechanisms.

### Python.txt

Contains Python programming language information used as a knowledge source.

### chatbot.py

Main chatbot implementation responsible for loading, updating, and retrieving information from the knowledge base.

## Installation

```bash
pip install sentence-transformers faiss-cpu pandas streamlit
```

## Run the Application

```bash
streamlit run chatbot.py
```

## Author

Danusree Devasenan
