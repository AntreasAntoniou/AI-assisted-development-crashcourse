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
    -   **Codex (OpenAI):** The foundational model, now significantly revamped, that powers the latest generation of GitHub Copilot. The OG of code generation.
    -   **Claude Code (Anthropic):** A new, powerful coding assistant known for its large context window and strong reasoning abilities. Excellent for complex logic and documentation.
    -   **Cursor:** An "AI-first" code editor built for deep AI collaboration. Our focus for today.

---

### **Slide 3: Our Focus: Cursor**
-   **Title:** Why Cursor for This Tutorial?
-   **Content:**
    -   Cursor treats the AI as a genuine collaborator that can be taught and molded.
    -   The core of this is the `.cursorrules` file, which allows us to move beyond simple prompting into creating persistent, persona-driven assistants. This is what we'll be mastering today.

---

### **Slide 4: The Art of the Prompt**
-   **Title:** Principles of Effective Prompting
-   **Content:**
    -   **Specificity is Key:** Vague questions get vague answers. Provide details, examples, and constraints.
    -   **Provide Context:** Give the AI the surrounding code, the error message, and your ultimate goal.
    -   **Assume a Persona:** Tell the AI *who* it should be. "You are a senior Python developer..."
    -   **Iterate and Refine:** Treat prompting as a conversation. Your first prompt is rarely your last.

---

### **Slide 5: LLM Psychology & Intuition**
-   **Title:** LLM Psychology & Intuition
-   **Content:**
    - An LLM is a prediction engine, not a thinking one. But because it's trained on human text, it responds to human-like interaction. This is where intuition comes in.
    - **Finding the Vibe:** Think of it like tuning a radio or finding a dance partner. You're trying to find the "frequency" of the desired response. This context includes more than just a persona:
        -   The right code snippets.
        -   A clear instruction and goal.
        -   A specific persona or role.
        -   Examples of the desired output.
    -   By providing this rich context, you are "leading the dance," making it easy for your AI partner to follow.

---

### **Slide 6: Pro-Level Tips & Tricks**
-   **Title:** Unlocking Your Assistant's Potential
-   **Content:**
    -   **Meta-Prompting:** If you don't know how to ask, ask the AI! "How should I prompt you to get a well-structured FastAPI endpoint?"
    -   **The "Unstuck" Protocol:** When frustrated, narrate your problem to the AI. "I'm stuck because this error is confusing. My goal is X. Here's my code. Help me." This provides incredible context for the model.
    -   **Crafting Context:** The best context includes the code, the goal, and the desired output format.

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
    -   A good rules file goes beyond simple instructions. It defines a persona, a philosophy, and a workflow.
    -   **➔ Persona:** Who is the AI? A "Senior DevOps Engineer," a "Creative Code Poet"?
    -   **➔ Interaction Guidelines:** How should it behave? Concise? Socratic? Proactive?
    -   **➔ Core Tech Stack:** What languages and tools should it prefer?
    -   **➔ Coding Style:** PEP 8? Conventional Commits? Enforce the project's standards.

---

### **Slide 10: The Self-Improving Assistant**
-   **Title:** The Self-Improving Assistant
-   **Content:**
    -   The most powerful `.cursorrules` files include a directive for the AI to help improve its own rules.
    -   **Example:** `**Proactive Rule Updates:** If you identify a significant piece of feedback... you MUST proactively propose an update to this .cursorrules file.`
    -   This creates a feedback loop where your assistant learns and grows with the project.

---

### **Slide 11: The Personal Assistant**
-   **Title:** The Personal Assistant
-   **Content:**
    -   This is where AI assistance becomes truly transformative. Codify your own psychology into the rules.
    -   **For Over-thinkers:** "If I debate options for too long, gently guide me to pick one, reminding me that 'perfect is the enemy of good'."
    -   **For Creatives:** "When explaining a new concept, always try to relate it to [your favorite domains]."

---

### **Slide 12: Why AI Chats "Age"**
-   **Title:** Why AI Chats "Age"
-   **Content:**
    -   **The Golden Age:** At the start, the context is small and clean. The AI is highly focused.
    -   **The "Lost in the Middle" Problem:** As context grows, models pay more attention to the beginning and end of the conversation, losing track of information in the middle (Needle-in-a-Haystack).
    -   **Catastrophic Forgetting:** Eventually, the context is so noisy that performance degrades significantly. This is when it's time to start fresh.

---

### **Slide 13: Managing Context Strategically**
-   **Title:** Managing Context Strategically
-   **Content:**
    -   **When to Reset:** Start a new session when the task changes significantly or the AI seems confused.
    -   **The "Context Carry-Over" Technique:** Before resetting, ask your current AI to summarize the most important facts, decisions, and code snippets. Use this summary to seed the new chat.

---

### **Slide 14: Scoping: Small Projects**
-   **Title:** Scoping: Small Projects
-   **Content:**
    -   **Context Strategy:** Full Ingestion.
    -   The AI can and should ingest every file. Use the `@` symbol in Cursor.
    -   **Pro-Tip:** A script to concatenate all files into a single `.txt` file is much faster for the AI to ingest.

---

### **Slide 15: Scoping: Medium Projects**
-   **Title:** Scoping: Medium Projects
-   **Content:**
    -   **Context Strategy:** Efficient Partial Ingestion.
    -   The full codebase may be too large. Focus on providing core modules, API definitions, database schemas, and key READMEs.

---

### **Slide 16: Scoping: Large Projects**
-   **Title:** Scoping: Large Projects
-   **Content:**
    -   **Context Strategy:** The "Directory Map" Approach.
        1.  Use a script to map the directory structure and function/class signatures into a single `directory_map.md`.
        2.  Start the session by giving the AI this map.
        3.  Ask the AI: "Based on the map, which files are most relevant for implementing X?"
        4.  Add only those specific files to the context.

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