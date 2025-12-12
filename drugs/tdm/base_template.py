"""
TDM Base Template
Cấu trúc chuẩn cho các TDM calculators
"""

import streamlit as st
from typing import Dict, Optional, Tuple


class TDMCalculator:
    """
    Base class cho TDM calculators
    Cung cấp cấu trúc chuẩn và các hàm helper
    """
    
    def __init__(
        self,
        drug_name: str,
        drug_icon: str,
        therapeutic_range: str,
        target_min: float,
        target_max: float,
        toxic_threshold: Optional[float] = None,
        unit: str = "ng/mL",
        sampling_time: str = "trough",
        half_life_hours: Optional[float] = None
    ):
        """
        Initialize TDM Calculator
        
        Args:
            drug_name: Tên thuốc
            drug_icon: Icon emoji
            therapeutic_range: Khoảng điều trị (text)
            target_min: Giá trị tối thiểu
            target_max: Giá trị tối đa
            toxic_threshold: Ngưỡng độc tính (optional)
            unit: Đơn vị đo
            sampling_time: Thời điểm lấy mẫu (trough/peak/both)
            half_life_hours: Thời gian bán thải (giờ)
        """
        self.drug_name = drug_name
        self.drug_icon = drug_icon
        self.therapeutic_range = therapeutic_range
        self.target_min = target_min
        self.target_max = target_max
        self.toxic_threshold = toxic_threshold
        self.unit = unit
        self.sampling_time = sampling_time
        self.half_life_hours = half_life_hours
    
    def interpret_level(self, level: float) -> Dict:
        """
        Interpret drug level
        
        Args:
            level: Nồng độ thuốc
            
        Returns:
            dict with interpretation
        """
        if level < self.target_min:
            status = "subtherapeutic"
            level_text = "⬇️ Dưới mục tiêu"
            recommendation = f"Nồng độ thấp (< {self.target_min} {self.unit}). Cân nhắc tăng liều hoặc kiểm tra compliance."
            color = "info"
        elif level <= self.target_max:
            status = "therapeutic"
            level_text = "✅ Trong mục tiêu điều trị"
            recommendation = "Nồng độ trong khoảng điều trị. Tiếp tục liều hiện tại."
            color = "success"
        elif self.toxic_threshold and level <= self.toxic_threshold:
            status = "supratherapeutic"
            level_text = "⚠️ Trên mục tiêu (chấp nhận được)"
            recommendation = f"Nồng độ hơi cao nhưng có thể chấp nhận. Theo dõi triệu chứng độc tính. Cân nhắc giảm liều."
            color = "warning"
        else:
            status = "toxic"
            threshold = self.toxic_threshold or self.target_max * 1.5
            level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
            recommendation = f"Nồng độ độc tính (> {threshold} {self.unit})! Ngừng thuốc ngay, đánh giá triệu chứng độc tính."
            color = "error"
        
        return {
            "status": status,
            "level_text": level_text,
            "therapeutic_range": self.therapeutic_range,
            "recommendation": recommendation,
            "color": color,
            "current_level": level
        }
    
    def render_header(self):
        """Render header section"""
        st.markdown(f"""
        <h2 style='text-align: center; color: #0EA5E9;'>{self.drug_icon} {self.drug_name} TDM Calculator</h2>
        <p style='text-align: center;'><em>Therapeutic Drug Monitoring & Dose Adjustment</em></p>
        """, unsafe_allow_html=True)
    
    def render_info_box(self, additional_info: str = ""):
        """Render info box with TDM information"""
        info_text = f"""
        **{self.drug_name} TDM:**
        - Mục tiêu: {self.therapeutic_range} ({self.unit})
        - Thời điểm lấy mẫu: {self.sampling_time}
        """
        if self.half_life_hours:
            info_text += f"\n- Half-life: {self.half_life_hours} giờ"
        if self.toxic_threshold:
            info_text += f"\n- Độc tính: > {self.toxic_threshold} {self.unit}"
        if additional_info:
            info_text += f"\n{additional_info}"
        
        st.info(info_text)
    
    def render_level_interpretation_tab(self):
        """Render level interpretation tab"""
        st.markdown(f"### 📊 Giải thích nồng độ {self.drug_name}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            level = st.number_input(
                f"Nồng độ {self.drug_name} ({self.unit})",
                min_value=0.0,
                max_value=100.0,
                value=(self.target_min + self.target_max) / 2,
                step=0.1,
                format="%.2f",
                key=f"{self.drug_name.lower()}_level"
            )
        
        with col2:
            time_since_dose = st.number_input(
                "Thời gian sau liều cuối (giờ)",
                min_value=0.0,
                max_value=48.0,
                value=12.0,
                step=1.0,
                format="%.1f",
                key=f"{self.drug_name.lower()}_time",
                help="Thời điểm lấy mẫu so với liều cuối"
            )
        
        st.markdown("---")
        
        if st.button("📊 Giải thích nồng độ", type="primary", use_container_width=True):
            interpretation = self.interpret_level(level)
            
            st.markdown("### 📈 Kết quả Giải thích")
            
            # Display status
            if interpretation['color'] == 'success':
                st.success(f"**{interpretation['level_text']}**")
            elif interpretation['color'] == 'info':
                st.info(f"**{interpretation['level_text']}**")
            elif interpretation['color'] == 'warning':
                st.warning(f"**{interpretation['level_text']}**")
            else:
                st.error(f"**{interpretation['level_text']}**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Nồng độ hiện tại",
                    f"{interpretation['current_level']:.2f} {self.unit}"
                )
            
            with col2:
                st.metric(
                    "Mục tiêu điều trị",
                    interpretation['therapeutic_range']
                )
            
            st.markdown("---")
            st.markdown(f"### 💡 Khuyến nghị")
            
            if interpretation['color'] == 'error':
                st.error(interpretation['recommendation'])
            elif interpretation['color'] == 'warning':
                st.warning(interpretation['recommendation'])
            elif interpretation['color'] == 'info':
                st.info(interpretation['recommendation'])
            else:
                st.success(interpretation['recommendation'])
    
    def render_references(self, references: str):
        """Render references section"""
        st.markdown("---")
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown(references)

