#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.namedto import NameDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class MeetingTagClient:
    """
    API methods related to MeetingTag
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def replace_meeting_tags(self, meetingId: str, body: List[NameDto]) -> AstroResult[List[TaskTagDto]]:
        """
        Replaces the existing tags on a Meeting with a newly provided
        list. A tag is a connection between a Meeting and a Tag. Each
        Meeting can have zero, one or many tags.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : List[NameDto]
            The replacement list of tags for this Meeting
        """
        path = f"/api/data/meetings/{meetingId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("POST", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def add_tags_to_meeting(self, meetingId: str, body: List[NameDto]) -> AstroResult[List[TaskTagDto]]:
        """
        Add one or more tags to a Meeting.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : List[NameDto]
            The tags to add
        """
        path = f"/api/data/meetings/{meetingId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("PUT", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_tags_from_meeting(self, meetingId: str, body: List[NameDto]) -> AstroResult[object]:
        """
        Removes one or more tags from a Meeting.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : List[NameDto]
            The tags to remove
        """
        path = f"/api/data/meetings/{meetingId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("DELETE", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_tags_for_a_meeting(self, meetingId: str) -> AstroResult[List[TaskTagDto]]:
        """
        Returns the list of tags assigned to the specified Meeting.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        """
        path = f"/api/data/meetings/{meetingId}/tags"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
