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

from models.astroresult import AstroResult
from models.createprojectfielddto import CreateProjectFieldDto
from models.createprojectfieldresponsedto import CreateProjectFieldResponseDto
from models.deleteprojectfielddto import DeleteProjectFieldDto
from models.getprojectfieldsresponsedto import GetProjectFieldsResponseDto
from models.updateprojectfieldvaluedto import UpdateProjectFieldValueDto
import json

class ProjectFieldClient:
    """
    API methods related to ProjectField
    """
    from projectmanagerclient import ProjectManagerClient

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
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[GetProjectFieldsResponseDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, CreateProjectFieldResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def delete_project_field(self, body: DeleteProjectFieldDto) -> AstroResult[object]:
        """
        Deletes an existing ProjectField within your Workspace.

        A ProjectField is a custom field defined within your Workspace.
        You can define ProjectFields for any integration purpose that is
        important to your business. Each ProjectField has a data type as
        well as options in how it is handled. ProjectFields can be
        edited for each Project within your Workspace.

        Parameters
        ----------
        body : DeleteProjectFieldDto
            The identity of the ProjectField to delete
        """
        path = "/api/data/projects/fields"
        result = self.client.send_request("DELETE", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def update_project_field(self, projectId: str, fieldId: str, body: UpdateProjectFieldValueDto) -> AstroResult[object]:
        """
        Updates an existing ProjectField with new information.

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
            The unique identifier of this ProjectField
        body : UpdateProjectFieldValueDto
            The new information for this ProjectField
        """
        path = f"/api/data/projects/{projectId}/fields/{fieldId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
