# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix3.reconst import FitTensor

def test_FitTensor_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bval_scale=dict(argstr='-bvalue_scaling %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    grad_file=dict(argstr='-grad %s',
    ),
    grad_fsl=dict(argstr='-fslgrad %s %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(),
    in_bvec=dict(argstr='-fslgrad %s %s',
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    in_mask=dict(argstr='-mask %s',
    ),
    method=dict(argstr='-method %s',
    ),
    nthreads=dict(argstr='-nthreads %d',
    nohash=True,
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    reg_term=dict(argstr='-regularisation %f',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = FitTensor.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_FitTensor_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = FitTensor.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

