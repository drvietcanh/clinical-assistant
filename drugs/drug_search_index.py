"""
Drug Search Index System
Provides fast O(1) lookup and advanced search capabilities
"""

from typing import Dict, List, Set, Optional
from collections import defaultdict
import re


class DrugSearchIndex:
    """
    Fast search index for drug database
    Supports:
    - Name lookup: O(1)
    - Group lookup: O(1)
    - Indication search: O(1)
    - Autocomplete: O(1)
    - Fuzzy search: O(n) but with small n
    """
    
    def __init__(self):
        # Primary indices
        self.name_index: Dict[str, dict] = {}           # Lowercase name → drug data
        self.group_index: Dict[str, List[str]] = defaultdict(list)  # Group → drug names
        self.indication_index: Dict[str, Set[str]] = defaultdict(set)  # Indication keyword → drug names
        self.prefix_index: Dict[str, List[str]] = defaultdict(list)  # 3-char prefix → drug names
        
        # Vietnamese name index
        self.vietnamese_index: Dict[str, str] = {}      # Vietnamese name → English name
        
        # Brand name index
        self.brand_index: Dict[str, str] = {}           # Brand name → Generic name
        
        # Route index
        self.route_index: Dict[str, Set[str]] = defaultdict(set)  # Route → drug names
        
        # Statistics
        self.total_drugs = 0
        self.indexed = False
    
    def build_index(self, all_drugs: dict):
        """
        Build all search indices from drug database
        
        Args:
            all_drugs: Dictionary of all drugs {name: drug_data}
        """
        print("Building drug search index...")
        
        for drug_name, drug_data in all_drugs.items():
            self._index_drug(drug_name, drug_data)
        
        self.total_drugs = len(all_drugs)
        self.indexed = True
        
        print(f"[OK] Indexed {self.total_drugs} drugs")
        print(f"   - {len(self.group_index)} groups")
        print(f"   - {len(self.indication_index)} indication keywords")
        print(f"   - {len(self.prefix_index)} prefixes")
        print(f"   - {len(self.brand_index)} brand names")
    
    def _index_drug(self, drug_name: str, drug_data: dict):
        """Index a single drug"""
        # 1. Name index (lowercase for case-insensitive search)
        name_lower = drug_name.lower()
        self.name_index[name_lower] = drug_data
        
        # 2. Group index
        group = drug_data.get('group', '')
        if group:
            self.group_index[group].append(drug_name)
            
            # Also index by main category (before " - ")
            main_category = group.split(' - ')[0].strip()
            if main_category != group:
                self.group_index[main_category].append(drug_name)
        
        # 3. Indication index (by keywords)
        for indication in drug_data.get('indications', []):
            # Extract keywords (words > 3 chars)
            keywords = self._extract_keywords(indication)
            for keyword in keywords:
                self.indication_index[keyword].add(drug_name)
        
        # 4. Prefix index (for autocomplete)
        if len(drug_name) >= 3:
            prefix = drug_name[:3].lower()
            self.prefix_index[prefix].append(drug_name)
        
        # 5. Vietnamese name index
        vietnamese_name = drug_data.get('vietnamese_name', '')
        if vietnamese_name:
            # Split by comma and index each name
            vn_names = [name.strip() for name in vietnamese_name.split(',')]
            for vn_name in vn_names:
                if vn_name:
                    self.vietnamese_index[vn_name.lower()] = drug_name
        
        # 6. Brand name index
        brand_names = drug_data.get('brand_names', {})
        if isinstance(brand_names, dict):
            # Common brands
            for brand in brand_names.get('common', []):
                self.brand_index[brand.lower()] = drug_name
            # Vietnam brands
            for brand in brand_names.get('vietnam', []):
                self.brand_index[brand.lower()] = drug_name
        
        # 7. Route index
        for route in drug_data.get('administration', []):
            self.route_index[route].add(drug_name)
    
    def _extract_keywords(self, text: str) -> Set[str]:
        """Extract searchable keywords from text"""
        # Remove special characters and split
        words = re.findall(r'\b\w+\b', text.lower())
        # Filter words > 3 characters
        keywords = {word for word in words if len(word) > 3}
        return keywords
    
    # ==================== SEARCH METHODS ====================
    
    def search_by_name(self, query: str) -> Optional[dict]:
        """
        Fast O(1) lookup by drug name
        
        Args:
            query: Drug name (case-insensitive)
        
        Returns:
            Drug data or None if not found
        """
        return self.name_index.get(query.lower())
    
    def search_by_vietnamese_name(self, query: str) -> Optional[dict]:
        """Search by Vietnamese name"""
        generic_name = self.vietnamese_index.get(query.lower())
        if generic_name:
            return self.name_index.get(generic_name.lower())
        return None
    
    def search_by_brand(self, brand_name: str) -> Optional[dict]:
        """Search by brand name"""
        generic_name = self.brand_index.get(brand_name.lower())
        if generic_name:
            return self.name_index.get(generic_name.lower())
        return None
    
    def search_by_group(self, group: str) -> List[str]:
        """
        Get all drugs in a therapeutic group
        
        Args:
            group: Group name (e.g., "Cardiovascular", "Diabetes")
        
        Returns:
            List of drug names
        """
        return self.group_index.get(group, [])
    
    def search_by_indication(self, indication: str) -> List[str]:
        """
        Search drugs by indication
        
        Args:
            indication: Indication keyword (e.g., "diabetes", "hypertension")
        
        Returns:
            List of drug names
        """
        keywords = self._extract_keywords(indication)
        
        # Find drugs that match ANY keyword
        matching_drugs = set()
        for keyword in keywords:
            matching_drugs.update(self.indication_index.get(keyword, set()))
        
        return list(matching_drugs)
    
    def autocomplete(self, prefix: str, limit: int = 10) -> List[str]:
        """
        Autocomplete drug names
        
        Args:
            prefix: Starting characters (min 3)
            limit: Max results
        
        Returns:
            List of matching drug names
        """
        if len(prefix) < 3:
            return []
        
        # Get candidates from prefix index
        prefix_key = prefix[:3].lower()
        candidates = self.prefix_index.get(prefix_key, [])
        
        # Filter by full prefix
        prefix_lower = prefix.lower()
        matches = [
            name for name in candidates
            if name.lower().startswith(prefix_lower)
        ]
        
        return matches[:limit]
    
    def fuzzy_search(self, query: str, max_results: int = 5) -> List[tuple]:
        """
        Fuzzy search for typo-tolerant matching
        
        Args:
            query: Search query (may have typos)
            max_results: Maximum results to return
        
        Returns:
            List of (drug_name, similarity_score) tuples
        """
        from difflib import SequenceMatcher
        
        query_lower = query.lower()
        matches = []
        
        # Compare with all drug names
        for drug_name in self.name_index.keys():
            similarity = SequenceMatcher(None, query_lower, drug_name).ratio()
            if similarity > 0.6:  # Threshold
                matches.append((drug_name.title(), similarity))
        
        # Sort by similarity (descending)
        matches.sort(key=lambda x: x[1], reverse=True)
        
        return matches[:max_results]
    
    def advanced_search(self, filters: dict) -> List[str]:
        """
        Multi-criteria search
        
        Args:
            filters: Dictionary of search criteria
                {
                    'group': 'Cardiovascular',
                    'indication': 'hypertension',
                    'route': 'PO',
                    'exclude_pregnancy_x': True
                }
        
        Returns:
            List of matching drug names
        """
        # Start with all drugs
        candidates = set(self.name_index.keys())
        
        # Apply group filter
        if 'group' in filters:
            group_drugs = set(d.lower() for d in self.search_by_group(filters['group']))
            candidates &= group_drugs
        
        # Apply indication filter
        if 'indication' in filters:
            indication_drugs = set(d.lower() for d in self.search_by_indication(filters['indication']))
            candidates &= indication_drugs
        
        # Apply route filter
        if 'route' in filters:
            route_drugs = set(d.lower() for d in self.route_index.get(filters['route'], set()))
            candidates &= route_drugs
        
        # Apply pregnancy filter
        if filters.get('exclude_pregnancy_x'):
            safe_drugs = set()
            for drug_name in candidates:
                drug_data = self.name_index[drug_name]
                pregnancy = drug_data.get('pregnancy_lactation', '')
                if 'Category X' not in pregnancy and 'Category D' not in pregnancy:
                    safe_drugs.add(drug_name)
            candidates = safe_drugs
        
        # Convert back to proper case
        results = []
        for drug_lower in candidates:
            # Find original case
            for original_name in self.name_index.keys():
                if original_name.lower() == drug_lower:
                    results.append(original_name.title())
                    break
        
        return results
    
    def get_statistics(self) -> dict:
        """Get index statistics"""
        return {
            'total_drugs': self.total_drugs,
            'total_groups': len(self.group_index),
            'total_indications': len(self.indication_index),
            'total_brands': len(self.brand_index),
            'total_routes': len(self.route_index),
            'indexed': self.indexed
        }


