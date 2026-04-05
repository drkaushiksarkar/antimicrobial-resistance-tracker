# Antimicrobial Resistance Tracker

Antimicrobial resistance surveillance system tracking resistance patterns using CARD genomics data and WHO GLASS antimicrobial data.

## Architecture Decision Records (ADRs)

This project utilizes Architecture Decision Records (ADRs) to document significant architectural decisions.  ADRs are short, text documents that capture important choices and their context.

The following ADRs have been created:

*   **ADR-001: Model Selection for Resistance Prediction:**  Details the decision to use [Specify Model - e.g., Random Forest] for predicting antimicrobial resistance, outlining alternatives considered (e.g., SVM, Neural Networks) and the rationale for the chosen model based on performance, interpretability, and scalability.
*   **ADR-002: Data Pipeline Design:** Describes the design of the data pipeline, including data sources (CARD, WHO GLASS), data ingestion methods (e.g., APIs, file uploads), data transformation steps, and data storage solutions (e.g., PostgreSQL, cloud storage).  Addresses data quality and validation procedures.
*   **ADR-003: Deployment Strategy:**  Outlines the deployment strategy, including the chosen platform (e.g., Docker, Kubernetes, serverless functions), infrastructure (e.g., AWS, Azure, GCP), and CI/CD pipeline.  Considers scalability, reliability, and cost.
*   **ADR-004: Technology Choices:**  Documents key technology choices, such as the programming language (Python), key libraries (e.g., pandas, scikit-learn, Flask/FastAPI), and database system (e.g., PostgreSQL).  Justifies these choices based on project requirements and team expertise.
*   **ADR-005: API Design:** Details the design of the API, including endpoints, data formats (JSON), authentication, and rate limiting.

ADRs are located in the `docs/adr` directory.

## Architecture

```
antimicrobial-resistance-tracker/
  src/           # Core modules
  tests/         # Unit and integration tests
  config/        # Configuration files
  docs/          # Documentation
    adr/         # Architecture Decision Records
  requirements.txt # Project dependencies
  LICENSE        # Project license
```

## Modules

- **resistance_profiler**: Core resistance profiler functionality
- **gene_mapper**: Core gene mapper functionality
- **susceptibility_analyzer**: Core susceptibility analyzer functionality
- **trend_tracker**: Core trend tracker functionality
- **outbreak_detector**: Core outbreak detector functionality

## Quick Start

```bash
pip install -r requirements.txt
python -m antimicrobial_resistance_tracker.main
```

## Testing

```bash
pytest tests/ -v
```

## License

MIT License - see LICENSE for details.