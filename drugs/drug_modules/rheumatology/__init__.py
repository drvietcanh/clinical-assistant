from .gout import GOUT_DRUGS
from .osteoporosis import OSTEOPOROSIS_DRUGS
from .dmards import DMARDS_DRUGS

RHEUMATOLOGY_DRUGS = {
    **GOUT_DRUGS,
    **OSTEOPOROSIS_DRUGS,
    **DMARDS_DRUGS,
}
