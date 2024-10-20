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
class TimeSheetProjectDto:
    """
    A Project is a collection of Tasks that contributes towards a goal.
    Within a Project, Tasks represent individual items of work that team
    members must complete. The sum total of Tasks within a Project
    represents the work to be completed for that Project.
    """

    id: str | None = None
    """
    The unique identifier of the Project.
    """

    name: str | None = None
    """
    The name of the Project.
    """

    description: str | None = None
    """
    An optional description of the Project
    """

    shortCode: str | None = None
    """
    A shortened name that will be used when reporting on Projects. This
    short name can be edited in the Project Settings page within the
    application and can be any text you wish.
    """

    shortId: str | None = None
    """
    A short identifier that uniquely identifies this Project within your
    Workspace using a single letter followed by a number. This code can
    be used for APIs that accept Project unique identifiers. You can
    observe the short ID within the application by observing the URL of
    the page you visit when you click on this project. The page's URL
    will appear in the form `https://pm.app.projectmanager.com/project/board/D16`
    - in this example, the `ShortId` is `D16`. This code is
    automatically assigned for you and cannot be changed.
    """

    startDate: str | None = None
    """
    The earliest planned or actual start date of tasks on the project.
    This field is calculated automatically and cannot be changed.
    """

    endDate: str | None = None
    """
    The latest planned or actual finish date of tasks on the project.
    This field is calculated automatically and cannot be changed.
    """

    targetDate: str | None = None
    """
    The target planned completion date for this Project, or null if one
    has not been selected. This value can be updated in the Project
    Settings page or the Portfolio Project page within the application.
    """

    budget: float | None = None
    """
    The proposed budget for this Project.
    """

    hourlyRate: float | None = None
    """
    The default hourly rate for work on this Project. This rate will be
    used if an assignee working on this Project does not have an hourly
    rate configured in their profile.
    """

    statusUpdate: str | None = None
    """
    Contains an optional status update for Projects that can be used to
    summarize the status of multiple Projects at a glance. You can edit
    the StatusUpdate field on the Portfolio page of the application.
    """

    modifyDate: str | None = None
    """
    The timestamp in UTC when the Project was most recently modified.
    """

    createDate: str | None = None
    """
    The timestamp in UTC when the Project was created.
    """

    isTemplate: bool | None = None
    """
    True if this Project is a template that will be reused as a
    framework for future Projects.
    """


