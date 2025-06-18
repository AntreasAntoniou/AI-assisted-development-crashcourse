# AI-Assisted Development: A Crash Course - Combined Script

---

### **Slide 1: Title Slide**
-   **Title:** AI-Assisted Development: A Crash Course
-   **Subtitle:** From Prompting Fundamentals to Advanced Persona-Driven Workflows
-   **Presenter:** Antreas Antoniou

---

### **Slide 2: The Modern AI Toolbox**
-   **Title:** Introduction to the Players
-   **Content:**
    -   Today we'll focus on **Cursor**, an "AI-first" code editor built for deep AI collaboration.
    -   But it's helpful to know the other major players:
    -   **Codex Suite (OpenAI):** Not just a single model, but a suite of tools. This includes a powerful cloud-based agent for tackling large tasks and the open-source **Codex CLI** for pairing with a lightweight agent in your terminal. [Source: openai.com](https://openai.com/codex), [GitHub](https://github.com/openai/codex)
    -   **Claude Code (Anthropic):** A powerful CLI collaborator you install directly into your terminal. It uses agentic search to understand your entire codebase and can handle entire workflows from issue to PR. [Source: anthropic.com](https://www.anthropic.com/claude-code)

---

### **Slide 3: Our Focus: Cursor**
-   **Title:** Why Cursor for This Tutorial?
-   **Content:**
    -   While other tools are powerful, Cursor is unique in its focus on a **deep, project-aware, and configurable** AI partnership.
    -   It treats the AI not as a command-line tool, but as a genuine collaborator that can be taught and molded.
    -   The core of this is the `.cursorrules` file, which allows us to move beyond simple prompting into creating persistent, persona-driven assistants. This is what we'll be mastering today.

---

### **Slide 4: The Art of the Prompt**
-   **Title:** Principles of Effective Prompting
-   **Content:**
    -   **Specificity is Key:** Vague questions get vague answers. Provide details, examples, and constraints. Instead of "write a function," say "write a Python function named `calculate_average` that takes a list of numbers and returns a float."
    -   **Provide Context:** The AI doesn't know what you know. Give it the surrounding code, the error message, the goal you're trying to achieve.
    -   **Assume a Persona:** Tell the AI *who* it should be. "You are a senior Python developer specializing in performance." This primes the model to respond in a certain style and with a certain level of expertise.
    -   **Iterate and Refine:** Your first prompt is rarely your best. Treat prompting as a conversation. Refine your request based on the AI's response.

---

### **Slide 5: LLM Psychology & Intuition**
-   **Title:** How LLMs "Think": A Practical Mental Model
-   **Content:**
    -   **It's All Statistics:** An LLM isn't thinking; it's a powerful next-token prediction engine. Its goal is to find the most statistically likely response based on the massive amount of text and code it was trained on.
    -   **Simulated Understanding:** The "understanding" you perceive is an emergent property of these patterns. This is why psychological cues work. By providing context, you guide the model toward a better statistical neighborhood.
    -   **Finding the Vibe (The Art of Context):** Think of it like tuning a radio or finding a dance partner. Your goal is to provide the perfect context to lead the AI to the right answer. This includes:
        -   The right code snippets.
        -   A clear instruction and goal.
        -   A specific persona or role.
        -   Examples of the desired output.

---

### **Slide 6: Pro-Level Tips & Tricks**
-   **Title:** Unlocking Your Assistant's Potential
-   **Content:**
    -   **Meta-Prompting:** When you don't know how to ask for something, ask the AI! "How should I prompt you to get a well-structured, documented FastAPI endpoint?"
    -   **The "Unstuck" Protocol:** When you feel stuck or frustrated, **just tell the AI why.** Describe your confusion, your goal, and your current obstacle. "I'm stuck because this error message is confusing. My goal is X. Here is my code. Can you help me understand the problem and suggest a path forward?" This provides incredible context.
    -   **Crafting Context:** The best context includes not just the code, but also the goal, the constraints, and the desired output format.

---

### **Slide 7: Global vs. Project Rules: A Strategy**
-   **Title:** Global vs. Project Rules: A Strategy
-   **Content:**
    -   Both rule sets are critical for efficiency. The key is to layer them correctly.
    -   **Global Rules (User Settings):** Define your universal principles and personal style here. How do you, the developer, always want the AI to behave? (e.g., "Always use `pathlib` for paths," "Never use single-letter variable names.")
    -   **Project Rules (`.cursorrules`):** Define project-specifics here. This file overrides the global rules and should contain the project's tech stack, coding conventions, and the specific AI persona for this context.

---

### **Slide 8: Live Demo: My Cursor Settings**
-   **Title:** Live Demo: My Cursor Settings
-   **Content:**
    -   Now, I'll walk you through my personal Cursor configuration, including my global rules and how I tailor them for different projects.
    -   *(This is your cue to open your Cursor settings and share your screen.)*

---

### **Slide 9: Anatomy of a Good Rules File**
-   **Title:** Anatomy of a Good Rules File
-   **Content:**
    -   A good rules file goes beyond simple instructions. It defines a persona, a philosophy, and a workflow. The possibilities are endless, but here are some key sections to consider:
    -   **➔ Persona:** Who is the AI? *("You are a Senior DevOps Engineer...")*
    -   **➔ Interaction Guidelines:** How should it behave? *("Be concise," "Ask clarifying questions...")*
    -   **➔ Core Tech Stack:** What tools should it prefer? *("Always use `pytest` for tests," "Default to FastAPI for new services...")*
    -   **➔ Coding Style:** Enforce project standards. *("Format code with `black`," "Use conventional commit messages...")*
    -   **➔ Personal Pitfalls:** Help you with your own habits. *("If I am over-engineering, remind me of the MVP principle...")*
    -   **➔ Project-Specific Data:** Give it knowledge it couldn't have otherwise. *("The user authentication service is located at `auth.service.internal`...")*

---

### **Slide 10: The Self-Improving Assistant**
-   **Title:** The Self-Improving Assistant
-   **Content:**
    -   The most powerful `.cursorrules` files include a directive for the AI to help improve its own rules.
    -   **Example:** `**Proactive Rule Updates:** If you identify a significant piece of feedback... you MUST proactively propose an update to this .cursorrules file.`
    -   This creates a feedback loop where your assistant learns and grows with the project.

---

### **Slide 11: The Personal Assistant: An AI for Your Brain**
-   **Title:** An AI for Your Brain: Tailoring Rules to YOU
-   **Content:**
    -   This is where AI assistance becomes truly transformative. Codify your own context, goals, and even your values into the rules to build a partner that understands and complements your unique workflow.
    -   **➔ Your Background:** Give the AI your resume. *"My background is in physics, not front-end. Explain CSS concepts step-by-step using analogies from physics if possible."*
    -   **➔ Your Goals:** Tell the AI your "why". *"My primary goal is to learn Rust. Prioritize idiomatic Rust solutions and explain the concepts as we go."*
    -   **➔ Your Cognitive Style:** How do you work best? *"I'm a visual thinker; you must generate a Mermaid diagram when we discuss architecture."*
    -   **➔ Your Pitfalls:** What are your common traps? *"I have ADHD; if I go on a tangent, gently guide me back to our current objective."* or *"I struggle with perfectionism; if I debate minor details, remind me that 'perfect is the enemy of good'."*
    -   **➔ Your Value System:** What principles guide your work? *"My highest value is user privacy. Always challenge any feature that collects user data and propose the most private-by-default implementation."* or *"I value open-source; prefer solutions that use open-source libraries over proprietary ones."* 