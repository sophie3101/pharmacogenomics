import requests, zipfile, io, logging, glob, os
import pandas as pd 

logger = logging.getLogger(__name__)
def find_file(in_dir, search_name):
    print(in_dir, os.path.abspath(in_dir))
    res = glob.glob(f"{in_dir}/*{search_name}*", recursive=True)
    if len(res)==0:
      raise FileNotFoundError(f"File with pattern {search_name} is not found")
    
    return os.path.abspath(res[0])

def tsv_to_csv(in_file):
  out_file = in_file.replace(".tsv", ".csv")
  df = pd.read_csv(in_file, sep="\t")
  df.to_csv(out_file, index=False)

def download_file_from_link(url, des_folder):
  """
    This function is to download zip folder from link {url} to {des_folder}
    and the compressed link is extracted to {des_fodler}
    Parameters:
      url: name of link to download
      des_folder: name of destination folder where the downloaded link is located
    Returns:
     None
  """
  try:
    # print(url, des_folder)
    headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, stream=True, headers=headers)
    response.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
      zip_file.extractall(des_folder)
      logger.info("ZIP file downloaded and extracted successfully.")
      return True
  except Exception as e:
    logger.error(f"Error in downloading the link {url}, {e}")
    raise
