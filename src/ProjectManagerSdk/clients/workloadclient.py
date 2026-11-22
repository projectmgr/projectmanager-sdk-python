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
from ProjectManagerSdk.models.resourceworkloadallocationdto import ResourceWorkloadAllocationDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class WorkloadClient:
    """
    API methods related to Workload
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_resource_workload(self, resourceId: str, filter: str, sort: str, include: str, page: int, pageSize: int) -> AstroResult[List[ResourceWorkloadAllocationDto]]:
        """
        Retrieve information about the expected workload for a Resource.
        The workload for a Resource is a list of tasks, days, and the
        amount of time spent on each task per day. You can examine a
        Resource's workload to identify when that Resource is required
        to contribute to specific tasks. To query for workload for a
        Resource, you must first know the unique identifier of the
        Resource. You may use the QueryResource API to identify the
        resource, and then use its `id` field to call
        `QueryResourceWorkload`. Workload is defined in two ways: either
        automatically by the ProjectManager.com system, or manually by
        editing the workload page within the ProjectManager.com app.
        When you query for workload information, each entry will specify
        whether the assignment was created manually or via the system.
        If a task does not have any workload allocated, it will not be
        returned by this API. The `QueryResourceWorkload` API uses
        Gridify-style querying. For a full description of query rules,
        see [Querying Tutorial](https://developer.projectmanager.com/getting-started/querying-tutorial).
        When querying for workload, you can use filters, sorting,
        pagination, and you can also request additional data to be
        included in the API result. The QueryResourceWorkload API
        returns a maximum of 1000 results per request as a single page.
        To retrieve all workload for a Resource, you must fetch pages
        starting with the number 1 until no additional data is returned.

        Parameters
        ----------
        resourceId : str
            The id of the Resource
        filter : str
            A Gridify formatted filter used to search by
            `task.projectId` and/or `date` and/or `minutes`
        sort : str
            A Gridify formatted ordering used to sort by `date`,
            `task.name` and/or `createdDate`. Defaults to `date asc`.
        include : str
            A comma separated list of additional data to include in each
            result. Set to `task` to include basic Task details, and/or
            `assignment` to include the assignment's total assigned
            minutes.
        page : int
            The page number to retrieve, starting at 1. Defaults to 1.
            Pages over individual allocations.
        pageSize : int
            The number of allocations, no less than 1 or more than 1000,
            per page. Defaults to 1000.
        """
        path = f"/api/data/workload/resources/{resourceId}"
        queryParams = {}
        if filter:
            queryParams['filter'] = filter
        if sort:
            queryParams['sort'] = sort
        if include:
            queryParams['include'] = include
        if page:
            queryParams['page'] = page
        if pageSize:
            queryParams['pageSize'] = pageSize
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ResourceWorkloadAllocationDto, data=dict))
            return AstroResult[List[ResourceWorkloadAllocationDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ResourceWorkloadAllocationDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
