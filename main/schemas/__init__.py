from marshmallow import Schema, pre_load


class BaseSchema(Schema):
    @pre_load
    def strip_input(self, data, **__):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip().lower()
        return data
