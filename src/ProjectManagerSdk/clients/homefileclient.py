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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.filedto import FileDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class HomeFileClient:
    """
    API methods related to HomeFile
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def upload_home_file(self, fileName: str) -> AstroResult[FileDto]:
        """
        Uploads a file to the My Files folder on your Home Files page.
        ProjectManager allows you to store Files connected to other
        elements of your Workspace such as a Project, a Task, or Home.
        Files are maintained separately based on the location where the
        file was stored. When you upload a File, please allow a few
        moments for the File to be processed and verified.
        ProjectManager may reject File uploads that contain problems
        such as malware. Once a File has completed the upload the
        process, you may retrieve it using the DownloadFile API. This
        API returns a JSON response indicating success or failure.

        Parameters
        ----------
        fileName : str
            The full path of a file to upload to the API
        """
        path = "/api/data/home/files"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, fileName)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=FileDto, data=json.loads(result.content)['data'])
            return AstroResult[FileDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[FileDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def upload_home_file_to_folder(self, folderId: str, fileName: str) -> AstroResult[FileDto]:
        """
        Uploads a file to a specific folder on your Home Files page.
        ProjectManager allows you to store Files connected to other
        elements of your Workspace such as a Project, a Task, or Home.
        Files are maintained separately based on the location where the
        file was stored. You can organize your files in the Home Files
        and Project Files pages by adding folders. When you upload a
        File, please allow a few moments for the File to be processed
        and verified. ProjectManager may reject File uploads that
        contain problems such as malware. Once a File has completed the
        upload the process, you may retrieve it using the DownloadFile
        API. This API returns a JSON response indicating success or
        failure.

        Parameters
        ----------
        folderId : str
            The reference to the sub folder to put the file into
        fileName : str
            The full path of a file to upload to the API
        """
        path = f"/api/data/home/folders/{folderId}/files"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, fileName)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=FileDto, data=json.loads(result.content)['data'])
            return AstroResult[FileDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[FileDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
