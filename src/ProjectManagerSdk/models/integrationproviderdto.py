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


from ProjectManagerSdk.models.integrationdto import IntegrationDto
from dataclasses import dataclass

@dataclass
class IntegrationProviderDto:
    """
    The Integrations API is intended for use by ProjectManager and its
    business development partners. Please contact ProjectManager's sales
    team to request use of this API.
    """

    id: str | None = None
    """
    The unique identifier of this Provider.
    """

    name: str | None = None
    """
    The friendly name of this Provider.
    """

    shortId: str | None = None
    """
    A short ID that uniquely identifies this Provider.
    """

    summary: str | None = None
    """
    A short summary of this Provider and their service.
    """

    description: str | None = None
    """
    A longer description of this Provider and their service.
    """

    licenseSkus: list[str] | None = None
    """
    A list of available license SKUs for this Provider.
    """

    categoryShortIds: list[str] | None = None
    """
    A list of category IDs that this Provider exists within.
    """

    activated: bool | None = None
    """
    True if this Provider is available for use.
    """

    authenticated: bool | None = None
    """
    True if this Provider requires authentication.
    """

    integrations: list[IntegrationDto] | None = None
    """
    The list of available Integrations for this Provider.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
