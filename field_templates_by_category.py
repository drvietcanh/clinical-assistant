"""
Template field theo nhóm thuốc
Template thông minh dựa trên group field
"""
from typing import Dict, Any, Optional

def get_template_for_category(group: str) -> Dict[str, Any]:
    """
    Lấy template field dựa trên group
    
    Args:
        group: Group field của thuốc
    
    Returns:
        Dict chứa template cho các field
    """
    group_lower = group.lower()
    
    # Template chung
    base_templates = {
        "pregnancy": "Use with caution during pregnancy. Consult healthcare provider.",
        "pharmacokinetics": {
            "absorption": "",
            "distribution": "",
            "metabolism": "",
            "elimination": "",
            "half_life": "",
            "bioavailability": ""
        },
        "storage": "Store at room temperature, away from light and moisture.",
        "interactions": [],
        "precautions": [],
        "contraindications": [],
        "mechanism_of_action": "",
        "monitoring": [],
        "side_effects": [],
    }
    
    # Template theo category
    if "vitamin" in group_lower or "nutrition" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Generally safe during pregnancy when used at recommended doses. Consult healthcare provider.",
            "pharmacokinetics": {
                "absorption": "Well absorbed from gastrointestinal tract",
                "distribution": "Distributed throughout body tissues",
                "metabolism": "Minimal metabolism",
                "elimination": "Renal elimination",
                "half_life": "Variable",
                "bioavailability": "High"
            },
            "storage": "Store at room temperature, away from light and moisture. Protect from heat.",
            "interactions": ["May interact with certain medications. Consult healthcare provider."],
            "precautions": ["Use as directed. Do not exceed recommended dose."],
            "contraindications": ["Hypersensitivity to any component"],
            "mechanism_of_action": "Essential nutrient required for normal physiological functions.",
            "monitoring": ["Monitor for signs of deficiency or excess"],
            "side_effects": ["Generally well-tolerated. May cause mild gastrointestinal upset at high doses."],
        }
    
    elif "fluid" in group_lower or "saline" in group_lower or "ringer" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Generally safe during pregnancy. Standard IV fluid therapy.",
            "pharmacokinetics": {
                "absorption": "IV administration - immediate availability",
                "distribution": "Distributed in extracellular fluid",
                "metabolism": "No metabolism",
                "elimination": "Renal elimination",
                "half_life": "N/A",
                "bioavailability": "100% (IV)"
            },
            "storage": "Store at room temperature. Do not freeze. Check for particulate matter before use.",
            "interactions": ["Generally no significant drug interactions"],
            "precautions": ["Monitor fluid balance, electrolytes, and renal function. Use with caution in patients with heart failure or renal impairment."],
            "contraindications": ["Hypersensitivity to components"],
            "mechanism_of_action": "Replaces fluid and electrolyte losses, maintains hydration and electrolyte balance.",
            "monitoring": ["Monitor fluid balance, electrolytes, blood pressure, and renal function"],
            "side_effects": ["Generally well-tolerated. May cause fluid overload if administered too rapidly or in excessive amounts."],
        }
    
    elif "anesthetic" in group_lower or "anesthesia" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Use with caution during pregnancy. Category varies by specific agent. Consult healthcare provider.",
            "pharmacokinetics": {
                "absorption": "Variable depending on route of administration",
                "distribution": "Distributed to tissues, including CNS",
                "metabolism": "Hepatic metabolism",
                "elimination": "Renal elimination",
                "half_life": "Variable",
                "bioavailability": "Variable"
            },
            "storage": "Store at room temperature or as directed. Protect from light.",
            "interactions": ["May interact with CNS depressants, MAOIs, and other medications. Consult healthcare provider."],
            "precautions": ["Use with caution in patients with cardiovascular disease, hepatic or renal impairment. Monitor vital signs."],
            "contraindications": ["Hypersensitivity, severe cardiovascular disease, severe hepatic or renal impairment"],
            "mechanism_of_action": "Blocks nerve conduction or alters CNS function to produce anesthesia or analgesia.",
            "monitoring": ["Monitor vital signs, level of consciousness, respiratory function, and cardiovascular status"],
            "side_effects": ["May cause hypotension, bradycardia, respiratory depression, nausea, vomiting, and local reactions."],
        }
    
    elif "vaccine" in group_lower or "antiserum" in group_lower or "antivenom" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Use with caution during pregnancy. Consult healthcare provider. Benefits must outweigh risks.",
            "pharmacokinetics": {
                "absorption": "IM/IV administration",
                "distribution": "Distributed in plasma",
                "metabolism": "Minimal metabolism",
                "elimination": "Renal elimination",
                "half_life": "Variable",
                "bioavailability": "Variable"
            },
            "storage": "Store in refrigerator (2-8°C). Do not freeze. Protect from light.",
            "interactions": ["May interact with immunosuppressive medications. Consult healthcare provider."],
            "precautions": ["Monitor for allergic reactions. Have epinephrine available. Use with caution in patients with known allergies."],
            "contraindications": ["Hypersensitivity to components, severe allergic reaction to previous dose"],
            "mechanism_of_action": "Provides passive immunity or stimulates active immune response against specific pathogens or toxins.",
            "monitoring": ["Monitor for allergic reactions, fever, and injection site reactions"],
            "side_effects": ["May cause injection site reactions, fever, allergic reactions, and rarely anaphylaxis."],
        }
    
    elif "antidote" in group_lower or "toxicology" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Use during pregnancy only if clearly needed. Benefits must outweigh risks.",
            "pharmacokinetics": {
                "absorption": "Variable depending on route",
                "distribution": "Variable",
                "metabolism": "Variable",
                "elimination": "Variable",
                "half_life": "Variable",
                "bioavailability": "Variable"
            },
            "storage": "Store as directed. Some require refrigeration. Check product labeling.",
            "interactions": ["May interact with other medications. Consult healthcare provider."],
            "precautions": ["Use only for specific poison/toxin. Monitor patient closely. May require supportive care."],
            "contraindications": ["Hypersensitivity to components"],
            "mechanism_of_action": "Binds to or neutralizes specific toxins or poisons, preventing or reversing their effects.",
            "monitoring": ["Monitor vital signs, response to treatment, and signs of toxicity"],
            "side_effects": ["May cause allergic reactions, injection site reactions, and other adverse effects depending on specific agent."],
        }
    
    elif "migraine" in group_lower or "triptan" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Not recommended during pregnancy. Category C. Use only if benefits outweigh risks.",
            "pharmacokinetics": {
                "absorption": "Well absorbed orally",
                "distribution": "Distributed to tissues",
                "metabolism": "Hepatic metabolism via CYP enzymes",
                "elimination": "Renal elimination",
                "half_life": "2-4 hours",
                "bioavailability": "Variable"
            },
            "storage": "Store at room temperature. Protect from light and moisture.",
            "interactions": ["Contraindicated with MAOIs. May interact with SSRIs, ergot derivatives, and other medications. Consult healthcare provider."],
            "precautions": ["Use with caution in patients with cardiovascular disease, uncontrolled hypertension, and hepatic or renal impairment."],
            "contraindications": ["Hypersensitivity, coronary artery disease, uncontrolled hypertension, history of stroke or TIA, use of MAOIs within 14 days"],
            "mechanism_of_action": "Selective serotonin 5-HT1B/1D receptor agonist. Causes vasoconstriction of cranial blood vessels and inhibits trigeminal nerve activation.",
            "monitoring": ["Monitor blood pressure, heart rate, and response to treatment"],
            "side_effects": ["May cause chest tightness, dizziness, fatigue, nausea, and injection site reactions."],
        }
    
    elif "hematology" in group_lower or "anemia" in group_lower or "iron" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Generally safe during pregnancy. May be used to treat iron deficiency anemia.",
            "pharmacokinetics": {
                "absorption": "Variable, better absorbed on empty stomach",
                "distribution": "Distributed to tissues, stored in ferritin",
                "metabolism": "Minimal metabolism",
                "elimination": "Minimal elimination, stored in body",
                "half_life": "Variable",
                "bioavailability": "Variable"
            },
            "storage": "Store at room temperature. Protect from light and moisture.",
            "interactions": ["May interact with antacids, tetracyclines, and other medications. Separate administration by 2 hours."],
            "precautions": ["Use with caution in patients with hemochromatosis or iron overload. May cause gastrointestinal upset."],
            "contraindications": ["Hypersensitivity, hemochromatosis, hemosiderosis, hemolytic anemia"],
            "mechanism_of_action": "Replaces iron stores in the body. Iron is essential for hemoglobin synthesis and oxygen transport.",
            "monitoring": ["Monitor hemoglobin, hematocrit, ferritin levels, and response to treatment"],
            "side_effects": ["May cause gastrointestinal upset, constipation, dark stools, and rarely allergic reactions."],
        }
    
    elif "psychiatry" in group_lower or "mood" in group_lower or "stabilizer" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Use with caution during pregnancy. Category varies. May cause birth defects. Consult healthcare provider.",
            "pharmacokinetics": {
                "absorption": "Well absorbed orally",
                "distribution": "Distributed to tissues, crosses blood-brain barrier",
                "metabolism": "Hepatic metabolism",
                "elimination": "Renal elimination",
                "half_life": "Variable",
                "bioavailability": "Variable"
            },
            "storage": "Store at room temperature. Protect from light and moisture.",
            "interactions": ["May interact with other CNS medications, oral contraceptives, and other medications. Consult healthcare provider."],
            "precautions": ["Use with caution in patients with hepatic or renal impairment. Monitor for signs of toxicity. May require dose adjustment."],
            "contraindications": ["Hypersensitivity, severe hepatic or renal impairment"],
            "mechanism_of_action": "Modulates neurotransmitter activity in the brain to stabilize mood and prevent mood episodes.",
            "monitoring": ["Monitor drug levels, liver function, renal function, complete blood count, and response to treatment"],
            "side_effects": ["May cause dizziness, drowsiness, nausea, rash, and rarely serious skin reactions or blood dyscrasias."],
        }
    
    elif "rheumatology" in group_lower or "osteoporosis" in group_lower or "bisphosphonate" in group_lower:
        return {
            **base_templates,
            "pregnancy": "Contraindicated during pregnancy. Category D. May cause fetal harm.",
            "pharmacokinetics": {
                "absorption": "Poor oral absorption, better with IV",
                "distribution": "Binds to bone",
                "metabolism": "Minimal metabolism",
                "elimination": "Renal elimination",
                "half_life": "Very long (years in bone)",
                "bioavailability": "Low (oral)"
            },
            "storage": "Store at room temperature. Protect from light and moisture.",
            "interactions": ["May interact with calcium supplements, antacids, and other medications. Separate administration."],
            "precautions": ["Use with caution in patients with renal impairment. May cause hypocalcemia. Monitor calcium and vitamin D levels."],
            "contraindications": ["Hypersensitivity, hypocalcemia, severe renal impairment, pregnancy"],
            "mechanism_of_action": "Inhibits bone resorption by osteoclasts, leading to increased bone density and reduced fracture risk.",
            "monitoring": ["Monitor calcium, phosphorus, vitamin D levels, renal function, and bone density"],
            "side_effects": ["May cause gastrointestinal upset, hypocalcemia, musculoskeletal pain, and rarely osteonecrosis of the jaw."],
        }
    
    else:
        # Default template
        return base_templates

