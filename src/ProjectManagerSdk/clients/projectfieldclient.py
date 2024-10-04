#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.projectfieldcreatedto import ProjectFieldCreateDto
from ProjectManagerSdk.models.projectfielddto import ProjectFieldDto
from ProjectManagerSdk.models.projectfieldvaluedto import ProjectFieldValueDto
from ProjectManagerSdk.models.updateprojectfieldvaluedto import UpdateProjectFieldValueDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectFieldClient:
    """
    API methods related to ProjectField
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_fields(self) -> AstroResult[List[ProjectFieldDto]]:
        """
        Retrieves all ProjectFields defined within your Workspace. A
        ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

        Parameters
        ----------
        """
        path = "/api/data/projects/fields"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectFieldDto, data=dict))
            return AstroResult[List[ProjectFieldDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectFieldDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_project_field(self, body: ProjectFieldCreateDto) -> AstroResult[ProjectFieldDto]:
        """
        Creates a new ProjectField within your Workspace. A ProjectField
        is a custom field defined within your Workspace. You can define
        ProjectFields for any integration purpose that is important to
        your business. Each ProjectField has a data type as well as
        options in how it is handled. ProjectFields can be edited for
        each Project within your Workspace.

        Parameters
        ----------
        body : ProjectFieldCreateDto
            Information about the ProjectField to create
        """
        path = "/api/data/projects/fields"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectFieldDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectFieldDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectFieldDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_project_field(self, fieldId: str) -> AstroResult[object]:
        """
        Deletes an existing ProjectField within your Workspace. A
        ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

        Parameters
        ----------
        fieldId : str
            The unique identifier or short ID of this ProjectField
        """
        path = f"/api/data/projects/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_projectfield_value(self, projectId: str, fieldId: str, body: UpdateProjectFieldValueDto) -> AstroResult[object]:
        """
        Replaces the current value of a ProjectField for a specific
        Project within your Workspace. A ProjectField is a custom field
        defined within your Workspace. You can define ProjectFields for
        any integration purpose that is important to your business. Each
        ProjectField has a data type as well as options in how it is
        handled. ProjectFields can be edited for each Project within
        your Workspace.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that contains this
            ProjectField
        fieldId : str
            The unique identifier or short ID of this ProjectField
        body : UpdateProjectFieldValueDto
            The new information for this ProjectField
        """
        path = f"/api/data/projects/{projectId}/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_projectfield_value(self, projectId: str, fieldId: str) -> AstroResult[ProjectFieldValueDto]:
        """
        Retrieves the current ProjectField value for a particular
        Project and ProjectField. A ProjectField is a custom field
        defined within your Workspace. You can define ProjectFields for
        any integration purpose that is important to your business. Each
        ProjectField has a data type as well as options in how it is
        handled. ProjectFields can be edited for each Project within
        your Workspace.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project of the value to
            retrieve
        fieldId : str
            The unique identifier or short ID of the ProjectField of the
            value to retrieve
        """
        path = f"/api/data/projects/{projectId}/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectFieldValueDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectFieldValueDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectFieldValueDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_all_projectfield_values(self, projectId: str) -> AstroResult[List[ProjectFieldValueDto]]:
        """
        Retrieves all ProjectField values for a particular Project. A
        ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project for which we want
            ProjectField values
        """
        path = f"/api/data/projects/{projectId}/fields"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectFieldValueDto, data=dict))
            return AstroResult[List[ProjectFieldValueDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectFieldValueDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
