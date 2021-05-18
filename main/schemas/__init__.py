from marshmallow import Schema, pre_load


class BaseSchema(Schema):
    @pre_load
    def strip_input(self, data, **__):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = data[key].strip()
        return data
