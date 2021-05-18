from marshmallow import Schema, fields
from marshmallow.validate import Length

from main.schemas import BaseSchema


class PredictSentimentSchema(BaseSchema):
    text = fields.String(required=True, validate=Length(min=1, max=256))
    language = fields.String()


class PredictionResultSchema(Schema):
    sentiment = fields.Integer()
    confidence = fields.Float()
