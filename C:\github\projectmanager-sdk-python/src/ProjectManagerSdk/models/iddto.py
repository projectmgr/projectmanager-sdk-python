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
class IdDto:
    """
    When uploading a list of unique identifiers to the API, this data
    structure represents one individual unique identifier within the
    list.
    """

    id: str | None = None
    """
    A unique identifier. To determine the meaning of this unique
    identifier, see the field to which this value is attached.
    """


