# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from linebot.module.models.module_bot import ModuleBot

class GetModulesResponse(BaseModel):
    """
    List of bots to which the module is attached
    https://developers.line.biz/en/reference/partner-docs/#get-multiple-bot-info-api
    """
    bots: conlist(ModuleBot) = Field(..., description="Array of Bot list Item objects representing basic information about the bot.")
    next: Optional[StrictStr] = Field(None, description="Continuation token. Used to get the next array of basic bot information. This property is only returned if there are more unreturned results. ")

    __properties = ["bots", "next"]

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
    def from_json(cls, json_str: str) -> GetModulesResponse:
        """Create an instance of GetModulesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bots (list)
        _items = []
        if self.bots:
            for _item in self.bots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bots'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetModulesResponse:
        """Create an instance of GetModulesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetModulesResponse.parse_obj(obj)

        _obj = GetModulesResponse.parse_obj({
            "bots": [ModuleBot.from_dict(_item) for _item in obj.get("bots")] if obj.get("bots") is not None else None,
            "next": obj.get("next")
        })
        return _obj

