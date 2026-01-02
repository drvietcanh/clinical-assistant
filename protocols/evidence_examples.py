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
        ),
        "fluid_resuscitation": create_evidence_metadata(
            level="B",
            citation="Evans L, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.",
            doi="10.1097/CCM.0000000000005337",
            pubmed_id="34605781",
            last_reviewed="2024-12-01",
            synopsis="Moderate evidence for balanced crystalloids over normal saline"
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
        ),
        "mechanical_thrombectomy": create_evidence_metadata(
            level="A",
            citation="Powers WJ, et al. 2019 Update to the 2018 Guidelines for the Early Management of Acute Ischemic Stroke. Stroke. 2019;50(12):e344-e418.",
            doi="10.1161/STR.0000000000000211",
            pubmed_id="31662037",
            last_reviewed="2024-11-15",
            synopsis="Class I evidence for mechanical thrombectomy within 24 hours for selected patients"
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
        ),
        "anticoagulation": create_evidence_metadata(
            level="A",
            citation="Collet JP, et al. 2020 ESC Guidelines for the management of acute coronary syndromes. Eur Heart J. 2021;42(14):1289-1367.",
            doi="10.1093/eurheartj/ehaa575",
            pubmed_id="32860058",
            last_reviewed="2024-10-20",
            synopsis="Strong recommendation for anticoagulation in addition to DAPT"
        ),
        "stemi_primary_pci": create_evidence_metadata(
            level="A",
            citation="Ibanez B, et al. 2017 ESC Guidelines for the management of acute myocardial infarction in patients presenting with ST-segment elevation. Eur Heart J. 2018;39(2):119-177.",
            doi="10.1093/eurheartj/ehx393",
            pubmed_id="28886621",
            last_reviewed="2024-10-20",
            synopsis="Class I evidence for primary PCI within 90 minutes"
        )
    },
    "heart_failure": {
        "ace_inhibitor": create_evidence_metadata(
            level="A",
            citation="McDonagh TA, et al. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2021;42(36):3599-3726.",
            doi="10.1093/eurheartj/ehab368",
            pubmed_id="34447992",
            last_reviewed="2024-09-15",
            synopsis="Class I evidence for ACE inhibitors in heart failure with reduced ejection fraction"
        )
    },
    "ards": {
        "low_tidal_volume": create_evidence_metadata(
            level="A",
            citation="ARDS Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med. 2000;342(18):1301-8.",
            doi="10.1056/NEJM200005043421801",
            pubmed_id="10793162",
            last_reviewed="2024-08-20",
            synopsis="Landmark trial showing reduced mortality with low tidal volume ventilation"
        ),
        "prone_positioning": create_evidence_metadata(
            level="A",
            citation="Guerin C, et al. Prone positioning in severe acute respiratory distress syndrome. N Engl J Med. 2013;368(23):2159-68.",
            doi="10.1056/NEJMoa1214103",
            pubmed_id="23688302",
            last_reviewed="2024-08-20",
            synopsis="Strong evidence for prone positioning in severe ARDS"
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

