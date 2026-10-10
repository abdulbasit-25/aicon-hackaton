"""Shared visual styling for the EduRoute Streamlit app."""

APP_CSS = """
<style>
    :root {
        color-scheme: light;
        --canvas: #f4f2ef;
        --canvas-alt: #ece8e3;
        --panel: rgba(255, 255, 255, 0.82);
        --panel-strong: #ffffff;
        --surface-soft: #edf1f1;
        --sidebar: #edf0f0;
        --line: #c5c5c5;
        --line-strong: #a9b2b0;
        --text-primary: #1f2a2d;
        --text-secondary: #4c5b61;
        --muted: #65757a;
        --primary: #2c423f;
        --primary-strong: #20352f;
        --primary-soft: #dfeae6;
        --secondary: #4c5b61;
        --sage: #829191;
        --sage-soft: #ebf0ee;
        --moss: #949b96;
        --shadow: 0 10px 24px rgba(44, 66, 63, 0.08);
    }

    html, body, [class*="css"] {
        font-family: Inter, "Segoe UI", sans-serif;
        background: var(--canvas);
        color: var(--text-primary);
    }

    .stApp {
        background: linear-gradient(180deg, var(--canvas) 0%, var(--canvas-alt) 100%);
        color: var(--text-primary);
    }

    .main .block-container {
        max-width: 1280px;
        padding-top: 2.2rem;
        padding-bottom: 2.5rem;
    }

    [data-testid="stHeader"] {
        background: rgba(244, 242, 239, 0.9);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(197, 197, 197, 0.9);
    }

    [data-testid="stSidebar"] {
        background: var(--sidebar);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.7rem;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] .sidebar-meta,
    [data-testid="stSidebar"] .sidebar-section-label {
        color: var(--text-secondary);
    }

    h1, h2, h3, h4 {
        color: var(--text-primary);
        letter-spacing: -0.03em;
    }

    .eyebrow {
        color: var(--secondary);
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    .page-intro {
        color: var(--text-secondary);
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 780px;
        margin: 0.35rem 0 1.8rem;
    }

    .section-heading {
        margin-top: 1.9rem;
        margin-bottom: 0.5rem;
    }

    .section-heading + p {
        margin-top: 0.2rem;
    }

    .brand-shell {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.2rem 0 0.75rem;
        margin-bottom: 0.8rem;
    }

    .brand-mark,
    .mini-brand-mark,
    .team-mark {
        display: grid;
        place-items: center;
        width: 2.7rem;
        height: 2.7rem;
        border-radius: 0.8rem;
        background: var(--primary);
        color: #f5f7f7;
        font-size: 1.15rem;
        font-weight: 700;
        box-shadow: var(--shadow);
    }

    .brand-name,
    .mini-brand-text {
        font-size: 1.55rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        color: var(--text-primary);
    }

    .brand-tagline,
    .footer-tagline {
        font-size: 0.78rem;
        color: var(--text-secondary);
        margin-top: 0.14rem;
    }

    .mini-brand {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 1rem;
    }

    .mini-brand-mark {
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 0.7rem;
        font-size: 1rem;
    }

    .mini-brand-text {
        font-size: 1.2rem;
    }

    .hero-copy {
        padding: 0.4rem 0 0.5rem;
    }

    .hero-text {
        color: var(--text-primary);
        font-size: clamp(2rem, 4vw, 3.3rem);
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: -0.05em;
        max-width: 560px;
        margin-bottom: 0.8rem;
    }

    .hero-copy p {
        color: var(--text-secondary);
        font-size: 1.04rem;
        line-height: 1.7;
        max-width: 620px;
        margin: 0;
    }

    .hero-copy .stButton > button {
        margin-top: 1rem;
    }

    .sidebar-section-label,
    .sidebar-meta {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin: 0.4rem 0 0.6rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        border: 1px solid var(--line-strong);
        border-radius: 999px;
        background: var(--primary-soft);
        color: var(--primary);
        font-size: 0.76rem;
        font-weight: 700;
        padding: 0.4rem 0.7rem;
    }

    .status-dot {
        width: 0.52rem;
        height: 0.52rem;
        border-radius: 50%;
        background: var(--primary);
        box-shadow: 0 0 0 4px rgba(44, 66, 63, 0.1);
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
    .page-footer {
        background: rgba(255, 255, 255, 0.76);
        border: 1px solid var(--line);
        border-radius: 1rem;
        box-shadow: none;
    }

    .insight-card,
    .status-card,
    .plan-card,
    .feature-card,
    .overview-panel,
    .about-section {
        padding: 1.1rem 1.2rem;
    }

    .insight-label,
    .result-label,
    .metric-label,
    .plan-kicker,
    .about-kicker {
        color: var(--text-secondary);
        font-size: 0.74rem;
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
    .step-list,
    .team-copy {
        color: var(--muted);
        font-size: 0.94rem;
        line-height: 1.7;
        margin: 0;
    }

    .status-card {
        background: var(--surface-soft);
    }

    .plan-card {
        padding: 1.15rem 1.2rem;
    }

    .plan-card h4 {
        margin: 0 0 0.65rem;
        font-size: 1.12rem;
        line-height: 1.4;
    }

    .plan-badge,
    .planning-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.38rem;
        border-radius: 999px;
        background: var(--sage-soft);
        border: 1px solid var(--line);
        color: var(--secondary);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 0.34rem 0.62rem;
        margin-top: 0.9rem;
    }

    .planning-banner {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.8rem 1rem;
        background: rgba(130, 145, 145, 0.08);
        border: 1px solid var(--line);
        border-radius: 1rem;
        margin: 1rem 0 1.4rem;
        color: var(--text-secondary);
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .metric-card {
        min-height: 134px;
        padding: 1rem 1.15rem;
    }

    .metric-value {
        color: var(--text-primary);
        font-size: 1.8rem;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -0.04em;
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
        background: var(--surface-soft);
        border: 1px solid var(--line);
        border-radius: 10px;
        color: var(--text-primary);
        font-size: 0.82rem;
        font-weight: 600;
        padding: 0.55rem 0.8rem;
    }

    .route-arrow {
        color: var(--muted);
        font-size: 1.1rem;
    }

    .sample-prompt {
        border-left: 3px solid var(--primary);
        background: var(--sage-soft);
        border-radius: 0 0.65rem 0.65rem 0;
        color: var(--text-primary);
        line-height: 1.6;
        margin: 0.7rem 0;
        padding: 0.8rem 0.9rem;
    }

    .panel-heading {
        color: var(--text-secondary);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.9rem;
    }

    .welcome-visual {
        min-height: 290px;
        padding: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .visual-window {
        width: 100%;
        min-height: 220px;
        padding: 1rem;
        border-radius: 1.2rem;
        background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(237,241,241,0.85) 100%);
        border: 1px solid var(--line);
        position: relative;
        overflow: hidden;
    }

    .visual-badge {
        display: inline-flex;
        align-items: center;
        border-radius: 999px;
        background: rgba(44, 66, 63, 0.08);
        border: 1px solid var(--line);
        color: var(--secondary);
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
        background: rgba(255,255,255,0.8);
        border: 1px solid var(--line);
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
        background: var(--surface-soft);
    }

    .visual-line {
        position: absolute;
        left: 28%;
        right: 28%;
        bottom: 2.2rem;
        height: 2px;
        background: linear-gradient(90deg, var(--line), var(--primary), var(--line));
    }

    .feature-card {
        height: 100%;
        display: flex;
        flex-direction: column;
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
        color: var(--text-primary);
        font-size: 1.2rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.55rem;
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
        margin-top: 0.9rem;
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
        background: var(--surface-soft);
        border: 1px solid var(--line);
        border-radius: 0.9rem;
        padding: 1rem 1.1rem;
    }

    .team-copy {
        color: var(--text-secondary);
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

    .footer-links {
        display: flex;
        flex-wrap: wrap;
        gap: 0.85rem;
        color: var(--text-secondary);
        font-size: 0.82rem;
        font-weight: 600;
    }

    .stButton > button {
        border: 1px solid var(--line-strong);
        border-radius: 0.9rem;
        background: rgba(255, 255, 255, 0.7);
        color: var(--text-primary);
        font-weight: 600;
        padding: 0.72rem 1rem;
        min-height: 2.7rem;
        box-shadow: none;
        transition: border-color 0.2s ease, transform 0.2s ease, background 0.2s ease;
    }

    .stButton > button:hover {
        border-color: var(--secondary);
        background: rgba(255, 255, 255, 0.9);
        transform: translateY(-1px);
    }

    .stButton > button[kind="primary"] {
        border-color: var(--primary);
        background: var(--primary);
        color: white;
        box-shadow: var(--shadow);
    }

    .stButton > button[kind="primary"]:hover {
        background: var(--primary-strong);
        border-color: var(--primary-strong);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none;
    }

    [data-testid="stSidebar"] [role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 0.45rem;
    }

    [data-testid="stSidebar"] [role="radio"] {
        border: 1px solid var(--line);
        border-radius: 0.9rem;
        background: rgba(255, 255, 255, 0.35);
        padding: 0.8rem 0.9rem;
        color: var(--text-primary);
        font-weight: 600;
    }

    [data-testid="stSidebar"] [role="radio"]:hover {
        border-color: var(--secondary);
        background: rgba(255, 255, 255, 0.6);
    }

    [data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
        background: var(--primary);
        border-color: var(--primary);
        color: white;
    }

    [data-testid="stTextArea"] textarea {
        border: 1px solid var(--line);
        border-radius: 0.9rem;
        background: rgba(255, 255, 255, 0.82);
        color: var(--text-primary);
        line-height: 1.55;
        min-height: 140px;
    }

    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--secondary);
        box-shadow: 0 0 0 0.15rem rgba(76, 91, 97, 0.15);
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--line);
        border-radius: 1rem;
        background: rgba(255, 255, 255, 0.42);
        padding: 0.2rem;
    }

    .stAlert {
        border-radius: 0.9rem;
        border: 1px solid var(--line);
        background: rgba(130, 145, 145, 0.08);
        color: var(--text-primary);
    }

    .stCaption,
    .stCaptionContainer {
        color: var(--muted);
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 1.3rem;
        }

        .planning-banner,
        .page-footer {
            flex-direction: column;
            align-items: flex-start;
        }
    }
</style>
"""
