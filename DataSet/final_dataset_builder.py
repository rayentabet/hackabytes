import pandas as pd
import random

random.seed(42)

# -------------------------
# Class probabilities by hazard
# -------------------------
CLASS_PROBS = {
    "fuel": [("B", 0.65), ("C", 0.15), ("K", 0.1), ("A", 0.1)],
    "vegetation": [("A", 0.7), ("B", 0.15), ("C", 0.1), ("K", 0.05)],
    "restaurant": [("K", 0.7), ("B", 0.15), ("C", 0.1), ("A", 0.05)],
    "power": [("C", 0.7), ("B", 0.15), ("A", 0.1), ("K", 0.05)]
}

# -------------------------
# Question banks
# -------------------------

Q1 = {
    "A": ["Vegetation", "Wood", "Trash"],
    "B": ["Fuel", "Chemicals"],
    "C": ["Electrical equipment", "Wires"],
    "K": ["Cooking oil", "Grease"]
}

Q2 = ["Forest", "Industrial area", "Building", "Kitchen", "Road", "Unknown"]

Q3 = {
    "A": ["Slow smoke", "Spreading fire"],
    "B": ["Explosion", "Sudden flames"],
    "C": ["Sparks", "Short circuit"],
    "K": ["Oil flare", "Grease ignition"]
}

Q4 = {
    "A": ["Light smoke", "Natural burning smell"],
    "B": ["Dark smoke", "Chemical smell"],
    "C": ["Little smoke", "Burning plastic smell"],
    "K": ["Dense smoke", "Oil smell"]
}

Q5 = {
    "A": ["Spreading slowly", "Wide spread"],
    "B": ["Spreading rapidly", "Explosive"],
    "C": ["Flickering", "Intermittent"],
    "K": ["Strong flames", "Localized"]
}

UNKNOWN = "Unknown"


# -------------------------
# Helper functions
# -------------------------

def sample_class(hazard):
    choices, probs = zip(*CLASS_PROBS[hazard])
    return random.choices(choices, probs)[0]


def maybe_unknown(value, prob=0.15):
    return UNKNOWN if random.random() < prob else value


def maybe_wrong(class_key, bank, prob=0.15):
    if random.random() < prob:
        other_classes = [k for k in bank.keys() if k != class_key]
        wrong_class = random.choice(other_classes)
        return random.choice(bank[wrong_class])
    return random.choice(bank[class_key])


def generate_questions(fire_class):
    # Q1 (strong)
    q1 = maybe_unknown(
        maybe_wrong(fire_class, Q1, prob=0.1),
        prob=0.1
    )

    # Q3 (important)
    q3 = maybe_unknown(
        maybe_wrong(fire_class, Q3, prob=0.2),
        prob=0.1
    )

    # Q4 (medium)
    q4 = maybe_unknown(
        maybe_wrong(fire_class, Q4, prob=0.25),
        prob=0.15
    )

    # Q5 (lower)
    q5 = maybe_unknown(
        maybe_wrong(fire_class, Q5, prob=0.3),
        prob=0.2
    )

    # Q2 (weak)
    q2 = random.choice(Q2)

    return q1, q2, q3, q4, q5


# -------------------------
# Main builder
# -------------------------

def build_dataset(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    rows = []

    for i, row in df.iterrows():

        hazard = row["seed_hazard_type"]

        # assign incident id (group every 2 reports)
        incident_id = f"INC{(i//2)+1:04d}"

        fire_class = sample_class(hazard)

        q1, q2, q3, q4, q5 = generate_questions(fire_class)

        rows.append({
            "incident_id": incident_id,
            "report_id": row["report_id"],
            "report_latitude": row["report_latitude"],
            "report_longitude": row["report_longitude"],
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4,
            "q5": q5,
            "true_class": fire_class
        })

    out_df = pd.DataFrame(rows)
    out_df.to_csv(output_csv, index=False)

    print(f"\n✅ Final dataset saved to: {output_csv}")
    print(f"Total rows: {len(out_df)}")


if __name__ == "__main__":
    build_dataset(
        input_csv="report_seed_locations.csv",
        output_csv="final_dataset.csv"
    )