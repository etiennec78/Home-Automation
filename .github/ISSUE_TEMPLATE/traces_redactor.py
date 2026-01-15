"""
This script redacts sensitive information from Home Assistant automation
traces. It replaces sensitive keys and IDs with placeholders to ensure
privacy.
"""

from sys import argv
import json

SENSITIVE_KEYS = {
    "default": {
        "latitude",
        "longitude",
    },
    "ids": {
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
        "alarm_code"
        "awaited_persons",
    },
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
    "ble_entity",
    "ble_entities",
    "ble_transmitter_entity",
    "ble_transmitter_entities",
    "ble_scanner_switch",
    "speaker_tts_devices",
    "gate_areas",
    "gps_trackers",
    "other_gps_to_wait_for",
    "drivers_near_gate",
}

SAVE_LOCATION = "trace_redacted.json"


class Config:
    """
    Configuration class to manage redaction settings.

    Attributes:
        keep_ids (bool): Determines whether to keep entity IDs unredacted.
    """

    keep_ids = False


class Redactor:
    """
    Handles the redaction of sensitive information from JSON data.

    Attributes:
        redacted_ids (list): List of already redacted entity IDs.
        config (Config): Configuration settings for redaction.
        sensitive_keys (list[str]): List of keys considered sensitive.
    """

    redacted_ids = []
    config: Config
    sensitive_keys: list[str]

    def __init__(self, config: Config):
        """
        Initializes the Redactor with the given configuration.

        Args:
            config (Config): Configuration settings for redaction.
        """
        self.config = config
        self._set_sensitive_keys()

    def _set_sensitive_keys(self) -> None:
        """
        Sets the list of sensitive keys based on the configuration.
        """
        self.sensitive_keys = list(SENSITIVE_KEYS["default"])
        if not self.config.keep_ids:
            self.sensitive_keys += SENSITIVE_KEYS["ids"]

    def redact_id(self, entity_id: str) -> str:
        """
        Redacts an entity ID by replacing it with a placeholder.

        Args:
            entity_id (str): The entity ID to redact.

        Returns:
            str: The redacted entity ID.
        """
        if len(splitted := entity_id.split(".")) > 1:
            domain = splitted[0]
            if entity_id in self.redacted_ids:
                index = self.redacted_ids.index(entity_id)
            else:
                index = len(self.redacted_ids)
                self.redacted_ids.append(entity_id)
            return f"{domain}.<redacted_{index}>"
        return "<redacted>"

    def get_replacement(self, key: str, value: str | list | dict) -> str | list | dict:
        """
        Replaces sensitive values with placeholders.

        Args:
            key (str): The key associated with the value.
            value (str | list | dict): The value to potentially redact.

        Returns:
            str | list | dict: The redacted value.
        """
        if isinstance(value, list):
            return [self.get_replacement(key, item) for item in value]
        if isinstance(value, dict):
            return {
                subkey: self.get_replacement(subkey, subvalue)
                for subkey, subvalue in value.items()
            }
        if key in self.sensitive_keys:
            return "<redacted>"
        if key in SENSITIVE_IDS and isinstance(value, str) and not self.config.keep_ids:
            return self.redact_id(value)
        return value

    def get_trace(self, input_file: str) -> dict | None:
        """
        Reads and parses a JSON trace file.

        Args:
            input_file (str): Path to the input JSON file.

        Returns:
            dict | None: The parsed JSON data, or None if an error occurs.
        """
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.decoder.JSONDecodeError:
                    f.seek(0)
                    print(
                        f"Error: the file '{input_file}' does not contain valid json"
                    )
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist")
        except IOError:
            print(f"Could not read the file '{input_file}'")

    def save_trace(self, data: dict, output_file: str) -> None:
        """
        Saves redacted JSON data to a file.

        Args:
            data (dict): The redacted JSON data.
            output_file (str): Path to the output JSON file.
        """
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError:
            print(f"Could not write to the file '{output_file}'")

    def redact_json_file(self, input_file: str, output_file: str) -> bool:
        """
        Redacts sensitive information from a JSON file and saves the result.

        Args:
            input_file (str): Path to the input JSON file.
            output_file (str): Path to the output JSON file.

        Returns:
            bool: Whereas the file redacting was successfull
        """
        if data := self.get_trace(input_file):
            redacted = {
                key: self.get_replacement(key, value) for key, value in data.items()
            }
            self.save_trace(redacted, output_file)

            return True

        return False


class ArgumentsManager:
    """
    Manages command-line arguments for the script.

    Attributes:
        argv (list[str]): List of command-line arguments.
        file_location (str): Path to the input file.
        config (Config): Configuration settings for redaction.
    """

    argv: list[str]
    file_location: str = ""
    config: Config

    HELP_MESSAGE = (
        "DESCRIPTION:\n"
        "    This Python script masks confidential information\n"
        "    before sending Home Assistant automation traces.\n"
        "    It is designed for blueprints from:\n"
        "    https://github.com/etiennec78/Home-Automation/\n"
        "    Note: It may not hide all confidential information\n"
        "    for third-party automations.\n\n"
        "VERSION:\n"
        "    2.0.0\n\n"
        "OPTIONS:\n"
        "    --help      Display this help message.\n"
        "    --keep-ids  Don't redact entity_ids.\n\n"
        "USAGE:\n"
        "    python3 traces_redactor.py <input_file> [options]\n\n"
        "EXAMPLE:\n"
        "    python3 traces_redactor.py trace.json"
    )

    def __init__(self, arguments: list[str]) -> None:
        """
        Initializes the ArgumentsManager with command-line arguments.

        Args:
            arguments (list[str]): Command-line arguments.
        """
        self.argv = arguments
        self.config = Config()
        trace_index = self._read_args(arguments)
        if trace_index >= 0:
            self.file_location = arguments[trace_index]

    def _show_help(self) -> None:
        """
        Displays the help message.
        """
        print(self.HELP_MESSAGE)

    def _read_args(self, arguments: list[str]) -> int:
        """
        Parses command-line arguments and sets configuration options.

        Args:
            arguments (list[str]): Command-line arguments.

        Returns:
            int: Index of the trace file argument, or an error code.
        """
        if len(arguments) < 2:
            print(
                "Error: Trace file was not passed as an argument.\nPlease see --help."
            )
            return -1

        args = []
        options = []
        for argument in arguments[1:]:
            if argument[:2] == "--":
                options.append(argument[2:])
            else:
                args.append(argument)

        if "help" in options:
            self._show_help()
            return -2

        for option in options:
            if option == "keep-ids":
                self.config.keep_ids = True
            elif option != "help":
                print(f"Error: Unrecognized option: {option}")
                return -1

        if len(args) > 1:
            print("Error: Too many arguments")
            return -1

        return arguments.index(args[0])

    def get_file_location(self) -> str:
        """
        Retrieves the file location argument.

        Returns:
            str: Path to the input file.
        """
        return self.file_location

    def get_config(self) -> Config:
        """
        Retrieves the configuration settings.

        Returns:
            Config: The configuration settings.
        """
        return self.config


if __name__ == "__main__":
    """
    Main entry point for the script. Handles argument parsing and redaction.
    """
    args_manager = ArgumentsManager(argv)
    if file_location := args_manager.get_file_location():
        config = args_manager.get_config()
        redactor = Redactor(config)
        if redactor.redact_json_file(file_location, SAVE_LOCATION):
            print(
                f"The file '{file_location}' has been successfuly redacted and saved in '{SAVE_LOCATION}'."
            )
