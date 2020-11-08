#!/usr/bin/env python
import logging
import sys
import os

import ldclient
import warnings
warnings.filterwarnings("ignore")
os.environ["https_proxy"] = "https://127.0.0.1:8080"
os.environ["http_proxy"] = "http://127.0.0.1:8080"

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

if __name__ == "__main__":
    http_config = ldclient.config.HTTPConfig(disable_ssl_verification = True, http_proxy = "https://127.0.0.1:8083")
    ldclient.set_config(ldclient.Config(sdk_key="sdk-da4e7cfe-e958-4c6c-9ad2-ced60853d668", http = http_config))

    user = {
      "key": "bob2@example.com",
      "firstName": "Bob2",
      "lastName": "Loblaw2",
      "custom": {
        "groups": "beta_testers"
      }
    }

    show_feature = ldclient.get().variation("my_feature_flag", user, False)

    if show_feature:
      print("Showing your feature")
    else:
      print("Not showing your feature")

    ldclient.get().close() # close the client before exiting the program - ensures that all events are delivered
