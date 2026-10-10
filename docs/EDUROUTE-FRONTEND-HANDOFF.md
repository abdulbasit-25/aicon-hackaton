# EduRoute frontend handoff

This document records the frontend work completed so far, describes the current
dashboard module by module, and captures the current visual design so it can be
used as context for a later redesign prompt.

## Project at a glance

EduRoute is currently a Streamlit frontend foundation for an educational
assistant concept. The interface presents a tutor workspace and planned
calibration and impact-analysis destinations. It does **not** connect to a
model, route questions, calculate metrics, or retrieve analytics data.

The app is launched from the project root with:

```powershell
Set-Location 'C:\Users\abdul\Downloads\hackatan\EduRoute'
.\.venv\Scripts\streamlit.exe run app/main.py
```

The existing project virtual environment is used, so no additional package or
dependency was added for the dashboard work.

## Work completed so far

### Import diagnosis

- The reported error referred to a package-qualified import,
  `from app.components ...`.
- Inspection of the current `app/main.py` found sibling imports instead:
  `from components ...` and `from styles ...`.
- The source tree contains `app/main.py`, `app/components.py`,
  `app/styles.py`, and `app/demo_data.py` together, as well as an existing
  `app/__init__.py`.
- The sibling imports are consistent with running `streamlit run app/main.py`
  from the EduRoute project root. No extra `__init__.py` or package
  restructuring was needed.
- The launch command was tested from the project root and Streamlit's local
  health endpoint returned `ok`.

### Dashboard shell

- Added branded sidebar navigation with three selectable destinations:
  Production AI Tutor, Calibration Studio, and SDG Analytics.
- Added page-specific headings, introductions, and frontend/backend status
  messaging.
- Kept page rendering in the existing single Streamlit entry point; no
  additional application modules were introduced.

### Production AI Tutor

- Added an introductory heading and description clarifying that routing and
  generated answers are not connected.
- Added four selectable preset scenarios:
  - Vocabulary Flashcard
  - Curriculum Synthesis
  - STEM Reasoning
  - Fallback Demonstration
- Selecting a preset loads its sample prompt into the editable educational
  question text area. The text area can then be edited by the user.
- Added a Run button. It deliberately sends no request; clicking it displays a
  notice that backend routing and answer generation are pending.
- Added result placeholders for the answer, routing path, latency, cost, and
  fallback status. They do not contain generated answers or claimed live
  measurements.

### Calibration Studio and SDG Analytics

- Added a concise introductory page for each destination.
- Calibration Studio describes future calibration workflow and evaluation-data
  areas.
- SDG Analytics describes future reporting areas for SDG 4 (Quality Education)
  and SDG 8 (Decent Work and Economic Growth).
- Both destinations explicitly mark backend-dependent content as pending and
  contain no fabricated data.

### Visual foundation

- Applied an obsidian-black page background with white primary text.
- Used deep red sparingly for the brand mark, status details, and primary
  interaction accents.
- Added restrained borders, dark raised surfaces, card-like containers,
  rounded corners, page spacing, and muted explanatory text.
- Kept typography to an Inter / Segoe UI sans-serif fallback stack.
- Avoided decorative gradients and animation.

## Current module inventory

### `app/main.py` — Streamlit entry point and page composition

- Sets the Streamlit page title, icon, wide layout, and expanded initial
  sidebar.
- Injects `APP_CSS` from `app/styles.py`.
- Defines the navigation destinations and preset-name-to-prompt mapping.
- Owns the page rendering functions:
  - `_render_sidebar()` displays the EduRoute brand, navigation radio, and
    frontend status.
  - `_render_page_header()` renders an escaped eyebrow and description around a
    Streamlit title.
  - `_select_scenario()` copies the selected preset prompt to the question
    input in `st.session_state`.
  - `_render_empty_result()` creates a labeled, empty-state result panel.
  - `_render_tutor()` lays out the presets, editable question, Run action, and
    empty result areas.
  - `_render_pending_destination()` provides shared structure for
    backend-pending pages.
  - `_render_calibration_studio()` and `_render_sdg_analytics()` supply the
    descriptions for their respective destinations.
- Uses a destination-to-render-function mapping to render the currently
  selected page.
- Escapes values inserted into custom HTML before rendering.
- Keeps the Run action intentionally disconnected from model or backend calls.

### `app/components.py` — reusable UI helpers

This module remains backend-independent and provides:

- `section_heading(title, description=None)` for a section heading and optional
  caption.
- `metric_card(label, value, note="")` for a reusable metric-card pattern. It
  is retained but is not used for the current tutor's empty metric states.
- `status_indicator(label)` for the compact status badge used in the sidebar
  and pending pages.
- `routing_path_display(stages)` for a generic route-stage sequence. The tutor
  currently calls it with an empty sequence, so it displays an empty-state
  message rather than an invented route.
- HTML escaping for text inserted into helper-generated HTML.

### `app/styles.py` — shared CSS theme

`APP_CSS` is a string containing the `<style>` block injected by `main.py`.
It defines the global theme, sidebar, headings, cards, status badges, route
items, preset radio controls, text area, primary button, result panels, pending
labels, and horizontal rules.

Current core CSS color tokens:

