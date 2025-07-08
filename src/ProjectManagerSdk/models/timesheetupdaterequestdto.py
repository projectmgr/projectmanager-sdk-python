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
class TimesheetUpdateRequestDto:
    """
    Payload to update time entry
    """

    hours: float | None = None
    """
    Reported hours. If minutes is specified this property is ignored
    """

    minutes: int | None = None
    """
    Specify the time in minutes. This overrides the Hours property.
    """

    notes: str | None = None
    """
    Notes
    """

    documentIds: List[str] | None = None
    """
    Document Ids
    """


