import os
import json
import sys
import shutil
import zipfile
import ssl
import urllib.request


class Utils:
    def cleanup(filename):
        print("Cleaning up " + filename)
        if os.path.exists(filename):
            os.remove(filename)

    def extract(filename):
        print("Extracting " + filename)
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall()


debug = False


def print(*args, **kwargs):
    force = kwargs.pop("force", False)
    if debug or force:
        __builtins__.print(*args, **kwargs)


default_steam_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Lethal Company"


def install_bepinex_latest():
    # Get latest release options from BePinEx repo
    response = urllib.request.urlopen(
        "https://api.github.com/repos/BepInEx/BepInEx/releases/latest"
    )
    data = response.read()
    encoding = response.info().get_content_charset("utf-8")
    result = json.loads(data.decode(encoding))
    # version = result['tag_name']

    # Select version to download

    options = result["assets"]
    # TODO: Check os and select correct platform
    print("Select your platform:", force=True)
    for i in range(1, len(options) + 1):
        print("[" + str(i) + "] " + options[i - 1]["name"], force=True)

    platform = int(input("Enter the number of your platform: "))
    option = options[platform - 1]
    filename = option["name"]
    url = option["browser_download_url"]

    # Download .zip and extract to script directory
    print("Downloading " + url)
    urllib.request.urlretrieve(url, filename)

    Utils.extract(filename)
    Utils.cleanup(filename)

    for filename in os.listdir("."):
        exclusion_list = {"install.py", "README.md", ".git", ".gitignore", ".vscode"}
        if filename not in exclusion_list:
            try:
                shutil.move(filename, default_steam_dir + "\\" + filename)
            except:
                shutil.rmtree(default_steam_dir + "\\" + filename)
                shutil.move(filename, default_steam_dir + "\\" + filename)
            finally:
                print("Moved " + filename)

def install_more_company_1_6_0():
    filename = "MoreCompany.zip"

    # Disable SSL verification to download from Thunderstore
    # TODO: ...don't?
    ssl._create_default_https_context = ssl._create_unverified_context
    more_company_url = (
        "https://thunderstore.io/package/download/notnotnotswipez/MoreCompany/1.6.0/"
    )

    print("Downloading " + more_company_url)
    req = urllib.request.Request(
        more_company_url, headers={"User-Agent": "Mozilla/5.0"}
    )
    response = urllib.request.urlopen(req)

    with open(filename, "wb") as out_file:
        data = response.read()
        out_file.write(data)

    Utils.extract(filename)
    Utils.cleanup(filename)

    # Move MoreCompany.dll to plugins folder
    downloaded_dll_path = "\\BepInEx\\plugins\\MoreCompany.dll"
    target_dll_path = default_steam_dir + downloaded_dll_path
    shutil.copy(downloaded_dll_path[1:], target_dll_path)


def post_install():
    # Remove all files except repo files
    exclusion_list = {"install.py", "README.md", ".git", ".gitignore", ".vscode"}
    for filename in os.listdir("."):
        if filename not in exclusion_list:
            try:
                os.remove(filename)
            except:
                shutil.rmtree(filename)
            finally:
                print("Removed " + filename)
    print("Done!", force=True)


def install():
    install_bepinex_latest()
    install_more_company_1_6_0()
    post_install()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            debug = True
    install()
