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
class TimesheetFileResponseDto:
    """
    Represents a document or file attached to a timesheet day entry.
    """

    id: str | None = None
    """
    The unique identifier of the document.
    """

    name: str | None = None
    """
    The name of the file (including extension).
    """

    url: str | None = None
    """
    The download or access URL for the file.
    """

    fileType: str | None = None
    """
    The file type or extension (e.g., "pdf", "png").
    """

    fileTypeLabel: str | None = None
    """
    A user-friendly label describing the file type (e.g., "PDF
    Document").
    """

    date: str | None = None
    """
    The date and time the file was uploaded or created.
    """

    size: int | None = None
    """
    The size of the file in bytes.
    """

    projectId: str | None = None
    """
    The ID of the project associated with the file.
    """

    projectType: str | None = None
    """
    The type of project (e.g., "project", "admin").
    """

    taskId: str | None = None
    """
    The ID of the task this file is associated with, if any.
    """

    newFilename: str | None = None
    """
    A new file name for the document, if renamed.
    """

    canRead: bool | None = None
    """
    Whether other users can read the document.
    """

    thumbnailUrl: str | None = None
    """
    A thumbnail URL for previewing the file (if applicable).
    """

    externalId: str | None = None
    """
    An optional external provider ID (e.g., for integrations).
    """

    canDelete: bool | None = None
    """
    Indicates whether the current user has permission to delete the
    file.
    """

    isLocked: bool | None = None
    """
    Indicates whether the file is locked and cannot be modified.
    """

    type: str | None = None
    """
    The object type identifier used by the frontend
    ("pm.models.Document").
    """

    dirty: bool | None = None
    """
    Indicates whether the document has unsaved changes (used by frontend
    only).
    """

    deleted: bool | None = None
    """
    Indicates whether the document is marked for deletion (used by
    frontend only).
    """

    isNew: bool | None = None
    """
    Indicates whether the document is newly added (used by frontend
    only).
    """


