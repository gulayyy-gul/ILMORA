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

    /* ---------------- GLOBAL ---------------- */

    .stApp {
        background: #F7F5EF;
    }

    [data-testid="stHeader"] {
        background: rgba(247, 245, 239, 0.95);
    }

    [data-testid="stSidebar"] {
        background: #F0EFE8;
        border-right: 1px solid #E2DED4;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------------- TYPOGRAPHY ---------------- */

    h1, h2, h3 {
        color: #30332F !important;
    }

    p {
        color: #666B63;
    }

    /* ---------------- BRAND ---------------- */

    .brand {
        text-align: center;
        padding: 8px 0 18px 0;
    }

    .brand-title {
        font-size: 52px;
        font-weight: 800;
        letter-spacing: 5px;
        color: #536A52;
        line-height: 1;
        margin-bottom: 10px;
    }

    .brand-tagline {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 4px;
        color: #7A9278;
    }

    .brand-subtitle {
        margin-top: 7px;
        font-size: 14px;
        color: #777A72;
    }

    /* ---------------- SIDEBAR ---------------- */

    .sidebar-brand {
        text-align: center;
        padding: 15px 5px 25px 5px;
    }

    .sidebar-logo {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: 3px;
        color: #536A52;
    }

    .sidebar-caption {
        font-size: 10px;
        letter-spacing: 2px;
        color: #7A9278;
        font-weight: 700;
    }

    .sidebar-section {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        color: #85877F;
        margin: 18px 0 8px 5px;
        text-transform: uppercase;
    }

    /* ---------------- HERO ---------------- */

    .hero {
        text-align: center;
        padding: 30px 0 20px 0;
    }

    .hero h1 {
        font-size: 38px;
        font-weight: 750;
        margin-bottom: 10px;
    }

    .hero p {
        max-width: 680px;
        margin: auto;
        font-size: 16px;
        line-height: 1.7;
        color: #777A72;
    }

    /* ---------------- RESEARCH CARD ---------------- */

    .research-card {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 22px;
        padding: 26px;
        margin-top: 20px;
        box-shadow: 0 8px 30px rgba(70, 75, 65, 0.04);
    }

    .research-label {
        font-size: 13px;
        font-weight: 700;
        color: #536A52;
        margin-bottom: 8px;
    }

    /* ---------------- BUTTONS ---------------- */

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #D8D8CF;
        min-height: 42px;
        font-weight: 600;
    }

    .stButton > button:hover {
        border-color: #7A9278;
        color: #536A52;
    }

    /* ---------------- PRIMARY BUTTON ---------------- */

    div.stButton > button[kind="primary"] {
        background: #536A52;
        color: white;
        border: none;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #435742;
        color: white;
    }

    /* ---------------- SECTION TITLE ---------------- */

    .section-title {
        font-size: 19px;
        font-weight: 750;
        color: #30332F;
        margin-top: 34px;
        margin-bottom: 14px;
    }

    .section-description {
        font-size: 13px;
        color: #85877F;
        margin-top: -8px;
        margin-bottom: 16px;
    }

    /* ---------------- SMALL CARDS ---------------- */

    .soft-card {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 17px;
        padding: 20px;
        height: 100%;
    }

    .soft-card-title {
        color: #536A52;
        font-weight: 700;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .soft-card-text {
        color: #777A72;
        font-size: 13px;
        line-height: 1.6;
    }

    /* ---------------- RESEARCH RESULT ---------------- */

    .result-card {
        background: #FFFDF8;
        border: 1px solid #E1DED5;
        border-radius: 20px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 8px 25px rgba(70, 75, 65, 0.04);
    }

    .result-label {
        display: inline-block;
        background: #E4ECDD;
        color: #536A52;
        border-radius: 20px;
        padding: 5px 11px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
    }

    .answer-text {
        color: #41443F;
        font-size: 15px;
        line-height: 1.8;
    }

    /* ---------------- EVIDENCE ---------------- */

    .evidence-card {
        background: #F4F5EE;
        border-left: 4px solid #7A9278;
        border-radius: 12px;
        padding: 18px;
        margin: 12px 0;
    }

    .evidence-id {
        font-weight: 800;
        color: #536A52;
        font-size: 12px;
    }

    .evidence-source {
        font-size: 13px;
        font-weight: 700;
        color: #454942;
        margin-top: 4px;
    }

    .evidence-text {
        margin-top: 10px;
        color: #5F635C;
        font-size: 14px;
        line-height: 1.8;
    }

    /* ---------------- SCHOLAR ---------------- */

    .scholar-card {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 18px;
        padding: 20px;
        height: 100%;
    }

    .scholar-name {
        font-size: 17px;
        font-weight: 750;
        color: #536A52;
    }

    .scholar-role {
        color: #8A8C84;
        font-size: 12px;
        margin-bottom: 12px;
    }

    .scholar-text {
        color: #60645D;
        font-size: 14px;
        line-height: 1.7;
    }

    /* ---------------- LIBRARY ---------------- */

    .book-card {
        background: #FFFDF8;
        border: 1px solid #E3E0D7;
        border-radius: 17px;
        padding: 19px;
        height: 100%;
    }

    .book-category {
        color: #9A856C;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .book-title {
        color: #3C403A;
        font-size: 16px;
        font-weight: 750;
        margin: 7px 0;
    }

    .book-author {
        color: #777A72;
        font-size: 13px;
    }

    /* ---------------- STATUS ---------------- */

    .status {
        background: #E6ECDD;
        color: #536A52;
        padding: 7px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
    }

    /* ---------------- FOOTER ---------------- */

    .footer {
        text-align: center;
        padding: 45px 0 10px 0;
        color: #888A83;
        font-size: 12px;
    }

    .footer-main {
        color: #536A52;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* ---------------- TEXT AREA ---------------- */

    textarea {
        border-radius: 14px !important;
    }

    /* ---------------- MOBILE ---------------- */

    @media (max-width: 768px) {

        .brand-title {
            font-size: 40px;
        }

        .hero h1 {
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
        """
        <div class="sidebar-brand">
            <div class="sidebar-logo">ILMORA</div>
            <div class="sidebar-caption">
                RESEARCH · DISCOVER · VERIFY
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-section">Workspace</div>',
        unsafe_allow_html=True,
    )

    if st.button("⌕  Research", use_container_width=True):
        st.session_state.page = "Research"

    if st.button("▣  Library", use_container_width=True):
        st.session_state.page = "Library"

    if st.button("⇄  Compare Scholars", use_container_width=True):
        st.session_state.page = "Compare"

    if st.button("✎  Notes", use_container_width=True):
        st.session_state.page = "Notes"

    if st.button("◷  History", use_container_width=True):
        st.session_state.page = "History"

    st.markdown(
        '<div class="sidebar-section">Sources</div>',
        unsafe_allow_html=True,
    )

    st.checkbox("Arabic", value=True)
    st.checkbox("Urdu", value=True)
    st.checkbox("English", value=True)

    st.markdown("---")

    st.markdown(
        """
        <div style="padding:5px;color:#777A72;font-size:12px;line-height:1.6;">
        <b style="color:#536A52;">Research responsibly.</b><br>
        ILMORA helps you discover and trace scholarly evidence.
        The sources remain the authority.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# TOP BRAND
# ============================================================

st.markdown(
    """
    <div class="brand">
        <div class="brand-title">ILMORA</div>

        <div class="brand-tagline">
            RESEARCH. DISCOVER. VERIFY.
        </div>

        <div class="brand-subtitle">
            AI-Assisted Islamic Research
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESEARCH PAGE
# ============================================================

if st.session_state.page == "Research":

    st.markdown(
        """
        <div class="hero">

            <h1>What would you like to research?</h1>

            <p>
                Explore scholarly sources, compare viewpoints,
                and trace ideas back to their original passages.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- RESEARCH INPUT ----------------

    st.markdown(
        '<div class="research-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="research-label">Research question</div>',
        unsafe_allow_html=True,
    )

    query = st.text_area(
        "Research question",
        value=st.session_state.query,
        placeholder=(
            "e.g. What do classical scholars say about patience "
            "in the Qur'an?"
        ),
        height=125,
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

        source_filter = st.selectbox(
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

        language_filter = st.selectbox(
            "Language",
            [
                "All Languages",
                "Arabic",
                "Urdu",
                "English",
            ],
            label_visibility="collapsed",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SUGGESTED RESEARCH ----------------

    st.markdown(
        '<div class="section-title">Suggested Research</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'Start with a focused research direction.'
        '</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    suggestions = [
        (
            c1,
            "Qur'anic Themes",
            "Explore how classical tafsir explains a Qur'anic concept.",
            "What do classical scholars say about patience in the Qur'an?"
        ),
        (
            c2,
            "Hadith Research",
            "Find evidence and scholarly discussion around a hadith topic.",
            "What are the scholarly explanations of the hadith about intentions?"
        ),
        (
            c3,
            "Compare Scholars",
            "Examine where major scholars agree and differ.",
            "How do Ibn Kathir and al-Tabari explain this concept?"
        ),
    ]

    for column, title, description, example in suggestions:

        with column:

            st.markdown(
                f"""
                <div class="soft-card">
                    <div class="soft-card-title">
                        {title}
                    </div>

                    <div class="soft-card-text">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "Try this →",
                key=f"suggestion_{title}",
                use_container_width=True,
            ):
                st.session_state.query = example
                st.rerun()

    # ---------------- RESEARCH ACTION ----------------

    if research_clicked:

        if not query.strip():

            st.warning(
                "Please enter a research question first."
            )

        else:

            st.session_state.query = query
            st.session_state.searched = True

    # ---------------- DEMO RESULT ----------------

    if st.session_state.searched:

        st.markdown(
            """
            <div class="result-card">

                <div class="result-label">
                    RESEARCH RESULT
                </div>

                <h3>Research synthesis</h3>

                <div class="answer-text">

                    The retrieved scholarly sources should be used
                    to construct a grounded answer to your question.
                    ILMORA is designed to distinguish between the
                    scholars' original statements and AI-generated
                    synthesis.

                    <br><br>

                    The final answer will be supported by evidence
                    from the selected sources rather than relying
                    only on the language model.

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # Evidence

        st.markdown(
            '<div class="section-title">Evidence</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="evidence-card">

                <div class="evidence-id">
                    E1
                </div>

                <div class="evidence-source">
                    Source information will appear here
                </div>

                <div class="evidence-text">
                    Original Arabic, Urdu, or English passage
                    retrieved from the indexed source will appear
                    here.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="evidence-card">

                <div class="evidence-id">
                    E2
                </div>

                <div class="evidence-source">
                    Another scholarly source
                </div>

                <div class="evidence-text">
                    Supporting evidence and source metadata
                    will appear here.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # Source actions

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

    # ---------------- CONTINUE RESEARCH ----------------

    st.markdown(
        '<div class="section-title">Continue Your Research</div>',
        unsafe_allow_html=True,
    )

    r1, r2 = st.columns(2)

    with r1:

        st.markdown(
            """
            <div class="soft-card">

                <div class="soft-card-title">
                    Recent Research
                </div>

                <div class="soft-card-text">
                    Your recent research sessions will appear here.
                    Reopen a question and continue where you left off.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with r2:

        st.markdown(
            """
            <div class="soft-card">

                <div class="soft-card-title">
                    Your Library
                </div>

                <div class="soft-card-text">
                    Browse built-in and uploaded scholarly sources,
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
        """
        <div class="hero">

            <h1>Scholarly Library</h1>

            <p>
                Explore indexed Islamic sources and conduct research
                directly across your selected collection.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search library",
        placeholder="Search books, authors, topics..."
    )

    st.markdown(
        '<div class="section-title">Your Sources</div>',
        unsafe_allow_html=True,
    )

    books = [
        (
            "TAFSIR",
            "Tafsir Collection",
            "Classical Qur'anic commentary"
        ),
        (
            "HADITH",
            "Hadith Collection",
            "Hadith texts and scholarly discussions"
        ),
        (
            "FIQH",
            "Fiqh Collection",
            "Jurisprudential sources"
        ),
        (
            "SEERAH",
            "Seerah Collection",
            "Prophetic biography and history"
        ),
    ]

    cols = st.columns(4)

    for column, book in zip(cols, books):

        with column:

            st.markdown(
                f"""
                <div class="book-card">

                    <div class="book-category">
                        {book[0]}
                    </div>

                    <div class="book-title">
                        {book[1]}
                    </div>

                    <div class="book-author">
                        {book[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                "Explore →",
                key=f"book_{book[0]}",
                use_container_width=True,
            )

    st.markdown(
        '<div class="section-title">Upload a Source</div>',
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Upload PDF or TXT",
        type=["pdf", "txt"],
        help="Upload a scholarly source to add it to your research workspace.",
    )

    if uploaded:

        st.success(
            f"{uploaded.name} uploaded successfully. "
            "Indexing will be connected in the next phase."
        )


# ============================================================
# COMPARE PAGE
# ============================================================

elif st.session_state.page == "Compare":

    st.markdown(
        """
        <div class="hero">

            <h1>Compare Scholars</h1>

            <p>
                Compare scholarly positions without hiding
                differences between sources.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.selectbox(
            "Scholar 1",
            [
                "Ibn Kathir",
                "Al-Tabari",
                "Al-Qurtubi",
            ]
        )

    with col2:
        st.selectbox(
            "Scholar 2",
            [
                "Al-Tabari",
                "Ibn Kathir",
                "Al-Qurtubi",
            ]
        )

    with col3:
        st.selectbox(
            "Scholar 3",
            [
                "Al-Qurtubi",
                "Ibn Kathir",
                "Al-Tabari",
            ]
        )

    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Patience in the Qur'an"
    )

    if st.button(
        "Compare Sources →",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            '<div class="section-title">Scholarly Views</div>',
            unsafe_allow_html=True,
        )

        scholars = [
            (
                "Ibn Kathir",
                "Tafsir perspective",
                "The retrieved position and supporting evidence will appear here."
            ),
            (
                "Al-Tabari",
                "Tafsir perspective",
                "The retrieved position and supporting evidence will appear here."
            ),
            (
                "Al-Qurtubi",
                "Tafsir perspective",
                "The retrieved position and supporting evidence will appear here."
            ),
        ]

        cols = st.columns(3)

        for column, scholar in zip(cols, scholars):

            with column:

                st.markdown(
                    f"""
                    <div class="scholar-card">

                        <div class="scholar-name">
                            {scholar[0]}
                        </div>

                        <div class="scholar-role">
                            {scholar[1]}
                        </div>

                        <div class="scholar-text">
                            {scholar[2]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown(
            '<div class="section-title">Agreements & Differences</div>',
            unsafe_allow_html=True,
        )

        st.info(
            "The comparison engine will identify agreements, "
            "differences, evidence, and methodological observations "
            "from the retrieved sources."
        )


# ============================================================
# NOTES PAGE
# ============================================================

elif st.session_state.page == "Notes":

    st.markdown(
        """
        <div class="hero">

            <h1>Your Research Notes</h1>

            <p>
                Save important passages, observations, and ideas
                while conducting your research.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    note_title = st.text_input(
        "Note title",
        placeholder="e.g. Different views on patience"
    )

    note = st.text_area(
        "Write your note",
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
                "Note saved. Persistent note storage will be "
                "connected in the next backend phase."
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
        """
        <div class="hero">

            <h1>Research History</h1>

            <p>
                Revisit previous research questions and continue
                exploring the evidence.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    history_items = [
        "What do classical scholars say about patience?",
        "How do scholars explain sincerity?",
        "Different interpretations of a Qur'anic concept.",
    ]

    for index, item in enumerate(history_items):

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(
                f"""
                <div class="soft-card">
                    <div class="soft-card-title">
                        {item}
                    </div>

                    <div class="soft-card-text">
                        Previous research session
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:

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
