from marshmallow import Schema, fields
from marshmallow.validate import Length


class PredictSentimentSchema(Schema):
    text = fields.String(required=True, validate=Length(max=256))
    language = fields.String()


class PredictionResultSchema(Schema):
    sentiment = fields.Integer()
    confidence = fields.Float()
