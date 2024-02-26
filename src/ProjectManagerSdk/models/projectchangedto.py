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


import dataclasses

@dataclasses.dataclass
class ProjectChangeDto:
    """
    The specific change action made against a project
    """

    id: str | None = None
    """
    Project Change ID
    """

    businessId: str | None = None
    """
    Workspace ID
    """

    projectId: str | None = None
    """
    Project ID
    """

    version: int | None = None
    """
    Version of this Project Change
    """

    createBy: str | None = None
    """
    Created by GUID
    """

    createDate: str | None = None
    """
    Created date
    """

    processDate: str | None = None
    """
    Processed date
    """

    status: int | None = None
    """
    The status of the Project Change
    """

    changeData: object | None = None
    """
    Project Change as JSON data
    """


