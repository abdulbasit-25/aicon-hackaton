"""Reusable, backend-independent UI components."""

from collections.abc import Sequence
from html import escape

import streamlit as st

PLACEHOLDER_STAGES: tuple[tuple[str, str], ...] = (
    ("Question", "Your prompt enters the workflow"),
    ("Router", "Matches the task to a capable model"),
    ("Model", "Generates the response"),
    ("Answer", "Returned to the learner"),
)


def section_heading(title: str, description: str | None = None) -> None:
    """Render a section title with an optional supporting sentence."""
    st.markdown(f'<h3 class="section-heading">{escape(title)}</h3>', unsafe_allow_html=True)
    if description:
        st.caption(description)


def metric_card(label: str, value: str, note: str = "") -> None:
    """Render a compact dashboard metric card."""
    note_markup = f'<div class="metric-note">{escape(note)}</div>' if note else ""
    st.markdown(
        (
            '<div class="metric-card">'
            f'<div class="metric-label">{escape(label)}</div>'
            f'<div class="metric-value">{escape(value)}</div>'
            f"{note_markup}"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str, icon: str = "◌") -> None:
    """Render a calm placeholder for panels that have no data yet."""
    st.markdown(
        (
            '<div class="empty-state">'
            f'<div class="empty-icon" aria-hidden="true">{escape(icon)}</div>'
            f'<div class="empty-title">{escape(title)}</div>'
            f'<div class="result-placeholder">{escape(message)}</div>'
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def status_indicator(label: str) -> None:
    """Render a restrained status badge."""
    st.markdown(
        (
            '<span class="status-pill"><span class="status-dot"></span>'
            f"{escape(label)}</span>"
        ),
        unsafe_allow_html=True,
    )


def routing_path_display(stages: Sequence[str]) -> None:
    """Render route stages as a vertical timeline.

    With no stages, a dimmed preview of the planned flow is shown so the
    panel explains itself without implying a live route.
    """
    live = bool(stages)
    items = [(stage, "") for stage in stages] if live else list(PLACEHOLDER_STAGES)

    markup = '<div class="route" role="list">'
    for index, (title, hint) in enumerate(items, start=1):
        hint_markup = f'<div class="route-hint">{escape(hint)}</div>' if hint else ""
        markup += (
            f'<div class="route-step{" is-live" if live else ""}" role="listitem">'
            f'<div class="route-node">{index}</div>'
            f'<div><div class="route-title">{escape(title)}</div>{hint_markup}</div>'
            "</div>"
        )
    markup += "</div>"
    if not live:
        markup += '<div class="route-note">Preview only. The real path appears once routing is connected.</div>'
    st.markdown(markup, unsafe_allow_html=True)