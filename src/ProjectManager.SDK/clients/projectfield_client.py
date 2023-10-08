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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models. import 
from ProjectManager.SDK.models.createprojectfielddto import CreateProjectFieldDto
from ProjectManager.SDK.models.createprojectfieldresponsedto import CreateProjectFieldResponseDto
from ProjectManager.SDK.models.deleteprojectfielddto import DeleteProjectFieldDto
from ProjectManager.SDK.models.getprojectfieldsresponsedtolist import GetProjectFieldsResponseDtoList
from ProjectManager.SDK.models.updateprojectfieldvaluedto import UpdateProjectFieldValueDto

class ProjectFieldClient:
    """
    API methods related to ProjectField
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_fields(self, ) -> AstroResult[AstroResult[GetProjectFieldsResponseDtoList]]:
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
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), GetProjectFieldsResponseDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_project_field(self, body: CreateProjectFieldDto) -> AstroResult[AstroResult[CreateProjectFieldResponseDto]]:
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
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), CreateProjectFieldResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_project_field(self, body: DeleteProjectFieldDto) -> AstroResult[AstroResult[]]:
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
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_project_field(self, projectId: str, fieldId: str, body: UpdateProjectFieldValueDto) -> AstroResult[AstroResult[]]:
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
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
