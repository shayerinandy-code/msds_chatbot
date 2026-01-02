# confidence.py
def calculate_confidence(question: str, answer: str, mode="exact"):
    if not answer:
        return 0.0

    if mode == "exact":
        return 9.5

    q_words = set(question.lower().split())
    a_words = set(answer.lower().split())

    overlap = len(q_words & a_words)
    ratio = overlap / max(len(q_words), 1)

    return round(min(8.0, max(5.0, ratio * 10)), 1)
