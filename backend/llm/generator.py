import json

from backend.llm.client import get_client
from config.settings import GROQ_MODEL


SYSTEM_PROMPT = """
You are ILMORA, an AI-assisted Islamic research assistant.

Your role is to help users research Islamic scholarly sources.

IMPORTANT RULES:

1. Use ONLY the supplied evidence.
2. Do not invent facts, quotations, scholars, books, pages, or citations.
3. Do not present yourself as a religious authority.
4. Do not issue unsupported fatwas.
5. Clearly distinguish quotation from paraphrase.
6. Preserve scholarly disagreements.
7. Do not claim that one scholar is correct unless the supplied
   evidence explicitly supports that conclusion.
8. If the evidence is insufficient, say so.
9. Cite important claims using [E1], [E2], etc.
10. Never create an evidence label that does not exist.

Return your answer in clear, concise English.

The answer should contain:

- A direct answer
- Scholarly views when available
- Important evidence
- Limitations when evidence is insufficient
"""


def generate_answer(query, evidence):

    client = get_client()

    evidence_text = []

    for item in evidence:

        label = item.get("label", "")
        author = item.get("author", "Unknown")
        book = item.get("book", "Unknown")
        volume = item.get("volume", "")
        page = item.get("page", "")
        text = item.get("text", "")

        reference = (
            f"{label}\n"
            f"Author: {author}\n"
            f"Book: {book}\n"
            f"Volume: {volume}\n"
            f"Page: {page}\n"
            f"Passage:\n{text}"
        )

        evidence_text.append(reference)

    evidence_block = "\n\n".join(evidence_text)

    user_prompt = f"""
Research Question:

{query}


Retrieved Evidence:

{evidence_block}


Using ONLY the retrieved evidence above, answer the research question.

Remember:

- Cite claims using [E1], [E2], etc.
- Do not invent citations.
- Do not invent quotations.
- Preserve differences between scholars.
- If evidence is insufficient, explicitly say so.
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.1,
    )

    answer = response.choices[0].message.content

    labels_used = []

    for item in evidence:

        label = item.get("label")

        if label and label in answer:
            labels_used.append(label)

    return {
        "answer": answer,
        "scholarly_views": [],
        "limitations": [],
        "evidence_labels_used": labels_used,
    }
