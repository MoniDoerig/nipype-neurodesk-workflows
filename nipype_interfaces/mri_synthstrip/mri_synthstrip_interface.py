#Author: Moni Dörig

import os
from nipype.interfaces.base import (
    TraitedSpec,
    File,
    CommandLine,
    CommandLineInputSpec,
    traits,
    isdefined
)

class MRISynthStripInputSpec(CommandLineInputSpec):
    in_file = File(exists=True, mandatory=True, desc="Input T1-weighted MRI file", argstr="--i %s")
    out_file = File("brain.nii.gz", usedefault=True, desc="Output brain-extracted image file", argstr="--o %s")
    out_mask_filename = traits.Str("brain_mask.nii.gz", usedefault=True, desc="Filename for output brain mask", argstr="--mask %s")
    no_csf = traits.Bool(False, desc="Do not include CSF in the brain mask", argstr="--no-csf")
    boundary_distance = traits.Int(desc="Boundary distance from the brain in millimeters", argstr="-b %d")

class MRISynthStripOutputSpec(TraitedSpec):
    mask_file = File(exists=True, desc="Output brain mask file")
    out_file = File(exists=True, desc="Output brain-extracted image file")
    
class MRISynthStrip(CommandLine):
    _cmd = "mri_synthstrip"
    input_spec = MRISynthStripInputSpec
    output_spec = MRISynthStripOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()

        if isdefined(self.inputs.out_file):
            outputs["out_file"] = os.path.abspath(os.path.join(os.getcwd(), os.path.basename(self.inputs.out_file)))
        
        if isdefined(self.inputs.out_mask_filename):
            outputs["mask_file"] = os.path.abspath(os.path.join(os.getcwd(),
                                    os.path.basename(self.inputs.out_mask_filename)))

        return outputs
