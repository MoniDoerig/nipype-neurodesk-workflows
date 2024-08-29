# Nipype Interfaces

## Overview
This directory contains custom Nipype interfaces for various neuroimaging tools, such as FreeSurfer's SynthStrp tool. Each subdirectory includes the interface script(s) and an example usage notebook to demonstrate how to integrate the tool into your workflow.

## Available Interfaces

- **MRI SynthStrip** (`mri_synthstrip`): A Nipype interface for running FreeSurfer's `mri_synthstrip` tool.
  - [Interface Script](./mri_synthstrip/mri_synthstrip_interface.py)
  - [Example Usage](./mri_synthstrip/example_usage_synthstrip_nipype.ipynb)
  
## Usage
1. Set up Neurodesk or Neurodesk Play:
   - Follow the setup instructions provided in the [README of the nipype-neurodesk-workflows](../README.md).
2. Integrate the Tool/Nipype Interface:
   - Navigate to the subdirectory for the desired tool (e.g., mri_synthstrip or NORDIC)
   - Follow the instructions provided in the example_usage notebook within that subdirectory to integrate the interface into your workflow.





