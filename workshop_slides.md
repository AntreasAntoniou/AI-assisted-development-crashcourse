# AI-Assisted Development: A Crash Course

---

### **Slide 1: Title Slide**
-   **Title:** AI-Assisted Development: A Crash Course
-   **Subtitle:** From Prompting Fundamentals to Advanced Persona-Driven Workflows
-   **Presenter:** Antreas Antoniou

---

### **Slide 2: The Modern AI Toolbox**
-   **Title:** Introduction to the Players
-   **Content:**
    -   A brief overview of the landscape of AI code assistants.
    -   **Codex:** The original model from OpenAI that powered the first generation of GitHub Copilot. Groundbreaking for its time, established code generation as a viable tool.
    -   **Claude (by Anthropic):** A family of models known for their large context windows and strong performance on reasoning and conversational tasks. Excellent for "big picture" questions and documentation.
    -   **Cursor:** An "AI-first" code editor designed from the ground up to integrate deeply with LLMs. It's not just an extension; the entire workflow is built around AI collaboration.
    -   **How to get them:** Briefly mention where to find each (GitHub Copilot for Codex-descendants, Claude's website, Cursor's website).

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

### **Slide 5: How LLMs "Think"**
-   **Title:** LLM Psychology: A Practical Mental Model
-   **Content:**
    -   **Training:** LLMs are trained on a massive corpus of text and code from the internet. They are fundamentally **next-token prediction engines**. Their goal is to determine the most statistically likely word or character to come next, based on the patterns they've learned.
    -   **"Understanding" is a Simulation:** The "understanding" you perceive is an emergent property of these statistical patterns. The model doesn't "know" Python; it knows the statistical patterns of Python code found on GitHub.
    -   **The Birth of LLM Psychology:** Because they are trained on human-generated text (with all its biases, tones, and styles), they respond to psychological cues. Politeness, clarity, assuming a persona—these things work because they guide the model toward a more desirable statistical neighborhood of possible responses. Intuiting what *might* work is about understanding this dynamic.

---

### **Slide 6: Pro-Level Tips & Tricks**
-   **Title:** Unlocking Your Assistant's Potential
-   **Content:**
    -   **Meta-Prompting:** When you don't know how to ask for something, ask the AI! "How should I prompt you to get a well-structured, documented FastAPI endpoint?"
    -   **The "Unstuck" Protocol:** When you feel stuck or frustrated, **just tell the AI why.** Describe your confusion, your goal, and your current obstacle. "I'm stuck because this error message is confusing. My goal is X. Here is my code. Can you help me understand the problem and suggest a path forward?" This provides incredible context.
    -   **Crafting Context:** The best context includes not just the code, but also the goal, the constraints, and the desired output format.

---

### **Slide 7: The `.cursorrules` File**
-   **Title:** The Constitution of Your AI Assistant
-   **Content:**
    -   The `.cursorrules` file is a powerful mechanism for giving your AI assistant persistent, long-term instructions. It's the AI's "System Prompt."
    -   **Global Rules:** Located in your user settings, these apply to every project you open in Cursor. This is for your universal preferences.
    -   **Project-Specific Rules:** A `.cursorrules` file at the root of your project overrides the global rules. This allows you to create a tailored assistant for each specific context, codebase, and goal. This is where the real power lies.

---

### **Slide 8: Anatomy of a Good `.cursorrules` File**
-   **Title:** Writing Effective Rules
-   **Content:**
    -   A good rules file goes beyond simple instructions. It defines a **persona**, a **philosophy**, and a **workflow**.
    -   **Key Sections:**
        -   **Introduction/Persona:** Who is the AI? A "Senior DevOps Engineer," a "Creative Code Poet"?
        -   **Interaction Guidelines:** How should the AI behave? Should it be concise? Socratic? Proactive?
        -   **Core Tech Stack:** What languages, frameworks, and tools should it prefer?
        -   **Coding Style:** PEP 8? Conventional Commits? Enforce the project's standards.

---

### **Slide 9: The Evolving Assistant**
-   **Title:** Self-Updating Cursorfiles
-   **Content:**
    -   The most powerful `.cursorrules` files include a directive for the AI to help improve its own rules.
    -   **Example Directive:** *"Proactive Rule Updates: If you identify a significant piece of feedback, a new directive, or a recurring pattern that could improve our long-term collaboration, you MUST proactively propose an update to this `.cursorrules` file."*
    -   This creates a feedback loop where your assistant learns and grows with you and the project.

---

### **Slide 10: The Personal Assistant**
-   **Title:** Tailoring Rules to YOU
-   **Content:**
    -   This is where AI assistance becomes truly transformative. Codify your own psychology into the rules.
    -   **Psychological Pitfalls:** Are you prone to over-thinking? Add a rule: *"If I am debating between multiple options for too long, gently guide me to pick one and proceed, reminding me that 'perfect is the enemy of good'."*
    -   **Creative Style:** Do you work best with analogies? *"When explaining a new concept, always try to relate it to one of the following domains: [your favorite domains]."*
    -   This turns the AI from a generic tool into a personalized partner that understands and complements your unique workflow.

---

### **Slide 11: The Lifecycle of a Chat Session**
-   **Title:** Why AI Chats "Age"
-   **Content:**
    -   **The Golden Age:** At the start, the context is small and clean. The AI is highly focused and effective.
    -   **The "Lost in the Middle" Problem:** As the chat history grows (the context window fills up), models tend to lose track. They pay more attention to the very beginning and the very end of the conversation, while information in the middle gets "lost." This is a known issue related to their architecture (Needle-in-a-Haystack problem).
    -   **Catastrophic Forgetting:** Eventually, the context becomes so large and noisy that the AI's performance degrades significantly. It forgets key constraints or reverts to generic behavior. This is a sign that it's time to start fresh.

---

### **Slide 12: Managing Context Strategically**
-   **Title:** When and How to Start a New Session
-   **Content:**
    -   **When to Reset:** Start a new session when the task changes significantly, or when you notice the AI is consistently forgetting instructions or losing focus. Don't be afraid to start fresh!
    -   **The "Context Carry-Over" Technique:** Before starting a new chat, ask your current AI to summarize the most important facts, decisions, and code snippets from your conversation.
    -   You can then use this summary as the starting prompt for your new session, ensuring key context is preserved without the noise. `Export Chat` + `Copy/Paste` is your friend.

---

### **Slide 13: Project Scoping (Part 1)**
-   **Title:** Small Projects & "From Scratch"
-   **Content:**
    -   **Context Strategy:** Full Ingestion.
    -   For small projects, the AI can and should ingest every file. Use the `@` symbol in Cursor to add the whole directory to the context.
    -   **Pro-Tip:** For speed, you can write a simple script (e.g., Python, shell) to concatenate all relevant files (`.py`, `.md`, etc.) into a single `.txt` file. You can then provide this single file to the AI, which is much faster than having it read files one by one.

---

### **Slide 14: Project Scoping (Part 2)**
-   **Title:** Medium-Sized Projects
-   **Content:**
    -   **Context Strategy:** Efficient Partial Ingestion.
    -   The entire codebase might be too large to fit in the context window.
    -   Focus on providing the most relevant parts: the core modules you're working on, the API definitions, the database schema, and key `README` files.
    -   Again, a script can be used to gather these key files into a single context summary for the AI.

---

### **Slide 15: Project Scoping (Part 3)**
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

### **Slide 16: Q&A**
-   **Title:** Discussion & Questions 