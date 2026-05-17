import math
import random
import pandas as pd

EARTH_RADIUS_M = 6371000
RANDOM_SEED = 42

MIN_DISTANCE_M = 30
MAX_DISTANCE_M = 250
REPORTS_PER_SEED = 2

random.seed(RANDOM_SEED)


def offset_coordinate(lat, lon, distance_m, angle_deg):
    """
    Move from (lat, lon) by distance_m in direction angle_deg.
    Returns new latitude, longitude.
    """
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    angle_rad = math.radians(angle_deg)

    angular_distance = distance_m / EARTH_RADIUS_M

    new_lat_rad = math.asin(
        math.sin(lat_rad) * math.cos(angular_distance) +
        math.cos(lat_rad) * math.sin(angular_distance) * math.cos(angle_rad)
    )

    new_lon_rad = lon_rad + math.atan2(
        math.sin(angle_rad) * math.sin(angular_distance) * math.cos(lat_rad),
        math.cos(angular_distance) - math.sin(lat_rad) * math.sin(new_lat_rad)
    )

    return math.degrees(new_lat_rad), math.degrees(new_lon_rad)


def generate_report_locations(
    input_csv="hazard_points_lebanon.csv",
    output_csv="report_seed_locations.csv",
    reports_per_seed=REPORTS_PER_SEED,
    min_distance_m=MIN_DISTANCE_M,
    max_distance_m=MAX_DISTANCE_M,
):
    df = pd.read_csv(input_csv)

    rows = []
    report_counter = 1

    for _, row in df.iterrows():
        seed_hazard_type = row["hazard_type"]
        seed_lat = float(row["lat"])
        seed_lon = float(row["lon"])

        for _ in range(reports_per_seed):
            distance_m = random.uniform(min_distance_m, max_distance_m)
            angle_deg = random.uniform(0, 360)

            report_lat, report_lon = offset_coordinate(
                seed_lat,
                seed_lon,
                distance_m,
                angle_deg
            )

            rows.append({
                "report_id": f"REP{report_counter:04d}",
                "seed_hazard_type": seed_hazard_type,
                "seed_lat": seed_lat,
                "seed_lon": seed_lon,
                "report_latitude": round(report_lat, 6),
                "report_longitude": round(report_lon, 6),
                "distance_from_seed_m": round(distance_m, 2)
            })

            report_counter += 1

    out_df = pd.DataFrame(rows)
    out_df.to_csv(output_csv, index=False)
    print(f"Saved {len(out_df)} report locations to {output_csv}")


if __name__ == "__main__":
    generate_report_locations()
    