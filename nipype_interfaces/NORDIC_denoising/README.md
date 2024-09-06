# Intergration of NIFTI_NORDIC in Nipype

This repository includes a Nipype interface for the NORDIC thermal noise reduction tool. To use this interface, please follow the steps below:

1. **Download NORDIC**:
- Obtain NORDIC from the [UMN site](https://github.com/SteenMoeller/NORDIC_Raw) and install it separately
     
2. **Adapt the NIFTI_NORDIC MATLAB Script**:
- Rename the script from `NFITI_NORDIC.m` to `NIFTI_NORDIC_nipype.m`
- Modify the script:
  - Update the function definition within the script to match the new name
  - Replace the input argument ARG with ARG_path

```matlab
function NIFTI_NORDIC_nipype(fn_magn_in, fn_phase_in, fn_out, ARG_path)
```

- Add the following 'if exist' statement at the beginning of the script to handle the new input structure:
  
```matlab
if exist('ARG_path') 
    arg_struct = load(ARG_path);
    ARG = arg_struct.ARG;
    ARG = structfun(@double, ARG, 'uniformoutput', 0); %fields need to be casted to double (from python struct with datatype int64) 
    disp(ARG)
end
```

- __Summary of changes:__
```matlab
function NIFTI_NORDIC_nipype(fn_magn_in, fn_phase_in, fn_out, ARG_path)

if exist('ARG_path') 
    arg_struct = load(ARG_path);
    ARG = arg_struct.ARG;
    ARG = structfun(@double, ARG, 'uniformoutput', 0); %fields need to be casted to double (from python struct with datatype int64) 
    disp(ARG)
end
```

3. **Set Up the Interface**:
   - Use the `NIFIT_NORDIC_interface.py` Nipype interface script to integrate NORDIC into your workflows.
   - Refer to the example notebook `example_usage_NORDIC_tsnr_nipype.ipynb` for guidance on how to use the NORDIC interface within Nipype and to see how TSNR is computed to evaluate the effects of NORDIC denoising.


## Compliance with License Terms

- **License Terms**: NORDIC and NIFTI_NORDIC are copyrighted by Regents of the University of Minnesota. They are licensed solely for educational and research purposes by non-profit institutions and U.S. government agencies. For more details, review the [NORDIC License Terms](https://github.com/SteenMoeller/NORDIC_Raw?tab=readme-ov-file#licensing) for more details.
- **Usage**: Ensure that NORDIC is used in compliance with its licensing terms. This repository does not distribute NORDIC software but provides the means to integrate it into a Nipype workflow.
  
For any questions regarding licensing or to request further permissions, please contact [umotc@umn.edu](mailto:umotc@umn.edu).
