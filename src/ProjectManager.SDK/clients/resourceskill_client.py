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
from ProjectManager.SDK.models.createresourceskilldto import CreateResourceSkillDto
from ProjectManager.SDK.models.resourceskilldto import ResourceSkillDto
from ProjectManager.SDK.models.resourceskilldtolist import ResourceSkillDtoList
from ProjectManager.SDK.models.updateresourceskilldto import UpdateResourceSkillDto

class ResourceSkillClient:
    """
    API methods related to ResourceSkill
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_resource_skills(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[ResourceSkillDtoList]]:
        """
        Retrieves all ResourceSkills defined within your Workspace.

        A ResourceSkill is a capability possessed by a Resource that can
        be used to distinguish different classes of Resources suitable
        for use by a Task. You can specify that a Task requires a
        Resource with a particular set of ResourceSkills and then
        allocate Resources based on whether or not they have the
        suitable ResourceSkills.

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $select : str
            Specify which properties should be returned
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/resources/skills"
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceSkillDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_resource_skill(self, body: CreateResourceSkillDto) -> AstroResult[AstroResult[ResourceSkillDto]]:
        """
        Create a Resource Skill.

        Parameters
        ----------
        body : CreateResourceSkillDto
            The name of the skill to create.
        """
        path = "/api/data/resources/skills"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceSkillDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_resource_skill(self, skillId: str, body: UpdateResourceSkillDto) -> AstroResult[AstroResult[ResourceSkillDto]]:
        """
        Update a Resource Skill.

        Parameters
        ----------
        skillId : str
            The id of the skill to update.
        body : UpdateResourceSkillDto
            The data of the skill to update.
        """
        path = f"/api/data/resources/skills/{skillId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceSkillDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_resource_skill(self, resourceSkillId: str) -> AstroResult[AstroResult[]]:
        """
        The endpoint is used to delete a resource skill. Users assigned
        to this skill will no longer be assigned thereafter.

        Parameters
        ----------
        resourceSkillId : str
            The Id of the skill to be removed.
        """
        path = f"/api/data/resources/skills/{resourceSkillId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
