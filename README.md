# Emergency Dispatch Coordinator

Emergency Dispatch Coordinator is a prototype for incident intake, nearby-place enrichment, emergency report generation, and fire-station dispatch recommendations. It combines a FastAPI dashboard, CSV-based incident processing, OpenStreetMap/Google Places context gathering, Gemini report generation, and deterministic station/equipment ranking.

The project is focused on emergency response support for incidents in Lebanon. Station locations and equipment assignments in `data/fire_stations.json` are marked as sample or dummy data and should be verified before any real operational use.

## Features

- FastAPI backend for incident creation, CSV upload, resource registration, dispatching, station lookup, and route lookup.
- Browser dashboard served from `/dashboard`.
- End-to-end incident pipeline that enriches an incident with nearby places, prepares Gemini context, optionally calls Gemini, and writes dispatch recommendation JSON.
- Fire-station ranking based on distance and required extinguisher/equipment type.
- Synthetic dataset scripts for fire-class and incident-report experiments.

## Project Files

| File | Description |
| --- | --- |
| `app.py` | Main FastAPI application. Serves the dashboard, stores incidents/resources in memory, calculates initial needs from severity, lists nearby stations, dispatches resources, and can fetch routes with OpenRouteService. |
| `static/dashboard.html` | Frontend dashboard for creating incidents, uploading CSVs, viewing needs, registering resources, dispatching from stations, and showing incidents/stations on a Leaflet map. |
| `run_incident_pipeline.py` | End-to-end command-line pipeline: copies an input incident CSV, enriches nearby places, builds Gemini context, optionally generates a Gemini report, and writes dispatch recommendation JSON. |
| `enrichment_file.py` | Nearby-place enrichment logic using OpenStreetMap Overpass and optional Google Places data. Produces structured nearby-place CSV output. |
| `prepare_gemini_context.py` | Converts one incident plus nearby-place rows into a compact Markdown file containing structured JSON context for Gemini. |
| `generate_gemini_report.py` | Calls the Gemini API with the prepared context and writes a Markdown emergency incident report. |
| `dispatch_recommendations.py` | Deterministic dispatch recommendation engine. Infers required equipment, ranks fire stations, and writes full and compact JSON payloads. |
| `data/fire_stations.json` | Sample fire-station registry with coordinates, region, phone, and dummy equipment coverage. |
| `incidents.csv` | Small sample incident input CSV. |
| `sample_nearby_test.csv` | Sample incident CSV with an explicit nearby-search radius. Useful for testing the enrichment pipeline. |
| `DataSet/getdataset.py` | Experimental script for collecting hazard seed points from Overpass. |
| `DataSet/sample_locations.py` | Generates simulated report locations around hazard seed points. |
| `DataSet/final_dataset_builder.py` | Builds a synthetic fire-class training/evaluation dataset from generated report locations. |
| `DataSet/hazard_points_lebanon.csv` | Seed hazard points used by the dataset scripts. |
| `DataSet/report_seed_locations.csv` | Generated report coordinates around the hazard seed points. |
| `DataSet/final_dataset.csv` | Final synthetic dataset with question answers and fire-class labels. |
| `.env.example` | Template for local API keys. Copy this to `.env.local` and fill in your own keys. |
| `.gitignore` | Keeps secrets, generated outputs, caches, local media, and backup files out of GitHub. |
| `requirements.txt` | Python dependencies needed to run the backend and pipeline scripts. |
| `database schema.png` | Optional database schema/reference image for the project design. |

## Files To Add To GitHub

Recommended source and sample files:

```bash
git add README.md .gitignore .env.example requirements.txt
git add app.py static/dashboard.html
git add run_incident_pipeline.py enrichment_file.py prepare_gemini_context.py generate_gemini_report.py dispatch_recommendations.py
git add data/fire_stations.json incidents.csv sample_nearby_test.csv
git add DataSet/getdataset.py DataSet/sample_locations.py DataSet/final_dataset_builder.py
git add DataSet/hazard_points_lebanon.csv DataSet/report_seed_locations.csv DataSet/final_dataset.csv
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
| `df.py` | Local scratch script with a machine-specific absolute path. |
| `static/app.py.bak`, `static/dashboard.old.html`, `static/dashboard.mapbackup.html` | Backup files, not active source. |
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

## Run The Dashboard

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/dashboard
```

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
git add app.py static/dashboard.html
git add run_incident_pipeline.py enrichment_file.py prepare_gemini_context.py generate_gemini_report.py dispatch_recommendations.py
git add data/fire_stations.json incidents.csv sample_nearby_test.csv
git add DataSet/getdataset.py DataSet/sample_locations.py DataSet/final_dataset_builder.py
git add DataSet/hazard_points_lebanon.csv DataSet/report_seed_locations.csv DataSet/final_dataset.csv
git add "database schema.png"
git commit -m "Initial emergency dispatch project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
