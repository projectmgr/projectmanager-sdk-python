#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.createprojectfielddto import CreateProjectFieldDto
from ProjectManagerSdk.models.createprojectfieldresponsedto import CreateProjectFieldResponseDto
from ProjectManagerSdk.models.getprojectfieldsresponsedto import GetProjectFieldsResponseDto
from ProjectManagerSdk.models.projectfieldsvalueresponsedto import ProjectFieldsValueResponseDto
from ProjectManagerSdk.models.updateprojectfieldvaluedto import UpdateProjectFieldValueDto
import json

class ProjectFieldClient:
    """
    API methods related to ProjectField
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_fields(self) -> AstroResult[list[GetProjectFieldsResponseDto]]:
        """
        Retrieves all ProjectFields defined within your Workspace.

        A ProjectField is a custom field defined within your Workspace.
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
                data.append(GetProjectFieldsResponseDto(**dict))
            return AstroResult[list[GetProjectFieldsResponseDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[GetProjectFieldsResponseDto]](result.json(), False, True, result.status_code, None)

    def create_project_field(self, body: CreateProjectFieldDto) -> AstroResult[CreateProjectFieldResponseDto]:
        """
        Creates a new ProjectField within your Workspace.

        A ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

        Parameters
        ----------
        body : CreateProjectFieldDto
            Information about the ProjectField to create
        """
        path = "/api/data/projects/fields"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[CreateProjectFieldResponseDto](None, True, False, result.status_code, CreateProjectFieldResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[CreateProjectFieldResponseDto](result.json(), False, True, result.status_code, None)

    def delete_project_field(self, fieldId: str) -> AstroResult[object]:
        """
        Deletes an existing ProjectField within your Workspace.

        A ProjectField is a custom field defined within your Workspace.
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
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def update_projectfield_value(self, projectId: str, fieldId: str, body: UpdateProjectFieldValueDto) -> AstroResult[object]:
        """
        Replaces the current value of a ProjectField for a specific
        Project within your Workspace.

        A ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

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
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def retrieve_projectfield_value(self, projectId: str, fieldId: str) -> AstroResult[ProjectFieldsValueResponseDto]:
        """
        Retrieves the current ProjectField value for a particular
        Project and ProjectField.

        A ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

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
            return AstroResult[ProjectFieldsValueResponseDto](None, True, False, result.status_code, ProjectFieldsValueResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectFieldsValueResponseDto](result.json(), False, True, result.status_code, None)

    def retrieve_all_projectfield_values(self, projectId: str) -> AstroResult[list[ProjectFieldsValueResponseDto]]:
        """
        Retrieves all ProjectField values for a particular Project.

        A ProjectField is a custom field defined within your Workspace.
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
                data.append(ProjectFieldsValueResponseDto(**dict))
            return AstroResult[list[ProjectFieldsValueResponseDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectFieldsValueResponseDto]](result.json(), False, True, result.status_code, None)
