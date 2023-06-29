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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from linebot.webhooks.models.module_content import ModuleContent

class AttachedModuleContent(ModuleContent):
    """
    AttachedModuleContent
    """
    bot_id: StrictStr = Field(..., alias="botId", description="User ID of the bot on the attached LINE Official Account")
    scopes: conlist(StrictStr) = Field(..., description="An array of strings indicating the scope permitted by the admin of the LINE Official Account.")
    type: str = "attached"

    __properties = ["type", "botId", "scopes"]

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
    def from_json(cls, json_str: str) -> AttachedModuleContent:
        """Create an instance of AttachedModuleContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AttachedModuleContent:
        """Create an instance of AttachedModuleContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AttachedModuleContent.parse_obj(obj)

        _obj = AttachedModuleContent.parse_obj({
            "type": obj.get("type"),
            "bot_id": obj.get("botId"),
            "scopes": obj.get("scopes")
        })
        return _obj

