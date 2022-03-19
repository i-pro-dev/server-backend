def format_records(records):
    if not records:
        return []
    return list(map(dict, records))

def format_record(record):
    return dict(record)