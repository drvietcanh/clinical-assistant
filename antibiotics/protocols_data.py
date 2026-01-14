"""
Antibiotic Protocols Data
Phác đồ kháng sinh chuẩn hóa dựa trên IDSA/Sanford guidelines
Tóm tắt, không copy nguyên văn - chỉ cấu trúc và thông tin cơ bản
"""

from .protocols_schema import (
    AntibioticProtocol, ProtocolCollection,
    InfectionSite, Severity, Setting, RegimenType, RecommendationLevel,
    DrugDose, Regimen
)


def get_antibiotic_protocols() -> ProtocolCollection:
    """
    Get all antibiotic protocols
    Returns ProtocolCollection with standardized protocols
    Cached in session state for performance
    """
    # Check cache first
    import streamlit as st
    cache_key = '_antibiotic_protocols_cache'
    
    if cache_key in st.session_state:
        return st.session_state[cache_key]
    
    protocols = []
    
    # ========== CAP (Community-Acquired Pneumonia) ==========
    
    # CAP Non-severe - Outpatient
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.CAP,
        severity=Severity.MILD,
        setting=Setting.OPD,
        title="CAP Non-severe (Outpatient)",
        description="Community-acquired pneumonia, non-severe, outpatient treatment",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Amoxicillin", "1g", "PO", "TID", "5-7 days"),
                    DrugDose("Azithromycin", "500mg", "PO", "once daily", "3 days")
                ],
                indication="First-line empiric therapy",
                rationale="Covers typical (S. pneumoniae) and atypical pathogens",
                recommendation_level=RecommendationLevel.STRONG,
                step_down_options=[
                    DrugDose("Amoxicillin-clavulanate", "875/125mg", "PO", "BID", "5-7 days")
                ]
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Doxycycline", "100mg", "PO", "BID", "7-10 days")
                ],
                indication="Penicillin allergy",
                rationale="Alternative for beta-lactam allergy",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA/ATS 2019",
        guideline_year=2019,
        notes=[
            "Consider MRSA risk factors: recent hospitalization, nursing home, IV drug use",
            "Duration: 5-7 days for uncomplicated CAP"
        ]
    ))
    
    # CAP Severe - Inpatient
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.CAP,
        severity=Severity.SEVERE,
        setting=Setting.WARD,
        title="CAP Severe (Inpatient)",
        description="Severe community-acquired pneumonia requiring hospitalization",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "once daily", "7-10 days"),
                    DrugDose("Azithromycin", "500mg", "IV/PO", "once daily", "5 days")
                ],
                indication="Severe CAP, no MRSA/Pseudomonas risk",
                rationale="Broad coverage for typical and atypical pathogens",
                recommendation_level=RecommendationLevel.STRONG,
                step_down_options=[
                    DrugDose("Amoxicillin-clavulanate", "875/125mg", "PO", "BID", "5-7 days"),
                    DrugDose("Levofloxacin", "750mg", "PO", "once daily", "5-7 days")
                ]
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Levofloxacin", "750mg", "IV/PO", "once daily", "5-7 days"),
                    DrugDose("Moxifloxacin", "400mg", "IV/PO", "once daily", "5-7 days")
                ],
                indication="Penicillin allergy or monotherapy option",
                rationale="Fluoroquinolone monotherapy for severe CAP",
                recommendation_level=RecommendationLevel.WEAK,
                warnings=["QT prolongation risk", "Tendon rupture risk"]
            )
        ],
        guideline_source="IDSA/ATS 2019",
        guideline_year=2019,
        risk_factors=["MRSA risk", "Pseudomonas risk"]
    ))
    
    # CAP ICU
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.CAP,
        severity=Severity.ICU,
        setting=Setting.ICU,
        title="CAP ICU",
        description="Severe CAP requiring ICU care",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "once daily", "7-10 days"),
                    DrugDose("Azithromycin", "500mg", "IV", "once daily", "5 days")
                ],
                indication="ICU CAP, no MRSA/Pseudomonas risk",
                rationale="Standard ICU empiric therapy",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.RESCUE,
                drugs=[
                    DrugDose("Piperacillin-tazobactam", "4.5g", "IV", "q6h", "7-10 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-10 days")
                ],
                indication="MRSA or Pseudomonas risk",
                rationale="Broad-spectrum coverage including MRSA and Pseudomonas",
                recommendation_level=RecommendationLevel.STRONG,
                warnings=["Requires TDM for vancomycin"]
            )
        ],
        guideline_source="IDSA/ATS 2019",
        guideline_year=2019,
        risk_factors=["MRSA risk", "Pseudomonas risk", "ESBL risk"]
    ))
    
    # ========== HAP/VAP ==========
    
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.HAP,
        severity=Severity.SEVERE,
        setting=Setting.WARD,
        title="HAP (Hospital-Acquired Pneumonia)",
        description="Hospital-acquired pneumonia, non-VAP",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Piperacillin-tazobactam", "4.5g", "IV", "q6h", "7-10 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-10 days")
                ],
                indication="HAP with MRSA risk",
                rationale="Covers Gram-negative, anaerobes, and MRSA",
                recommendation_level=RecommendationLevel.STRONG,
                warnings=["Requires TDM for vancomycin"]
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Cefepime", "2g", "IV", "q8h", "7-10 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-10 days")
                ],
                indication="Alternative for HAP",
                rationale="Cefepime covers Pseudomonas and Enterobacteriaceae",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA/ATS 2016",
        guideline_year=2016
    ))
    
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.VAP,
        severity=Severity.ICU,
        setting=Setting.ICU,
        title="VAP (Ventilator-Associated Pneumonia)",
        description="Ventilator-associated pneumonia",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Piperacillin-tazobactam", "4.5g", "IV", "q6h", "7-10 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-10 days")
                ],
                indication="VAP empiric therapy",
                rationale="Broad-spectrum coverage for VAP pathogens",
                recommendation_level=RecommendationLevel.STRONG,
                warnings=["Requires TDM for vancomycin", "De-escalate after 48-72h if improving"]
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Meropenem", "2g", "IV", "q8h", "7-10 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-10 days")
                ],
                indication="ESBL risk or severe VAP",
                rationale="Carbapenem for ESBL-producing organisms",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA/ATS 2016",
        guideline_year=2016,
        notes=[
            "De-escalate after 48-72 hours if clinical improvement",
            "Consider shorter duration (7 days) if responding well"
        ]
    ))
    
    # ========== UTI ==========
    
    # UTI Uncomplicated
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.UTI,
        severity=Severity.MILD,
        setting=Setting.OPD,
        title="UTI Uncomplicated",
        description="Uncomplicated urinary tract infection",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Nitrofurantoin", "100mg", "PO", "BID", "5 days"),
                    DrugDose("Trimethoprim-SMX", "160/800mg", "PO", "BID", "3 days")
                ],
                indication="First-line for uncomplicated UTI",
                rationale="Narrow-spectrum, effective against E. coli",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Ciprofloxacin", "500mg", "PO", "BID", "3 days"),
                    DrugDose("Levofloxacin", "750mg", "PO", "once daily", "3 days")
                ],
                indication="Alternative if resistance to first-line",
                rationale="Fluoroquinolones for resistant pathogens",
                recommendation_level=RecommendationLevel.WEAK,
                warnings=["Reserve for resistant cases", "QT prolongation risk"]
            )
        ],
        guideline_source="IDSA 2010",
        guideline_year=2010,
        notes=["3-day course sufficient for uncomplicated UTI"]
    ))
    
    # UTI Complicated
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.UTI,
        severity=Severity.MODERATE,
        setting=Setting.WARD,
        title="UTI Complicated",
        description="Complicated urinary tract infection",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "once daily", "7-14 days"),
                    DrugDose("Ciprofloxacin", "400mg", "IV", "q12h", "7-14 days")
                ],
                indication="Complicated UTI",
                rationale="IV therapy for complicated infections",
                recommendation_level=RecommendationLevel.STRONG,
                step_down_options=[
                    DrugDose("Ciprofloxacin", "500mg", "PO", "BID", "7-14 days")
                ]
            )
        ],
        guideline_source="IDSA 2010",
        guideline_year=2010,
        notes=["7-14 days duration for complicated UTI"]
    ))
    
    # ========== SSTI (Skin and Soft Tissue Infection) ==========
    
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.SSTI,
        severity=Severity.MILD,
        setting=Setting.OPD,
        title="SSTI Mild (Cellulitis)",
        description="Mild skin and soft tissue infection",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Cephalexin", "500mg", "PO", "QID", "7-10 days"),
                    DrugDose("Dicloxacillin", "500mg", "PO", "QID", "7-10 days")
                ],
                indication="Mild cellulitis, no MRSA risk",
                rationale="Covers S. aureus and Streptococcus",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Clindamycin", "300-450mg", "PO", "TID", "7-10 days")
                ],
                indication="Penicillin allergy or MRSA risk",
                rationale="Covers MRSA and anaerobes",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA 2014",
        guideline_year=2014
    ))
    
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.SSTI,
        severity=Severity.SEVERE,
        setting=Setting.WARD,
        title="SSTI Severe",
        description="Severe skin and soft tissue infection",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days"),
                    DrugDose("Piperacillin-tazobactam", "4.5g", "IV", "q6h", "7-14 days")
                ],
                indication="Severe SSTI with MRSA risk",
                rationale="Broad coverage including MRSA",
                recommendation_level=RecommendationLevel.STRONG,
                warnings=["Requires TDM for vancomycin"]
            )
        ],
        guideline_source="IDSA 2014",
        guideline_year=2014
    ))
    
    # ========== Sepsis ==========
    
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.SEPSIS,
        severity=Severity.ICU,
        setting=Setting.ICU,
        title="Sepsis / Septic Shock",
        description="Sepsis and septic shock empiric therapy",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Piperacillin-tazobactam", "4.5g", "IV", "q6h", "7-14 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days")
                ],
                indication="Sepsis/septic shock, unknown source",
                rationale="Broadest coverage: Gram-negative, Gram-positive, anaerobes, MRSA",
                recommendation_level=RecommendationLevel.STRONG,
                warnings=["Start within 1 hour", "Requires TDM for vancomycin", "De-escalate after 48-72h"]
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Meropenem", "2g", "IV", "q8h", "7-14 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days")
                ],
                indication="ESBL risk or severe sepsis",
                rationale="Carbapenem for ESBL-producing organisms",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="Surviving Sepsis Campaign 2021",
        guideline_year=2021,
        notes=[
            "Start antibiotics within 1 hour of recognition",
            "Obtain cultures BEFORE starting antibiotics",
            "De-escalate after 48-72 hours if improving"
        ]
    ))
    
    # ========== CNS INFECTIONS ==========
    
    # Bacterial Meningitis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.CNS,
        severity=Severity.SEVERE,
        setting=Setting.ICU,
        title="Viêm màng não do vi khuẩn",
        description="Bacterial meningitis - empiric therapy based on age and risk factors",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q12h", "7-14 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days")
                ],
                indication="Empiric therapy for suspected bacterial meningitis",
                rationale="Covers S. pneumoniae, N. meningitidis, H. influenzae, and resistant S. pneumoniae",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Cefotaxime", "2g", "IV", "q6h", "7-14 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days")
                ],
                indication="Alternative to Ceftriaxone",
                rationale="Similar spectrum, alternative cephalosporin",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.RESCUE,
                drugs=[
                    DrugDose("Meropenem", "2g", "IV", "q8h", "7-14 days"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "7-14 days")
                ],
                indication="Penicillin allergy or resistant organisms",
                rationale="Carbapenem for beta-lactam allergy or ESBL-producing organisms",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA 2016",
        guideline_year=2016,
        notes=[
            "Add Ampicillin if Listeria risk (age >50, immunocompromised, pregnancy)",
            "Dexamethasone before or with first dose if S. pneumoniae suspected",
            "Adjust Vancomycin dose based on TDM"
        ]
    ))
    
    # Brain Abscess
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.CNS,
        severity=Severity.SEVERE,
        setting=Setting.ICU,
        title="Áp xe não",
        description="Brain abscess - empiric therapy covering common pathogens",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q12h", "4-8 weeks"),
                    DrugDose("Metronidazole", "500mg", "IV", "q8h", "4-8 weeks")
                ],
                indication="Empiric therapy for brain abscess",
                rationale="Covers aerobic and anaerobic bacteria",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Meropenem", "2g", "IV", "q8h", "4-8 weeks")
                ],
                indication="Single agent alternative",
                rationale="Broad spectrum including anaerobes",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA 2017",
        guideline_year=2017,
        notes=[
            "Duration typically 4-8 weeks",
            "Surgical drainage often required",
            "Add Vancomycin if MRSA suspected"
        ]
    ))
    
    # ========== INTRA-ABDOMINAL INFECTIONS ==========
    
    # Peritonitis (Secondary)
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.IAI,
        severity=Severity.SEVERE,
        setting=Setting.WARD,
        title="Viêm phúc mạc thứ phát",
        description="Secondary peritonitis - community or hospital-acquired",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Piperacillin-Tazobactam", "4.5g", "IV", "q8h", "5-7 days")
                ],
                indication="Community-acquired secondary peritonitis",
                rationale="Broad spectrum including anaerobes and Enterobacteriaceae",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "5-7 days"),
                    DrugDose("Metronidazole", "500mg", "IV", "q8h", "5-7 days")
                ],
                indication="Alternative regimen",
                rationale="Covers Gram-negative and anaerobes",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.RESCUE,
                drugs=[
                    DrugDose("Meropenem", "1g", "IV", "q8h", "5-7 days")
                ],
                indication="Hospital-acquired or ESBL risk",
                rationale="Carbapenem for resistant organisms",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA/SIS 2017",
        guideline_year=2017,
        notes=[
            "Source control is critical",
            "Duration typically 5-7 days if source controlled",
            "Consider ESBL risk in hospital-acquired cases"
        ]
    ))
    
    # Cholecystitis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.IAI,
        severity=Severity.MODERATE,
        setting=Setting.WARD,
        title="Viêm túi mật",
        description="Acute cholecystitis - biliary tract infection",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Piperacillin-Tazobactam", "4.5g", "IV", "q8h", "3-5 days")
                ],
                indication="Empiric therapy for cholecystitis",
                rationale="Covers Enterobacteriaceae and anaerobes",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "3-5 days"),
                    DrugDose("Metronidazole", "500mg", "IV", "q8h", "3-5 days")
                ],
                indication="Alternative regimen",
                rationale="Covers common biliary pathogens",
                recommendation_level=RecommendationLevel.STRONG
            )
        ],
        guideline_source="Tokyo Guidelines 2018",
        guideline_year=2018,
        notes=[
            "Cholecystectomy is definitive treatment",
            "Antibiotics typically 3-5 days if source controlled",
            "Consider ESBL risk in severe cases"
        ]
    ))
    
    # Appendicitis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.IAI,
        severity=Severity.MODERATE,
        setting=Setting.WARD,
        title="Viêm ruột thừa",
        description="Acute appendicitis - uncomplicated or complicated",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "1-3 days"),
                    DrugDose("Metronidazole", "500mg", "IV", "q8h", "1-3 days")
                ],
                indication="Uncomplicated appendicitis",
                rationale="Covers Enterobacteriaceae and anaerobes",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Piperacillin-Tazobactam", "4.5g", "IV", "q8h", "3-5 days")
                ],
                indication="Complicated appendicitis",
                rationale="Broader spectrum for perforated appendicitis",
                recommendation_level=RecommendationLevel.STRONG
            )
        ],
        guideline_source="WSES 2020",
        guideline_year=2020,
        notes=[
            "Appendectomy is definitive treatment",
            "Uncomplicated: 1-3 days antibiotics",
            "Complicated: 3-5 days if source controlled"
        ]
    ))
    
    # ========== ENDOCARDITIS ==========
    
    # Native Valve Endocarditis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.ENDOCARDITIS,
        severity=Severity.SEVERE,
        setting=Setting.ICU,
        title="Viêm nội tâm mạc van tự nhiên",
        description="Native valve endocarditis - empiric therapy",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "4-6 weeks"),
                    DrugDose("Gentamicin", "1mg/kg", "IV", "q8h", "2 weeks")
                ],
                indication="Empiric therapy pending culture",
                rationale="Covers MRSA, MSSA, and Enterococcus",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "4-6 weeks"),
                    DrugDose("Gentamicin", "1mg/kg", "IV", "q8h", "2 weeks")
                ],
                indication="MSSA or Streptococcus if no MRSA risk",
                rationale="Narrower spectrum if organism known",
                recommendation_level=RecommendationLevel.STRONG
            )
        ],
        guideline_source="AHA/IDSA 2015",
        guideline_year=2015,
        notes=[
            "Obtain blood cultures BEFORE starting antibiotics",
            "Duration typically 4-6 weeks",
            "TDM required for Vancomycin and Gentamicin",
            "Consider surgical evaluation"
        ]
    ))
    
    # Prosthetic Valve Endocarditis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.ENDOCARDITIS,
        severity=Severity.SEVERE,
        setting=Setting.ICU,
        title="Viêm nội tâm mạc van nhân tạo",
        description="Prosthetic valve endocarditis - early (<1 year) or late (>1 year)",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "6 weeks"),
                    DrugDose("Gentamicin", "1mg/kg", "IV", "q8h", "2 weeks"),
                    DrugDose("Rifampin", "300mg", "PO", "q8h", "6 weeks")
                ],
                indication="Empiric therapy for prosthetic valve endocarditis",
                rationale="Covers coagulase-negative staphylococci and other pathogens",
                recommendation_level=RecommendationLevel.STRONG
            )
        ],
        guideline_source="AHA/IDSA 2015",
        guideline_year=2015,
        notes=[
            "Early PVE (<1 year): Usually coagulase-negative staphylococci",
            "Late PVE (>1 year): Similar to native valve",
            "Surgical evaluation often required",
            "TDM required for all antibiotics"
        ]
    ))
    
    # ========== OSTEOMYELITIS ==========
    
    # Acute Osteomyelitis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.OSTEOMYELITIS,
        severity=Severity.MODERATE,
        setting=Setting.WARD,
        title="Viêm xương tủy cấp",
        description="Acute osteomyelitis - hematogenous or contiguous spread",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "4-6 weeks"),
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "4-6 weeks")
                ],
                indication="Empiric therapy pending culture",
                rationale="Covers S. aureus (including MRSA) and Gram-negative",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Cefazolin", "2g", "IV", "q8h", "4-6 weeks")
                ],
                indication="MSSA confirmed",
                rationale="Narrower spectrum if organism known",
                recommendation_level=RecommendationLevel.STRONG
            )
        ],
        guideline_source="IDSA 2012",
        guideline_year=2012,
        notes=[
            "Obtain bone culture if possible",
            "Duration typically 4-6 weeks",
            "Consider surgical debridement",
            "Step-down to PO after 2-4 weeks if improving"
        ]
    ))
    
    # Chronic Osteomyelitis
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.OSTEOMYELITIS,
        severity=Severity.SEVERE,
        setting=Setting.WARD,
        title="Viêm xương tủy mạn",
        description="Chronic osteomyelitis - requires prolonged therapy",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "6-12 weeks"),
                    DrugDose("Ciprofloxacin", "400mg", "IV", "q12h", "6-12 weeks")
                ],
                indication="Empiric therapy for chronic osteomyelitis",
                rationale="Covers MRSA and Gram-negative including Pseudomonas",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Linezolid", "600mg", "IV/PO", "q12h", "6-12 weeks")
                ],
                indication="MRSA with vancomycin intolerance",
                rationale="Oral option for long-term therapy",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA 2012",
        guideline_year=2012,
        notes=[
            "Surgical debridement usually required",
            "Duration typically 6-12 weeks",
            "Consider suppressive therapy after initial course",
            "TDM required for Vancomycin"
        ]
    ))
    
    # Diabetic Foot Infection
    protocols.append(AntibioticProtocol(
        infection_site=InfectionSite.OSTEOMYELITIS,
        severity=Severity.MODERATE,
        setting=Setting.WARD,
        title="Nhiễm trùng bàn chân đái tháo đường",
        description="Diabetic foot infection - soft tissue and/or bone",
        regimens=[
            Regimen(
                regimen_type=RegimenType.FIRST_LINE,
                drugs=[
                    DrugDose("Ceftriaxone", "2g", "IV", "q24h", "2-4 weeks"),
                    DrugDose("Metronidazole", "500mg", "IV", "q8h", "2-4 weeks")
                ],
                indication="Mild to moderate infection",
                rationale="Covers Gram-negative and anaerobes",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.ALTERNATIVE,
                drugs=[
                    DrugDose("Piperacillin-Tazobactam", "4.5g", "IV", "q8h", "2-4 weeks")
                ],
                indication="Moderate to severe infection",
                rationale="Broader spectrum including Pseudomonas",
                recommendation_level=RecommendationLevel.STRONG
            ),
            Regimen(
                regimen_type=RegimenType.RESCUE,
                drugs=[
                    DrugDose("Vancomycin", "15-20 mg/kg", "IV", "q8-12h", "2-4 weeks"),
                    DrugDose("Meropenem", "1g", "IV", "q8h", "2-4 weeks")
                ],
                indication="Severe infection or MRSA risk",
                rationale="Covers MRSA and resistant Gram-negative",
                recommendation_level=RecommendationLevel.WEAK
            )
        ],
        guideline_source="IDSA 2012",
        guideline_year=2012,
        notes=[
            "Wound care and debridement critical",
            "Duration: 2 weeks for soft tissue, 4 weeks if bone involved",
            "Step-down to PO after improvement",
            "Consider surgical evaluation"
        ]
    ))
    
    collection = ProtocolCollection(protocols=protocols)
    
    # Cache in session state
    import streamlit as st
    st.session_state['_antibiotic_protocols_cache'] = collection
    
    return collection
