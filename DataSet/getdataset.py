import time
import random
import requests
import pandas as pd

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

HEADERS = {
    "User-Agent": "hazard-extractor/1.0"
}

# Same grid as before (Lebanon split)
BBOXES = [
    (33.05, 35.10, 33.35, 35.40),
    (33.05, 35.40, 33.35, 35.70),
    (33.05, 35.70, 33.35, 36.00),

    (33.35, 35.10, 33.65, 35.40),
    (33.35, 35.40, 33.65, 35.70),
    (33.35, 35.70, 33.65, 36.00),

    (33.65, 35.10, 33.95, 35.40),
    (33.65, 35.40, 33.95, 35.70),
    (33.65, 35.70, 33.95, 36.00),

    (33.95, 35.10, 34.25, 35.40),
    (33.95, 35.40, 34.25, 35.70),
    (33.95, 35.70, 34.25, 36.00),

    (34.25, 35.10, 34.55, 35.40),
    (34.25, 35.40, 34.55, 35.70),
    (34.25, 35.70, 34.55, 36.00),
]

# Industrial hazard
TAG = '["landuse"="industrial"]'

KEEP_POINTS = 25
FETCH_PER_BOX = 10
RANDOM_SEED = 42

def build_query(bbox):
    south, west, north, east = bbox
    return f"""
    [out:json][timeout:25];
    (
      node({south},{west},{north},{east}){TAG};
      way({south},{west},{north},{east}){TAG};
    );
    out center {FETCH_PER_BOX};
    """
    

def send_query(query, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(
                OVERPASS_URL,
                params={"data": query},
                headers=HEADERS,
                timeout=60
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            code = e.response.status_code if e.response else None
            if code in (429, 504):
                wait = 8 * (attempt + 1)
                print(f"Server busy ({code}). Waiting {wait}s...")
                time.sleep(wait)
            else:
                raise

        except requests.exceptions.RequestException:
            wait = 8 * (attempt + 1)
            print(f"Request error. Waiting {wait}s...")
            time.sleep(wait)

    return {"elements": []}


def extract_coords(el):
    if "lat" in el and "lon" in el:
        return el["lat"], el["lon"]
    if "center" in el:
        return el["center"]["lat"], el["center"]["lon"]
    return None, None


def deduplicate(points):
    seen = set()
    unique = []
    for p in points:
        key = (round(p["lat"], 6), round(p["lon"], 6))
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def main():
    print("Fetching industrial points...\n")

    all_points = []

    for i, bbox in enumerate(BBOXES):
        print(f"Box {i+1}/{len(BBOXES)}")

        query = build_query(bbox)
        data = send_query(query)

        for el in data.get("elements", []):
            lat, lon = extract_coords(el)
            if lat is None:
                continue

            all_points.append({
                "hazard_type": "industrial",
                "lat": lat,
                "lon": lon
            })

        all_points = deduplicate(all_points)

        if len(all_points) >= KEEP_POINTS:
            break

        time.sleep(8)

    # randomize
    random.seed(RANDOM_SEED)
    random.shuffle(all_points)

    final_points = all_points[:KEEP_POINTS]

    df = pd.DataFrame(final_points)
    df.to_csv("industrial_points_lebanon.csv", index=False)

    print(f"\nSaved {len(final_points)} industrial points to industrial_points_lebanon.csv")


if __name__ == "__main__":
    main()