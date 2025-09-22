from sys import argv
import json

SENSITIVE_KEYS = {
    "latitude",
    "longitude",
    "friendly_name",
    "description",
    "service",
    "id",
    "source",
    "context_source",
    "message",
    "context_message",
    "trigger",
    "driver_name",
    "confirmation",
}

SENSITIVE_IDS = {
    "item",
    "gate_location",
    "zones_to_notify",
    "entity_id",
    "entities",
    "person",
    "persons",
    "driver",
    "device_tracker",
    "device_trackers",
    "driving_sensor",
    "driving_sensors",
    "gates",
    "gate",
    "travel_time_sensor",
    "travel_time_sensors",
    "notify_service",
    "notify_services",
    "active_notify_services",
    "itinerary_sensor",
    "itinerary_sensors",
    "ble_entitie",
    "ble_entities",
    "ble_transmitter_entity",
    "ble_transmitter_entities",
    "ble_scanner_switch",
    "speaker_tts_devices",
}


class Redactor:
    redacted_ids = []

    def redact_id(self, entity_id: str) -> str:
        if len(splitted := entity_id.split(".")) > 1:
            domain = splitted[0]
            if entity_id in self.redacted_ids:
                index = self.redacted_ids.index(entity_id)
            else:
                index = len(self.redacted_ids)
                self.redacted_ids.append(entity_id)
            return f"{domain}.<redacted_{index}>"
        else:
            return "<redacted>"

    def get_replacement(self, key: str, value: str | list | dict) -> str | list | dict:
        if isinstance(value, list):
            return [self.get_replacement(key, item) for item in value]
        elif isinstance(value, dict):
            return {
                subkey: self.get_replacement(subkey, subvalue)
                for subkey, subvalue in value.items()
            }
        else:
            if key in SENSITIVE_KEYS:
                return "<redacted>"
            elif key in SENSITIVE_IDS and isinstance(value, str):
                return self.redact_id(value)
            else:
                return value

    def get_trace(self, input_file: str) -> dict | None:
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.decoder.JSONDecodeError:
                    print(
                        f"Error: the file '{input_file}' does not contain valid json: {f.read()}"
                    )
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist")
        except IOError:
            print(f"Could not read the file '{input_file}'")

    def save_trace(self, data: dict, output_file: str) -> None:
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError:
            print(f"Could not write to the file '{output_file}'")

    def redact_json_file(self, input_file: str, output_file: str) -> None:
        if data := self.get_trace(input_file):
            redacted = {
                key: self.get_replacement(key, value) for key, value in data.items()
            }
            self.save_trace(redacted, output_file)


if __name__ == "__main__":
    if len(argv) > 1:
        trace_file = argv[1]
        redactor = Redactor()
        redactor.redact_json_file(trace_file, "trace_redacted.json")
    else:
        print("Error: Trace file was not passed as an argument")
