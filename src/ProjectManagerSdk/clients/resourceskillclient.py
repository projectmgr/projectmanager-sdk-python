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
from ProjectManagerSdk.models.createresourceskilldto import CreateResourceSkillDto
from ProjectManagerSdk.models.resourceskilldto import ResourceSkillDto
from ProjectManagerSdk.models.updateresourceskilldto import UpdateResourceSkillDto
import json

class ResourceSkillClient:
    """
    API methods related to ResourceSkill
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_resource_skills(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[ResourceSkillDto]]:
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
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if select:
            queryParams['$select'] = select
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ResourceSkillDto(**dict))
            return AstroResult[list[ResourceSkillDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ResourceSkillDto]](result.json(), False, True, result.status_code, None)

    def create_resource_skill(self, body: CreateResourceSkillDto) -> AstroResult[ResourceSkillDto]:
        """
        Create a Resource Skill.

        Parameters
        ----------
        body : CreateResourceSkillDto
            The name of the skill to create.
        """
        path = "/api/data/resources/skills"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ResourceSkillDto](None, True, False, result.status_code, ResourceSkillDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ResourceSkillDto](result.json(), False, True, result.status_code, None)

    def update_resource_skill(self, skillId: str, body: UpdateResourceSkillDto) -> AstroResult[ResourceSkillDto]:
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
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ResourceSkillDto](None, True, False, result.status_code, ResourceSkillDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ResourceSkillDto](result.json(), False, True, result.status_code, None)

    def delete_resource_skill(self, resourceSkillId: str) -> AstroResult[object]:
        """
        The endpoint is used to delete a resource skill. Users assigned
        to this skill will no longer be assigned thereafter.

        Parameters
        ----------
        resourceSkillId : str
            The Id of the skill to be removed.
        """
        path = f"/api/data/resources/skills/{resourceSkillId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
