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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from linebot.messaging.models.action import Action
from linebot.messaging.models.flex_component import FlexComponent

class FlexButton(FlexComponent):
    """
    FlexButton
    """
    flex: Optional[StrictInt] = None
    color: Optional[StrictStr] = None
    style: Optional[StrictStr] = None
    action: Optional[Action] = None
    gravity: Optional[StrictStr] = None
    margin: Optional[StrictStr] = None
    position: Optional[StrictStr] = None
    offset_top: Optional[StrictStr] = Field(None, alias="offsetTop")
    offset_bottom: Optional[StrictStr] = Field(None, alias="offsetBottom")
    offset_start: Optional[StrictStr] = Field(None, alias="offsetStart")
    offset_end: Optional[StrictStr] = Field(None, alias="offsetEnd")
    height: Optional[StrictStr] = None
    adjust_mode: Optional[StrictStr] = Field(None, alias="adjustMode")
    type: str = "button"

    __properties = ["type", "flex", "color", "style", "action", "gravity", "margin", "position", "offsetTop", "offsetBottom", "offsetStart", "offsetEnd", "height", "adjustMode"]

    @validator('style')
    def style_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('primary', 'secondary', 'link'):
            raise ValueError("must be one of enum values ('primary', 'secondary', 'link')")
        return value

    @validator('gravity')
    def gravity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('top', 'bottom', 'center'):
            raise ValueError("must be one of enum values ('top', 'bottom', 'center')")
        return value

    @validator('position')
    def position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('relative', 'absolute'):
            raise ValueError("must be one of enum values ('relative', 'absolute')")
        return value

    @validator('height')
    def height_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('md', 'sm'):
            raise ValueError("must be one of enum values ('md', 'sm')")
        return value

    @validator('adjust_mode')
    def adjust_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('shrink-to-fit'):
            raise ValueError("must be one of enum values ('shrink-to-fit')")
        return value

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
    def from_json(cls, json_str: str) -> FlexButton:
        """Create an instance of FlexButton from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexButton:
        """Create an instance of FlexButton from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexButton.parse_obj(obj)

        _obj = FlexButton.parse_obj({
            "type": obj.get("type"),
            "flex": obj.get("flex"),
            "color": obj.get("color"),
            "style": obj.get("style"),
            "action": Action.from_dict(obj.get("action")) if obj.get("action") is not None else None,
            "gravity": obj.get("gravity"),
            "margin": obj.get("margin"),
            "position": obj.get("position"),
            "offset_top": obj.get("offsetTop"),
            "offset_bottom": obj.get("offsetBottom"),
            "offset_start": obj.get("offsetStart"),
            "offset_end": obj.get("offsetEnd"),
            "height": obj.get("height"),
            "adjust_mode": obj.get("adjustMode")
        })
        return _obj

