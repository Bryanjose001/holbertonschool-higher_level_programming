def generate_invitations(template, attendees):
    if type(template) is not str or not isinstance(attendees, list):
        print("Invalid input. Please provide a valid template and a list of attendees.")
        return
    if not template:
        print("Template is empty. Please provide a valid template.")
        return
    if not attendees:
        print("No attendees provided. Please provide a list of attendees.")
        return
    i = 1
    for attendee in attendees:
        tmp_template = template

        # Prepare the invitation text by replacing placeholders
        print(attendee)
        tmp_template = tmp_template.replace("{name}", str(attendee.get("name") or "N/A"))
        tmp_template = tmp_template.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        tmp_template = tmp_template.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        tmp_template = tmp_template.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        file_name = f"output_{i}.txt"
        with open(file_name, 'w') as f:
            f.write(tmp_template)
        i = i + 1