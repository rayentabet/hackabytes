# Emergency Dispatch Recommendation Pipeline

Emergency Dispatch Recommendation Pipeline is a prototype for enriching emergency incident coordinates with nearby-place context, generating an operational incident report, and ranking fire stations by distance and required equipment.

The project is focused on emergency response support for incidents in Lebanon. Station locations and equipment assignments in `data/fire_stations.json` are sample or dummy data and must be verified before any real operational use.

## Features

- Enrich incident coordinates with nearby OpenStreetMap and optional Google Places context.
- Prepare compact Markdown/JSON context for Gemini.
- Optionally generate a Gemini emergency incident report.
- Infer required fire equipment types and rank fire stations deterministically.
- Write both full dispatch recommendation JSON and compact frontend-friendly JSON.

## Project Files

| File | Description |
| --- | --- |
| `run_incident_pipeline.py` | End-to-end command-line pipeline: copies an input incident CSV, enriches nearby places, builds Gemini context, optionally generates a Gemini report, and writes dispatch recommendation JSON. |
| `enrichment_file.py` | Nearby-place enrichment logic using OpenStreetMap Overpass and optional Google Places data. Produces structured nearby-place CSV output. |
| `prepare_gemini_context.py` | Converts one incident plus nearby-place rows into a compact Markdown file containing structured JSON context for Gemini. |
| `generate_gemini_report.py` | Calls the Gemini API with the prepared context and writes a Markdown emergency incident report. |
| `dispatch_recommendations.py` | Deterministic dispatch recommendation engine. Infers required equipment, ranks fire stations, and writes full and compact JSON payloads. |
| `data/fire_stations.json` | Sample fire-station registry with coordinates, region, phone, and dummy equipment coverage. |
| `incidents.csv` | Small sample incident input CSV. |
| `sample_nearby_test.csv` | Sample incident CSV with an explicit nearby-search radius. Useful for testing the enrichment pipeline. |
| `.env.example` | Template for local API keys. Copy this to `.env.local` and fill in your own keys. |
| `.gitignore` | Keeps secrets, generated outputs, caches, removed app/dataset folders, and local media out of GitHub. |
| `requirements.txt` | Python dependencies needed to run the pipeline scripts. |
| `database schema.png` | Optional database schema/reference image for the project design. |

## Files To Add To GitHub

Recommended source and sample files:

```bash
git add README.md .gitignore .env.example requirements.txt
git add run_incident_pipeline.py enrichment_file.py prepare_gemini_context.py generate_gemini_report.py dispatch_recommendations.py
git add data/fire_stations.json incidents.csv sample_nearby_test.csv
git add "database schema.png"
```

Do not add these by default:

| Path | Reason |
| --- | --- |
| `.env.local` | Contains local API keys and secrets. |
| `pipeline_output/` | Generated pipeline output; it can be recreated. |
| `gemini_incident_context.md` | Generated context file. |
| `incident_nearby_places_structured.csv` | Generated nearby-place CSV. |
| `incident_report.md` | Generated Gemini report. |
| `app.py` | Removed FastAPI app; no longer part of this project. |
| `static/` | Removed dashboard/static frontend; no longer part of this project. |
| `DataSet/` | Removed dataset-building/training scripts and generated dataset files. |
| `df.py` | Local scratch script with a machine-specific absolute path. |
| `Hackabytes/` | Large local media files. |
| `*.docx`, `*.pptx`, `*.HEIC`, `*.MOV` | Working documents and large binary media. |

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create local environment variables:

```bash
cp .env.example .env.local
```

Then edit `.env.local` with your own keys.

## Run The Incident Pipeline

Run without Gemini, useful for testing enrichment and deterministic dispatch output:

```bash
python3 run_incident_pipeline.py --input sample_nearby_test.csv --places-source osm --skip-llm
```

Run with Gemini and Google Places:

```bash
python3 run_incident_pipeline.py --input sample_nearby_test.csv --places-source both
```

Pipeline outputs are written to `pipeline_output/` by default.

## GitHub Setup Commands

```bash
git init
git add README.md .gitignore .env.example requirements.txt
git add run_incident_pipeline.py enrichment_file.py prepare_gemini_context.py generate_gemini_report.py dispatch_recommendations.py
git add data/fire_stations.json incidents.csv sample_nearby_test.csv
git add "database schema.png"
git commit -m "Initial emergency dispatch pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
