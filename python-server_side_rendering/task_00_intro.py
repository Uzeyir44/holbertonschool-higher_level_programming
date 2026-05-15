def generate_invitations(template_content, attendees):
    def check_el(element):
        if element == None:
            return ('N/A')
        return (element)

    n = 1

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i in attendees:
        template = template_content
        
        if len(template) == 0:
            print("Template is empty, no output files generated.")
            return
        
        if not isinstance(template, str):
            print(f"Error: template must be a string, got {type(template)}")
            return
        
        if not isinstance(attendees, list):
            print(f"Error: attendees must be a list, got {type(attendees)}")
            return
        
        if not isinstance(i, dict):
            print(f"Error: list must contain dictionaries, got {type(item)}")
            return

        template = template.replace('{name}', check_el(i['name']))
        template = template.replace('{event_title}', check_el(i['event_title']))
        template = template.replace('{event_date}', check_el(i['event_date']))
        template = template.replace('{event_location}', check_el(i['event_location']))

        output = 'output_' + str(n) + '.txt'
        with open(output, 'w') as file:
            file.write(template)

        n += 1
