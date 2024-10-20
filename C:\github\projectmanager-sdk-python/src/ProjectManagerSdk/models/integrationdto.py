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


from ProjectManagerSdk.models.integrationinstancedto import IntegrationInstanceDto
from typing import List
import dataclasses

@dataclasses.dataclass
class IntegrationDto:
    """
    The Integrations API is intended for use by ProjectManager and its
    business development partners. Please contact ProjectManager's sales
    team to request use of this API.
    """

    id: str | None = None
    """
    The unique identifier of this Integration
    """

    name: str | None = None
    """
    The friendly name of this Integration
    """

    description: str | None = None
    """
    A description of this Integration that can be shared with users
    """

    shortId: str | None = None
    """
    A short ID that uniquely identifies this Integration
    """

    isMultiInstance: bool | None = None
    """
    True if this Integration allows multiple Instances. An example of a
    multi-Instance Integration is one that can be connected to many
    different folders or channels within a remote application.
    """

    config: object | None = None
    """
    Extra configuration metadata for this Instance.
    """

    licenseSkus: List[str] | None = None
    """
    The list of SKUS for this Integration.
    """

    instances: List[IntegrationInstanceDto] | None = None
    """
    For multi-Instance Integrations, this contains the list of
    IntegrationInstances.
    """

    enabled: bool | None = None
    """
    True if this Integration is enabled for the current Workspace.
    """

    authenticated: bool | None = None
    """
    True if the user has authenticated
    """

    autoEnabled: bool | None = None
    """
    True if the integration is auto-enabled
    """

    noAdminPermission: bool | None = None
    """
    No Admin Permission
    """


