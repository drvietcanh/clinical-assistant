from .induction_agents import INDUCTION_AGENTS
from .neuromuscular_blockers import NEUROMUSCULAR_BLOCKERS
from .local_anesthetics import LOCAL_ANESTHETICS

ANESTHESIA_DRUGS = {
    **INDUCTION_AGENTS,
    **NEUROMUSCULAR_BLOCKERS,
    **LOCAL_ANESTHETICS
}
