# iterate

This repo contains code related to `iterate`, a machine learning hosting, versioning and testing library.

## Running the code

To run the code create a new Python environment `pip3 -m venv ./venv` and activate it `source ./venv/bin/activate`. From there, install any dependencies `pip3 install -r requirements.txt`. As this is a utility library there is no `main` file to run, however if you would like to run the test suite, you can run `python3 -m unittest discover tests`.

## Workflows

This repository contains Github workflows for CI/CD. Currently we have workflows for automated unit testing. This workflow runs on push and pull request on all branches. Additionally, you can manually trigger all workflows through Github's Workflows pane. 