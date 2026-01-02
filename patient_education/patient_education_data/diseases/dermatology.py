"""
Patient Education Topics - Dermatology
"""
from patient_education.models import PatientEducationTopic


DERMATOLOGY_TOPICS = [
        PatientEducationTopic(
            id="atopic_dermatitis_basics",
            title="Understanding Atopic Dermatitis",
            title_vn="Hiểu về Viêm da cơ địa",
            category="Disease",
            content="""
            # Hiểu về Viêm da cơ địa

            ## Viêm da cơ địa là gì?

            Viêm da cơ địa là bệnh viêm da mạn tính, tái phát, thường gặp ở trẻ em, đặc trưng bởi ngứa và tổn thương da. Bệnh có thể kéo dài đến tuổi trưởng thành.

            **⚠️ Đặc điểm:**
            - Viêm da mạn tính, tái phát
            - Ngứa dữ dội
            - Thường gặp ở trẻ em (20% trẻ em)
            - Có thể kéo dài đến tuổi trưởng thành
            - Liên quan đến hen, viêm mũi dị ứng

            **Phân loại:**
            - **Trẻ em:** Mặt, tay chân
            - **Người lớn:** Nếp gấp (khuỷu tay, đầu gối)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ngứa dữ dội:** Đặc biệt ban đêm
            - **Tổn thương da:**
              - Đỏ, khô, bong vảy
              - Mụn nước (có thể vỡ, chảy dịch)
              - Da dày lên, nứt nẻ (lichenification)
            - **Vị trí:**
              - Trẻ em: Mặt, tay chân, thân mình
              - Người lớn: Nếp gấp (khuỷu tay, đầu gối, cổ)

            **Triệu chứng khác:**
            - Da khô toàn thân
            - Nhiễm trùng da thứ phát (gãi → nhiễm khuẩn)
            - Rối loạn giấc ngủ (do ngứa)

            **⚠️ Bội nhiễm:**
            - Da đỏ, sưng, đau
            - Mủ, vảy vàng
            - Sốt (nếu nặng)

            ## Nguyên nhân:

            **1. Yếu tố di truyền:**
            - Tiền sử gia đình (hen, viêm mũi dị ứng, viêm da cơ địa)
            - Rối loạn hàng rào da

            **2. Dị ứng:**
            - Bụi, phấn hoa
            - Thức ăn (trẻ em: trứng, sữa, đậu phộng)
            - Lông động vật

            **3. Yếu tố môi trường:**
            - Khô, lạnh
            - Hóa chất (xà phòng, chất tẩy rửa)
            - Mồ hôi
            - Stress

            ## Chẩn đoán:

            **Tiêu chuẩn:**
            - Triệu chứng lâm sàng điển hình
            - Tiền sử dị ứng (hen, viêm mũi dị ứng)
            - Test dị ứng (nếu cần)

            ## Điều trị:

            **1. Dưỡng ẩm:**
            - **Quan trọng nhất!**
            - Dưỡng ẩm 2-3 lần/ngày
            - Sau tắm (trong vòng 3 phút)
            - Dùng kem dưỡng ẩm không mùi, không màu

            **2. Corticosteroid tại chỗ:**
            - Mức độ nhẹ-trung bình
            - Hydrocortisone (nhẹ), Betamethasone (trung bình)
            - Bôi 1-2 lần/ngày, 7-14 ngày
            - **Không dùng lâu dài** (teo da)

            **3. Calcineurin inhibitor:**
            - Tacrolimus, Pimecrolimus
            - Nếu kháng corticosteroid
            - Dùng lâu dài được

            **4. Kháng histamine:**
            - Nếu ngứa nhiều
            - Cetirizine, Loratadine

            **5. Kháng sinh:**
            - Nếu nhiễm trùng
            - Mupirocin tại chỗ, kháng sinh uống

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Trẻ em (nếu dị ứng thức ăn):**
            - Tránh: Trứng, sữa, đậu phộng, cá, tôm (nếu dị ứng)
            - Test dị ứng trước khi loại bỏ

            **2. Người lớn:**
            - Chế độ ăn bình thường
            - Tránh thức ăn gây dị ứng (nếu biết)

            **3. Thực phẩm chống viêm:**
            - Cá béo (omega-3)
            - Rau xanh, trái cây
            - Tránh thực phẩm chế biến

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, rau
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa (nếu không dị ứng)

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tắm ngay sau tập (tránh mồ hôi kích thích)
            - Dưỡng ẩm sau tắm
            - Mặc quần áo cotton, thoáng mát

            **3. Tránh:**
            - Tập quá mệt (mồ hôi nhiều)
            - Quần áo bó sát, không thấm mồ hôi

            ## 💊 QUẢN LÝ THUỐC:

            **1. Dưỡng ẩm:**
            - Dùng 2-3 lần/ngày
            - Sau tắm (trong vòng 3 phút)
            - Dùng đều đặn, kể cả khi da tốt

            **2. Corticosteroid tại chỗ:**
            - Bôi mỏng, 1-2 lần/ngày
            - Chỉ bôi vùng tổn thương
            - Không dùng > 2 tuần liên tiếp
            - Giảm dần liều

            **3. Tác dụng phụ:**
            - **Corticosteroid:** Teo da, giãn mạch (nếu dùng lâu)
            - **Tacrolimus:** Nóng rát, ngứa (tạm thời)

            **4. Lưu ý:**
            - Không tự ý tăng liều
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Bội nhiễm:**
            - Da đỏ, sưng, đau
            - Mủ, vảy vàng
            - Sốt

            **2. Tổn thương lan rộng:**
            - > 30% diện tích da
            - Không đáp ứng điều trị

            **3. Tác dụng phụ thuốc:**
            - Teo da nặng
            - Nhiễm trùng nặng

            ## 💡 PHÒNG NGỪA:

            **1. Dưỡng ẩm:**
            - Dưỡng ẩm thường xuyên (quan trọng nhất!)
            - Sau tắm, trước khi ngủ

            **2. Tránh yếu tố kích thích:**
            - Tránh dị nguyên (nếu biết)
            - Tránh hóa chất mạnh
            - Mặc quần áo cotton, tránh len

            **3. Chăm sóc da:**
            - Tắm nước ấm, không quá nóng
            - Dùng xà phòng nhẹ, không mùi
            - Không chà xát mạnh
            - Cắt móng tay (tránh gãi)

            **4. Môi trường:**
            - Giữ ẩm không khí (nếu khô)
            - Tránh thay đổi nhiệt độ đột ngột
            - Vệ sinh nhà cửa (giảm bụi)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm da cơ địa:**
            - Dưỡng ẩm thường xuyên (quan trọng!)
            - Tránh gãi (cắt móng, đeo găng tay khi ngủ)
            - Dùng thuốc đúng cách
            - Tránh yếu tố kích thích

            **2. Chăm sóc da:**
            - Tắm nước ấm, ngắn (10-15 phút)
            - Dưỡng ẩm ngay sau tắm
            - Mặc quần áo cotton, thoáng mát

            **3. Sống tích cực:**
            - Viêm da cơ địa có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng
            - Nhiều trẻ em tự khỏi khi lớn

            **4. Hỗ trợ:**
            - Giáo dục gia đình
            - Tư vấn tâm lý (nếu cần)
            - Tham gia nhóm hỗ trợ
            """,
            related_disease="atopic_dermatitis",
            related_drugs=["Hydrocortisone", "Betamethasone", "Tacrolimus", "Pimecrolimus", "Cetirizine"],
            printable=True
        ),

        PatientEducationTopic(
            id="conjunctivitis_basics",
            title="Understanding Conjunctivitis",
            title_vn="Hiểu về Viêm kết mạc",
            category="Disease",
            content="""
            # Hiểu về Viêm kết mạc

            ## Viêm kết mạc là gì?

            Viêm kết mạc là tình trạng viêm màng kết mạc, rất phổ biến, có thể do virus, vi khuẩn, hoặc dị ứng. Bệnh thường tự khỏi (virus) hoặc cần điều trị (vi khuẩn, dị ứng).

            **⚠️ Đặc điểm:**
            - Viêm màng kết mạc
            - Rất phổ biến
            - Có thể lây (virus, vi khuẩn)
            - Thường tự khỏi (virus)

            **Phân loại:**
            - **Virus:** Adenovirus (phổ biến nhất)
            - **Vi khuẩn:** Staphylococcus, Streptococcus
            - **Dị ứng:** Phấn hoa, bụi, hóa chất

            ## Triệu chứng:

            **Triệu chứng chung:**
            - **Đỏ mắt:** Một hoặc hai mắt
            - **Ngứa mắt:** Đặc biệt dị ứng
            - **Chảy nước mắt**
            - **Dử mắt (ghèn):** Vàng/xanh nếu vi khuẩn
            - **Cảm giác cộm, rát**
            - **Sưng mí mắt**

            **Triệu chứng virus:**
            - Dử mắt ít, trong
            - Thường hai mắt
            - Có thể kèm cảm lạnh

            **Triệu chứng vi khuẩn:**
            - Dử mắt nhiều, vàng/xanh
            - Dính mắt khi thức dậy
            - Có thể một hoặc hai mắt

            **Triệu chứng dị ứng:**
            - Ngứa nhiều
            - Chảy nước mắt
            - Thường hai mắt
            - Kèm hắt hơi, sổ mũi

            **⚠️ Biến chứng:**
            - Viêm giác mạc (nếu nặng)
            - Giảm thị lực (hiếm)

            ## Nguyên nhân:

            **1. Virus:**
            - Adenovirus (phổ biến nhất)
            - Herpes

            **2. Vi khuẩn:**
            - Staphylococcus
            - Streptococcus
            - Haemophilus

            **3. Dị ứng:**
            - Phấn hoa
            - Bụi
            - Hóa chất

            **4. Yếu tố nguy cơ:**
            - Tiếp xúc người bệnh
            - Vệ sinh kém
            - Dị ứng

            ## Chẩn đoán:

            **Khám:**
            - Kết mạc đỏ, phù
            - Dử mắt
            - Phân loại: virus, vi khuẩn, dị ứng

            ## Điều trị:

            **1. Virus:**
            - Điều trị triệu chứng
            - Nước mắt nhân tạo
            - Chườm lạnh
            - Tự khỏi 1-2 tuần

            **2. Vi khuẩn:**
            - Kháng sinh nhỏ mắt: Chloramphenicol, Ofloxacin, Tobramycin
            - 4-6 lần/ngày, 5-7 ngày

            **3. Dị ứng:**
            - Antihistamine nhỏ mắt
            - Corticosteroid nhỏ mắt (nếu nặng)
            - Tránh dị nguyên

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Bình thường:**
            - Ăn đủ dinh dưỡng
            - Uống nhiều nước

            **2. Dị ứng:**
            - Tránh thức ăn gây dị ứng (nếu biết)
            - Thực phẩm chống viêm: Cá béo, rau xanh

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Tránh bơi lội (nước vào mắt)
            - Tập nhẹ nếu không khó chịu

            **2. Khi đã khỏi:**
            - Tập bình thường
            - Đi bộ, chạy bộ, bơi lội

            ## 💊 QUẢN LÝ THUỐC:

            **1. Nhỏ mắt đúng cách:**
            - Rửa tay trước
            - Kéo mí mắt dưới
            - Nhỏ 1-2 giọt
            - Nhắm mắt 1-2 phút
            - Không chạm đầu lọ vào mắt

            **2. Kháng sinh nhỏ mắt:**
            - 4-6 lần/ngày
            - 5-7 ngày
            - Không tự ý ngừng

            **3. Lưu ý:**
            - Không dùng chung thuốc nhỏ mắt
            - Vứt thuốc sau khi hết bệnh

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Đau mắt dữ dội
            - Giảm thị lực
            - Nhạy cảm ánh sáng nặng
            - Sưng mắt nhiều

            **2. Không cải thiện:**
            - Sau 5-7 ngày điều trị
            - Triệu chứng nặng hơn

            **3. Biến chứng:**
            - Viêm giác mạc
            - Giảm thị lực

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh:**
            - Rửa tay thường xuyên
            - Không dụi mắt
            - Không dùng chung khăn, gối

            **2. Dị ứng:**
            - Tránh dị nguyên
            - Đeo kính râm
            - Vệ sinh môi trường

            **3. Khi có người bệnh:**
            - Cách ly
            - Vệ sinh tay
            - Không dùng chung đồ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm kết mạc:**
            - Vệ sinh mắt
            - Nhỏ thuốc đúng cách
            - Không dụi mắt
            - Tránh lây cho người khác

            **2. Sống tích cực:**
            - Hầu hết tự khỏi (virus)
            - Điều trị đúng → Khỏi nhanh
            - Phòng ngừa tốt → Ít mắc bệnh

            **3. Trẻ em:**
            - Theo dõi sát
            - Không cho dụi mắt
            - Vệ sinh tay thường xuyên
            """,
            related_disease="conjunctivitis",
            related_drugs=["Chloramphenicol", "Ofloxacin", "Tobramycin", "Antihistamine"],
            printable=True
        ),

        PatientEducationTopic(
            id="psoriasis_basics",
            title="Understanding Psoriasis",
            title_vn="Hiểu về Vẩy nến",
            category="Disease",
            content="""
            # Hiểu về Vẩy nến

            ## Vẩy nến là gì?

            Vẩy nến là bệnh viêm da mạn tính, đặc trưng bởi các mảng đỏ, bong vảy bạc, tái phát. Bệnh ảnh hưởng đến thẩm mỹ và chất lượng cuộc sống.

            **⚠️ Đặc điểm:**
            - Viêm da mạn tính, tái phát
            - Mảng đỏ, bong vảy bạc
            - Không lây
            - Có thể ảnh hưởng khớp (viêm khớp vẩy nến)

            **Phân loại:**
            - **Vẩy nến mảng:** Phổ biến nhất
            - **Vẩy nến giọt:** Tổn thương nhỏ
            - **Viêm khớp vẩy nến:** 30% bệnh nhân

            ## Triệu chứng:

            **Triệu chứng da:**
            - **Mảng đỏ, bong vảy bạc:** Đặc trưng
            - **Vị trí:** Khuỷu tay, đầu gối, da đầu, thân mình
            - **Ngứa:** Nhẹ đến trung bình
            - **Tổn thương móng:** Rỗ, dày, tách móng

            **Triệu chứng khớp (viêm khớp vẩy nến):**
            - Đau, sưng khớp
            - Cứng khớp buổi sáng
            - Thường khớp ngón tay, chân

            **⚠️ Yếu tố kích thích:**
            - Nhiễm trùng (viêm họng)
            - Stress
            - Chấn thương da
            - Thuốc (beta-blocker, lithium)
            - Rượu bia, hút thuốc

            ## Nguyên nhân:

            **1. Yếu tố di truyền:**
            - Có tiền sử gia đình

            **2. Yếu tố miễn dịch:**
            - Rối loạn hệ miễn dịch

            **3. Yếu tố kích thích:**
            - Nhiễm trùng
            - Stress
            - Chấn thương da
            - Thuốc

            ## Chẩn đoán:

            **Khám:**
            - Triệu chứng lâm sàng điển hình
            - Dấu hiệu Auspitz (chảy máu khi cạo vảy)
            - Sinh thiết da (nếu không rõ)

            ## Điều trị:

            **1. Nhẹ (< 5% diện tích):**
            - Corticosteroid tại chỗ
            - Vitamin D analogues (Calcipotriol)
            - Dưỡng ẩm

            **2. Trung bình (5-10%):**
            - Quang trị liệu (UVB, PUVA)
            - Kết hợp thuốc tại chỗ

            **3. Nặng (> 10%):**
            - Methotrexate, Cyclosporine
            - Sinh học: Adalimumab, Etanercept

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chống viêm:**
            - Cá béo (omega-3)
            - Rau xanh, trái cây
            - Tránh thực phẩm chế biến sẵn

            **2. Tránh:**
            - Rượu bia (kích thích)
            - Thực phẩm gây dị ứng (nếu biết)

            **3. Thực đơn mẫu:**
            - **Sáng:** Trứng, rau xanh, trái cây
            - **Trưa:** Cơm, cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (giảm stress)
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            **2. Viêm khớp vẩy nến:**
            - Tập nhẹ nhàng
            - Vật lý trị liệu

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc tại chỗ:**
            - Corticosteroid: Bôi mỏng, 1-2 lần/ngày
            - Calcipotriol: Bôi 1-2 lần/ngày
            - Không dùng lâu dài (teo da)

            **2. Thuốc toàn thân:**
            - Methotrexate: Uống 1 lần/tuần
            - Theo dõi chức năng gan, thận

            **3. Lưu ý:**
            - Bôi đều đặn
            - Không tự ý ngừng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Tổn thương lan rộng:**
            - > 10% diện tích da
            - Không đáp ứng điều trị

            **2. Viêm khớp:**
            - Đau, sưng khớp
            - Cần điều trị

            **3. Nhiễm trùng:**
            - Da đỏ, sưng, đau
            - Mủ

            ## 💡 PHÒNG NGỪA:

            **1. Tránh yếu tố kích thích:**
            - Giảm stress
            - Tránh chấn thương da
            - Điều trị nhiễm trùng sớm

            **2. Lối sống:**
            - Bỏ thuốc lá
            - Hạn chế rượu bia
            - Dưỡng ẩm da

            **3. Tập thể dục:**
            - Giảm stress
            - Cải thiện sức khỏe

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị vẩy nến:**
            - Dưỡng ẩm da thường xuyên
            - Bôi thuốc đúng cách
            - Tránh yếu tố kích thích
            - Giảm stress

            **2. Sống tích cực:**
            - Vẩy nến có thể kiểm soát
            - Điều trị đúng → Giảm tổn thương
            - Có thể sống bình thường

            **3. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Tư vấn tâm lý (nếu cần)
            """,
            related_disease="psoriasis",
            related_drugs=["Topical Corticosteroid", "Calcipotriol", "Methotrexate", "Cyclosporine", "Adalimumab"],
            printable=True
        ),

        PatientEducationTopic(
            id="scabies_basics",
            title="Understanding Scabies",
            title_vn="Hiểu về Ghẻ",
            category="Disease",
            content="""
            # Hiểu về Ghẻ

            ## Ghẻ là gì?

            Ghẻ là bệnh da do ký sinh trùng Sarcoptes scabiei gây ra, đặc trưng bởi ngứa dữ dội, đặc biệt về đêm. Bệnh rất phổ biến ở Việt Nam, lây qua tiếp xúc trực tiếp hoặc gián tiếp.

            **⚠️ Đặc điểm:**
            - Bệnh da do ký sinh trùng
            - Ngứa dữ dội, đặc biệt về đêm
            - Rất phổ biến ở Việt Nam
            - Lây qua tiếp xúc gần

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ngứa dữ dội:** Đặc biệt về đêm, khi nóng
            - **Đường hầm:** Đường ngoằn ngoèo, màu xám, dài 5-15mm (nơi cái ghẻ đào)
            - **Mụn nước, sẩn:** Ở kẽ ngón tay, cổ tay, khuỷu tay, nách, bẹn
            - **Vết xước:** Do gãi
            - **Nhiễm khuẩn thứ phát:** Do gãi

            **Vị trí thường gặp:**
            - Kẽ ngón tay, ngón chân
            - Cổ tay, khuỷu tay
            - Nách, bẹn
            - Quanh thắt lưng
            - Bộ phận sinh dục (nam)
            - Vú, núm vú (nữ)
            - **Trẻ em:** Có thể ở lòng bàn tay, lòng bàn chân, mặt

            **⚠️ Ghẻ Na Uy (nặng):**
            - Vảy dày, lan rộng
            - Ngứa ít hoặc không ngứa
            - Gặp ở người suy giảm miễn dịch

            ## Nguyên nhân:

            **1. Ký sinh trùng:**
            - Sarcoptes scabiei (cái ghẻ)
            - Đào hang dưới da, đẻ trứng

            **2. Lây truyền:**
            - **Tiếp xúc trực tiếp:** Da kề da, quan hệ tình dục
            - **Tiếp xúc gián tiếp:** Quần áo, chăn màn, khăn tắm (ít gặp hơn)
            - **Thời gian:** Cần tiếp xúc lâu (15-20 phút)

            **3. Yếu tố nguy cơ:**
            - Sống đông đúc
            - Vệ sinh kém
            - Tiếp xúc gần với người bệnh
            - Trẻ em, người cao tuổi

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Đường hầm
            - Vị trí đặc trưng

            **Xét nghiệm:**
            - **Soi da:** Tìm cái ghẻ, trứng
            - **Test mực:** Bôi mực lên đường hầm, lau sạch, thấy đường hầm

            ## Điều trị:

            **1. Thuốc bôi:**
            - **Permethrin 5%:** Bôi toàn thân, để 8-12 giờ, rửa sạch (thuốc đầu tay)
            - **Benzyl benzoate 25%:** Bôi 3 ngày liên tiếp
            - **Lindane 1%:** Ít dùng (độc)
            - **Ivermectin bôi:** Nếu có

            **2. Thuốc uống:**
            - **Ivermectin:** 200mcg/kg, uống 1-2 lần (cách 7-14 ngày)
            - Dùng cho ghẻ nặng, ghẻ Na Uy

            **3. Điều trị ngứa:**
            - **Antihistamine:** Cetirizine, Loratadine
            - **Corticosteroid bôi:** Nếu viêm nhiều

            **4. Điều trị nhiễm khuẩn:**
            - Kháng sinh bôi hoặc uống nếu nhiễm khuẩn thứ phát

            **5. Quan trọng:**
            - **Bôi toàn thân:** Từ cổ xuống chân (trừ mặt, trừ trẻ em)
            - **Điều trị đồng thời:** Tất cả người trong gia đình
            - **Lặp lại:** Sau 7-14 ngày nếu cần

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Bình thường:**
            - Ăn uống bình thường
            - Không cần kiêng khem đặc biệt

            **2. Tránh:**
            - Thức ăn gây dị ứng (nếu có)
            - Đồ cay nóng (có thể làm ngứa tăng)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang điều trị:**
            - Tập thể dục bình thường
            - Tránh đổ mồ hôi nhiều (có thể làm ngứa tăng)

            **2. Sau khi khỏi:**
            - Tập thể dục bình thường

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc bôi:**
            - **Permethrin:** Bôi toàn thân, để 8-12 giờ, rửa sạch
            - **Bôi đúng cách:** Từ cổ xuống chân, kể cả kẽ ngón tay, ngón chân
            - **Lặp lại:** Sau 7-14 ngày nếu cần

            **2. Thuốc uống:**
            - **Ivermectin:** Uống đúng liều, đúng thời điểm
            - Có thể cần uống 2 lần (cách 7-14 ngày)

            **3. Điều trị ngứa:**
            - Antihistamine: Uống buổi tối (giảm ngứa về đêm)

            **4. Lưu ý:**
            - **Điều trị đồng thời:** Tất cả người trong gia đình
            - **Vệ sinh:** Giặt quần áo, chăn màn bằng nước nóng
            - **Phơi nắng:** Quần áo, chăn màn

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Ghẻ nặng:**
            - Ghẻ lan rộng
            - Ghẻ Na Uy
            - Không đáp ứng điều trị

            **2. Nhiễm khuẩn:**
            - Nhiễm khuẩn da nặng
            - Sốt, sưng đau

            **3. Tác dụng phụ:**
            - Dị ứng thuốc bôi
            - Tác dụng phụ nặng

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Rửa tay thường xuyên
            - **Tắm rửa:** Tắm rửa sạch sẽ hàng ngày
            - **Quần áo:** Mặc quần áo sạch

            **2. Tránh tiếp xúc:**
            - Tránh tiếp xúc gần với người bệnh
            - Không dùng chung quần áo, khăn tắm

            **3. Khi có người bệnh:**
            - **Điều trị đồng thời:** Tất cả người trong gia đình
            - **Vệ sinh:** Giặt quần áo, chăn màn bằng nước nóng (60°C)
            - **Phơi nắng:** Quần áo, chăn màn
            - **Cách ly:** Tránh tiếp xúc gần cho đến khi khỏi

            **4. Môi trường:**
            - Vệ sinh nhà cửa
            - Phơi nắng chăn màn, gối

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị ghẻ:**
            - Điều trị sớm (quan trọng!)
            - Bôi thuốc đúng cách, toàn thân
            - Điều trị đồng thời tất cả người trong gia đình
            - Vệ sinh quần áo, chăn màn

            **2. Ngứa:**
            - Ngứa có thể kéo dài 2-4 tuần sau điều trị (do dị ứng)
            - Dùng antihistamine để giảm ngứa
            - Tránh gãi (gây nhiễm khuẩn)

            **3. Sống tích cực:**
            - Ghẻ có thể điều trị khỏi hoàn toàn
            - Điều trị đúng → Khỏi trong 1-2 tuần
            - Phòng ngừa tốt → Không tái phát

            **4. Gia đình:**
            - Tất cả người trong gia đình cần điều trị đồng thời
            - Vệ sinh quần áo, chăn màn
            - Tránh tiếp xúc gần cho đến khi khỏi
            """,
            related_disease="scabies",
            related_drugs=["Permethrin", "Benzyl benzoate", "Ivermectin", "Cetirizine", "Loratadine"],
            printable=True
        ),

        PatientEducationTopic(
            id="contact_dermatitis_basics",
            title="Understanding Contact Dermatitis",
            title_vn="Hiểu về Viêm da tiếp xúc",
            category="Disease",
            content="""
            # Hiểu về Viêm da tiếp xúc

            ## Viêm da tiếp xúc là gì?

            Viêm da tiếp xúc là tình trạng viêm da do tiếp xúc với chất gây kích ứng hoặc dị ứng. Bệnh rất phổ biến, gây ngứa, đỏ da, có thể ảnh hưởng đến chất lượng cuộc sống.

            **⚠️ Đặc điểm:**
            - Viêm da do tiếp xúc
            - Kích ứng hoặc dị ứng
            - Rất phổ biến
            - Gây ngứa, đỏ da

            **Phân loại:**
            - **Viêm da tiếp xúc kích ứng:** Do chất kích ứng (phổ biến hơn)
            - **Viêm da tiếp xúc dị ứng:** Do dị ứng (phản ứng miễn dịch)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ngứa:** Ngứa nhiều
            - **Đỏ da:** Đỏ da tại vị trí tiếp xúc
            - **Sẩn, mụn nước:** Có thể có
            - **Khô da, nứt nẻ:** Nếu mạn tính
            - **Đau, rát:** Có thể có

            **Vị trí:**
            - Vị trí tiếp xúc với chất gây kích ứng/dị ứng
            - Tay, chân, mặt, cổ, thân mình

            **⚠️ Viêm da tiếp xúc kích ứng:**
            - Ngứa ít hơn
            - Đau, rát nhiều hơn
            - Xuất hiện ngay sau tiếp xúc

            **⚠️ Viêm da tiếp xúc dị ứng:**
            - Ngứa nhiều
            - Có thể lan ra ngoài vị trí tiếp xúc
            - Xuất hiện sau 24-48 giờ

            ## Nguyên nhân:

            **1. Chất kích ứng:**
            - **Hóa chất:** Xà phòng, chất tẩy rửa, dung môi
            - **Kim loại:** Nikel (trang sức, khóa)
            - **Mỹ phẩm:** Son, kem, nước hoa
            - **Thực vật:** Cây thường xuân độc, xoài
            - **Thuốc bôi:** Neomycin, Bacitracin

            **2. Yếu tố nguy cơ:**
            - Tiếp xúc với chất kích ứng/dị ứng
            - Da khô, nhạy cảm
            - Tiền sử dị ứng
            - Nghề nghiệp (thợ làm tóc, y tá, thợ xây)

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Vị trí tiếp xúc

            **Xét nghiệm:**
            - **Test áp da:** Tìm chất dị ứng (nếu viêm da tiếp xúc dị ứng)
            - **Sinh thiết da:** Nếu không rõ ràng

            ## Điều trị:

            **1. Tránh tiếp xúc (QUAN TRỌNG NHẤT!):**
            - Tránh chất gây kích ứng/dị ứng
            - Mang găng tay, quần áo bảo hộ nếu cần

            **2. Thuốc bôi:**
            - **Corticosteroid bôi:** Hydrocortisone, Betamethasone (giảm viêm, ngứa)
            - **Kem dưỡng ẩm:** Giữ da ẩm, giảm khô
            - **Calamine lotion:** Giảm ngứa

            **3. Thuốc uống:**
            - **Antihistamine:** Cetirizine, Loratadine (giảm ngứa)
            - **Corticosteroid uống:** Nếu nặng, lan rộng (Prednisone)

            **4. Chăm sóc da:**
            - Rửa sạch vùng tiếp xúc
            - Dưỡng ẩm da
            - Tránh gãi (gây nhiễm khuẩn)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Bình thường:**
            - Ăn uống bình thường
            - Không cần kiêng khem đặc biệt

            **2. Tránh:**
            - Thức ăn gây dị ứng (nếu có)
            - Đồ cay nóng (có thể làm ngứa tăng)

            ## 🏃 TẬP THỂ DỤC:

            **1. Bình thường:**
            - Tập thể dục bình thường
            - Tránh đổ mồ hôi nhiều (có thể làm ngứa tăng)

            **2. Lưu ý:**
            - Rửa sạch sau khi tập
            - Dưỡng ẩm da

            ## 💊 QUẢN LÝ THUỐC:

            **1. Corticosteroid bôi:**
            - Bôi 1-2 lần/ngày
            - Bôi mỏng, không bôi quá nhiều
            - Không bôi quá 2 tuần (trừ khi có chỉ định)

            **2. Antihistamine:**
            - Uống buổi tối (giảm ngứa về đêm)
            - Có thể gây buồn ngủ

            **3. Kem dưỡng ẩm:**
            - Bôi thường xuyên
            - Sau khi tắm

            **4. Lưu ý:**
            - Tránh gãi (quan trọng!)
            - Báo bác sĩ nếu không cải thiện

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Viêm da nặng:**
            - Viêm da lan rộng
            - Không đáp ứng điều trị

            **2. Nhiễm khuẩn:**
            - Nhiễm khuẩn da (mủ, sưng đau)
            - Sốt

            **3. Phản ứng dị ứng nặng:**
            - Phù nề
            - Khó thở

            ## 💡 PHÒNG NGỪA:

            **1. Tránh tiếp xúc:**
            - **Tránh chất gây kích ứng/dị ứng** (quan trọng nhất!)
            - Đọc nhãn sản phẩm
            - Test trước khi dùng sản phẩm mới

            **2. Bảo vệ da:**
            - Mang găng tay khi tiếp xúc hóa chất
            - Quần áo bảo hộ nếu cần
            - Dưỡng ẩm da

            **3. Vệ sinh:**
            - Rửa sạch sau khi tiếp xúc
            - Dưỡng ẩm da sau khi rửa

            **4. Mỹ phẩm:**
            - Chọn sản phẩm không gây dị ứng
            - Test trước khi dùng
            - Tránh sản phẩm có chất gây dị ứng đã biết

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tránh tiếp xúc** (quan trọng nhất!)
            - Đọc nhãn sản phẩm
            - Test trước khi dùng sản phẩm mới

            **2. Khi bị viêm da tiếp xúc:**
            - Tránh tiếp xúc ngay
            - Rửa sạch vùng tiếp xúc
            - Bôi thuốc theo chỉ định
            - Tránh gãi

            **3. Sống tích cực:**
            - Viêm da tiếp xúc có thể điều trị khỏi
            - Tránh tiếp xúc → Không tái phát
            - Điều trị đúng → Giảm triệu chứng

            **4. Nghề nghiệp:**
            - Nếu do nghề nghiệp, cần bảo vệ da
            - Mang găng tay, quần áo bảo hộ
            - Dưỡng ẩm da thường xuyên
            """,
            related_disease="contact_dermatitis",
            related_drugs=["Hydrocortisone", "Betamethasone", "Cetirizine", "Loratadine", "Calamine"],
            printable=True
        ),

]
