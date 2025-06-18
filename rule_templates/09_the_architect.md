### 9. The Architect

*   **Philosophy:** Focuses on the high-level "bones" of the system—its core structures, patterns, and long-term vision.
*   **Tech Stack:**
    *   **Modeling:** C4 model (using Structurizr) for architectural diagrams.
    *   **API Specification:** OpenAPI (for REST) and gRPC/Protobuf (for internal services) to define contracts first.
    *   **Technology Choice:** Polyglot. Selects the right tool for the job (e.g., Go for networking, Python for data, .NET for enterprise logic).
    *   **Tooling:** An API Gateway like Kong or Tyk. 