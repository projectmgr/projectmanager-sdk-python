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
from ProjectManagerSdk.models.meetingcreatedto import MeetingCreateDto
from ProjectManagerSdk.models.meetingdetailsdto import MeetingDetailsDto
from ProjectManagerSdk.models.meetingdto import MeetingDto
from ProjectManagerSdk.models.meetingupdatedto import MeetingUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class MeetingsClient:
    """
    API methods related to Meetings
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_meetings(self, projectId: str) -> AstroResult[List[MeetingDto]]:
        """
        Retrieve a list of Meetings. This endpoint does not use OData.
        If `projectId` is provided, results are limited to that Project.

        Parameters
        ----------
        projectId : str
            Optional project id to scope results
        """
        path = "/api/data/meetings"
        queryParams = {}
        if projectId:
            queryParams['projectId'] = projectId
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=MeetingDto, data=dict))
            return AstroResult[List[MeetingDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[MeetingDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_meeting(self, body: MeetingCreateDto) -> AstroResult[MeetingDto]:
        """
        Creates a new Meeting for the current user. If you specify an
        assignee for this Meeting, that user will be assigned to it. If
        you do not specify an assignee, the Meeting will be
        automatically assigned to you.

        Parameters
        ----------
        body : MeetingCreateDto
            The data used to create the Meeting
        """
        path = "/api/data/meetings"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def get_meeting(self, meetingId: str) -> AstroResult[MeetingDetailsDto]:
        """
        Retrieve a Meeting by its unique identifier or by its short ID.
        A Meeting has both a unique identifier, which is a GUID, and a
        short ID, which is a small text label that is unique only within
        your Workspace.

        Parameters
        ----------
        meetingId : str
            the id of the meeting
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDetailsDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDetailsDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDetailsDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_meeting(self, meetingId: str, body: MeetingUpdateDto) -> AstroResult[MeetingDto]:
        """
        Updates a Meeting by its unique identifier, which is a GUID.

        Parameters
        ----------
        meetingId : str
            the id of the meeting
        body : MeetingUpdateDto
            the fields to update
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_meeting(self, meetingId: str) -> AstroResult[object]:
        """
        Removes a Meeting by its unique identifier, which is a GUID.

        Parameters
        ----------
        meetingId : str
            the id of the meeting to remove
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
