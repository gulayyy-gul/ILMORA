import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ILMORA — Islamic Research",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background: #F7F5EF;
    }

    [data-testid="stHeader"] {
        background: #F7F5EF;
    }

    [data-testid="stSidebar"] {
        background: #F0EFE8;
        border-right: 1px solid #E2DED4;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    /* ========================================================
       TYPOGRAPHY
       ======================================================== */

    h1, h2, h3 {
        color: #30332F !important;
    }

    p {
        color: #666B63;
    }

    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #D8D8CF;
        min-height: 42px;
        font-weight: 600;
        background: #FFFDF8;
        color: #454942;
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
        background: #435742;
        color: white;
    }

    /* ========================================================
       BRAND
       ======================================================== */

    .brand-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        letter-spacing: 5px;
        color: #536A52;
        line-height: 1.1;
        margin-top: 10px;
        margin-bottom: 8px;
    }

    .brand-tagline {
        text-align: center;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 4px;
        color: #7A9278;
        margin-bottom: 8px;
    }

    .brand-subtitle {
        text-align: center;
        font-size: 14px;
        color: #777A72;
        margin-bottom: 25px;
    }

    /* ========================================================
       HERO
       ======================================================== */

    .hero-title {
        text-align: center;
        font-size: 38px;
        font-weight: 750;
        color: #30332F;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .hero-text {
        text-align: center;
        max-width: 680px;
        margin: 0 auto 25px auto;
        font-size: 16px;
        line-height: 1.7;
        color: #777A72;
    }

    /* ========================================================
       CARDS
       ======================================================== */

    .card {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .card-title {
        color: #536A52;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .card-text {
        color: #777A72;
        font-size: 13px;
        line-height: 1.65;
    }

    /* ========================================================
       RESEARCH AREA
       ======================================================== */

    .research-box {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 22px;
        padding: 24px;
        margin-top: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 28px rgba(70, 75, 65, 0.04);
    }

    .research-label {
        color: #536A52;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    /* ========================================================
       SECTION HEADINGS
       ======================================================== */

    .section-title {
        color: #30332F;
        font-size: 20px;
        font-weight: 750;
        margin-top: 35px;
        margin-bottom: 5px;
    }

    .section-text {
        color: #85877F;
        font-size: 13px;
        margin-bottom: 15px;
    }

    /* ========================================================
       RESULT
       ======================================================== */

    .result-box {
        background: #FFFDF8;
        border: 1px solid #E1DED5;
        border-radius: 20px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 8px 25px rgba(70, 75, 65, 0.04);
    }

    .result-badge {
        display: inline-block;
        background: #E4ECDD;
        color: #536A52;
        border-radius: 20px;
        padding: 6px 12px;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    .answer {
        color: #4A4D47;
        font-size: 15px;
        line-height: 1.8;
    }

    /* ========================================================
       EVIDENCE
       ======================================================== */

    .evidence {
        background: #F2F4ED;
        border-left: 4px solid #7A9278;
        border-radius: 12px;
        padding: 18px;
        margin: 12px 0;
    }

    .evidence-id {
        color: #536A52;
        font-size: 12px;
        font-weight: 800;
    }

    .evidence-source {
        color: #454942;
        font-size: 13px;
        font-weight: 700;
        margin-top: 5px;
    }

    .evidence-text {
        color: #62665E;
        font-size: 14px;
        line-height: 1.8;
        margin-top: 9px;
    }

    /* ========================================================
       SCHOLAR CARDS
       ======================================================== */

    .scholar {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 18px;
        padding: 20px;
        min-height: 190px;
    }

    .scholar-name {
        color: #536A52;
        font-size: 17px;
        font-weight: 750;
    }

    .scholar-role {
        color: #8A8C84;
        font-size: 12px;
        margin-top: 3px;
        margin-bottom: 12px;
    }

    .scholar-text {
        color: #62665E;
        font-size: 14px;
        line-height: 1.7;
    }

    /* ========================================================
       BOOK CARDS
       ======================================================== */

    .book {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 17px;
        padding: 20px;
        min-height: 150px;
    }

    .book-category {
        color: #9A856C;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .book-title {
        color: #3C403A;
        font-size: 16px;
        font-weight: 750;
        margin-top: 7px;
        margin-bottom: 6px;
    }

    .book-description {
        color: #777A72;
        font-size: 13px;
        line-height: 1.5;
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */

    .sidebar-logo {
        text-align: center;
        color: #536A52;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: 3px;
        margin-top: 8px;
    }

    .sidebar-tagline {
        text-align: center;
        color: #7A9278;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    .sidebar-heading {
        color: #85877F;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin: 20px 0 8px 4px;
        text-transform: uppercase;
    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 25px;
        border-top: 1px solid #E3E0D7;
        color: #888A83;
        font-size: 12px;
        line-height: 1.7;
    }

    .footer-main {
        color: #536A52;
        font-weight: 700;
        margin-bottom: 4px;
    }

    /* ========================================================
       TEXT INPUT
       ======================================================== */

    textarea,
    input {
        border-radius: 12px !important;
    }

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .brand-title {
            font-size: 40px;
        }

        .hero-title {
            font-size: 29px;
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


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">ILMORA</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-tagline">'
        'RESEARCH · DISCOVER · VERIFY'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-heading">Workspace</div>',
        unsafe_allow_html=True,
    )

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

    st.markdown(
        '<div class="sidebar-heading">Language</div>',
        unsafe_allow_html=True,
    )

    st.checkbox("Arabic", value=True)
    st.checkbox("Urdu", value=True)
    st.checkbox("English", value=True)

    st.markdown("---")

    st.caption(
        "The sources are the authority.\n"
        "AI is the research assistant."
    )


# ============================================================
# MAIN BRAND
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


# ============================================================
# RESEARCH PAGE
# ============================================================

if st.session_state.page == "Research":

    st.markdown(
        '<div class="hero-title">'
        'What would you like to research?'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-text">'
        'Explore scholarly sources, compare viewpoints, '
        'and trace ideas back to their original passages.'
        '</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # RESEARCH BOX
    # --------------------------------------------------------

    st.markdown(
        '<div class="research-box">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="research-label">'
        'Research question'
        '</div>',
        unsafe_allow_html=True,
    )

    query = st.text_area(
        "Research question",
        value=st.session_state.query,
        placeholder=(
            "e.g. What do classical scholars say about "
            "patience in the Qur'an?"
        ),
        height=120,
        label_visibility="collapsed",
    )

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        research_clicked = st.button(
            "Research  →",
            type="primary",
            use_container_width=True,
        )

    with col2:

        source_type = st.selectbox(
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
            label_visibility="collapsed",
        )

    with col3:

        language = st.selectbox(
            "Language",
            [
                "All Languages",
                "Arabic",
                "Urdu",
                "English",
            ],
            label_visibility="collapsed",
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # SUGGESTED RESEARCH
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        'Suggested Research'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-text">'
        'Explore a focused research direction.'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Qur'anic Themes
                </div>
                <div class="card-text">
                    Explore how classical tafsir explains
                    important Qur'anic concepts.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Explore Tafsir →",
            key="tafsir",
            use_container_width=True,
        ):

            st.session_state.query = (
                "What do classical scholars say about patience "
                "in the Qur'an?"
            )

            st.rerun()

    with col2:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Hadith Research
                </div>
                <div class="card-text">
                    Search hadith-related sources and examine
                    scholarly explanations.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Explore Hadith →",
            key="hadith",
            use_container_width=True,
        ):

            st.session_state.query = (
                "What are the scholarly explanations "
                "of the hadith about intentions?"
            )

            st.rerun()

    with col3:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Compare Scholars
                </div>
                <div class="card-text">
                    Examine where major scholars agree,
                    differ, and use different evidence.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Compare Views →",
            key="compare",
            use_container_width=True,
        ):

            st.session_state.page = "Compare"
            st.rerun()

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    if research_clicked:

        if not query.strip():

            st.warning(
                "Please enter a research question first."
            )

        else:

            st.session_state.query = query
            st.session_state.searched = True

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if st.session_state.searched:

        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="result-badge">'
            'RESEARCH RESULT'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "### Research synthesis"
        )

        st.markdown(
            f"""
            <div class="answer">

            <b>Research question:</b><br>
            {st.session_state.query}

            <br><br>

            ILMORA will analyze the selected scholarly sources,
            retrieve relevant passages, and construct a grounded
            synthesis from the available evidence.

            <br><br>

            The final research answer will distinguish between
            the original statements of scholars and AI-generated
            synthesis.

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            'Evidence'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-text">'
            'Important claims should be traceable to source passages.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="evidence">

                <div class="evidence-id">
                    E1
                </div>

                <div class="evidence-source">
                    Source title · Author · Volume · Page
                </div>

                <div class="evidence-text">
                    The original Arabic, Urdu, or English passage
                    retrieved from the selected source will appear
                    here.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="evidence">

                <div class="evidence-id">
                    E2
                </div>

                <div class="evidence-source">
                    Supporting scholarly source
                </div>

                <div class="evidence-text">
                    Supporting evidence and complete source metadata
                    will appear here.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        e1, e2, e3 = st.columns(3)

        with e1:
            st.button(
                "View Evidence",
                use_container_width=True,
            )

        with e2:
            st.button(
                "Save Passage",
                use_container_width=True,
            )

        with e3:
            st.button(
                "Add Note",
                use_container_width=True,
            )

    # --------------------------------------------------------
    # CONTINUE RESEARCH
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        'Continue Your Research'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-text">'
        'Pick up where you left off.'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Recent Research
                </div>
                <div class="card-text">
                    Your recent research sessions will appear here.
                    Reopen a question and continue exploring.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Your Library
                </div>
                <div class="card-text">
                    Browse built-in and uploaded scholarly sources
                    organized by author, subject, language, and type.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# LIBRARY PAGE
# ============================================================

elif st.session_state.page == "Library":

    st.markdown(
        '<div class="hero-title">'
        'Scholarly Library'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-text">'
        'Explore Islamic sources and research directly across '
        'your selected collection.'
        '</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search library",
        placeholder="Search books, authors, topics..."
    )

    st.markdown(
        '<div class="section-title">'
        'Collections'
        '</div>',
        unsafe_allow_html=True,
    )

    books = [
        (
            "TAFSIR",
            "Tafsir Collection",
            "Classical Qur'anic commentary and interpretation."
        ),
        (
            "HADITH",
            "Hadith Collection",
            "Hadith texts and scholarly explanations."
        ),
        (
            "FIQH",
            "Fiqh Collection",
            "Jurisprudential sources and discussions."
        ),
        (
            "SEERAH",
            "Seerah Collection",
            "Prophetic biography and Islamic history."
        ),
    ]

    columns = st.columns(4)

    for column, book in zip(columns, books):

        with column:

            st.markdown(
                f"""
                <div class="book">

                    <div class="book-category">
                        {book[0]}
                    </div>

                    <div class="book-title">
                        {book[1]}
                    </div>

                    <div class="book-description">
                        {book[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Explore →",
                key=f"library_{book[0]}",
                use_container_width=True,
            )

    st.markdown(
        '<div class="section-title">'
        'Upload a Source'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-text">'
        'Add a PDF or TXT source to your research workspace.'
        '</div>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Upload source",
        type=["pdf", "txt"],
        label_visibility="collapsed",
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
# COMPARE PAGE
# ============================================================

elif st.session_state.page == "Compare":

    st.markdown(
        '<div class="hero-title">'
        'Compare Scholars'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-text">'
        'Compare scholarly positions while preserving '
        'differences between sources.'
        '</div>',
        unsafe_allow_html=True,
    )

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
        placeholder="e.g. Patience in the Qur'an",
    )

    if st.button(
        "Compare Sources →",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            '<div class="section-title">'
            'Scholarly Views'
            '</div>',
            unsafe_allow_html=True,
        )

        scholars = [
            (
                scholar_1,
                "Classical tafsir perspective",
            ),
            (
                scholar_2,
                "Classical tafsir perspective",
            ),
            (
                scholar_3,
                "Classical tafsir perspective",
            ),
        ]

        columns = st.columns(3)

        for column, scholar in zip(columns, scholars):

            with column:

                st.markdown(
                    f"""
                    <div class="scholar">

                        <div class="scholar-name">
                            {scholar[0]}
                        </div>

                        <div class="scholar-role">
                            {scholar[1]}
                        </div>

                        <div class="scholar-text">
                            The retrieved scholarly position,
                            supporting evidence, and source references
                            will appear here.
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown(
            '<div class="section-title">'
            'Agreements & Differences'
            '</div>',
            unsafe_allow_html=True,
        )

        st.info(
            "The comparison engine will identify agreements, "
            "differences, evidence, and methodological observations "
            "from retrieved sources."
        )


# ============================================================
# NOTES PAGE
# ============================================================

elif st.session_state.page == "Notes":

    st.markdown(
        '<div class="hero-title">'
        'Research Notes'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-text">'
        'Save important passages, observations, and ideas '
        'from your research.'
        '</div>',
        unsafe_allow_html=True,
    )

    note_title = st.text_input(
        "Note title",
        placeholder="e.g. Different scholarly views on patience",
    )

    note = st.text_area(
        "Your note",
        placeholder="Write your research observation here...",
        height=220,
    )

    if st.button(
        "Save Note",
        type="primary",
        use_container_width=True,
    ):

        if note.strip():

            st.success(
                "Note saved successfully."
            )

        else:

            st.warning(
                "Write something before saving."
            )


# ============================================================
# HISTORY PAGE
# ============================================================

elif st.session_state.page == "History":

    st.markdown(
        '<div class="hero-title">'
        'Research History'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-text">'
        'Revisit previous research questions and continue '
        'exploring the evidence.'
        '</div>',
        unsafe_allow_html=True,
    )

    history = [
        "What do classical scholars say about patience?",
        "How do scholars explain sincerity?",
        "Different interpretations of a Qur'anic concept.",
    ]

    for index, question in enumerate(history):

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(
                f"""
                <div class="card">

                    <div class="card-title">
                        {question}
                    </div>

                    <div class="card-text">
                        Previous research session
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
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

st.markdown(
    """
    <div class="footer">

        <div class="footer-main">
            The sources are the authority.
            AI is the research assistant.
        </div>

        ILMORA · AI-Assisted Islamic Research

    </div>
    """,
    unsafe_allow_html=True,
)