| Token | Value | Use |
|---|---|---|
| `--obsidian` | `#101012` | Main app background |
| `--surface` | `#171719` | Card and control surfaces |
| `--surface-raised` | `#1d1d20` | Raised surfaces and route steps |
| `--border` | `#303034` | Subtle borders |
| `--text-primary` | `#f4f3f2` | Primary text |
| `--text-secondary` | `#aaa8a8` | Secondary text |
| `--accent` | `#a8323d` | Deep-red accent token |
| `--accent-soft` | `#351c20` | Muted red surface |

Additional deep-red shades are used on the brand mark and primary button.
Layout styling constrains the main content width to 1440px and gives the main
and sidebar content distinct top spacing. Radio options and text input use
dark surfaces with restrained borders.

### `app/demo_data.py` — sample-only content from the original foundation

This module still contains:

- Three example study prompts.
- Three placeholder dashboard metric dictionaries.
- An illustrative sequence of route-stage labels.

Its module documentation says these are not live responses or measurements.
The current `app/main.py` does not import or use this module: its four tutor
presets are defined directly in `main.py`, and the tutor shows empty results
instead of those old illustrative examples. The module remains in the project
without being deleted or repurposed.

### `app/__init__.py` — package marker

This existing file marks `app` as a Python package. It contains only a
descriptive module docstring. It was not necessary to add or modify it for the
Streamlit sibling-import launch path.

## Interaction and state

- The active destination is controlled by the `st.radio` widget using the
  session-state key `active_destination`.
- The selected preset is held at `st.session_state["scenario"]`.
- The current question is held at `st.session_state["question_input"]`.
- On preset change, `_select_scenario()` replaces the input with that preset's
  sample prompt. The user can edit the question afterward.
- Pressing Run causes a Streamlit rerun and shows an explicit informational
  message. It does not submit the question anywhere.
- The empty result areas are currently static UI placeholders; no route, answer,
  timing, cost, or fallback result is calculated.

## Validation performed

- Compiled `main.py`, `components.py`, `styles.py`, and `demo_data.py` with the
  project's virtual-environment Python; compilation succeeded.
- Checked editor diagnostics for `main.py` and `styles.py`; no errors were
  reported.
- Started the app from the project root and checked the local Streamlit health
  endpoint; it returned `ok`.
- Opened the running app in a browser and verified the three sidebar
  destinations render.
- Verified that all four preset choices load their corresponding prompt into
  the question text area.
- Clicked Run and verified the pending notice appears while the answer remains
  empty and metrics remain unavailable.

These are smoke checks, not a comprehensive automated test suite.

## Current boundaries and follow-up notes

- No backend integration has been started.
- No real model calls, question routing, answer verification, fallback
  execution, calibration, analytics, persistence, or telemetry are present.
- No real latency, cost, accuracy, savings, or impact figures are displayed.
- The root `README.md` still describes the earlier initial overview screen and
  should be refreshed separately if project-level documentation is updated.
- `app/PROGRESS.md` is a shorter progress summary. This handoff provides the
  more detailed module and design inventory.
- Earlier import troubleshooting was documented in the root
  `IMPORT-FIX.md`; the present application imports and root launch command are
  described above.

## Design summary for a future redesign prompt

### Design currently in place

EduRoute currently has a restrained, dark, professional dashboard foundation.
It uses an obsidian-black canvas, near-white primary text, muted gray
descriptions, and a limited deep-red accent. The left sidebar carries an
outlined red-tinted “E” brand tile, the EduRoute name, the tagline “Learning,
thoughtfully routed,” a radio-based three-page navigation, and a compact
frontend-status indicator.

The main content uses a wide, centered layout with generous top spacing. Each
page begins with a small uppercase, letter-spaced red eyebrow, a prominent
white heading, and a short muted description. The tutor page puts the question
workflow in a bordered dark container: four horizontally arranged preset
choices, an editable multiline prompt, and a restrained red Run button. Below
it, answer and routing areas sit above three compact status/metric placeholders
for latency, cost, and fallback status. The other pages use simple bordered
content cards and muted pending labels instead of charts or invented results.
Borders are subtle gray, corners are moderately rounded, and typography uses
Inter with Segoe UI as a fallback. There are no gradients or animations.

### Prompt-ready handoff

> Redesign the existing EduRoute Streamlit dashboard UI while preserving the
> current app structure, navigation destinations, preset-driven editable tutor
> input, and backend-pending empty states. The current visual baseline is a
> dark obsidian background (`#101012`), near-white text (`#f4f3f2`), muted
> secondary text (`#aaa8a8`), dark card surfaces (`#171719`), subtle borders
> (`#303034`), and restrained deep-red accents (`#a8323d`, with muted red
> surfaces such as `#351c20`). The left sidebar currently contains an “E” brand
> tile, EduRoute name/tagline, a radio navigation for Production AI Tutor,
> Calibration Studio, and SDG Analytics, and a frontend status indicator. The
> tutor page has a page heading and description, four selectable scenarios
> (Vocabulary Flashcard, Curriculum Synthesis, STEM Reasoning, Fallback
> Demonstration), an editable question area, a Run button, and empty answer,
> routing, latency, cost, and fallback sections. Calibration Studio and SDG
> Analytics are introductory pages with pending backend content. Rework the
> visual presentation to the new direction I specify, but keep the interface
> clear, accessible, responsive, and honest about unavailable backend data.
> Do not fabricate results or implement backend behavior unless separately
> requested. Preserve existing public component names and function signatures.
