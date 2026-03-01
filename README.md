# Antimicrobial Resistance Tracker

Antimicrobial resistance surveillance system tracking resistance patterns using CARD genomics data and WHO GLASS antimicrobial data.

## Architecture

```
antimicrobial-resistance-tracker/
  src/           # Core modules
  tests/         # Unit and integration tests
  config/        # Configuration files
  docs/          # Documentation
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
