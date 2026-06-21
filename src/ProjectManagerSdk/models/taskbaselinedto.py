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
class TaskBaselineDto:
    """
    Baseline schedule and cost values captured for a Task when a project
    baseline is set.
    """

    id: str | None = None
    """
    The unique identifier of this baseline record.
    """

    number: int | None = None
    """
    The baseline number for this Task.
    """

    duration: int | None = None
    """
    The baselined duration (in minutes) for this Task.
    """

    effort: int | None = None
    """
    The baselined effort (in minutes) for this Task.
    """

    start: str | None = None
    """
    The baselined start date for this Task.
    """

    finish: str | None = None
    """
    The baselined finish date for this Task.
    """

    cost: float | None = None
    """
    The baselined cost for this Task.
    """

    durationFormat: str | None = None
    """
    The duration format for this baseline value.
    """

    effortFormat: str | None = None
    """
    The effort format for this baseline value.
    """


