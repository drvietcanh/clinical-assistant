"""
MIC Breakpoints and Susceptibility Data
Based on CLSI, EUCAST, and clinical guidelines
"""

MIC_BREAKPOINTS = {
    "Vancomycin": {
        "organisms": {
            "Staphylococcus aureus (MSSA)": {
                "sensitive": "< 2 mg/L",
                "intermediate": "2-4 mg/L",
                "resistant": "> 4 mg/L",
                "notes": "MRSA: S < 2, I 2-4, R > 4"
            },
            "Enterococcus faecalis": {
                "sensitive": "< 4 mg/L",
                "intermediate": "4-8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Streptococcus pneumoniae": {
                "sensitive": "< 1 mg/L",
                "intermediate": "1-2 mg/L",
                "resistant": "> 2 mg/L"
            }
        },
        "common_susceptibility": {
            "MSSA": "S (95-98%)",
            "MRSA": "S (90-95%)",
            "Enterococcus faecalis": "S (85-90%)",
            "Enterococcus faecium": "R (60-70%)",
            "Coagulase-negative staphylococci": "S (90-95%)"
        }
    },
    "Ceftriaxone": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 1 mg/L",
                "intermediate": "1-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 1 mg/L",
                "intermediate": "1-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Streptococcus pneumoniae": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "0.5-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Neisseria meningitidis": {
                "sensitive": "< 0.12 mg/L",
                "intermediate": "0.12-0.5 mg/L",
                "resistant": "> 0.5 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (55-65%) - R: 35-45% tại VN",
            "K. pneumoniae": "S (50-60%) - R: 40-50% tại VN",
            "S. pneumoniae": "S (85-90%)",
            "N. meningitidis": "S (95-98%)",
            "H. influenzae": "S (90-95%)"
        }
    },
    "Meropenem": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 1 mg/L",
                "intermediate": "2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 1 mg/L",
                "intermediate": "2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Acinetobacter baumannii": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (90-95%) - R: 5-10% tại VN",
            "K. pneumoniae": "S (75-85%) - R: 15-25% tại VN",
            "P. aeruginosa": "S (70-80%) - R: 20-30% tại VN",
            "A. baumannii": "S (40-50%) - R: 50-60% tại VN",
            "Enterobacteriaceae": "S (85-90%)"
        }
    },
    "Piperacillin-Tazobactam": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 8/4 mg/L",
                "intermediate": "16/4 mg/L",
                "resistant": "> 16/4 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 8/4 mg/L",
                "intermediate": "16/4 mg/L",
                "resistant": "> 16/4 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 16/4 mg/L",
                "intermediate": "32/4 mg/L",
                "resistant": "> 32/4 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (60-70%) - R: 30-40% tại VN",
            "K. pneumoniae": "S (55-65%) - R: 35-45% tại VN",
            "P. aeruginosa": "S (70-80%) - R: 20-30% tại VN",
            "Enterococcus faecalis": "S (85-90%)"
        }
    },
    "Ciprofloxacin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 0.25 mg/L",
                "intermediate": "0.5 mg/L",
                "resistant": "> 1 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 0.25 mg/L",
                "intermediate": "0.5 mg/L",
                "resistant": "> 1 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "1 mg/L",
                "resistant": "> 2 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (40-50%) - R: 50-60% tại VN",
            "K. pneumoniae": "S (35-45%) - R: 55-65% tại VN",
            "P. aeruginosa": "S (60-70%) - R: 30-40% tại VN",
            "Enterobacteriaceae": "S (45-55%) - R: 45-55% tại VN"
        }
    },
    "Levofloxacin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "1 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Streptococcus pneumoniae": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (45-55%) - R: 45-55% tại VN",
            "S. pneumoniae": "S (85-90%)",
            "H. influenzae": "S (95-98%)"
        }
    },
    "Gentamicin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (70-80%) - R: 20-30% tại VN",
            "K. pneumoniae": "S (65-75%) - R: 25-35% tại VN",
            "P. aeruginosa": "S (75-85%) - R: 15-25% tại VN"
        }
    },
    "Amikacin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 16 mg/L",
                "intermediate": "32 mg/L",
                "resistant": "> 32 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 16 mg/L",
                "intermediate": "32 mg/L",
                "resistant": "> 32 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 16 mg/L",
                "intermediate": "32 mg/L",
                "resistant": "> 32 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (85-90%) - R: 10-15% tại VN",
            "K. pneumoniae": "S (80-85%) - R: 15-20% tại VN",
            "P. aeruginosa": "S (80-85%) - R: 15-20% tại VN",
            "Acinetobacter": "S (60-70%) - R: 30-40% tại VN"
        }
    },
    "Azithromycin": {
        "organisms": {
            "Streptococcus pneumoniae": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "0.5-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Haemophilus influenzae": {
                "sensitive": "< 4 mg/L",
                "intermediate": "4-8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Staphylococcus aureus": {
                "sensitive": "< 2 mg/L",
                "intermediate": "2-8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "S. pneumoniae": "S (50-60%) - R: 40-50% tại VN",
            "H. influenzae": "S (90-95%)",
            "M. pneumoniae": "S (95-98%)",
            "C. pneumoniae": "S (95-98%)",
            "S. aureus": "S (60-70%) - R: 30-40% tại VN"
        }
    },
    "Clindamycin": {
        "organisms": {
            "Staphylococcus aureus": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "0.5-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Streptococcus pyogenes": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "0.5-2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Bacteroides fragilis": {
                "sensitive": "< 4 mg/L",
                "intermediate": "4-8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "MSSA": "S (85-90%)",
            "MRSA": "S (75-85%) - R: 15-25% tại VN",
            "S. pyogenes": "S (90-95%)",
            "B. fragilis": "S (85-90%)"
        }
    },
    "Cefepime": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4-8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4-8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 8 mg/L",
                "intermediate": "16 mg/L",
                "resistant": "> 16 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (60-70%) - R: 30-40% tại VN",
            "K. pneumoniae": "S (55-65%) - R: 35-45% tại VN",
            "P. aeruginosa": "S (70-80%) - R: 20-30% tại VN",
            "Enterobacteriaceae": "S (65-75%)"
        }
    },
    "Ceftazidime": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 8 mg/L",
                "intermediate": "16 mg/L",
                "resistant": "> 16 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (55-65%) - R: 35-45% tại VN",
            "P. aeruginosa": "S (65-75%) - R: 25-35% tại VN",
            "K. pneumoniae": "S (50-60%) - R: 40-50% tại VN"
        }
    },
    "Tobramycin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (70-80%) - R: 20-30% tại VN",
            "P. aeruginosa": "S (75-85%) - R: 15-25% tại VN",
            "K. pneumoniae": "S (65-75%) - R: 25-35% tại VN"
        }
    },
    "Linezolid": {
        "organisms": {
            "Staphylococcus aureus (MSSA)": {
                "sensitive": "< 4 mg/L",
                "intermediate": "N/A",
                "resistant": "> 4 mg/L"
            },
            "Staphylococcus aureus (MRSA)": {
                "sensitive": "< 4 mg/L",
                "intermediate": "N/A",
                "resistant": "> 4 mg/L"
            },
            "Enterococcus faecalis": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Enterococcus faecium": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Streptococcus pneumoniae": {
                "sensitive": "< 2 mg/L",
                "intermediate": "N/A",
                "resistant": "> 2 mg/L"
            }
        },
        "common_susceptibility": {
            "MSSA": "S (> 99%)",
            "MRSA": "S (> 99%)",
            "VRE (E. faecalis)": "S (> 99%)",
            "VRE (E. faecium)": "S (> 99%)",
            "S. pneumoniae": "S (> 99%)"
        }
    },
    "Colistin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "Acinetobacter baumannii": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli (MDR)": "S (85-90%) - R: 10-15% tại VN",
            "K. pneumoniae (MDR)": "S (80-85%) - R: 15-20% tại VN",
            "P. aeruginosa (MDR)": "S (75-85%) - R: 15-25% tại VN",
            "A. baumannii (MDR)": "S (90-95%) - R: 5-10% tại VN",
            "notes": "Lựa chọn cuối cùng cho MDR/XDR. Độc tính cao (thận, thần kinh)"
        }
    },
    "Ertapenem": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "1 mg/L",
                "resistant": "> 1 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 0.5 mg/L",
                "intermediate": "1 mg/L",
                "resistant": "> 1 mg/L"
            },
            "Bacteroides fragilis": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (90-95%) - R: 5-10% tại VN",
            "K. pneumoniae": "S (80-90%) - R: 10-20% tại VN",
            "B. fragilis": "S (95-98%)",
            "Enterobacteriaceae": "S (85-90%)",
            "notes": "KHÔNG hiệu quả với Pseudomonas, Acinetobacter"
        }
    },
    "Imipenem-Cilastatin": {
        "organisms": {
            "E. coli": {
                "sensitive": "< 1 mg/L",
                "intermediate": "2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 1 mg/L",
                "intermediate": "2 mg/L",
                "resistant": "> 2 mg/L"
            },
            "Pseudomonas aeruginosa": {
                "sensitive": "< 4 mg/L",
                "intermediate": "8 mg/L",
                "resistant": "> 8 mg/L"
            },
            "Acinetobacter baumannii": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            }
        },
        "common_susceptibility": {
            "E. coli": "S (90-95%) - R: 5-10% tại VN",
            "K. pneumoniae": "S (75-85%) - R: 15-25% tại VN",
            "P. aeruginosa": "S (70-80%) - R: 20-30% tại VN",
            "A. baumannii": "S (40-50%) - R: 50-60% tại VN"
        }
    },
    "Cefazolin": {
        "organisms": {
            "Staphylococcus aureus (MSSA)": {
                "sensitive": "< 2 mg/L",
                "intermediate": "4 mg/L",
                "resistant": "> 4 mg/L"
            },
            "E. coli": {
                "sensitive": "< 8 mg/L",
                "intermediate": "16 mg/L",
                "resistant": "> 16 mg/L"
            },
            "Klebsiella pneumoniae": {
                "sensitive": "< 8 mg/L",
                "intermediate": "16 mg/L",
                "resistant": "> 16 mg/L"
            }
        },
        "common_susceptibility": {
            "MSSA": "S (90-95%)",
            "E. coli": "S (60-70%) - R: 30-40% tại VN",
            "K. pneumoniae": "S (55-65%) - R: 35-45% tại VN",
            "S. pyogenes": "S (95-98%)"
        }
    }
}


def get_mic_breakpoints(antibiotic_name):
    """Get MIC breakpoints for an antibiotic"""
    return MIC_BREAKPOINTS.get(antibiotic_name, {})


def get_common_susceptibility(antibiotic_name):
    """Get common susceptibility patterns for an antibiotic"""
    mic_data = get_mic_breakpoints(antibiotic_name)
    return mic_data.get("common_susceptibility", {})

