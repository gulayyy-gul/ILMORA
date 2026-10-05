from groq import Groq

from config.settings import GROQ_API_KEY


def get_client():

    if not GROQ_API_KEY:

        raise ValueError(
            "GROQ_API_KEY is missing."
        )

    return Groq(
        api_key=GROQ_API_KEY
    )
