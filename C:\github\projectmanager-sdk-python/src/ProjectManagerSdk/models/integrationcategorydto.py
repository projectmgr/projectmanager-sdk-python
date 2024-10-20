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
class IntegrationCategoryDto:
    """
    Information about a category of Integrations available on the
    Marketplace.
    """

    id: str | None = None
    """
    The unique identifier of this Integration Category.
    """

    name: str | None = None
    """
    A friendly name for this Integration Category.
    """

    shortId: str | None = None
    """
    A short identifier that uniquely identifies this Integration
    Category.
    """

    integrationShortIds: List[str] | None = None
    """
    A list of short identifiers for Integrations available within this
    Integration Category.
    """


