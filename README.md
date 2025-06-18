# AI-Assisted Development: A Crash Course

This repository contains the materials for a crash course on AI-Assisted Development, focusing on leveraging modern tools like Cursor to their full potential.

## Contents

-   `.cursorrules`: The master rules file for the AI assistant.
-   `rule_templates/`: A collection of 15 unique, persona-driven `.cursorrules` files for different development scenarios.
-   `website/`: An interactive slide-deck showcase built with HTML/CSS/JS and served by a Python script.
-   `use_cases/`: Example projects to be developed during the workshop.
-   `workshop_slides.md`: The full content of the presentation in markdown format.

## Setup

To install the necessary dependencies, run:

```bash
pip install -e .[dev]
```

To run the interactive slide theme showcase:

```bash
python website/server.py
```

Then, navigate to `http://localhost:8000` in your browser. 