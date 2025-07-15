import json
import re
from pathlib import Path

def load_json_strip_comments(path):
    text = Path(path).read_text()
    # strip C-style comments /* ... */
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    return json.loads(text)

def main():
    combined = {
        "catalog_rows": [],
        "docs_rows": []
    }

    # ITS-90 temperature standards kept as a separate block
    combined["ITS90_temperature_standards"] = load_json_strip_comments(
        "ITS90_temperature_standards.json"
    )["ITS90_temperature_standards"]

    # Electrical calibrator specs list
    combined["electrical_calibrator_specs"] = load_json_strip_comments(
        "electrical_calibrator_specs_clean.json"
    )

    def merge_catalog(path):
        data = load_json_strip_comments(path)
        combined["catalog_rows"].extend(data.get("catalog_rows", []))
        combined["docs_rows"].extend(data.get("docs_rows", []))

    # Merge all catalog/doc style JSON files
    merge_catalog("fluke_calibrator_catalog_master_v_1.json")
    merge_catalog("fluke_catalog_master_demo.json")
    merge_catalog("digital_thermometer_readouts.json")
    merge_catalog("multifunction_temp_calibrators.json")
    merge_catalog("temperature_probes_sensors.json")
    merge_catalog("piston_gauge_pressure_calibration.json")

    Path("combined.json").write_text(json.dumps(combined, indent=2))

if __name__ == '__main__':
    main()
