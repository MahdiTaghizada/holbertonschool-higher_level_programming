import os

def generate_invitations(template, attendees):
    # ---- Input Type Validation ----
    if not isinstance(template, isinstance(template, str).__class__):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ---- Empty Template ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ---- Empty Attendee List ----
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---- Process and Generate Files ----
    for index, attendee in enumerate(attendees, start=1):

        # Replace placeholders, use "N/A" if key missing or value None
        processed = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed = processed.replace("{" + key + "}", value)

        # Output filename
        filename = f"output_{index}.txt"

        # Write the file
        try:
            with open(filename, "w") as f:
                f.write(processed)

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            return
