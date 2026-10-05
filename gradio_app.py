import gradio as gr


CSS = """
body {
    background: #F7F5EF !important;
}

#brand {
    text-align: center;
    padding: 28px 0 12px;
}

#brand h1 {
    margin: 0;
    font-size: 52px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #536A52;
}

#brand .tagline {
    margin-top: 6px;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
    color: #7A9278;
}

#brand .subtitle {
    margin-top: 8px;
    color: #777A72;
    font-size: 16px;
}

.nav {
    text-align: center;
    color: #536A52;
    font-weight: 600;
    padding: 8px;
}

.hero {
    text-align: center;
    padding: 35px 10px 20px;
}

.hero h2 {
    font-size: 34px;
    color: #30332F;
    margin-bottom: 8px;
}

.hero p {
    color: #777A72;
    font-size: 16px;
}

.card {
    background: #FFFDF8;
    border: 1px solid #E3E0D7;
    border-radius: 18px;
    padding: 18px;
}

.footer {
    text-align: center;
    color: #777A72;
    padding: 30px 0;
    font-size: 13px;
}
"""


def research(query):
    if not query.strip():
        return "Enter a research question to begin."

    return f"""
### Research Preview

**Question:** {query}

The research interface is ready.

The RAG backend will retrieve scholarly evidence,
compare viewpoints, and display citations here.
"""


with gr.Blocks(css=CSS, title="ILMORA") as demo:

    gr.HTML(
        """
        <div id="brand">

            <h1>ILMORA</h1>

            <div class="tagline">
                RESEARCH. DISCOVER. VERIFY.
            </div>

            <div class="subtitle">
                AI-Assisted Islamic Research
            </div>

        </div>

        <div class="nav">
            Research &nbsp;&nbsp;
            Library &nbsp;&nbsp;
            Compare &nbsp;&nbsp;
            Notes &nbsp;&nbsp;
            History
        </div>
        """
    )

    gr.HTML(
        """
        <div class="hero">

            <h2>
                What would you like to research?
            </h2>

            <p>
                Explore scholarly sources, compare viewpoints,
                and trace ideas back to their original passages.
            </p>

        </div>
        """
    )

    with gr.Column(elem_classes="card"):

        query = gr.Textbox(
            label="Research question",
            placeholder="e.g. What do classical scholars say about patience?",
            lines=3
        )

        research_btn = gr.Button(
            "Research",
            variant="primary"
        )

        result = gr.Markdown()

    gr.Markdown("### Suggested Research")

    with gr.Row():

        gr.Button("Tafsir")
        gr.Button("Hadith")
        gr.Button("Compare Scholars")

    gr.Markdown("### Continue Your Research")

    with gr.Row():

        gr.Markdown(
            """
            **Recent Research**

            Your recent research sessions will appear here.
            """
        )

        gr.Markdown(
            """
            **Your Library**

            Browse built-in and uploaded scholarly sources.
            """
        )

    gr.HTML(
        """
        <div class="footer">
            The sources are the authority.
            AI is the research assistant.
        </div>
        """
    )

    research_btn.click(
        research,
        inputs=query,
        outputs=result
    )


if __name__ == "__main__":
    demo.launch()
