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
from ProjectManagerSdk.models.updaterequestdto import UpdateRequestDto
import json

class FileClient:
    """
    API methods related to File
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def download_file(self, documentId: str, type: str) -> AstroResult[object]:
        """
        Downloads the contents of a file that was previously uploaded to
        ProjectManager.com.

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
        documentId : str
            The unique identifier of the document to download
        type : str
            If you specify a type of `html`, processes the file using
            text encoding, otherwise binary
        """
        path = f"/api/data/files/{documentId}/download"
        queryParams = {}
        if type:
            queryParams['type'] = type
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def update_file(self, fileId: str, body: UpdateRequestDto) -> AstroResult[object]:
        """
        Updates information about a File uploaded to your Workspace.

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
        fileId : str
            The unique identifier of the File to update
        body : UpdateRequestDto
            Information to change about the File and its location
        """
        path = f"/api/data/files/{fileId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
