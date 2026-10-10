"""Shared visual styling for the EduRoute Streamlit app."""

APP_CSS = """
<style>
    /* Theme tokens */
    :root {
        --page-background: #f5f3ef;
        --page-background-alt: #f1efe9;
        --sidebar-background: #eef1f0;
        --card-background: #ffffff;
        --border: #d9d8d3;
        --primary: #2c423f;
        --primary-strong: #1d312d;
        --primary-soft: #dfeae6;
        --accent: #3f7a6d;
        --text-primary: #1b2629;
        --text-secondary: #46555b;
        --text-muted: #5a686d;
        --warning-bg: #f7efd9;
        --warning-text: #5e4a14;
        --warning-border: #e8d9a8;
        --shadow-soft: 0 8px 18px rgba(27, 38, 41, 0.05);
        --shadow-hover: 0 12px 24px rgba(27, 38, 41, 0.08);
    }

    /* Base app shell */
    html, body {
        font-family: Inter, "Segoe UI", sans-serif;
        background: var(--page-background);
        color: var(--text-primary);
    }

    .stApp {
        color-scheme: light;
        background: var(--page-background) !important;
        color: var(--text-primary) !important;
    }

    .main .block-container {
        max-width: 1280px;
        padding: 2.5rem 1.5rem 3rem;
    }

    [data-testid="stHeader"] {
        background: rgba(245, 243, 239, 0.9);
        border-bottom: 1px solid var(--border);
    }

    [data-testid="stSidebar"] {
        background: var(--sidebar-background);
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.8rem;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] .sidebar-meta,
    [data-testid="stSidebar"] .sidebar-section-label {
        color: var(--text-secondary) !important;
    }

    .stMarkdown,
    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown div,
    .stMarkdown span,
    label,
    p,
    li,
    h1, h2, h3, h4,
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p,
    .stTitle,
    .stSubheader,
    .stTextInput label,
    .stTextArea label,
    textarea,
    .stNumberInput label,
    .stSelectbox label,
    .stRadio label,
    .stCheckbox label {
        color: var(--text-primary) !important;
    }

    .stCaption,
    .stCaptionContainer,
    .stCaptionContainer p,
    .stCaptionContainer div {
        color: var(--text-muted) !important;
    }

    h1, h2, h3, h4 {
        letter-spacing: -0.04em;
        margin-top: 0;
        color: var(--text-primary) !important;
    }

    h1 {
        font-size: 2.6rem;
        line-height: 1.1;
        margin-bottom: 0.6rem;
    }

    h2 {
        font-size: 2rem;
        line-height: 1.2;
    }

    h3 {
        font-size: 1.4rem;
        line-height: 1.35;
    }

    h4 {
        font-size: 1.1rem;
        line-height: 1.4;
    }

    .eyebrow {
        color: var(--text-secondary) !important;
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.65rem;
    }

    .page-intro {
        color: var(--text-secondary) !important;
        font-size: 1.04rem;
        line-height: 1.7;
        max-width: 72ch;
        margin: 0.35rem 0 1.8rem;
    }

    .section-heading {
        margin-top: 2.2rem;
        margin-bottom: 0.4rem;
    }

    .section-heading + p {
        margin-top: 0.2rem;
    }

    .brand-shell {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.2rem 0 0.8rem;
        margin-bottom: 0.8rem;
    }

    .brand-mark {
        display: grid;
        place-items: center;
        width: 2.7rem;
        height: 2.7rem;
        border-radius: 0.8rem;
        background: var(--primary);
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 700;
        box-shadow: var(--shadow-soft);
    }

    .brand-name {
        font-size: 1.55rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        color: var(--text-primary);
    }

    .brand-tagline {
        font-size: 0.78rem;
        color: var(--text-secondary);
        margin-top: 0.14rem;
    }

    .sidebar-section-label,
    .sidebar-meta {
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin: 0.5rem 0 0.7rem;
        color: var(--text-secondary);
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        border-radius: 999px;
        border: 1px solid var(--warning-border);
        background: var(--warning-bg);
        color: var(--warning-text);
        font-size: 0.76rem;
        font-weight: 700;
        padding: 0.45rem 0.7rem;
    }

    .status-dot {
        width: 0.55rem;
        height: 0.55rem;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 4px rgba(63, 122, 109, 0.1);
    }

    .insight-card,
    .status-card,
    .plan-card,
    .result-panel,
    .metric-card,
    .feature-card,
    .about-section,
    .overview-panel,
    .welcome-visual,
    .page-footer,
    .team-placeholder {
        background: var(--card-background);
        border: 1px solid var(--border);
        border-radius: 1rem;
        box-shadow: var(--shadow-soft);
    }

    .insight-card,
    .status-card,
    .plan-card,
    .feature-card,
    .overview-panel,
    .about-section,
    .metric-card,
    .welcome-visual {
        padding: 1.25rem 1.25rem;
    }

    .insight-label,
    .result-label,
    .metric-label,
    .plan-kicker,
    .about-kicker {
        color: var(--text-secondary) !important;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }

    .insight-card p,
    .status-card p,
    .plan-card p,
    .result-placeholder,
    .metric-note,
    .pending-copy,
    .feature-card p,
    .overview-panel p,
    .about-section p,
    .team-copy,
    .step-list,
    .step-list li,
    .page-intro,
    .hero-copy p {
        color: var(--text-muted) !important;
        font-size: 0.96rem;
        line-height: 1.7;
        margin: 0;
    }

    .status-card {
        background: var(--sidebar-background);
    }

    .plan-card {
        padding: 1.2rem 1.3rem;
    }

    .plan-card h4 {
        margin: 0 0 0.7rem;
        font-size: 1.15rem;
        line-height: 1.4;
        color: var(--text-primary) !important;
    }

    .planning-banner {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.9rem 1rem;
        background: var(--warning-bg);
        border: 1px solid var(--warning-border);
        border-radius: 1rem;
        color: var(--warning-text);
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 1rem 0 1.6rem;
    }

    .plan-badge,
    .planning-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.38rem;
        border-radius: 999px;
        background: #edf3ef;
        border: 1px solid #cfe1d8;
        color: var(--primary);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 0.36rem 0.66rem;
        margin-top: 0.9rem;
    }

    .metric-card {
        min-height: 134px;
    }

    .metric-value {
        color: #8a969a !important;
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -0.05em;
    }

    .metric-note {
        margin-top: 0.65rem;
    }

    .result-panel {
        min-height: 154px;
    }

    .route-list {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.55rem;
        margin-top: 0.8rem;
    }

    .route-step {
        background: var(--sidebar-background);
        border: 1px solid var(--border);
        border-radius: 10px;
        color: var(--text-primary);
        font-size: 0.82rem;
        font-weight: 600;
        padding: 0.55rem 0.8rem;
    }

    .route-arrow {
        color: var(--text-muted);
        font-size: 1.1rem;
    }

    .route-note {
        color: var(--text-muted);
        font-size: 0.82rem;
        margin-top: 0.7rem;
    }

    .sample-prompt {
        border-left: 3px solid var(--primary);
        background: var(--primary-soft);
        border-radius: 0 0.7rem 0.7rem 0;
        color: var(--text-primary);
        line-height: 1.6;
        margin: 0.7rem 0;
        padding: 0.8rem 0.9rem;
    }

    .panel-heading {
        color: var(--text-secondary);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.9rem;
    }

    .brand-shell .brand-name,
    .mini-brand .mini-brand-text,
    .feature-title {
        color: var(--text-primary) !important;
    }

    .mini-brand {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 1rem;
    }

    .mini-brand-mark {
        display: grid;
        place-items: center;
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 0.7rem;
        background: var(--primary);
        color: #ffffff;
        font-size: 1rem;
        font-weight: 700;
    }

    .hero-copy {
        padding: 0.4rem 0 0.5rem;
    }

    .hero-text {
        color: var(--text-primary) !important;
        font-size: clamp(2.2rem, 4vw, 3.2rem);
        font-weight: 700;
        line-height: 1.08;
        letter-spacing: -0.06em;
        max-width: 560px;
        margin-bottom: 0.9rem;
    }

    .hero-copy p {
        font-size: 1.03rem;
        max-width: 620px;
    }

    .welcome-visual {
        min-height: 290px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .visual-window {
        width: 100%;
        min-height: 220px;
        padding: 1rem;
        border-radius: 1.2rem;
        background: linear-gradient(180deg, #ffffff 0%, #f2f4f3 100%);
        border: 1px solid var(--border);
        position: relative;
        overflow: hidden;
    }

    .visual-badge {
        display: inline-flex;
        align-items: center;
        border-radius: 999px;
        background: rgba(44, 66, 63, 0.08);
        border: 1px solid var(--border);
        color: var(--text-secondary);
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 0.38rem 0.7rem;
    }

    .visual-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(120px, 1fr));
        gap: 0.85rem;
        margin-top: 1rem;
    }

    .visual-card {
        min-height: 72px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 0.9rem;
        background: #ffffff;
        border: 1px solid var(--border);
        color: var(--text-primary);
        font-weight: 600;
        letter-spacing: -0.02em;
    }

    .visual-card.primary {
        background: var(--primary-soft);
        border-color: rgba(44, 66, 63, 0.2);
        color: var(--primary);
    }

    .visual-card.muted {
        background: var(--sidebar-background);
    }

    .visual-line {
        position: absolute;
        left: 28%;
        right: 28%;
        bottom: 2.2rem;
        height: 2px;
        background: linear-gradient(90deg, var(--border), var(--primary), var(--border));
    }

    .feature-card {
        height: 100%;
        display: flex;
        flex-direction: column;
        transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }

    .feature-card:hover {
        transform: translateY(-2px);
        border-color: var(--primary);
        box-shadow: var(--shadow-hover);
    }

    .feature-icon {
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 0.8rem;
        background: var(--primary-soft);
        color: var(--primary);
        display: grid;
        place-items: center;
        font-weight: 700;
        margin-bottom: 0.9rem;
    }

    .feature-title {
        font-size: 1.2rem;
        font-weight: 700;
        line-height: 1.35;
        letter-spacing: -0.02em;
        margin-bottom: 0.6rem;
    }

    .feature-card p {
        margin-bottom: 0.85rem;
    }

    .feature-actions {
        margin-top: auto;
    }

    .overview-panel {
        margin-top: 0.8rem;
    }

    .step-list {
        padding-left: 1.2rem;
        margin-top: 0.85rem;
    }

    .step-list li {
        margin-bottom: 0.7rem;
        padding-left: 0.2rem;
    }

    .about-section {
        margin-top: 1.3rem;
    }

    .team-placeholder {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        background: var(--sidebar-background);
        border: 1px solid var(--border);
        border-radius: 0.9rem;
        padding: 1rem 1.1rem;
    }

    .team-mark {
        display: grid;
        place-items: center;
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 0.8rem;
        background: var(--primary);
        color: #ffffff;
        font-size: 1rem;
        font-weight: 700;
        box-shadow: var(--shadow-soft);
    }

    .team-copy {
        color: var(--text-secondary) !important;
        font-weight: 500;
    }

    .page-footer {
        margin-top: 2rem;
        padding: 1rem 1.1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }

    .footer-brand {
        display: flex;
        align-items: center;
        gap: 0.7rem;
    }

    .footer-brand .mini-brand-mark {
        width: 2rem;
        height: 2rem;
        border-radius: 0.7rem;
    }

    .footer-tagline {
        font-size: 0.78rem;
        color: var(--text-secondary);
        margin-top: 0.14rem;
    }

    .footer-links {
        display: flex;
        flex-wrap: wrap;
        gap: 0.85rem;
        color: var(--text-secondary);
        font-size: 0.82rem;
        font-weight: 600;
    }

    /* Buttons and form controls */
    .stButton > button,
    button[kind="secondary"],
    .stDownloadButton > button,
    .stForm button {
        border: 1px solid var(--border);
        border-radius: 999px;
        background: #ffffff;
        color: var(--text-primary) !important;
        font-weight: 600;
        padding: 0.72rem 1.05rem;
        min-height: 2.9rem;
        box-shadow: none;
        transition: border-color 0.18s ease, transform 0.18s ease, background 0.18s ease, box-shadow 0.18s ease;
    }

    .stButton > button:hover,
    button[kind="secondary"]:hover {
        border-color: var(--primary);
        background: #ffffff;
        transform: translateY(-1px);
        box-shadow: var(--shadow-soft);
    }

    .stButton > button[kind="primary"],
    .stDownloadButton > button[kind="primary"] {
        border-color: var(--primary);
        background: var(--primary);
        color: #ffffff !important;
        box-shadow: var(--shadow-soft);
    }

    .stButton > button[kind="primary"]:hover,
    .stDownloadButton > button[kind="primary"]:hover {
        background: var(--primary-strong);
        border-color: var(--primary-strong);
        box-shadow: var(--shadow-hover);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none;
    }

    [data-testid="stSidebar"] [role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    [data-testid="stSidebar"] [role="radio"] {
        border: 1px solid var(--border);
        border-radius: 0.9rem;
        background: rgba(255, 255, 255, 0.5);
        padding: 0.8rem 0.9rem;
        color: var(--text-primary);
        font-weight: 600;
        min-height: 2.75rem;
        transition: border-color 0.18s ease, background 0.18s ease, transform 0.18s ease;
    }

    [data-testid="stSidebar"] [role="radio"]:hover {
        border-color: var(--primary);
        background: rgba(255, 255, 255, 0.8);
    }

    [data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
        background: var(--primary);
        border-color: var(--primary);
        color: #ffffff !important;
    }

    .stTextInput > div > div,
    .stTextArea > div > div,
    .stSelectbox > div > div,
    .stNumberInput > div > div {
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 0.9rem;
    }

    [data-testid="stTextArea"] textarea,
    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] input,
    [data-testid="stNumberInput"] input {
        background: #ffffff !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border);
        border-radius: 0.9rem;
        line-height: 1.6;
        min-height: 2.8rem;
    }

    [data-testid="stTextArea"] textarea {
        min-height: 140px;
        border-radius: 0.95rem;
    }

    [data-testid="stTextArea"] textarea::placeholder,
    [data-testid="stTextInput"] input::placeholder {
        color: var(--text-muted) !important;
    }

    textarea:focus,
    input:focus,
    button:focus-visible,
    [role="radio"]:focus-visible,
    [data-testid="stSidebar"] [role="radio"]:focus-visible,
    .stButton > button:focus-visible {
        outline: 2px solid var(--accent) !important;
        outline-offset: 2px !important;
    }

    .composer-meta {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        min-height: 2.9rem;
        color: var(--text-secondary);
        font-size: 0.76rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .empty-state {
        display: grid;
        justify-items: center;
        align-content: center;
        gap: 0.5rem;
        min-height: 160px;
        text-align: center;
        padding: 1.1rem 0.8rem;
    }

    .empty-icon {
        display: grid;
        place-items: center;
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        background: var(--sidebar-background);
        border: 1px solid var(--border);
        color: var(--text-primary);
        font-size: 1.3rem;
        font-weight: 600;
    }

    .empty-title {
        color: var(--text-primary) !important;
        font-size: 1rem;
        font-weight: 700;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--border);
        border-radius: 1rem;
        background: rgba(255, 255, 255, 0.5);
        padding: 0.2rem;
    }

    [data-testid="stAlert"],
    .stAlert {
        border-radius: 0.9rem;
        border: 1px solid var(--warning-border);
        background: var(--warning-bg) !important;
        color: var(--warning-text) !important;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div,
    [data-testid="stAlert"] strong {
        color: var(--warning-text) !important;
    }

    [data-testid="stHorizontalRule"] {
        border-color: var(--border) !important;
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 1.5rem;
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }

        h1 {
            font-size: 2.15rem;
        }

        .planning-banner,
        .page-footer {
            flex-direction: column;
            align-items: flex-start;
        }

        .hero-copy,
        .feature-card,
        .about-section,
        .overview-panel,
        .plan-card,
        .insight-card,
        .status-card,
        .page-footer {
            width: 100%;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
            scroll-behavior: auto !important;
        }
    }
</style>
"""
