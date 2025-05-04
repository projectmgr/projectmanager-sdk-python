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
class ProjectWorkingDaysDto:
    """
    Indicate which days of the week are considered working days for this
    project. This value can be set when the project is created but may
    not be updated afterwards.
    """

    monday: bool | None = None
    """
    Set this value to true if Monday is considered a working day for
    this project.
    """

    tuesday: bool | None = None
    """
    Set this value to true if Tuesday is considered a working day for
    this project.
    """

    wednesday: bool | None = None
    """
    Set this value to true if Wednesday is considered a working day for
    this project.
    """

    thursday: bool | None = None
    """
    Set this value to true if Thursday is considered a working day for
    this project.
    """

    friday: bool | None = None
    """
    Set this value to true if Friday is considered a working day for
    this project.
    """

    saturday: bool | None = None
    """
    Set this value to true if Saturday is considered a working day for
    this project.
    """

    sunday: bool | None = None
    """
    Set this value to true if Sunday is considered a working day for
    this project.
    """


