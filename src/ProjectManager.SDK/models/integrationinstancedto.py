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

    config: object | None = None
    """
    Metadata for this IntegrationInstance
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


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
