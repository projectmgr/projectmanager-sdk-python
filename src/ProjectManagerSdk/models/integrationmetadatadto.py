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


from typing import List
import dataclasses

@dataclasses.dataclass
class IntegrationMetadataDto:
    """
    A key-value pair of metadata stored against an Integration. Values
    are stored as comma-separated strings to support multiple values
    (e.g. a list of IDs, names, or reference values).
    """

    key: str | None = None
    """
    The metadata key (e.g. "ProjectStatus").
    """

    value: str | None = None
    """
    The metadata value, stored as a comma-separated string to support
    multiple values.
    """


