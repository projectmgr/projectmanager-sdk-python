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
class FileDto:
    """
    Represents a file in project manager
    """

    id: str | None = None
    """
    The identifier for this file
    """

    projectId: str | None = None
    """
    If specified this file belongs to a project. The value is the id of
    this project
    """

    taskId: str | None = None
    """
    If specified, the file has been associated with this task.
    """

    ownerId: str | None = None
    """
    The reference for who uploaded the file
    """

    createdDate: str | None = None
    """
    The UTC time the file was created.
    """

    folderId: str | None = None
    """
    A reference to the folder
    """

    fileType: str | None = None
    """
    The type of the file
    """

    fileTypeLabel: str | None = None
    """
    A user friendly label for the file type
    """

    size: int | None = None
    """
    Size of the file in bytes
    """

    downloadPath: str | None = None
    """
    Path to download the file
    """

    deleted: bool | None = None
    """
    Is the file in the trash can
    """

    type: str | None = None
    """
    Defines the object type the file belongs to.
    """

    name: str | None = None
    """
    The name of the file
    """

    entityOwnerId: str | None = None
    """
    Id of owner of parent entity
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
