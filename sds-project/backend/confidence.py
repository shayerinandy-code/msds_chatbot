from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from config import OPENAI_MODEL

llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)

CONFIDENCE_PROMPT = """
Rate confidence (0-10) that the provided SDS text
DIRECTLY answers the user's question.

Rules:
- 9–10: Exact match
- 7–8: Good match
- 6: Needs review
- Below 6: No solid answer

Return ONLY a number.
"""

def score_confidence(query: str, sds_text: str) -> int:
    response = llm.invoke([
        HumanMessage(content=CONFIDENCE_PROMPT),
        HumanMessage(content=f"Question:\n{query}\n\nSDS Text:\n{sds_text}")
    ])
    return int(response.content.strip())
