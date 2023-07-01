from typing import get_type_hints, get_args, get_origin


def load_dataclass_from_dict(data_class, data):
    if get_origin(data_class) is list:
        # It's a List type
        return [load_dataclass_from_dict(get_args(data_class)[0], item) for item in data]
    elif get_origin(data_class) is dict:
        # It's a Dict type
        args = get_args(data_class)
        if args:  # if args is not empty, i.e., key and value types are specified
            key_type, value_type = args
            return {key_type(key): load_dataclass_from_dict(value_type, value) for key, value in data.items()}
        else:  # if args is empty, i.e., key and value types are not specified
            return data
    elif get_origin(data_class) is None:
        # It's not a higher level type like List or Dict
        if data_class in (int, str, bool):  # add more basic types if needed
            return data
        else:
            # It's a dataclass
            return data_class(**{key: load_dataclass_from_dict(value, data[key]) for key, value in get_type_hints(data_class).items() if key in data})
