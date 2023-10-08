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


from dataclasses import dataclass

@dataclass
class IntegrationDto:
    """
    The Integrations API is intended for use by ProjectManager and its
    business development partners. Please contact ProjectManager's sales
    team to request use of this API.
    """

    id: str | None = None
    name: str | None = None
    description: str | None = None
    shortId: str | None = None
    isMultiInstance: bool | None = None
    config: object | None = None
    licenseSkus: list[str] | None = None
    instances: list[IntegrationInstanceDto] | None = None
    enabled: bool | None = None
    authenticated: bool | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
