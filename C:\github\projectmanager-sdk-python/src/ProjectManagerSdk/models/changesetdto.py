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
class ChangeSetDto:
    """
    The project task change set
    """

    projectChangeSetId: int | None = None
    """
    Project Changeset ID
    """

    id: str | None = None
    """
    The unique identifier of this Changeset
    """

    projectId: str | None = None
    """
    Project ID
    """

    version: int | None = None
    """
    Task version
    """

    createBy: str | None = None
    """
    Created by GUID
    """

    createDate: str | None = None
    """
    Created date
    """

    actions: str | None = None
    """
    Change set action
    """

    changeSets: str | None = None
    """
    Change set in json string
    """

    processDate: str | None = None
    """
    Processed date
    """

    success: bool | None = None
    """
    If process was successful
    """

    exception: str | None = None
    """
    Error message
    """

    clientId: str | None = None
    """
    UI ID
    """

    jsonData: str | None = None
    """
    Changeset JSON data
    """

    isUndo: bool | None = None
    """
    Is change set from UNDO
    """

    state: int | None = None
    """
    The state of the changeset
    """

    businessId: str | None = None
    """
    Business ID
    """


