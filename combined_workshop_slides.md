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

---

### **Slide 12: Why AI Chats "Age"**
-   **Title:** Why AI Chats "Age"
-   **Content:**
    -   **The Golden Age:** At the start of a chat, the context is small and clean. The AI is highly focused and effective.
    -   **The "Lost in the Middle" Problem:** As the chat history grows, models tend to pay more attention to the very beginning and the very end of the conversation. Critical details mentioned in the middle can get "lost" or ignored. (This is a known issue sometimes called the "Needle-in-a-Haystack" problem).
    -   **Catastrophic Forgetting:** Eventually, the context becomes so large and noisy that performance degrades significantly. The AI forgets key constraints or reverts to generic behavior. This is your cue to start a new session.

---

### **Slide 13: Managing Context Strategically**
-   **Title:** When and How to Start a New Session
-   **Content:**
    -   **When to Reset:** Start a new session when the task changes significantly, or when you notice the AI is consistently forgetting instructions. Don't be afraid to start fresh!
    -   **The "Context Carry-Over" Technique:**
        1.  Use the `Export Chat` feature to get a full transcript of your conversation.
        2.  Open the transcript and manually copy the most critical pieces of context: key decisions, final code snippets, and important constraints.
        3.  **This curation is the most important step.** A small, highly-relevant context is far more powerful than a large, noisy one.
        4.  Paste this curated context as the very first prompt in your new chat session to get the AI up to speed instantly.

---

### **Slide 14: Scoping: Small Projects**
-   **Title:** Small Projects & "From Scratch"
-   **Content:**
    -   **Context Strategy:** Full Ingestion.
    -   For small projects, the AI can and should ingest every file. Use the `@` symbol in Cursor to add the whole directory to the context.
    -   **Pro-Tip:** For speed, you can write a simple script (e.g., Python, shell) to concatenate all relevant files (`.py`, `.md`, etc.) into a single `.txt` file. You can then provide this single file to the AI, which is much faster than having it read files one by one.

---

### **Slide 15: Scoping: Medium Projects**
-   **Title:** Medium-Sized Projects
-   **Content:**
    -   **Context Strategy:** Efficient Partial Ingestion.
    -   The entire codebase might be too large to fit in the context window.
    -   Focus on providing the most relevant parts: the core modules you're working on, the API definitions, the database schema, and key `README` files.
    -   Again, a script can be used to gather these key files into a single context summary for the AI.

---

### **Slide 16: Scoping: Large Projects**
-   **Title:** Large-Scale & Legacy Projects
-   **Content:**
    -   **Context Strategy:** The "Directory Map" Approach.
    -   Full ingestion is impossible and undesirable.
    -   **The Strategy:** Use a script to map the entire directory structure, including function and class signatures from key files, into a single markdown file (`directory_map.md`).
    -   **Workflow:**
        1.  Start your session by giving the AI the `directory_map.md`. It now has a high-level "map" of the entire codebase.
        2.  When you need to work on a specific feature, ask the AI: "Based on the map, which files are most relevant for implementing X?"
        3.  Add only those specific files to the context. This allows you to navigate massive codebases effectively.

---

### **Slide 17: Configuring Your Cursor IDE**
-   **Title:** Configuring Your Cursor IDE
-   **Content:**
    -   Beyond the `.cursorrules`, you can fine-tune the editor itself in the settings:
        -   **AI Model Selection:** Choose your preferred models (e.g., GPT-4o, Claude 3 Opus).
        -   **Temperature Settings:** Adjust the "creativity" vs. determinism of the AI.
        -   **Editor & Linter Integrations:** Configure format-on-save and other helpers.
        -   **Global Rules File:** Point to a global `.cursorrules` file to use as a default.

---

### **Slide 18: The 10x Workflow: A Structured Approach**
-   **Title:** The 10x Workflow: A Structured Approach
-   **Content:** To gain massive efficiency, you need a structured, responsive partnership with your AI. This is a workflow that balances AI speed with human oversight.

---

### **Slide 19: Phase 1: Planning & Alignment**
-   **Title:** Phase 1: Planning & Alignment
-   **Content:**
    1.  **Discuss the Feature:** Massage the ideas back and forth. Crucially, tell the AI: **"Do not act until I approve the plan."**
    2.  **Demand a Plan:** Ask for a plan, architecture, and stack if it's complex.
    3.  **Create Milestones:** Have the AI create a `features_built/feature_name/milestones.md` file to track its own progress.

---

### **Slide 20: Phase 2: Test-Driven Development**
-   **Title:** Phase 2: Test-Driven Development
-   **Content:**
    1.  **Define Interfaces & Write Tests First:** Decide on the function/class interfaces *before* implementation. Then, ask the AI to write tests.
    2.  **Skim-Review the Tests:** Ensure the tests cover the main use cases and edge cases. This is your safety net.

---

### **Slide 21: Phase 3: Implementation & Verification**
-   **Title:** Phase 3: Implementation & Verification
-   **Content:**
    1.  **Step-by-Step Implementation:** Ask the AI to develop code one step at a time. **DO NOT SKIP THE REVIEW.**
    2.  **Warning:** Blindly accepting code is how you lose work. The AI may "fix" a trivial issue by deleting a complex module if left unsupervised.
    3.  **Run ALL Tests:** After every significant change, run the full test suite. Repeat until all tests pass.

---

### **Slide 22: Warning: The "Ground Truth" Spiral**
-   **Title:** Warning: The "Ground Truth" Spiral
-   **Content:**
    -   This is a catastrophic failure mode. It begins when a test fails and the AI is unsure what is correct: the test or the feature.
    -   **The Spiral:**
        1.  You tell the AI "fix the tests."
        2.  The AI sees a flawed test and **changes your working feature code to be incorrect** to satisfy the bad test.
        3.  This change causes other, correct tests to fail.
        4.  You say "fix the new failing tests." The AI, now believing the feature is wrong, continues to "fix" or delete other features.
    -   **You are the Arbiter of Truth.** You must explicitly tell the AI which part is correct.

---

### **Slide 23: Phase 4: Finalization**
-   **Title:** Phase 4: Finalization
-   **Content:**
    1.  **Verify with Examples:** Have the AI write simple execution examples (e.g., in `if __name__ == "__main__:"`). Run them and inspect the output together.
    2.  **Document and Comment:** Once everything is working, ask the AI to thoroughly document the code.

---

### **Slide 24: Q&A**
-   **Title:** Discussion & Questions
-   **Content:** Q&A 