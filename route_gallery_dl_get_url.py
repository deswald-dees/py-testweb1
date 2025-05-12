from flask import jsonify
from __main__ import app
from gallery_dl import config, option, job, exception
from pprint import pprint

@app.route("/gallery-dl-get-url", methods = ['GET'])
def gallery_dl_get_url():
  data = {
    "Modules" : 15,
    "Subject" : "Data Structures and Algorithms"
  } 
  return jsonify(data)

@app.route("/gallery-dl/retrieve/<path:target_url>", methods = ['GET'])
def gallery_dl_get_url2(target_url):

  # except Exception as e:
  #   status = -1
  # except KeyboardInterrupt:
	# 	pass

  # pprint(vars(option.AppendCommandAction))
    #   output.add_argument(
    #     "-g", "--get-urls",
    #     dest="list_urls", action="count",
    #     help="Print URLs instead of downloading",
    # )

  status = 0
  msg = "DL_OK"

  try:
    # option.AppendCommandAction("-g", dest="list_urls")
    # job.DownloadJob.run()
    conf_options = {
            "list-urls": True,      # Equivalent to --list-urls
            "download": False,      # Ensure download is off
            "write-metadata": False # Don't write metadata files
            # Add other necessary options here if needed, e.g., for authentication:
            # "cookies": "/path/to/cookies.txt",
            # "username": "your_username",
            # "password": "your_password",
        }
    config.load()
    for key, value in conf_options.items():
      config.set('extractor', key, value)

    status = job.DownloadJob(target_url).run()
  except exception.GalleryDLException as e:
    status = e.code
    msg = str(e)
  except Exception as e:
    status = -1
    msg = str(e)

  data = {
    "gallery_dl_run_status" : status,
    "gallery_dl_run_msg" : msg,
    "gallery_dl_run_target_url" : target_url
  } 
  return jsonify(data)
