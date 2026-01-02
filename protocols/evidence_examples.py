"""
Evidence Metadata Examples
Sample evidence metadata for protocols (to be integrated)
"""

from utils.evidence_levels import create_evidence_metadata, EvidenceLevel

# Example evidence metadata for some protocols
PROTOCOL_EVIDENCE_EXAMPLES = {
    "sepsis": {
        "3_hour_bundle": create_evidence_metadata(
            level="A",
            citation="Rhodes A, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Intensive Care Med. 2021;47(11):1181-1247.",
            doi="10.1007/s00134-021-06506-y",
            pubmed_id="34599691",
            last_reviewed="2024-12-01",
            synopsis="High-quality evidence from systematic review and meta-analysis supporting early intervention"
        ),
        "antibiotic_timing": create_evidence_metadata(
            level="A",
            citation="Kumar A, et al. Duration of hypotension before initiation of effective antimicrobial therapy is the critical determinant of survival in human septic shock. Crit Care Med. 2006;34(6):1589-96.",
            doi="10.1097/01.CCM.0000217961.75225.E9",
            pubmed_id="16625125",
            last_reviewed="2024-12-01",
            synopsis="Strong evidence that each hour of delay increases mortality"
        )
    },
    "stroke": {
        "tpa_eligibility": create_evidence_metadata(
            level="A",
            citation="Powers WJ, et al. 2018 Guidelines for the Early Management of Patients With Acute Ischemic Stroke. Stroke. 2018;49(3):e46-e110.",
            doi="10.1161/STR.0000000000000158",
            pubmed_id="29367334",
            last_reviewed="2024-11-15",
            synopsis="Class I evidence for tPA within 3-4.5 hours window"
        )
    },
    "acs": {
        "dual_antiplatelet": create_evidence_metadata(
            level="A",
            citation="Collet JP, et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J. 2021;42(14):1289-1367.",
            doi="10.1093/eurheartj/ehaa575",
            pubmed_id="32860058",
            last_reviewed="2024-10-20",
            synopsis="Strong recommendation for DAPT in NSTE-ACS"
        )
    }
}


def get_protocol_evidence(protocol_name: str, recommendation_key: str = None):
    """
    Get evidence metadata for a protocol
    
    Args:
        protocol_name: Protocol name (e.g., "sepsis", "stroke")
        recommendation_key: Specific recommendation key (optional)
    
    Returns:
        EvidenceMetadata or dict of EvidenceMetadata
    """
    if protocol_name not in PROTOCOL_EVIDENCE_EXAMPLES:
        return None
    
    evidence_dict = PROTOCOL_EVIDENCE_EXAMPLES[protocol_name]
    
    if recommendation_key:
        return evidence_dict.get(recommendation_key)
    
    return evidence_dict


__all__ = ['PROTOCOL_EVIDENCE_EXAMPLES', 'get_protocol_evidence']

