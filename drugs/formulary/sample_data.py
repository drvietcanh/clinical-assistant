"""
Sample Formulary Data
Example BHYT coverage data (to be expanded)
"""

from . import FormularyStatus, FormularyInfo

# Sample formulary data (BHYT coverage)
SAMPLE_FORMULARY_DATA = {
    "Paracetamol": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Amoxicillin": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Metformin": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Atorvastatin": FormularyInfo(
        status=FormularyStatus.PARTIAL,
        coverage_percentage=50,
        generic_available=True,
        notes="BHYT chi trả 50% cho generic, không chi trả cho brand"
    ),
    "Warfarin": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        requires_prior_auth=False,
        notes="BHYT chi trả 100%, cần theo dõi INR"
    ),
    "Clopidogrel": FormularyInfo(
        status=FormularyStatus.PRIOR_AUTH,
        coverage_percentage=80,
        generic_available=True,
        requires_prior_auth=True,
        notes="Cần xác nhận trước khi kê đơn, BHYT chi trả 80%"
    ),
    "Rivaroxaban": FormularyInfo(
        status=FormularyStatus.NOT_COVERED,
        coverage_percentage=0,
        generic_available=False,
        alternative_drugs=["Warfarin", "Dabigatran"],
        notes="Không trong danh mục BHYT, có thể dùng Warfarin thay thế"
    ),
    "Aspirin": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Furosemide": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Amlodipine": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Losartan": FormularyInfo(
        status=FormularyStatus.COVERED,
        coverage_percentage=100,
        generic_available=True,
        notes="BHYT chi trả 100% cho generic"
    ),
    "Insulin Glargine": FormularyInfo(
        status=FormularyStatus.PARTIAL,
        coverage_percentage=50,
        generic_available=False,
        requires_prior_auth=True,
        notes="BHYT chi trả 50%, cần xác nhận trước cho bệnh nhân đái tháo đường type 1 hoặc type 2 khó kiểm soát"
    )
}


def get_sample_formulary(drug_name: str):
    """
    Get sample formulary info for a drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        FormularyInfo or None
    """
    return SAMPLE_FORMULARY_DATA.get(drug_name)


__all__ = ['SAMPLE_FORMULARY_DATA', 'get_sample_formulary']

