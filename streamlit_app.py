
import os
import hashlib
import tempfile

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
# CUSTOM THEME
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
       ========================= */

    .stApp {
        background-color: #F7F5EF;
    }

    [data-testid="stHeader"] {
        background-color: #F7F5EF;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* =========================
       TYPOGRAPHY
       ========================= */

    h1, h2, h3, h4 {
        color: #30332F !important;
        letter-spacing: -0.3px;
    }

    p {
        color: #686C64;
    }

    /* =========================
       SIDEBAR
       ========================= */

    [data-testid="stSidebar"] {
        background-color: #F0EFE8;
        border-right: 1px solid #E0DED5;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    /* =========================
       ILMORA BRAND
       ========================= */

    .ilmora-brand {
        text-align: center;
        color: #536A52;
        font-size: 48px;
        font-weight: 800;
        letter-spacing: 7px;
        margin-top: 10px;
        margin-bottom: 2px;
    }

    .ilmora-tagline {
        text-align: center;
        color: #789075;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 4px;
    }

    .ilmora-subtitle {
        text-align: center;
        color: #777A72;
        font-size: 14px;
        margin-top: 6px;
    }

    /* =========================
       SIDEBAR BRAND
       ========================= */

    .sidebar-brand {
        text-align: center;
        color: #536A52;
        font-size: 27px;
        font-weight: 800;
        letter-spacing: 4px;
    }

    .sidebar-tagline {
        text-align: center;
        color: #789075;
        font-size: 8px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 24px;
    }

    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #D8D6CC;
        background-color: #FFFDF8;
        color: #454942;
        font-weight: 600;
        min-height: 42px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #7A9278;
        color: #536A52;
    }

    /* =========================
       INPUTS
       ========================= */

    textarea,
    input {
        border-radius: 12px !important;
        border-color: #D8D5CB !important;
        background-color: #FFFDF8 !important;
    }

    /* =========================
       METRICS
       ========================= */

    [data-testid="stMetric"] {
        background-color: #FFFDF8;
        border: 1px solid #E1DED5;
        border-radius: 14px;
        padding: 14px;
    }

    /* =========================
       EXPANDERS
       ========================= */

    [data-testid="stExpander"] {
        background-color: #FFFDF8;
        border: 1px solid #E1DED5;
        border-radius: 14px;
    }

    /* =========================
       FILE UPLOADER
       ========================= */

    [data-testid="stFileUploader"] {
        background-color: #FFFDF8;
        border-radius: 14px;
    }

    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #E1DED5 !important;
    }

    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 768px) {

        .ilmora-brand {
            font-size: 38px;
            letter-spacing: 5px;
        }

        .ilmora-tagline {
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


if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "indexed_count" not in st.session_state:
    st.session_state.indexed_count = 0


# ============================================================
# BACKEND CONNECTION
# ============================================================

def _configure_secrets():
    """Make Streamlit secrets available to the backend configuration."""
    try:
        if st.secrets.get("GROQ_API_KEY"):
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

        if st.secrets.get("GROQ_MODEL"):
            os.environ["GROQ_MODEL"] = st.secrets["GROQ_MODEL"]

        if st.secrets.get("EMBEDDING_MODEL"):
            os.environ["EMBEDDING_MODEL"] = st.secrets["EMBEDDING_MODEL"]

        if st.secrets.get("CHROMA_DIR"):
            os.environ["CHROMA_DIR"] = st.secrets["CHROMA_DIR"]
    except Exception:
        # Local .env configuration can still be used.
        pass


_configure_secrets()


@st.cache_resource(show_spinner="Loading ILMORA research engine...")
def get_rag_engine():
    from backend.rag_engine import ILMORARAG
    return ILMORARAG()


def get_research_service():
    from backend.services.research_service import ResearchService
    return ResearchService(get_rag_engine())


def _source_id(filename, file_bytes):
    digest = hashlib.sha1(file_bytes).hexdigest()[:10]
    stem = os.path.splitext(filename)[0]
    safe_stem = "".join(
        char.lower() if char.isalnum() else "_"
        for char in stem
    ).strip("_")
    return f"{safe_stem or 'source'}_{digest}"


def _save_uploaded_file(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[1].lower()
    file_bytes = uploaded_file.getvalue()

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    )
    temp.write(file_bytes)
    temp.close()

    return temp.name, file_bytes


def _display_research_result(result):
    answer = result.get("answer", "").strip()

    if answer:
        st.markdown("#### Answer")
        st.write(answer)

    limitations = result.get("limitations", [])
    if limitations:
        st.warning(" | ".join(str(item) for item in limitations))

    evidence = result.get("evidence", [])

    st.markdown("#### Evidence")

    if not evidence:
        st.info(
            "No supporting evidence was retrieved from the indexed sources."
        )
        return

    for item in evidence:
        label = item.get("label", "Evidence")
        author = item.get("author") or "Unknown author"
        book = item.get("book") or "Unknown source"
        volume = item.get("volume")
        page = item.get("page")
        passage = item.get("text", "")

        reference_parts = [book, author]

        if volume:
            reference_parts.append(f"Vol. {volume}")

        if page:
            reference_parts.append(f"p. {page}")

        with st.expander(
            f"{label} · {' · '.join(reference_parts)}",
            expanded=(label == "E1"),
        ):
            st.caption("SOURCE")
            st.write(f"{book} — {author}")

            st.caption("ORIGINAL PASSAGE")
            st.write(passage)

            st.caption("REFERENCE")
            st.write(" · ".join(reference_parts))

            if item.get("chunk_id"):
                st.caption(f"Evidence ID: {item['chunk_id']}")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">ILMORA</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-tagline">'
        'RESEARCH · DISCOVER · VERIFY'
        '</div>',
        unsafe_allow_html=True,
    )

    st.caption("WORKSPACE")

    if st.button(
        "⌕  Research",
        use_container_width=True,
    ):
        st.session_state.page = "Research"
        st.rerun()

    if st.button(
        "▣  Library",
        use_container_width=True,
    ):
        st.session_state.page = "Library"
        st.rerun()

    if st.button(
        "⇄  Compare Scholars",
        use_container_width=True,
    ):
        st.session_state.page = "Compare"
        st.rerun()

    if st.button(
        "✎  Notes",
        use_container_width=True,
    ):
        st.session_state.page = "Notes"
        st.rerun()

    if st.button(
        "◷  History",
        use_container_width=True,
    ):
        st.session_state.page = "History"
        st.rerun()

    st.divider()

    st.caption("SOURCE FILTERS")

    language = st.selectbox(
        "Language",
        [
            "All Languages",
            "Arabic",
            "Urdu",
            "English",
        ],
    )

    source_type = st.selectbox(
        "Source Type",
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
# MAIN BRAND
# ============================================================

st.markdown(
    '<div class="ilmora-brand">ILMORA</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="ilmora-tagline">'
    'RESEARCH. DISCOVER. VERIFY.'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="ilmora-subtitle">'
    'AI-Assisted Islamic Research'
    '</div>',
    unsafe_allow_html=True,
)

st.divider()


# ============================================================
# RESEARCH PAGE
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
            "Research across your selected scholarly sources."
        )

    with col2:

        if st.button(
            "Research →",
            type="primary",
            use_container_width=True,
        ):

            if not query.strip():

                st.warning(
                    "Enter a research question to begin."
                )

            else:

                st.session_state.query = query
                st.session_state.searched = True

                st.rerun()

    st.write("")

    # --------------------------------------------------------
    # SUGGESTED RESEARCH
    # --------------------------------------------------------

    st.subheader("Suggested Research")

    st.caption(
        "Start with a research direction."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.caption("QUR'AN")

            st.markdown("### Qur'anic Themes")

            st.write(
                "Explore how classical scholars "
                "explain important Qur'anic concepts."
            )

            if st.button(
                "Explore Tafsir →",
                key="tafsir_button",
                use_container_width=True,
            ):

                st.session_state.query = (
                    "What do classical scholars say "
                    "about patience in the Qur'an?"
                )

                st.rerun()

    with col2:

        with st.container(border=True):

            st.caption("HADITH")

            st.markdown("### Hadith Research")

            st.write(
                "Search hadith sources and examine "
                "scholarly explanations."
            )

            if st.button(
                "Explore Hadith →",
                key="hadith_button",
                use_container_width=True,
            ):

                st.session_state.query = (
                    "What are the scholarly explanations "
                    "of the hadith about intentions?"
                )

                st.rerun()

    with col3:

        with st.container(border=True):

            st.caption("SCHOLARS")

            st.markdown("### Compare Views")

            st.write(
                "Compare scholarly positions, "
                "evidence, and differences."
            )

            if st.button(
                "Compare Scholars →",
                key="compare_button",
                use_container_width=True,
            ):

                st.session_state.page = "Compare"
                st.rerun()

    # --------------------------------------------------------
    # RESEARCH RESULT
    # --------------------------------------------------------

    if st.session_state.searched:

        st.divider()

        st.subheader("Research Result")

        st.caption(
            f"Question: {st.session_state.query}"
        )

        if st.session_state.research_result is None:

            with st.spinner("Researching the indexed sources..."):

                try:
                    service = get_research_service()

                    filters = {}

                    if language != "All Languages":
                        filters["language"] = language

                    if source_type != "All Sources":
                        filters["category"] = source_type

                    st.session_state.research_result = service.research(
                        st.session_state.query,
                        **filters,
                    )

                except Exception as error:
                    st.session_state.research_result = {
                        "answer": "",
                        "evidence": [],
                        "scholarly_views": [],
                        "limitations": [
                            f"Research engine error: {error}"
                        ],
                        "evidence_labels_used": [],
                    }

        result = st.session_state.research_result

        if result:
            _display_research_result(result)

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "New Research",
                use_container_width=True,
                key="new_research",
            ):
                st.session_state.query = ""
                st.session_state.searched = False
                st.session_state.research_result = None
                st.rerun()

        with col2:
            if st.button(
                "Save Answer as Note",
                use_container_width=True,
                key="save_answer_note",
            ):
                answer_text = result.get("answer", "") if result else ""

                if answer_text:
                    st.session_state.notes.append(
                        {
                            "title": st.session_state.query,
                            "text": answer_text,
                        }
                    )
                    st.success("Answer saved to Notes.")
                else:
                    st.warning("There is no answer to save yet.")

    # --------------------------------------------------------
    # CONTINUE RESEARCH
    # --------------------------------------------------------

    st.divider()

    st.subheader("Continue Your Research")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("### Research History")

            st.write(
                "Return to previous questions and "
                "continue your research."
            )

            if st.button(
                "Open History →",
                key="open_history",
                use_container_width=True,
            ):

                st.session_state.page = "History"
                st.rerun()

    with col2:

        with st.container(border=True):

            st.markdown("### Scholarly Library")

            st.write(
                "Browse built-in and uploaded "
                "research sources."
            )

            if st.button(
                "Open Library →",
                key="open_library",
                use_container_width=True,
            ):

                st.session_state.page = "Library"
                st.rerun()


# ============================================================
# LIBRARY PAGE
# ============================================================

elif st.session_state.page == "Library":

    st.title("Scholarly Library")

    st.write(
        "Browse books, authors, collections, "
        "and research documents."
    )

    st.write("")

    search = st.text_input(
        "Search library",
        placeholder="Search books, authors, topics...",
    )

    st.write("")

    st.subheader("Collections")

    collections = [
        (
            "TAFSIR",
            "Qur'anic Commentary",
            "Classical and contemporary tafsir sources.",
        ),
        (
            "HADITH",
            "Hadith Sources",
            "Hadith texts and scholarly explanations.",
        ),
        (
            "FIQH",
            "Jurisprudence",
            "Fiqh sources and comparative discussions.",
        ),
        (
            "SEERAH",
            "Prophetic Biography",
            "Seerah and early Islamic history.",
        ),
    ]

    columns = st.columns(4)

    for index, collection in enumerate(collections):

        with columns[index]:

            with st.container(border=True):

                st.caption(collection[0])

                st.markdown(
                    f"### {collection[1]}"
                )

                st.write(
                    collection[2]
                )

                st.button(
                    "Explore →",
                    key=f"collection_{index}",
                    use_container_width=True,
                )

    st.divider()

    st.subheader("Add a Source")

    st.write(
        "Upload a PDF or TXT document "
        "to your research workspace."
    )

    uploaded_file = st.file_uploader(
        "Upload source",
        type=["pdf", "txt"],
    )

    if uploaded_file:

        col1, col2 = st.columns(2)

        with col1:
            author = st.text_input(
                "Author / Scholar",
                placeholder="Example: Ibn Kathir",
            )

            book = st.text_input(
                "Book title",
                value=os.path.splitext(uploaded_file.name)[0],
            )

        with col2:
            volume = st.text_input(
                "Volume",
                placeholder="Example: 2",
            )

            source_language = st.selectbox(
                "Language",
                ["Arabic", "Urdu", "English", "Other"],
            )

        category = st.selectbox(
            "Source type",
            [
                "Tafsir",
                "Hadith",
                "Fiqh",
                "Aqidah",
                "Seerah",
                "History",
                "Other",
            ],
        )

        if st.button(
            "Index Source →",
            type="primary",
            use_container_width=True,
        ):

            try:
                file_path, file_bytes = _save_uploaded_file(
                    uploaded_file
                )

                source_id = _source_id(
                    uploaded_file.name,
                    file_bytes,
                )

                metadata = {
                    "source_id": source_id,
                    "author": author or "Unknown",
                    "book": book or uploaded_file.name,
                    "volume": volume or "",
                    "language": source_language,
                    "category": category,
                }

                with st.spinner(
                    "Extracting, chunking, embedding, and indexing source..."
                ):

                    from backend.ingestion_service import IngestionService

                    ingestion = IngestionService()

                    documents = ingestion.ingest(
                        file_path,
                        metadata=metadata,
                    )

                    rag = get_rag_engine()

                    indexed_count = rag.index_documents(
                        documents
                    )

                st.session_state.indexed_count += indexed_count

                st.success(
                    f"Indexed {indexed_count} chunks from "
                    f"{uploaded_file.name}."
                )

                st.info(
                    "The source is now available to the Research page."
                )

            except Exception as error:

                st.error(
                    f"Could not index the source: {error}"
                )

    try:
        rag = get_rag_engine()
        total_chunks = len(rag.indexed_chunks())

        st.metric(
            "Indexed chunks",
            total_chunks,
        )
    except Exception:
        pass


# ============================================================
# COMPARE SCHOLARS PAGE
# ============================================================

elif st.session_state.page == "Compare":

    st.title("Compare Scholars")

    st.write(
        "Compare scholarly positions while preserving "
        "the differences between sources."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        scholar_1 = st.selectbox(
            "Scholar 1",
            [
                "Ibn Kathir",
                "Al-Tabari",
                "Al-Qurtubi",
            ],
        )

    with col2:

        scholar_2 = st.selectbox(
            "Scholar 2",
            [
                "Al-Tabari",
                "Ibn Kathir",
                "Al-Qurtubi",
            ],
        )

    with col3:

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
        placeholder="Example: Patience in the Qur'an",
    )

    if st.button(
        "Compare Sources →",
        type="primary",
        use_container_width=True,
    ):

        if not topic.strip():

            st.warning(
                "Enter a research topic first."
            )

        else:

            st.divider()

            st.subheader("Scholarly Views")

            selected_scholars = [
                scholar_1,
                scholar_2,
                scholar_3,
            ]

            columns = st.columns(3)

            for index, scholar in enumerate(
                selected_scholars
            ):

                with columns[index]:

                    with st.container(border=True):

                        st.markdown(
                            f"### {scholar}"
                        )

                        st.caption(
                            "SCHOLARLY POSITION"
                        )

                        st.write(
                            "Retrieved scholarly position "
                            "will appear here."
                        )

                        st.caption(
                            "EVIDENCE"
                        )

                        st.write(
                            "Supporting passages will appear here."
                        )

            st.subheader(
                "Agreements & Differences"
            )

            st.info(
                "The comparison engine will identify "
                "agreements, differences, evidence, "
                "and methodological observations."
            )


# ============================================================
# NOTES PAGE
# ============================================================

elif st.session_state.page == "Notes":

    st.title("Research Notes")

    st.write(
        "Save important passages, observations, "
        "and research ideas."
    )

    st.write("")

    note_title = st.text_input(
        "Note title",
        placeholder="Example: Different views on patience",
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
                "Note saved successfully."
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
# HISTORY PAGE
# ============================================================

elif st.session_state.page == "History":

    st.title("Research History")

    st.write(
        "Revisit previous research questions "
        "and continue exploring the evidence."
    )

    st.write("")

    history = [
        "What do classical scholars say about patience?",
        "How do scholars explain sincerity?",
        "Different interpretations of a Qur'anic concept.",
    ]

    for index, question in enumerate(history):

        with st.container(border=True):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    f"### {question}"
                )

                st.caption(
                    "Previous research session"
                )

            with col2:

                if st.button(
                    "Open",
                    key=f"history_{index}",
                    use_container_width=True,
                ):

                    st.session_state.query = question
                    st.session_state.page = "Research"
                    st.session_state.searched = True
                    st.rerun()


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