def get_smart_template(drug_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Lấy template thông minh dựa trên dữ liệu thuốc
    
    Args:
        drug_data: Dữ liệu thuốc
    
    Returns:
        Dict chứa template cho các field thiếu
    """
    group = drug_data.get('group', '')
    return get_template_for_category(group)

def fill_missing_fields_with_template(drug_data: Dict[str, Any], 
                                     fields_to_fill: Optional[list] = None) -> Dict[str, Any]:
    """
    Điền field thiếu với template thông minh
    
    Args:
        drug_data: Dữ liệu thuốc
        fields_to_fill: Danh sách field cần điền (None = tất cả field thiếu)
    
    Returns:
        Dict với field đã điền
    """
    from drugs.field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
    
    result = drug_data.copy()
    template = get_smart_template(drug_data)
    
    if fields_to_fill is None:
        # Fill all missing standard fields
        fields_to_fill = [f for f in STANDARD_14_FIELDS if f not in result]
    
    for field in fields_to_fill:
        if field not in result and field in template:
            import copy
            result[field] = copy.deepcopy(template[field])
    
    return result

if __name__ == "__main__":
    # Test
    test_drugs = [
        {"group": "Nutrition - Vitamins", "vietnamese_name": "Vitamin C"},
        {"group": "Emergency - IV Fluids", "vietnamese_name": "Sodium Chloride"},
        {"group": "Anesthesia - Local Anesthetics", "vietnamese_name": "Lidocaine"},
    ]
    
    for drug in test_drugs:
        print(f"\nDrug: {drug['vietnamese_name']}")
        print(f"Group: {drug['group']}")
        template = get_smart_template(drug)
        print(f"Template pregnancy: {template.get('pregnancy', 'N/A')[:50]}...")
        print(f"Template storage: {template.get('storage', 'N/A')[:50]}...")

