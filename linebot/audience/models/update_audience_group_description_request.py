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
from pydantic import BaseModel, Field, constr

class UpdateAudienceGroupDescriptionRequest(BaseModel):
    """
    Rename an audience
    https://developers.line.biz/en/reference/messaging-api/#set-description-audience-group
    """
    description: Optional[constr(strict=True, max_length=120, min_length=1)] = Field(None, description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")

    __properties = ["description"]

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
    def from_json(cls, json_str: str) -> UpdateAudienceGroupDescriptionRequest:
        """Create an instance of UpdateAudienceGroupDescriptionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateAudienceGroupDescriptionRequest:
        """Create an instance of UpdateAudienceGroupDescriptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateAudienceGroupDescriptionRequest.parse_obj(obj)

        _obj = UpdateAudienceGroupDescriptionRequest.parse_obj({
            "description": obj.get("description")
        })
        return _obj

