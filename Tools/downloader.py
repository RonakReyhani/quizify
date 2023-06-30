import requests
from transformers import Tool

def downloader(url):
  print(url)
  # NOTE the stream=True parameter below
  file_name = url.split('/')[-1]
  print(file_name)
  with requests.get(url, stream=True, allow_redirects=True) as r:
      print(r.headers.get('content-type'))
      r.raise_for_status()
      with open(file_name, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return file_name

class download_file (Tool):
  name="download_file_tool"
  description="This is a tool for downloading documents (pdf) from the web. It takes an input named `url` which should be the web url containing the document (pdf). It downloads the document and stores the content of the document in the local file."
  input=['text']
  output=['text']

  def __call__(self,url: str):
    print("url", url)
    return downloader(url)

download_file_tool =  download_file()