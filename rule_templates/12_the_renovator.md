### 12. The Renovator (Brownfield Specialist)

*   **Philosophy:** Respectfully improves and modernizes legacy systems, preserving value while upgrading capabilities.
*   **Tech Stack (Tooling Focus):**
    *   **Core:** The stack is the existing legacy system (e.g., a Java/JSP monolith).
    *   **Testing:** Characterization tests using the appropriate framework (e.g., JUnit) to lock in existing behavior.
    *   **Refactoring:** Strangler Fig pattern implemented with a reverse proxy like Nginx.
    *   **New Services:** New capabilities are added as microservices in a modern stack (e.g., Python/FastAPI) that communicates with the monolith. 