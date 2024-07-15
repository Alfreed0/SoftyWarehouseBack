import json


def get_search_params(filters: str):
    decoded_dict = json.loads(filters)
    match, range, contain = (
        decoded_dict.get("match"),
        decoded_dict.get("range"),
        decoded_dict.get("contain"),
    )
    return match, range, contain


def filter_search(filters: str, base_query, get_model_type):
    match, range, contain = get_search_params(filters)
    if match:
        for key, value in match.items():
            model = get_model_type(key)
            base_query = base_query.filter(getattr(model, key).in_(value))
    if contain:
        for key, value in contain.items():
            model = get_model_type(key)
            base_query = base_query.filter(getattr(model, key).contains(value))
    if range:
        for key, value in range.items():
            if not value[0] or (value[0] == "" and value[1] == ""):
                continue
            model = get_model_type(key)
            if value[0] != "" and value[1] == "":
                base_query = base_query.filter(getattr(model, key) >= value[0])
            elif value[1] != "" and value[0] == "":
                base_query = base_query.filter(getattr(model, key) <= value[1])
            else:
                base_query = base_query.filter(
                    getattr(model, key).between(value[0], value[1])
                )
    return base_query
