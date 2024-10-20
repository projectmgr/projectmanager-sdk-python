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
from ProjectManagerSdk.models.projecttemplatecategorydto import ProjectTemplateCategoryDto
from ProjectManagerSdk.models.projecttemplatedto import ProjectTemplateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectTemplateClient:
    """
    API methods related to ProjectTemplate
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_templates(self) -> AstroResult[List[ProjectTemplateDto]]:
        """
        Retrieves all ProjectTemplates defined in the system. A
        ProjectTemplate is a definition of default project related data
        (eg. Tasks) that can be applied to a new project when it is
        created. ProjectTemplates are categorized using the
        TemplateCategory system.

        Parameters
        ----------
        """
        path = "/api/data/projects/templates"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectTemplateDto, data=dict))
            return AstroResult[List[ProjectTemplateDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectTemplateDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_template_categories(self) -> AstroResult[List[ProjectTemplateCategoryDto]]:
        """
        Retrieves all ProjectTemplate Categories defined in the system.
        A ProjectTemplate is a definition of default project related
        data (eg. Tasks) that can be applied to a new project when it is
        created. ProjectTemplates are categorized using the
        TemplateCategory system.

        Parameters
        ----------
        """
        path = "/api/data/projects/templates/categories"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectTemplateCategoryDto, data=dict))
            return AstroResult[List[ProjectTemplateCategoryDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectTemplateCategoryDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