# ==================== USAGE EXAMPLE ====================

if __name__ == "__main__":
    # Example usage
    import sys
    sys.path.insert(0, r'd:\1 medical\drugs')
    from drug_modules import ALL_DRUGS
    
    # Create and build index
    search_index = DrugSearchIndex()
    search_index.build_index(ALL_DRUGS)
    
    # Test searches
    print("\n" + "="*50)
    print("SEARCH EXAMPLES")
    print("="*50)
    
    # 1. Name search
    print("\n1. Search by name: 'metformin'")
    result = search_index.search_by_name("metformin")
    if result:
        print(f"   Found: {result.get('vietnamese_name')}")
    
    # 2. Group search
    print("\n2. Search by group: 'Cardiovascular'")
    cv_drugs = search_index.search_by_group("Cardiovascular")
    print(f"   Found {len(cv_drugs)} drugs")
    print(f"   Examples: {cv_drugs[:5]}")
    
    # 3. Indication search
    print("\n3. Search by indication: 'diabetes'")
    diabetes_drugs = search_index.search_by_indication("diabetes")
    print(f"   Found {len(diabetes_drugs)} drugs")
    print(f"   Examples: {diabetes_drugs[:5]}")
    
    # 4. Autocomplete
    print("\n4. Autocomplete: 'met'")
    suggestions = search_index.autocomplete("met")
    print(f"   Suggestions: {suggestions}")
    
    # 5. Fuzzy search
    print("\n5. Fuzzy search: 'metfromin' (typo)")
    matches = search_index.fuzzy_search("metfromin")
    print(f"   Did you mean: {[m[0] for m in matches]}")
    
    # 6. Advanced search
    print("\n6. Advanced search: CV drugs for hypertension, oral only")
    results = search_index.advanced_search({
        'group': 'Cardiovascular',
        'indication': 'hypertension',
        'route': 'PO'
    })
    print(f"   Found {len(results)} drugs")
    print(f"   Examples: {results[:5]}")
    
    # Statistics
    print("\n" + "="*50)
    print("INDEX STATISTICS")
    print("="*50)
    stats = search_index.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")
