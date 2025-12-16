"""
Comprehensive Protocol Checker
Kiểm tra toàn diện tất cả các protocol trong hệ thống
"""

import os
import ast
import importlib.util
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import sys

# Colors for output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(80)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*80}{Colors.END}\n")

def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text: str):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text: str):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

class ProtocolChecker:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.protocols_path = self.base_path / "protocols"
        self.pages_path = self.base_path / "pages"
        self.issues = []
        self.stats = {
            "total_protocols": 0,
            "protocols_with_issues": 0,
            "missing_exports": 0,
            "missing_routes": 0,
            "missing_references": 0,
            "missing_files": 0
        }
        
    def check_all(self):
        """Run all checks"""
        print_header("KIỂM TRA TOÀN DIỆN CÁC PROTOCOL")
        
        # 1. Check protocol files exist
        print_header("1. KIỂM TRA FILE PROTOCOL")
        protocol_files = self.check_protocol_files()
        
        # 2. Check exports in __init__.py files
        print_header("2. KIỂM TRA EXPORTS")
        exports = self.check_exports()
        
        # 3. Check imports in main page
        print_header("3. KIỂM TRA IMPORTS TRONG TRANG CHÍNH")
        imports = self.check_main_page_imports()
        
        # 4. Check routing
        print_header("4. KIỂM TRA ROUTING")
        routes = self.check_routing()
        
        # 5. Check references
        print_header("5. KIỂM TRA REFERENCES")
        references = self.check_references()
        
        # 6. Check render functions exist
        print_header("6. KIỂM TRA RENDER FUNCTIONS")
        render_functions = self.check_render_functions()
        
        # 7. Cross-check everything
        print_header("7. KIỂM TRA CHÉO")
        self.cross_check(protocol_files, exports, imports, routes, references, render_functions)
        
        # 8. Generate report
        print_header("8. BÁO CÁO TỔNG KẾT")
        self.generate_report()
        
    def check_protocol_files(self) -> Dict[str, Path]:
        """Check all protocol files exist"""
        protocol_files = {}
        
        # Expected protocol structure
        expected_protocols = {
            # Emergency
            "emergency/sepsis.py": "render_sepsis",
            "emergency/sepsis_3hour.py": "render_sepsis_3hour",
            "emergency/shock.py": "render_shock",
            "emergency/stroke.py": "render_stroke",
            "emergency/gi_bleeding.py": "render_gi_bleeding",
            "emergency/dka.py": "render_dka",
            "emergency/electrolytes.py": "render_electrolytes",
            "emergency/anaphylaxis.py": "render_anaphylaxis",
            "emergency/hypertensive_emergency.py": "render_hypertensive_emergency",
            "emergency/status_epilepticus.py": "render_status_epilepticus",
            "emergency/opioid_overdose.py": "render_opioid_overdose",
            "emergency/alcohol_withdrawal.py": "render_alcohol_withdrawal",
            "emergency/paracetamol_overdose.py": "render_paracetamol_overdose",
            "emergency/salicylate_overdose.py": "render_salicylate_overdose",
            "emergency/carbon_monoxide_poisoning.py": "render_carbon_monoxide_poisoning",
            "emergency/organophosphate_poisoning.py": "render_organophosphate_poisoning",
            "emergency/toxic_alcohol_poisoning.py": "render_toxic_alcohol_poisoning",
            "emergency/malignant_arrhythmias.py": "render_malignant_arrhythmias",
            "emergency/pneumothorax.py": "render_pneumothorax",
            "emergency/traumatic_brain_injury.py": "render_traumatic_brain_injury",
            "emergency/drowning.py": "render_drowning",
            "emergency/heat_stroke.py": "render_heat_stroke",
            "emergency/hypothermia.py": "render_hypothermia",
            
            # Respiratory
            "respiratory/copd.py": "render_copd",
            "respiratory/asthma.py": "render_asthma",
            
            # Cardiology
            "cardiology/acs.py": "render_acs",
            "cardiology/heart_failure.py": "render_hf",
            "cardiology/atrial_fibrillation.py": "render_atrial_fibrillation",
            "cardiology/dvt_pe.py": "render_dvt_pe",
            "cardiology/bradycardia.py": "render_bradycardia",
            "cardiology/tachycardia.py": "render_tachycardia",
            
            # Nephrology
            "nephrology/aki.py": "render_aki",
            
            # Infectious
            "infectious/cap.py": "render_cap",
            "infectious/hap_vap.py": "render_hap_vap",
            "infectious/cdiff.py": "render_cdiff",
            "infectious/meningitis.py": "render_meningitis",
            "infectious/endocarditis.py": "render_endocarditis",
            
            # Endocrinology
            "endocrinology/thyrotoxic_crisis.py": "render_thyrotoxic_crisis",
            "endocrinology/myxedema_coma.py": "render_myxedema_coma",
            "endocrinology/adrenal_crisis.py": "render_adrenal_crisis",
            "endocrinology/hhs.py": "render_hhs",
            "endocrinology/hypoglycemia.py": "render_hypoglycemia",
            
            # Neurology
            "neurology/serotonin_syndrome.py": "render_serotonin_syndrome",
            "neurology/neuroleptic_malignant_syndrome.py": "render_neuroleptic_malignant_syndrome",
            "neurology/intracranial_hypertension.py": "render_intracranial_hypertension",
            
            # Obstetrics
            "obstetrics/eclampsia.py": "render_eclampsia",
            "obstetrics/postpartum_hemorrhage.py": "render_postpartum_hemorrhage",
            
            # Dermatology
            "dermatology/stevens_johnson_syndrome.py": "render_stevens_johnson_syndrome",
            
            # Gastroenterology
            "gastroenterology/acute_pancreatitis.py": "render_acute_pancreatitis",
            "gastroenterology/acute_liver_failure.py": "render_acute_liver_failure",
            "gastroenterology/ibd_exacerbation.py": "render_ibd_exacerbation",
            
            # Hematology
            "hematology/transfusion.py": "render_transfusion",
            "hematology/anticoagulation_reversal.py": "render_anticoagulation_reversal",
            
            # Oncology
            "oncology/tls.py": "render_tls",
            "oncology/febrile_neutropenia.py": "render_febrile_neutropenia",
            "oncology/hypercalcemia.py": "render_hypercalcemia",
            
            # Critical Care
            "critical_care/delirium.py": "render_delirium",
            "critical_care/sedation.py": "render_sedation",
            "critical_care/ards.py": "render_ards",
            "critical_care/ventilator_weaning.py": "render_ventilator_weaning",
            "critical_care/stress_ulcer.py": "render_stress_ulcer",
            
            # Pain
            "pain/acute_pain.py": "render_acute_pain",
            
            # Rheumatology
            "rheumatology/acute_gout.py": "render_acute_gout",
            "rheumatology/ra_flare.py": "render_ra_flare",
        }
        
        for rel_path, func_name in expected_protocols.items():
            file_path = self.protocols_path / rel_path
            if file_path.exists():
                protocol_files[func_name] = file_path
                print_success(f"Found: {rel_path}")
                self.stats["total_protocols"] += 1
            else:
                print_error(f"Missing: {rel_path}")
                self.issues.append(f"Missing file: {rel_path}")
                self.stats["missing_files"] += 1
                self.stats["protocols_with_issues"] += 1
        
        return protocol_files
    
    def check_exports(self) -> Set[str]:
        """Check exports in protocols/__init__.py"""
        init_file = self.protocols_path / "__init__.py"
        if not init_file.exists():
            print_error("protocols/__init__.py not found!")
            return set()
        
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the file to find all exports
        exports = set()
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        exports.add(alias.name)
        except Exception as e:
            print_error(f"Error parsing __init__.py: {e}")
        
        # Also check __all__
        if '__all__' in content:
            # Extract __all__ list
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id == '__all__':
                                if isinstance(node.value, ast.List):
                                    for elt in node.value.elts:
                                        if isinstance(elt, ast.Constant):
                                            exports.add(elt.value)
            except:
                pass
        
        print_info(f"Found {len(exports)} exports in protocols/__init__.py")
        return exports
    
    def check_main_page_imports(self) -> Set[str]:
        """Check imports in pages/04_📋_Protocols.py"""
        main_page = self.pages_path / "04_📋_Protocols.py"
        if not main_page.exists():
            print_error("Main protocol page not found!")
            return set()
        
        with open(main_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        imports = set()
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    if node.module and 'protocols' in node.module:
                        for alias in node.names:
                            imports.add(alias.name)
        except Exception as e:
            print_error(f"Error parsing main page: {e}")
        
        print_info(f"Found {len(imports)} imports in main page")
        return imports
    
    def check_routing(self) -> Dict[str, List[str]]:
        """Check routing logic in main page"""
        main_page = self.pages_path / "04_📋_Protocols.py"
        if not main_page.exists():
            return {}
        
        with open(main_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        routes = {}
        # Find all render_* function calls
        import re
        pattern = r'(\w+)\s*\(\)'
        matches = re.findall(pattern, content)
        
        render_calls = [m for m in matches if m.startswith('render_')]
        
        for call in render_calls:
            routes[call] = []
            # Find the condition that leads to this call
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if call in line and 'render_' in line:
                    # Get context (previous lines)
                    context_start = max(0, i-3)
                    context = '\n'.join(lines[context_start:i+1])
                    routes[call].append(context)
        
        print_info(f"Found {len(routes)} route handlers")
        return routes
    
    def check_references(self) -> Set[str]:
        """Check references configuration"""
        ref_file = self.protocols_path / "references_config.py"
        if not ref_file.exists():
            print_error("references_config.py not found!")
            return set()
        
        with open(ref_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all protocol names in PROTOCOL_REFERENCES
        protocols_with_refs = set()
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    # This is PROTOCOL_REFERENCES dict
                    for key in node.keys:
                        if isinstance(key, ast.Constant):
                            protocols_with_refs.add(key.value)
        except Exception as e:
            print_error(f"Error parsing references_config.py: {e}")
        
        print_info(f"Found {len(protocols_with_refs)} protocols with references")
        return protocols_with_refs
    
    def check_render_functions(self) -> Dict[str, bool]:
        """Check if render functions exist in protocol files"""
        render_functions = {}
        
        # Get all protocol files
        for py_file in self.protocols_path.rglob("*.py"):
            if py_file.name == "__init__.py" or py_file.name == "TEMPLATE_PROTOCOL.py":
                continue
            
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for render_* functions
            import re
            pattern = r'def\s+(render_\w+)\s*\('
            matches = re.findall(pattern, content)
            
            for func_name in matches:
                render_functions[func_name] = True
                if func_name not in render_functions:
                    render_functions[func_name] = True
        
        print_info(f"Found {len(render_functions)} render functions")
        return render_functions
    
    def cross_check(self, protocol_files: Dict, exports: Set, imports: Set, 
                   routes: Dict, references: Set, render_functions: Dict):
        """Cross-check everything for consistency"""
        
        # Get all expected render functions from protocol files
        expected_render_functions = set(protocol_files.keys())
        
        # 1. Check exports vs expected
        missing_exports = expected_render_functions - exports
        if missing_exports:
            print_warning(f"Missing exports: {len(missing_exports)}")
            for func in sorted(missing_exports):
                print_error(f"  - {func} not exported in protocols/__init__.py")
                self.stats["missing_exports"] += 1
        
        # 2. Check imports vs exports
        missing_imports = exports - imports
        if missing_imports:
            print_warning(f"Exported but not imported in main page: {len(missing_imports)}")
            for func in sorted(missing_imports):
                print_warning(f"  - {func} exported but not imported")
        
        # 3. Check routes vs imports
        imported_functions = imports
        routed_functions = set(routes.keys())
        missing_routes = imported_functions - routed_functions
        if missing_routes:
            print_warning(f"Imported but not routed: {len(missing_routes)}")
            for func in sorted(missing_routes):
                print_warning(f"  - {func} imported but no route handler found")
                self.stats["missing_routes"] += 1
        
        # 4. Check render functions exist
        missing_render = expected_render_functions - set(render_functions.keys())
        if missing_render:
            print_error(f"Render functions not found: {len(missing_render)}")
            for func in sorted(missing_render):
                print_error(f"  - {func} function not found in protocol files")
        
        # 5. Check references
        # Map protocol names to render function names
        protocol_name_map = {
            "Sepsis": "render_sepsis",
            "Sepsis 3-Hour": "render_sepsis_3hour",
            "Shock": "render_shock",
            "Stroke": "render_stroke",
            "GI Bleeding": "render_gi_bleeding",
            "DKA": "render_dka",
            "Electrolytes": "render_electrolytes",
            "Anaphylaxis": "render_anaphylaxis",
            "Hypertensive Emergency": "render_hypertensive_emergency",
            "Status Epilepticus": "render_status_epilepticus",
            "Opioid Overdose": "render_opioid_overdose",
            "Alcohol Withdrawal": "render_alcohol_withdrawal",
            "Paracetamol Overdose": "render_paracetamol_overdose",
            "Salicylate Overdose": "render_salicylate_overdose",
            "Carbon Monoxide Poisoning": "render_carbon_monoxide_poisoning",
            "Organophosphate Poisoning": "render_organophosphate_poisoning",
            "Toxic Alcohol Poisoning": "render_toxic_alcohol_poisoning",
            "Malignant Arrhythmias": "render_malignant_arrhythmias",
            "Pneumothorax": "render_pneumothorax",
            "Traumatic Brain Injury": "render_traumatic_brain_injury",
            "Drowning": "render_drowning",
            "Heat Stroke": "render_heat_stroke",
            "Hypothermia": "render_hypothermia",
            "COPD": "render_copd",
            "Asthma": "render_asthma",
            "ACS": "render_acs",
            "Heart Failure": "render_hf",
            "Atrial Fibrillation": "render_atrial_fibrillation",
            "DVT/PE": "render_dvt_pe",
            "Bradycardia": "render_bradycardia",
            "Tachycardia": "render_tachycardia",
            "AKI": "render_aki",
            "CAP": "render_cap",
            "HAP/VAP": "render_hap_vap",
            "C. diff": "render_cdiff",
            "Meningitis": "render_meningitis",
            "Endocarditis": "render_endocarditis",
            "Thyrotoxic Crisis": "render_thyrotoxic_crisis",
            "Myxedema Coma": "render_myxedema_coma",
            "Adrenal Crisis": "render_adrenal_crisis",
            "HHS": "render_hhs",
            "Hypoglycemia": "render_hypoglycemia",
            "Serotonin Syndrome": "render_serotonin_syndrome",
            "Neuroleptic Malignant Syndrome": "render_neuroleptic_malignant_syndrome",
            "Intracranial Hypertension": "render_intracranial_hypertension",
            "Eclampsia": "render_eclampsia",
            "Postpartum Hemorrhage": "render_postpartum_hemorrhage",
            "Stevens-Johnson Syndrome": "render_stevens_johnson_syndrome",
            "Acute Pancreatitis": "render_acute_pancreatitis",
            "Acute Liver Failure": "render_acute_liver_failure",
            "IBD Exacerbation": "render_ibd_exacerbation",
            "Transfusion": "render_transfusion",
            "Anticoagulation Reversal": "render_anticoagulation_reversal",
            "TLS": "render_tls",
            "Febrile Neutropenia": "render_febrile_neutropenia",
            "Hypercalcemia": "render_hypercalcemia",
            "Delirium": "render_delirium",
            "Sedation": "render_sedation",
            "ARDS": "render_ards",
            "Ventilator Weaning": "render_ventilator_weaning",
            "Stress Ulcer": "render_stress_ulcer",
            "Acute Pain": "render_acute_pain",
            "Acute Gout": "render_acute_gout",
            "RA Flare": "render_ra_flare",
        }
        
        render_funcs_with_refs = set()
        for protocol_name, render_func in protocol_name_map.items():
            if protocol_name in references:
                render_funcs_with_refs.add(render_func)
        
        missing_refs = expected_render_functions - render_funcs_with_refs
        if missing_refs:
            print_warning(f"Protocols without references: {len(missing_refs)}")
            for func in sorted(missing_refs):
                print_warning(f"  - {func} may not have references configured")
                self.stats["missing_references"] += 1
    
    def generate_report(self):
        """Generate final report"""
        print("\n" + "="*80)
        print(f"{Colors.BOLD}THỐNG KÊ TỔNG KẾT{Colors.END}")
        print("="*80)
        
        print(f"\n{Colors.BOLD}Tổng số protocol:{Colors.END} {self.stats['total_protocols']}")
        print(f"{Colors.BOLD}Protocol có vấn đề:{Colors.END} {self.stats['protocols_with_issues']}")
        print(f"{Colors.BOLD}Thiếu exports:{Colors.END} {self.stats['missing_exports']}")
        print(f"{Colors.BOLD}Thiếu routes:{Colors.END} {self.stats['missing_routes']}")
        print(f"{Colors.BOLD}Thiếu references:{Colors.END} {self.stats['missing_references']}")
        print(f"{Colors.BOLD}Thiếu files:{Colors.END} {self.stats['missing_files']}")
        
        if self.issues:
            print(f"\n{Colors.BOLD}{Colors.RED}CÁC VẤN ĐỀ PHÁT HIỆN:{Colors.END}")
            for i, issue in enumerate(self.issues, 1):
                print(f"  {i}. {issue}")
        else:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ KHÔNG CÓ VẤN ĐỀ NÀO!{Colors.END}")
        
        print("\n" + "="*80)

if __name__ == "__main__":
    checker = ProtocolChecker()
    checker.check_all()

