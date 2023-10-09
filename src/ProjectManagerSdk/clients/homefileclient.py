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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.filedto import FileDto
import json

class HomeFileClient:
    """
    API methods related to HomeFile
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def upload_home_file(self, filename: str) -> AstroResult[FileDto]:
        """
        Uploads a file to a Home folder.

        ProjectManager allows you to store Files connected to other
        elements of your Workspace such as a Project, a Task, or Home.
        Files are maintained separately based on the location where the
        file was stored.

        When you upload a File, please allow a few moments for the File
        to be processed and verified. ProjectManager may reject File
        uploads that contain problems such as malware. Once a File has
        completed the upload the process, you may retrieve it using the
        DownloadFile API.

        Parameters
        ----------
        filename : str
            The full path of a file to upload to the API
        """
        path = "/api/data/home/files"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, filename)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[FileDto](None, True, False, result.status_code, FileDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[FileDto](result.json(), False, True, result.status_code, None)

    def upload_home_file_to_folder(self, folderId: str, filename: str) -> AstroResult[FileDto]:
        """
        Uploads a file to a home folder.

        ProjectManager allows you to store Files connected to other
        elements of your Workspace such as a Project, a Task, or Home.
        Files are maintained separately based on the location where the
        file was stored.

        When you upload a File, please allow a few moments for the File
        to be processed and verified. ProjectManager may reject File
        uploads that contain problems such as malware. Once a File has
        completed the upload the process, you may retrieve it using the
        DownloadFile API.

        Parameters
        ----------
        folderId : str
            The reference to the sub folder to put the file into
        filename : str
            The full path of a file to upload to the API
        """
        path = f"/api/data/home/folders/{folderId}/files"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, filename)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[FileDto](None, True, False, result.status_code, FileDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[FileDto](result.json(), False, True, result.status_code, None)
