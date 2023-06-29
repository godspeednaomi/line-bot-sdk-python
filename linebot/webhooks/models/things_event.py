# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from linebot.webhooks.models.delivery_context import DeliveryContext
from linebot.webhooks.models.event import Event
from linebot.webhooks.models.event_mode import EventMode
from linebot.webhooks.models.source import Source
from linebot.webhooks.models.things_content import ThingsContent

class ThingsEvent(Event):
    """
    Indicates that a user linked a device with LINE.
    """
    reply_token: StrictStr = Field(..., alias="replyToken", description="Reply token used to send reply message to this event")
    things: ThingsContent = Field(...)
    type: str = "things"

    __properties = ["type", "source", "timestamp", "mode", "webhookEventId", "deliveryContext", "replyToken", "things"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ThingsEvent:
        """Create an instance of ThingsEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_context
        if self.delivery_context:
            _dict['deliveryContext'] = self.delivery_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of things
        if self.things:
            _dict['things'] = self.things.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ThingsEvent:
        """Create an instance of ThingsEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ThingsEvent.parse_obj(obj)

        _obj = ThingsEvent.parse_obj({
            "type": obj.get("type"),
            "source": Source.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "timestamp": obj.get("timestamp"),
            "mode": obj.get("mode"),
            "webhook_event_id": obj.get("webhookEventId"),
            "delivery_context": DeliveryContext.from_dict(obj.get("deliveryContext")) if obj.get("deliveryContext") is not None else None,
            "reply_token": obj.get("replyToken"),
            "things": ThingsContent.from_dict(obj.get("things")) if obj.get("things") is not None else None
        })
        return _obj

