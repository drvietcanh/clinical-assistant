from .gout import GOUT_DRUGS
from .osteoporosis import OSTEOPOROSIS_DRUGS
from .dmards import DMARDS_DRUGS
from .bone_joint_supplements import BONE_JOINT_SUPPLEMENTS

RHEUMATOLOGY_DRUGS = {
    **GOUT_DRUGS,
    **OSTEOPOROSIS_DRUGS,
    **DMARDS_DRUGS,
    **BONE_JOINT_SUPPLEMENTS,
}
