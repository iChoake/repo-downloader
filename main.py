import requests, os
from zipfile import ZipFile

# Format: https://github.com/{owner}/{repo}
OWNER   = "" # Owner of the GitHub repo
REPO    = "" # GitHub repository name
EXT     = ".zip" # Extension

def zip_extractor(filename):
    with ZipFile(filename+EXT, 'r') as zObject:
        zObject.extractall(filename)

def version_downloader(repo,name,url):
    print("Processing... "+url)
    response = requests.get(url)
    filename = repo+"/"+name
    open(filename+EXT, "wb").write(response.content)
    
    zip_extractor(filename) # Extracting Zip files
    

def repo_downloader(owner, repo):
    url = "https://api.github.com/repos/"+owner+"/"+repo+"/tags"
    response = requests.get(url).json()

    # Create directory for versions of repo if not exists
    try:
        os.makedirs(repo)
    except:
        pass

    for data in response:
        version_downloader(repo,data["name"],data["zipball_url"])

def main():
    repo_downloader(OWNER,REPO)

if __name__ == '__main__':
    main()