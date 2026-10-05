```python
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ILMORA | Islamic Research",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# THEME
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- APP ---------- */

    .stApp {
        background: #F7F5EF;
    }

    [data-testid="stHeader"] {
        background: #F7F5EF;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background: #F1F0E9;
        border-right: 1px solid #E1DED5;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }


    /* ---------- TYPOGRAPHY ---------- */

    h1, h2, h3, h4 {
        color: #30332F !important;
    }

    p, label {
        color: #686C64;
    }


    /* ---------- BRAND ---------- */

    .brand-title {
        text-align: center;
        color: #536A52;
        font-size: 50px;
        font-weight: 800;
        letter-spacing: 6px;
        margin: 0;
        padding: 0;
    }

    .brand-tagline {
        text-align: center;
        color: #7A9278;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 4px;
        margin-top: 4px;
    }

    .brand-subtitle {
        text-align: center;
        color: #777A72;
        font-size: 14px;
        margin-top: 7px;
    }


    /* ---------- SIDEBAR BRAND ---------- */

    .sidebar-title {
        color: #536A52;
        font-size: 27px;
        font-weight: 800;
        letter-spacing: 3px;
        text-align: center;
    }

    .sidebar-tagline {
        color: #7A9278;
        font-size: 8px;
        font-weight: 700;
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 25px;
    }


    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #D8D6CC;
        background: #FFFDF8;
        color: #454942;
        font-weight: 600;
        min-height: 42px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #7A9278;
        color: #536A52;
    }

    div.stButton > button[kind="primary"] {
        background: #536A52;
        color: white;
        border: none;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #465C45;
        color: white;
    }


    /* ---------- INPUTS ---------- */

    textarea,
    input {
        border-radius: 12px !important;
        border-color: #D9D6CC !important;
        background: #FFFDF8 !important;
    }


    /* ---------- HERO ---------- */

    .hero-space {
        margin-top: 35px;
    }


    /* ---------- DIVIDER ---------- */

    hr {
        border-color: #E2DED4 !important;
    }


    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        padding: 15px;
        border-radius: 14px;
    }


    /* ---------- EXPANDERS ---------- */

    [data-testid="stExpander"] {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 14px;
    }


    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ---------- FOOTER ---------- */

    .footer-text {
        text-align: center;
        color: #777A72;
        font-size: 12px;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        .brand-title {
            font-size: 38px;
        }

        .brand-tagline {
            font-size: 8px;
            letter-spacing: 3px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Research"

if "query" not in st.session_state:
    st.session_state.query = ""

if "searched" not in st.session_state:
    st.session_state.searched = False

if "notes" not in st.session_state:
    st.session_state.notes = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">ILMORA</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-tagline">'
        'RESEARCH · DISCOVER · VERIFY'
        '</div>',
        unsafe_allow_html=True,
    )

    st.caption("WORKSPACE")

    if st.button("⌕  Research", use_container_width=True):
        st.session_state.page = "Research"
        st.rerun()

    if st.button("▣  Library", use_container_width=True):
        st.session_state.page = "Library"
        st.rerun()

    if st.button("⇄  Compare Scholars", use_container_width=True):
        st.session_state.page = "Compare"
        st.rerun()

    if st.button("✎  Notes", use_container_width=True):
        st.session_state.page = "Notes"
        st.rerun()

    if st.button("◷  History", use_container_width=True):
        st.session_state.page = "History"
        st.rerun()

    st.divider()

    st.caption("SOURCE FILTERS")

    st.selectbox(
        "Language",
        [
            "All Languages",
            "Arabic",
            "Urdu",
            "English",
        ],
    )

    st.selectbox(
        "Source type",
        [
            "All Sources",
            "Tafsir",
            "Hadith",
            "Fiqh",
            "Aqidah",
            "Seerah",
            "History",
        ],
    )

    st.divider()

    st.caption(
        "The sources are the authority.\n\n"
        "AI is the research assistant."
    )


# ============================================================
# BRAND
# ============================================================

st.markdown(
    '<div class="brand-title">ILMORA</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="brand-tagline">'
    'RESEARCH. DISCOVER. VERIFY.'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="brand-subtitle">'
    'AI-Assisted Islamic Research'
    '</div>',
    unsafe_allow_html=True,
)

st.divider()


# ============================================================
# RESEARCH
# ============================================================

if st.session_state.page == "Research":

    st.write("")

    st.title("What would you like to research?")

    st.write(
        "Explore scholarly sources, compare viewpoints, "
        "and trace ideas back to their original passages."
    )

    st.write("")

    query = st.text_area(
        "Research question",
        value=st.session_state.query,
        height=130,
        placeholder=(
            "Ask a research question...\n\n"
            "Example: What do classical scholars say "
            "about patience in the Qur'an?"
        ),
    )

    col1, col2 = st.columns([4, 1])

    with col1:

        st.caption(
            "Your question will be answered using retrieved "
            "scholarly evidence."
        )

    with col2:

        research_clicked = st.button(
            "Research →",
            type="primary",
            use_container_width=True,
        )

    if research_clicked:

        if not query.strip():

            st.warning(
                "Enter a research question to begin."
            )

        else:

            st.session_state.query = query
            st.session_state.searched = True

    st.write("")

    # --------------------------------------------------------
    # SUGGESTED RESEARCH
    # --------------------------------------------------------

    st.subheader("Suggested Research")

    st.caption(
        "Choose a starting point if you're not sure what to ask."
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        with st.container(border=True):

            st.markdown("### Qur'anic Themes")

            st.caption(
                "Explore how classical scholars explain "
                "important Qur'anic concepts."
            )

            if st.button(
                "Explore Tafsir",
                key="suggest_tafsir",
                use_container_width=True,
            ):

                st.session_state.query = (
                    "What do classical scholars say "
                    "about patience in the Qur'an?"
                )

                st.rerun()

    with c2:

        with st.container(border=True):

            st.markdown("### Hadith Research")

            st.caption(
                "Search hadith sources and examine "
                "scholarly explanations."
            )

            if st.button(
                "Explore Hadith",
                key="suggest_hadith",
                use_container_width=True,
            ):

                st.session_state.query = (
                    "What are the scholarly explanations "
                    "of the hadith about intentions?"
                )

                st.rerun()

    with c3:

        with st.container(border=True):

            st.markdown("### Compare Scholars")

            st.caption(
                "Examine agreements, differences, "
                "and supporting evidence."
            )

            if st.button(
                "Compare Views",
                key="suggest_compare",
                use_container_width=True,
            ):

                st.session_state.page = "Compare"
                st.rerun()

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if st.session_state.searched:

        st.divider()

        st.subheader("Research Result")

        st.caption(
            f"Research question: {st.session_state.query}"
        )

        st.info(
            "The RAG engine will retrieve relevant passages "
            "from the selected scholarly sources and generate "
            "a grounded synthesis."
        )

        st.markdown("#### Evidence")

        with st.expander(
            "E1 · View source evidence",
            expanded=True,
        ):

            st.write(
                "Source: Scholarly collection"
            )

            st.write(
                "Author: Source metadata will appear here"
            )

            st.write(
                "Volume / Page: Source metadata will appear here"
            )

            st.markdown(
                "Original passage will appear here after "
                "the retrieval pipeline is connected."
            )

        with st.expander("E2 · Supporting evidence"):

            st.write(
                "Supporting source information will appear here."
            )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.button(
                "View Evidence",
                use_container_width=True,
            )

        with col2:
            st.button(
                "Save Passage",
                use_container_width=True,
            )

        with col3:
            st.button(
                "Add Note",
                use_container_width=True,
            )

    # --------------------------------------------------------
    # CONTINUE
    # --------------------------------------------------------

    st.divider()

    st.subheader("Continue Your Research")

    c1, c2 = st.columns(2)

    with c1:

        with st.container(border=True):

            st.markdown("### Recent Research")

            st.caption(
                "Your previous research sessions will appear here."
            )

            st.button(
                "Open History →",
                key="research_history",
                use_container_width=True,
            )

    with c2:

        with st.container(border=True):

            st.markdown("### Your Library")

            st.caption(
                "Browse built-in and uploaded scholarly sources."
            )

            st.button(
                "Open Library →",
                key="research_library",
                use_container_width=True,
            )


# ============================================================
# LIBRARY
# ============================================================

elif st.session_state.page == "Library":

    st.title("Scholarly Library")

    st.write(
        "Browse sources, authors, collections, and uploaded documents."
    )

    st.write("")

    search = st.text_input(
        "Search library",
        placeholder="Search books, authors, topics...",
    )

    st.subheader("Collections")

    books = [
        (
            "Tafsir",
            "Qur'anic Commentary",
            "Classical and contemporary tafsir sources."
        ),
        (
            "Hadith",
            "Hadith Sources",
            "Hadith texts and scholarly explanations."
        ),
        (
            "Fiqh",
            "Jurisprudence",
            "Fiqh sources and comparative discussions."
        ),
        (
            "Seerah",
            "Prophetic Biography",
            "Seerah and early Islamic history."
        ),
    ]

    columns = st.columns(4)

    for column, book in zip(columns, books):

        with column:

            with st.container(border=True):

                st.caption(book[0].upper())

                st.markdown(
                    f"### {book[1]}"
                )

                st.caption(
                    book[2]
                )

                st.button(
                    "Explore →",
                    key=f"book_{book[0]}",
                    use_container_width=True,
                )

    st.divider()

    st.subheader("Add a Source")

    st.caption(
        "Upload a PDF or TXT document to your research workspace."
    )

    uploaded_file = st.file_uploader(
        "Upload source",
        type=["pdf", "txt"],
    )

    if uploaded_file:

        st.success(
            f"{uploaded_file.name} uploaded successfully."
        )

        st.info(
            "Document extraction and indexing will be connected "
            "to the RAG pipeline next."
        )


# ============================================================
# COMPARE
# ============================================================

elif st.session_state.page == "Compare":

    st.title("Compare Scholars")

    st.write(
        "Compare scholarly positions while preserving "
        "differences between sources."
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        scholar_1 = st.selectbox(
            "Scholar 1",
            [
                "Ibn Kathir",
                "Al-Tabari",
                "Al-Qurtubi",
            ],
        )

    with c2:

        scholar_2 = st.selectbox(
            "Scholar 2",
            [
                "Al-Tabari",
                "Ibn Kathir",
                "Al-Qurtubi",
            ],
        )

    with c3:

        scholar_3 = st.selectbox(
            "Scholar 3",
            [
                "Al-Qurtubi",
                "Ibn Kathir",
                "Al-Tabari",
            ],
        )

    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Patience in the Qur'an",
    )

    if st.button(
        "Compare Sources →",
        type="primary",
        use_container_width=True,
    ):

        st.divider()

        st.subheader("Scholarly Views")

        columns = st.columns(3)

        selected = [
            scholar_1,
            scholar_2,
            scholar_3,
        ]

        for column, scholar in zip(columns, selected):

            with column:

                with st.container(border=True):

                    st.markdown(
                        f"### {scholar}"
                    )

                    st.caption(
                        "Classical scholarly perspective"
                    )

                    st.write(
                        "The retrieved position, evidence, "
                        "and source references will appear here."
                    )

        st.subheader("Agreements & Differences")

        st.info(
            "The comparison engine will identify agreements, "
            "differences, evidence, and methodological observations."
        )


# ============================================================
# NOTES
# ============================================================

elif st.session_state.page == "Notes":

    st.title("Research Notes")

    st.write(
        "Save important passages, observations, and ideas "
        "from your research."
    )

    st.write("")

    note_title = st.text_input(
        "Note title",
        placeholder="e.g. Different views on patience",
    )

    note_text = st.text_area(
        "Your note",
        height=220,
        placeholder="Write your research observation here...",
    )

    if st.button(
        "Save Note",
        type="primary",
        use_container_width=True,
    ):

        if not note_text.strip():

            st.warning(
                "Write something before saving."
            )

        else:

            st.session_state.notes.append(
                {
                    "title": note_title or "Untitled note",
                    "text": note_text,
                }
            )

            st.success(
                "Note saved."
            )

    if st.session_state.notes:

        st.divider()

        st.subheader("Saved Notes")

        for note in reversed(
            st.session_state.notes
        ):

            with st.expander(
                note["title"]
            ):

                st.write(
                    note["text"]
                )


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.title("Research History")

    st.write(
        "Revisit previous research questions and continue "
        "exploring the evidence."
    )

    st.write("")

    history = [
        "What do classical scholars say about patience?",
        "How do scholars explain sincerity?",
        "Different interpretations of a Qur'anic concept.",
    ]

    for index, question in enumerate(history):

        with st.container(border=True):

            col1, col2 = st.columns(
                [5, 1]
            )

            with col1:

                st.markdown(
                    f"### {question}"
                )

                st.caption(
                    "Previous research session"
                )

            with col2:

                st.write("")

                st.button(
                    "Open",
                    key=f"history_{index}",
                    use_container_width=True,
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "The sources are the authority. "
    "AI is the research assistant."
)

st.caption(
    "ILMORA · AI-Assisted Islamic Research"
)
```
