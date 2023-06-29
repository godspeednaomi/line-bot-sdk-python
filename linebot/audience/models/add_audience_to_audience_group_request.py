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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from linebot.audience.models.audience import Audience

class AddAudienceToAudienceGroupRequest(BaseModel):
    """
    Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON)
    https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group
    """
    audience_group_id: Optional[StrictInt] = Field(None, alias="audienceGroupId", description="The audience ID.")
    upload_description: Optional[StrictStr] = Field(None, alias="uploadDescription", description="The audience's name.")
    audiences: Optional[conlist(Audience, max_items=10000)] = Field(None, description="An array of up to 10,000 user IDs or IFAs.")

    __properties = ["audienceGroupId", "uploadDescription", "audiences"]

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
    def from_json(cls, json_str: str) -> AddAudienceToAudienceGroupRequest:
        """Create an instance of AddAudienceToAudienceGroupRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in audiences (list)
        _items = []
        if self.audiences:
            for _item in self.audiences:
                if _item:
                    _items.append(_item.to_dict())
            _dict['audiences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddAudienceToAudienceGroupRequest:
        """Create an instance of AddAudienceToAudienceGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddAudienceToAudienceGroupRequest.parse_obj(obj)

        _obj = AddAudienceToAudienceGroupRequest.parse_obj({
            "audience_group_id": obj.get("audienceGroupId"),
            "upload_description": obj.get("uploadDescription"),
            "audiences": [Audience.from_dict(_item) for _item in obj.get("audiences")] if obj.get("audiences") is not None else None
        })
        return _obj

