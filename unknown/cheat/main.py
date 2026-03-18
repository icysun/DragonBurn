#!/usr/bin/env python3
# Original content before modification...
# ... (original code) ... 
# Modified code:
def parse_json_offsets(json_data):
    try:
        offsets = json.loads(json_data)
        return offsets
    except json.JSONDecodeError:
        print('Error parsing JSON offsets')
        return None
# ... (rest of the code) ...