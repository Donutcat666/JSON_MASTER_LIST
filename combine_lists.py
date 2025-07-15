import json, re
from pathlib import Path

def load_json_strip_comments(path):
    text = Path(path).read_text()
    # strip C-style comments /* ... */
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    return json.loads(text)

def main():
    combined = {}
    # ITS90_temperature_standards
    combined['ITS90_temperature_standards'] = load_json_strip_comments('ITS90_temperature_standards.json')['ITS90_temperature_standards']
    # electrical_calibrator_specs
    # use cleaned file for valid JSON
    combined['electrical_calibrator_specs'] = load_json_strip_comments('electrical_calibrator_specs_clean.json')
    # fluke catalog master
    combined['fluke_calibrator_catalog'] = load_json_strip_comments('fluke_calibrator_catalog_master_v_1.json')
    # demo
    combined['fluke_catalog_demo'] = load_json_strip_comments('fluke_catalog_master_demo.json')
    # digital thermometer readouts
    combined['digital_thermometer_readouts'] = load_json_strip_comments('digital_thermometer_readouts.json')
    # multifunction temp calibrators
    combined['multifunction_temp_calibrators'] = load_json_strip_comments('multifunction_temp_calibrators.json')
    # temperature probes and sensors
    combined['temperature_probes_sensors'] = load_json_strip_comments('temperature_probes_sensors.json')
    # piston gauge pressure calibration
    combined['piston_gauge_pressure_calibration'] = load_json_strip_comments('piston_gauge_pressure_calibration.json')
    Path('combined.json').write_text(json.dumps(combined, indent=2))

if __name__ == '__main__':
    main()
