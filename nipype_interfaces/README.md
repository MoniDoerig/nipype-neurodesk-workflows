# Nipype Interfaces

## Overview
This directory contains custom Nipype interfaces for various neuroimaging tools, such as FreeSurfer's SynthStrip and the NORDIC denoising tools. Each subdirectory includes the Nipype interface script(s) and an example usage notebook to demonstrate how to integrate the tool into your workflow. You'll find resources, publications, and code references in the corresponding *example_usage notebooks*.

## Available Interfaces

- **MRI SynthStrip** (`mri_synthstrip`): A Nipype interface for running FreeSurfer's `mri_synthstrip` tool.
  - [Nipype Interface](./mri_synthstrip/mri_synthstrip_interface.py)
  - [Example Usage](./mri_synthstrip/example_usage_synthstrip_nipype.ipynb)
 
- **NORDIC Denoising** ('NORDIC_denoising'): A Nipype interface for running NORDIC thermal noise reduction. Instructions for integrating NIFIT_NORDIC, including script adaptation and licensing compliance, are provided in the [README file within the NORDIC_denoising](./NORDIC_denoising/README.md) subdirectory. Requires MATLAB.
  - [Nipype Interface](./NORDIC_denoising/NIFTI_NORDIC_interface.py)
  - [Example Usage](./NORDIC_denoising/example_usage_NORDIC_tsnr_nipype.ipynb)
  
## Usage
1. Set up Neurodesk or Neurodesk Play:
   - Follow the setup instructions provided in the [README of the nipype-neurodesk-workflows](../README.md).
2. Integrate the Tool/Nipype Interface:
   - Navigate to the subdirectory for the desired tool (e.g., mri_synthstrip)
   - Follow the instructions provided in the example_usage notebook within that subdirectory to integrate the interface into your workflow.





