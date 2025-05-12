from flask import jsonify
from __main__ import app
from gallery_dl import config, option, job, exception
from pprint import pprint
import re
from util_download_with_bash import perform_download_with_bash

@app.route("/gallery-dl/fetch/<path:target_url>", methods = ['GET'])
def fetch(target_url):

	status = 9
	msg = "DL_OK"
	output, error = perform_download_with_bash(target_url)

	if error:
		return jsonify({'error': error})
	else:
		# Extract image URLs using a regular expression
		image_urls = re.findall(r'(https?://\S+\.(?:jpg|jpeg|png|gif|webp|svg))', output)
		if image_urls:
			return jsonify({'images': image_urls})
		else:
			return jsonify({'images': []})
  # try:
  #   status = job.DownloadJob(target_url).run()
  # except exception.GalleryDLException as e:
  #   status = e.code
  #   msg = str(e)
  # except Exception as e:
  #   status = -1
  #   msg = str(e)

	# data = {
	# 	"gallery_dl_run_status" : status,
	# 	"gallery_dl_run_msg" : msg,
	# 	"gallery_dl_run_target_url" : target_url
  # } 
	# return jsonify(data)
