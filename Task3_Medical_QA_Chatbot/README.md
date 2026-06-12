# Medical Q&A Chatbot using MedQuAD

## Project Overview

The Medical Q&A Chatbot is an AI-powered application developed using the MedQuAD (Medical Question Answering Dataset). It enables users to ask medical questions and retrieves the most relevant answers using semantic search techniques and basic medical entity recognition.

The application is built with Python and Streamlit, providing a simple and interactive interface for users to explore medical information.

---

## Key Features

* Retrieves relevant answers from the MedQuAD dataset.
* Uses Sentence Transformers for semantic similarity search.
* Recognizes basic medical entities such as:

  * Symptoms
  * Treatments
  * Diagnoses
* Displays a confidence score for the retrieved result.
* Provides a user-friendly web interface using Streamlit.

---

## Technologies Used

* Python
* Streamlit
* Sentence Transformers
* XML Parsing
* MedQuAD Dataset

---

## Project Structure

```text
Task3_Medical_QA_Chatbot/
│── app.py
│── chatbot_v3.py
│── REPORT.docx
│── README.md
```

---

## How to Run the Project

1. Install the required Python libraries.
2. Open a terminal in the project folder.
3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in your browser.
5. Enter a medical query such as:

   * `breast cancer symptoms`
   * `breast cancer treatment`
   * `melanoma diagnosis`

---

## Sample Functionality

The chatbot:

* Detects the type of medical query.
* Performs semantic search on the MedQuAD dataset.
* Calculates a confidence score.
* Returns the most relevant medical question and answer available in the dataset.

---

## Disclaimer

This project is intended for educational purposes only. The information provided is retrieved from the MedQuAD dataset and should not be considered professional medical advice, diagnosis, or treatment. Users should consult qualified healthcare professionals for medical concerns.

---

## Author

Jency Jerushiya J

