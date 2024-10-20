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


from typing import List
import dataclasses

@dataclasses.dataclass
class IntegrationInstanceDto:
    """
    The Integrations API is intended for use by ProjectManager and its
    business development partners. Please contact ProjectManager's sales
    team to request use of this API.
    """

    id: str | None = None
    """
    The unique identifier of this IntegrationInstance
    """

    integrationShortId: str | None = None
    """
    A short ID that uniquely identifies this IntegrationInstance
    """

    enabledBy: str | None = None
    """
    The unique identifier of the user who enabled this
    IntegrationInstance
    """

    createDate: str | None = None
    """
    Timestamp when this record was created
    """

    modifyDate: str | None = None
    """
    Timestamp when this record was most recently modified
    """

    projectId: str | None = None
    """
    The id of the project manager project this instance is related to
    """

    providerItemId: str | None = None
    """
    The identifier in the integration provider, could be a reference to
    a file, task, project.
    """

    providerItemName: str | None = None
    """
    The name of the item in the integration provider.
    """


