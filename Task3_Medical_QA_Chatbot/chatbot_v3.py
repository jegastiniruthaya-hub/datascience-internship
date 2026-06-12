import os
import warnings
import xml.etree.ElementTree as ET

from sentence_transformers import SentenceTransformer, util

warnings.filterwarnings("ignore")

folder_path = r"C:\Users\jency jerushiya\Downloads\MedQuAD-master\MedQuAD-master\1_CancerGov_QA"

print("Loading AI model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

questions = []
answers = []

print("Reading dataset...")

for filename in os.listdir(folder_path):

    if filename.endswith(".xml"):

        file_path = os.path.join(folder_path, filename)

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            for qa in root.findall(".//QAPair"):

                question = qa.find("Question")
                answer = qa.find("Answer")

                if question is not None and answer is not None:

                    questions.append(question.text)
                    answers.append(answer.text)

        except Exception:
            pass

print("Creating AI embeddings...")

question_embeddings = model.encode(
    questions,
    convert_to_tensor=True
)

print("AI ready!")


# ----------------------------
# Basic Medical Entity Recognition
# ----------------------------
def detect_entity(question):

    question = question.lower()

    if "symptom" in question or "symptoms" in question:
        return "Symptom"

    elif "treatment" in question or "treat" in question:
        return "Treatment"

    elif "diagnosis" in question or "diagnose" in question:
        return "Diagnosis"

    elif "disease" in question:
        return "Disease"

    return "General Medical Query"


# ----------------------------
# Main Chatbot Function
# ----------------------------
def get_response(user_question):

    entity = detect_entity(user_question)

    query_embedding = model.encode(
        user_question,
        convert_to_tensor=True
    )

    scores = util.cos_sim(
        query_embedding,
        question_embeddings
    )[0]

    best_idx = scores.argmax().item()

    best_question = questions[best_idx]
    best_answer = answers[best_idx]

    confidence = float(scores[best_idx])

    if confidence < 0.50:

        return (
            f"Detected Entity: {entity}\n\n"
            f"Confidence Score: {confidence:.2f}\n\n"
            "No reliable answer found in the current dataset.\n"
            "Please try a more specific medical question."
        )

    return (
    f"Detected Entity: {entity}\n\n"
    f"Confidence Score: {confidence:.2f}\n\n"
    f"Best Match:\n{best_question}\n\n"
    f"Answer:\n{best_answer}"
)