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
class RecurringTaskSettingsDto:
    """
    Recurring settings for a task
    """

    type: int | None = None
    """
    Type
    """

    repeatEvery: int | None = None
    """
    RepeatEvery
    """

    repeatOn: List[int] | None = None
    """
    RepeatOn
    """

    repeatOn2Level: int | None = None
    """
    RepeatOn2Level
    """

    endsOn: str | None = None
    """
    EndsOn
    """

    endsAfter: int | None = None
    """
    EndsAfter
    """


