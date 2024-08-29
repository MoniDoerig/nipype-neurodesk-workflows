# Nipype Interfaces

## Overview
This directory contains custom Nipype interfaces for various neuroimaging tools, such as mri_synthstrip and NORDIC. Each subdirectory includes the interface script(s) and an example usage notebook to demonstrate how to integrate the tool into your workflow.

## Available Interfaces

- **MRI SynthStrip** (`mri_synthstrip`): A Nipype interface for running FreeSurfer's `mri_synthstrip` tool.
  - [Interface Script](./mri_synthstrip/mri_synthstrip_interface.py)
  - [Example Usage](./mri_synthstrip/example_usage_synthstrip_nipype.ipynb)

  ## Coming Soon
- **NORDIC Denoising** (`NORDIC`): A Nipype interface for running NORDIC thermal noise reduction. Requires MATLAB version 2017b or newer.
  - [Interface Script](./NORDIC/NIFIT_NORDIC_interface.py) *(Coming soon)*
  - [MATLAB Script](./NORDIC/NIFTI_NORDIC_nipype.m) *(Coming soon)*
  - [Example Usage](./NORDIC/example_usage_NORDIC_nipype.ipynb) *(Coming soon)*
  
## Usage
1. Set up Neurodesk or Neurodesk Play:
   - Follow the setup instructions provided in the [README of the nipype-neurodesk-workflows](../README.md).
2. Integrate the Tool/Nipype Interface:
   - Navigate to the subdirectory for the desired tool (e.g., mri_synthstrip or NORDIC)
   - Follow the instructions provided in the example_usage notebook within that subdirectory to integrate the interface into your workflow.





