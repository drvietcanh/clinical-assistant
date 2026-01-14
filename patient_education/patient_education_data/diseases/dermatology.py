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

        PatientEducationTopic(
            id="tinea_dermatophytosis_basics",
            title="Understanding Tinea (Ringworm)",
            title_vn="Hiểu về Nấm da",
            category="Disease",
            content="""
            # Hiểu về Nấm da

            ## Nấm da là gì?

            Nấm da (Tinea, Dermatophytosis) là bệnh nhiễm nấm ở da, tóc, móng do các loại nấm sợi (dermatophytes) gây ra. Bệnh rất phổ biến ở Việt Nam do khí hậu nóng ẩm, đặc biệt vào mùa mưa.

            **⚠️ Đặc điểm:**
            - Nhiễm nấm ở da, tóc, móng
            - Rất phổ biến ở khí hậu nóng ẩm
            - Dễ lây lan
            - Có thể điều trị khỏi

            **Phân loại theo vị trí:**
            - **Nấm da đầu (Tinea capitis):** Ở da đầu, tóc
            - **Nấm da thân (Tinea corporis):** Ở thân mình, tay chân
            - **Nấm bẹn (Tinea cruris):** Ở vùng bẹn, đùi trong
            - **Nấm chân (Tinea pedis):** Ở bàn chân, kẽ ngón chân
            - **Nấm tay (Tinea manuum):** Ở bàn tay
            - **Nấm móng (Tinea unguium/Onychomycosis):** Ở móng tay, móng chân

            **Loại nấm:**
            - **Trichophyton:** Phổ biến nhất
            - **Microsporum:** Thường ở da đầu
            - **Epidermophyton:** Thường ở bẹn, bàn chân

            ## Triệu chứng:

            **Nấm da thân (Tinea corporis):**
            - **Tổn thương:** Mảng đỏ, tròn, có viền rõ, bong vảy
            - **Ngứa:** Ngứa nhẹ đến vừa
            - **Lan rộng:** Từ trung tâm ra ngoài
            - **Vị trí:** Thân mình, tay, chân, mặt

            **Nấm bẹn (Tinea cruris):**
            - **Tổn thương:** Mảng đỏ, bong vảy ở vùng bẹn, đùi trong
            - **Ngứa:** Ngứa nhiều, đặc biệt khi ra mồ hôi
            - **Đối xứng:** Thường cả hai bên
            - **Không lan:** Không lan đến bìu, dương vật

            **Nấm chân (Tinea pedis):**
            - **Kẽ ngón chân:** Trắng, ẩm ướt, nứt nẻ (kẽ ngón 4-5)
            - **Lòng bàn chân:** Đỏ, bong vảy, khô
            - **Mụn nước:** Mụn nước nhỏ, ngứa (dạng mụn nước)
            - **Ngứa:** Ngứa nhiều

            **Nấm da đầu (Tinea capitis):**
            - **Rụng tóc:** Rụng tóc từng mảng
            - **Bong vảy:** Vảy trắng, xám
            - **Ngứa:** Ngứa nhẹ
            - **Sưng hạch:** Có thể sưng hạch cổ
            - **Thường gặp:** Trẻ em

            **Nấm móng (Tinea unguium):**
            - **Móng dày:** Móng dày, giòn, dễ gãy
            - **Đổi màu:** Móng vàng, nâu, trắng
            - **Bong móng:** Móng bong khỏi nền móng
            - **Mất bóng:** Móng mất độ bóng
            - **Thường gặp:** Móng chân

            **⚠️ Bội nhiễm:**
            - Da đỏ, sưng, đau
            - Mủ, vảy vàng
            - Sốt (hiếm)

            ## Nguyên nhân:

            **1. Nấm:**
            - **Dermatophytes:** Trichophyton, Microsporum, Epidermophyton
            - Sống trên da, tóc, móng
            - Phát triển trong môi trường ẩm ướt

            **2. Lây truyền:**
            - **Tiếp xúc trực tiếp:** Từ người bệnh
            - **Tiếp xúc gián tiếp:** Đồ dùng, quần áo, khăn tắm, giày dép
            - **Từ động vật:** Chó, mèo (nấm da đầu)
            - **Từ đất:** Hiếm

            **3. Yếu tố nguy cơ:**
            - **Khí hậu nóng ẩm:** Mùa mưa, mùa hè
            - **Ra mồ hôi nhiều:** Tập thể dục, lao động
            - **Vệ sinh kém:** Không tắm rửa thường xuyên
            - **Dùng chung đồ:** Khăn tắm, giày dép, quần áo
            - **Đi chân đất:** Ở nơi công cộng (hồ bơi, phòng tắm)
            - **Hệ miễn dịch yếu:** Đái tháo đường, HIV
            - **Mang giày kín:** Giày bít, không thông thoáng

            **4. Bệnh khác:**
            - Đái tháo đường
            - Béo phì
            - Suy giảm miễn dịch

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Tổn thương đặc trưng

            **Xét nghiệm:**
            - **Soi tươi:** Lấy vảy da, tóc, móng, soi dưới kính hiển vi
            - **Nuôi cấy:** Nuôi cấy nấm (2-4 tuần)
            - **Đèn Wood:** Phát quang (một số loại nấm)

            **⚠️ Phân biệt:**
            - **Vẩy nến:** Mảng đỏ, bong vảy dày, không ngứa nhiều
            - **Chàm:** Mảng đỏ, ngứa, không có viền rõ
            - **Viêm da tiếp xúc:** Tổn thương sau tiếp xúc chất gây dị ứng

            ## Điều trị:

            **1. Điều trị tại chỗ (Nấm da nhẹ, khu trú):**
            - **Kem, mỡ chống nấm:**
              - **Clotrimazole, Miconazole:** Bôi 2 lần/ngày, 2-4 tuần
              - **Terbinafine:** Bôi 1-2 lần/ngày, 1-2 tuần
              - **Ketoconazole:** Bôi 1-2 lần/ngày, 2-4 tuần
            - **Dầu gội chống nấm:** Ketoconazole (nấm da đầu)
            - **Cách dùng:** Bôi rộng ra ngoài viền tổn thương 1-2cm
            - **Thời gian:** Tiếp tục 1-2 tuần sau khi hết triệu chứng

            **2. Điều trị toàn thân (Nấm nặng, lan rộng, nấm móng, nấm da đầu):**
            - **Terbinafine:** 250mg/ngày, 2-4 tuần (nấm da), 6-12 tuần (nấm móng)
            - **Itraconazole:** 200mg/ngày, 1-2 tuần (nấm da), 12 tuần (nấm móng)
            - **Fluconazole:** 150-300mg/tuần, 2-4 tuần (nấm da)
            - **Griseofulvin:** 500-1000mg/ngày, 4-8 tuần (nấm da đầu)

            **3. Điều trị nấm móng:**
            - **Thuốc uống:** Terbinafine, Itraconazole (12 tuần)
            - **Sơn móng:** Ciclopirox, Amorolfine (6-12 tháng)
            - **Cắt móng:** Cắt móng bị bệnh

            **4. Điều trị nấm da đầu:**
            - **Thuốc uống:** Griseofulvin, Terbinafine (4-8 tuần)
            - **Dầu gội:** Ketoconazole (giảm lây lan)
            - **Cắt tóc:** Cắt tóc ngắn (nếu cần)

            **⚠️ Lưu ý:**
            - Điều trị đủ thời gian (quan trọng!)
            - Không ngừng thuốc sớm (tái phát)
            - Vệ sinh sạch sẽ
            - Tránh lây lan

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Thực phẩm chống nấm:** Tỏi, hành, gừng, nghệ
            - **Probiotic:** Sữa chua, kefir (tăng lợi khuẩn)
            - **Vitamin C:** Trái cây, rau xanh (tăng miễn dịch)
            - **Kẽm:** Thịt, cá, đậu (tăng miễn dịch)
            - **Chất xơ:** Rau xanh, trái cây (tăng miễn dịch)

            **2. Thực phẩm nên tránh:**
            - **Đường:** Đường, bánh kẹo, nước ngọt (nấm phát triển)
            - **Tinh bột tinh chế:** Bánh mì trắng, gạo trắng
            - **Rượu bia:** Làm suy giảm miễn dịch
            - **Thực phẩm chế biến:** Đồ hộp, thức ăn nhanh

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + sữa chua + trái cây
            - **Trưa:** Cơm + canh (có tỏi, gừng) + thịt/cá + rau xanh
            - **Chiều:** Cơm + canh (có tỏi, gừng) + thịt/cá + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            **4. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Tăng miễn dịch
            - Tránh đường (nấm phát triển)

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - Tăng miễn dịch

            **2. Lưu ý:**
            - **Tắm rửa ngay sau tập:** Tránh mồ hôi ứ đọng
            - **Thay quần áo:** Quần áo khô, sạch
            - **Giày dép:** Thông thoáng, khô ráo
            - **Tránh:** Tập ở nơi ẩm ướt, bẩn

            **3. Vệ sinh:**
            - Rửa tay sau khi chạm vào tổn thương
            - Không dùng chung khăn tắm, quần áo

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc bôi:**
            - **Cách dùng:** Bôi 2 lần/ngày (sáng, tối)
            - **Bôi rộng:** Ra ngoài viền tổn thương 1-2cm
            - **Thời gian:** 2-4 tuần, tiếp tục 1-2 tuần sau khi hết
            - **Lưu ý:** Rửa tay trước và sau khi bôi

            **2. Thuốc uống:**
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Đủ thời gian:** Không ngừng sớm (quan trọng!)
            - **Tác dụng phụ:** Đau bụng, buồn nôn, phát ban (hiếm)
            - **Lưu ý:** Xét nghiệm chức năng gan (nếu dùng lâu)

            **3. Dầu gội:**
            - **Ketoconazole:** 2-3 lần/tuần (nấm da đầu)
            - **Để 5 phút:** Trước khi gội sạch

            **4. Lưu ý:**
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu không cải thiện
            - Tránh lây lan cho người khác

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Nấm nặng:**
            - Lan rộng, không đáp ứng điều trị tại chỗ
            - Nấm móng, nấm da đầu
            - Bội nhiễm (sưng, đau, mủ)

            **2. Tác dụng phụ:**
            - Phát ban, ngứa toàn thân
            - Đau bụng, buồn nôn nặng
            - Vàng da (tổn thương gan)

            **3. Tái phát nhiều lần:**
            - Tái phát > 3 lần/năm
            - Cần đánh giá thêm

            **4. Bệnh nền:**
            - Đái tháo đường
            - Suy giảm miễn dịch

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Tắm rửa thường xuyên:** Mỗi ngày, đặc biệt sau khi ra mồ hôi
            - **Lau khô:** Lau khô người, đặc biệt kẽ ngón chân, bẹn
            - **Quần áo:** Quần áo sạch, khô, thông thoáng
            - **Giày dép:** Thông thoáng, khô ráo, thay thường xuyên

            **2. Tránh lây lan:**
            - **Không dùng chung:** Khăn tắm, quần áo, giày dép
            - **Vệ sinh:** Giặt quần áo, khăn tắm thường xuyên
            - **Phơi nắng:** Phơi nắng quần áo, giày dép

            **3. Môi trường:**
            - **Thông thoáng:** Phòng ốc thông thoáng, khô ráo
            - **Tránh ẩm ướt:** Tránh nơi ẩm ướt, bẩn
            - **Vệ sinh:** Vệ sinh nhà tắm, phòng thay đồ

            **4. Khi có người bệnh:**
            - Điều trị ngay
            - Tránh tiếp xúc trực tiếp
            - Vệ sinh đồ dùng

            **5. Đi chân đất:**
            - **Tránh:** Đi chân đất ở nơi công cộng (hồ bơi, phòng tắm)
            - **Mang dép:** Mang dép riêng
            - **Rửa chân:** Rửa chân sau khi đi

            **6. Vật nuôi:**
            - Khám thú y nếu vật nuôi có nấm
            - Điều trị vật nuôi

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Vệ sinh sạch sẽ** (quan trọng nhất!)
            - **Tránh ẩm ướt**
            - **Không dùng chung đồ**

            **2. Khi bị nấm:**
            - Điều trị ngay, đủ thời gian
            - Vệ sinh sạch sẽ
            - Tránh lây lan

            **3. Sống tích cực:**
            - Nấm da rất phổ biến
            - Có thể điều trị khỏi
            - Phòng ngừa tốt → Không tái phát

            **4. Kiên nhẫn:**
            - Điều trị cần thời gian (2-4 tuần)
            - Không ngừng thuốc sớm
            - Tiếp tục điều trị sau khi hết triệu chứng
            """,
            related_disease="tinea",
            related_drugs=["Clotrimazole", "Miconazole", "Terbinafine", "Ketoconazole", "Itraconazole", "Fluconazole"],
            printable=True
        ),

        PatientEducationTopic(
            id="acne_basics",
            title="Understanding Acne",
            title_vn="Hiểu về Mụn trứng cá",
            category="Disease",
            content="""
            # Hiểu về Mụn trứng cá

            ## Mụn trứng cá là gì?

            Mụn trứng cá (Acne) là bệnh viêm da mạn tính do tắc nghẽn nang lông-tuyến bã, đặc trưng bởi mụn đầu đen, mụn đầu trắng, mụn viêm. Bệnh rất phổ biến ở thanh thiếu niên (80-90%), nhưng có thể gặp ở mọi lứa tuổi.

            **⚠️ Đặc điểm:**
            - Viêm da mạn tính do tắc nghẽn nang lông-tuyến bã
            - Rất phổ biến ở thanh thiếu niên (80-90%)
            - Có thể ảnh hưởng đến tâm lý
            - Có thể điều trị và phòng ngừa

            **Phân loại:**
            - **Mụn đầu đen (Comedones):** Lỗ chân lông bị tắc, mở
            - **Mụn đầu trắng (Whiteheads):** Lỗ chân lông bị tắc, đóng
            - **Mụn viêm (Papules):** Mụn đỏ, sưng
            - **Mụn mủ (Pustules):** Mụn có mủ
            - **Mụn nang (Cysts):** Mụn sâu, lớn, đau

            **Độ nặng:**
            - **Nhẹ:** Mụn đầu đen, đầu trắng, vài mụn viêm
            - **Trung bình:** Nhiều mụn viêm, mụn mủ
            - **Nặng:** Mụn nang, sẹo, viêm nặng

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Mụn đầu đen:** Lỗ chân lông mở, màu đen (do oxy hóa)
            - **Mụn đầu trắng:** Lỗ chân lông đóng, màu trắng
            - **Mụn viêm:** Mụn đỏ, sưng, đau
            - **Mụn mủ:** Mụn có mủ trắng/vàng
            - **Mụn nang:** Mụn sâu, lớn, đau, có thể để lại sẹo

            **Vị trí:**
            - **Mặt:** Trán, má, cằm, mũi (phổ biến nhất)
            - **Lưng:** Lưng trên, vai
            - **Ngực:** Ngực trên
            - **Cổ:** Cổ

            **Triệu chứng khác:**
            - Da nhờn
            - Lỗ chân lông to
            - Sẹo (sau khi mụn lành)
            - Thâm (sau khi mụn lành)

            **⚠️ Ảnh hưởng tâm lý:**
            - Tự ti, mặc cảm
            - Trầm cảm, lo âu
            - Tránh giao tiếp xã hội

            ## Nguyên nhân:

            **1. Cơ chế:**
            - **Tăng tiết bã nhờn:** Tuyến bã tiết nhiều dầu
            - **Tắc nghẽn nang lông:** Tế bào chết + bã nhờn tắc lỗ chân lông
            - **Vi khuẩn:** Propionibacterium acnes (P. acnes) phát triển
            - **Viêm:** Viêm do vi khuẩn, tế bào chết

            **2. Hormone:**
            - **Androgen (testosterone):** Tăng ở tuổi dậy thì → Tăng tiết bã nhờn
            - **Thay đổi hormone:** Kinh nguyệt, mang thai, mãn kinh
            - **Hội chứng buồng trứng đa nang (PCOS):** Tăng androgen

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** Thanh thiếu niên (12-24 tuổi)
            - **Di truyền:** Có người thân bị mụn
            - **Hormone:** Thay đổi hormone
            - **Mỹ phẩm:** Mỹ phẩm gây tắc lỗ chân lông
            - **Stress:** Căng thẳng, lo âu
            - **Chế độ ăn:** Đường, sữa (có thể)
            - **Thuốc:** Corticosteroid, lithium, một số thuốc

            **4. Yếu tố làm nặng:**
            - **Nặn mụn:** Làm viêm nặng, sẹo
            - **Chà xát:** Chà xát da mạnh
            - **Mỹ phẩm:** Mỹ phẩm gây tắc
            - **Ánh nắng:** Có thể làm nặng (một số người)
            - **Ra mồ hôi:** Mồ hôi + bụi bẩn

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Vị trí đặc trưng

            **Khám:**
            - Đánh giá độ nặng
            - Loại mụn
            - Sẹo, thâm

            **Xét nghiệm:**
            - Thường không cần
            - Xét nghiệm hormone (nếu nghi ngờ PCOS)

            **⚠️ Phân biệt:**
            - **Rosacea:** Đỏ mặt, mụn mủ, không có mụn đầu đen
            - **Viêm nang lông:** Viêm nang lông do vi khuẩn
            - **Dị ứng mỹ phẩm:** Phát ban sau dùng mỹ phẩm

            ## Điều trị:

            **1. Điều trị tại chỗ (Mụn nhẹ-trung bình):**
            - **Benzoyl Peroxide:**
              - 2.5-10%, bôi 1-2 lần/ngày
              - Diệt vi khuẩn, giảm viêm
              - Tác dụng phụ: Khô da, kích ứng
            - **Retinoid (Tretinoin, Adapalene):**
              - Bôi tối, 1 lần/ngày
              - Giảm tắc nghẽn, tái tạo da
              - Tác dụng phụ: Khô da, đỏ, bong vảy (ban đầu)
            - **Kháng sinh tại chỗ (Clindamycin, Erythromycin):**
              - Bôi 2 lần/ngày
              - Diệt vi khuẩn
              - Thường kết hợp với Benzoyl Peroxide
            - **Azelaic Acid:**
              - Bôi 2 lần/ngày
              - Diệt vi khuẩn, giảm viêm, làm sáng da

            **2. Điều trị toàn thân (Mụn trung bình-nặng):**
            - **Kháng sinh uống:**
              - **Doxycycline, Minocycline:** 50-100mg/ngày, 3-6 tháng
              - **Erythromycin:** 500-1000mg/ngày
              - Diệt vi khuẩn, giảm viêm
            - **Isotretinoin (Accutane):**
              - 0.5-1mg/kg/ngày, 4-6 tháng
              - Rất hiệu quả, nhưng có tác dụng phụ nặng
              - **⚠️ Quan trọng:** Không được mang thai khi dùng!
            - **Thuốc tránh thai (phụ nữ):**
              - Giảm androgen, giảm mụn
            - **Spironolactone (phụ nữ):**
              - Giảm androgen, giảm mụn

            **3. Điều trị sẹo, thâm:**
            - **Retinoid:** Tretinoin (làm mờ sẹo, thâm)
            - **Chemical peel:** Lột da bằng hóa chất
            - **Laser:** Laser resurfacing
            - **Microneedling:** Kim vi điểm
            - **Filler:** Tiêm filler (sẹo lõm)

            **⚠️ Lưu ý:**
            - Điều trị cần thời gian (4-12 tuần)
            - Kết hợp nhiều phương pháp
            - Tránh nặn mụn

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Rau xanh, trái cây:** Vitamin, chất chống oxy hóa
            - **Cá béo:** Omega-3 (giảm viêm)
            - **Ngũ cốc nguyên hạt:** Chỉ số đường huyết thấp
            - **Protein nạc:** Thịt, cá, đậu
            - **Nước:** Uống nhiều nước (2-3 lít/ngày)

            **2. Thực phẩm nên tránh (có thể):**
            - **Đường:** Đường, bánh kẹo, nước ngọt (có thể làm nặng)
            - **Sữa:** Sữa, phô mai (một số người)
            - **Tinh bột tinh chế:** Bánh mì trắng, gạo trắng
            - **Thức ăn nhanh:** Hamburger, pizza, đồ chiên rán
            - **Chocolate:** Có thể (một số người)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây + sữa chua
            - **Trưa:** Cơm gạo lứt + canh rau + cá/thịt + rau xanh
            - **Chiều:** Cơm gạo lứt + canh rau + cá/thịt + rau xanh
            - **Bữa phụ:** Trái cây, hạt

            **4. Lưu ý:**
            - Chế độ ăn ảnh hưởng khác nhau ở mỗi người
            - Ghi nhật ký thức ăn để tìm yếu tố kích thích
            - Ăn đủ dinh dưỡng

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - Giảm stress (có thể giảm mụn)

            **2. Lưu ý:**
            - **Tắm rửa ngay sau tập:** Tránh mồ hôi + bụi bẩn
            - **Thay quần áo:** Quần áo khô, sạch
            - **Rửa mặt:** Rửa mặt sau khi tập
            - **Tránh:** Chà xát da mạnh

            **3. Vệ sinh:**
            - Rửa tay trước khi chạm mặt
            - Không chạm tay vào mặt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc bôi:**
            - **Cách dùng:** Bôi tối (Retinoid), sáng-tối (Benzoyl Peroxide, kháng sinh)
            - **Lượng:** Một lớp mỏng, không quá nhiều
            - **Thời gian:** 4-12 tuần
            - **Lưu ý:** Bắt đầu với liều thấp, tăng dần

            **2. Thuốc uống:**
            - **Kháng sinh:** Uống đều đặn, đủ thời gian
            - **Isotretinoin:** 
              - **⚠️ Quan trọng:** Không được mang thai!
              - Xét nghiệm máu trước và trong điều trị
              - Tác dụng phụ: Khô da, môi, mắt, đau khớp
            - **Thuốc tránh thai:** Uống đều đặn

            **3. Tác dụng phụ:**
            - **Khô da:** Dưỡng ẩm
            - **Kích ứng:** Giảm tần suất, liều
            - **Nhạy cảm ánh nắng:** Dùng kem chống nắng

            **4. Lưu ý:**
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ nặng
            - Điều trị cần thời gian (4-12 tuần)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Mụn nặng:**
            - Mụn nang, sẹo
            - Không đáp ứng điều trị tại chỗ
            - Cần điều trị toàn thân

            **2. Tác dụng phụ:**
            - Phát ban, ngứa toàn thân
            - Đau bụng, buồn nôn nặng
            - Vàng da (tổn thương gan)
            - Trầm cảm (Isotretinoin)

            **3. Ảnh hưởng tâm lý:**
            - Trầm cảm, lo âu
            - Tự ti, mặc cảm nặng
            - Cần tư vấn tâm lý

            **4. Sẹo:**
            - Sẹo nhiều, ảnh hưởng thẩm mỹ
            - Cần điều trị sẹo

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh da:**
            - **Rửa mặt:** 2 lần/ngày (sáng, tối) với sữa rửa mặt nhẹ
            - **Không chà xát:** Rửa nhẹ nhàng
            - **Tẩy trang:** Tẩy trang trước khi rửa mặt (nếu trang điểm)
            - **Dưỡng ẩm:** Dưỡng ẩm sau khi rửa mặt

            **2. Mỹ phẩm:**
            - **Không gây tắc:** Mỹ phẩm không gây tắc lỗ chân lông (non-comedogenic)
            - **Tránh:** Mỹ phẩm dầu, nặng
            - **Tẩy trang:** Tẩy trang trước khi ngủ

            **3. Tránh:**
            - **Nặn mụn:** Làm viêm nặng, sẹo
            - **Chạm tay vào mặt:** Tay có vi khuẩn
            - **Ánh nắng:** Dùng kem chống nắng (SPF 30+)

            **4. Chế độ ăn:**
            - Ăn đủ dinh dưỡng
            - Tránh đường, sữa (nếu có ảnh hưởng)

            **5. Quản lý stress:**
            - Tập thể dục, yoga, thiền
            - Ngủ đủ giấc

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Vệ sinh da sạch sẽ** (quan trọng nhất!)
            - **Tránh nặn mụn**
            - **Dùng mỹ phẩm phù hợp**

            **2. Khi bị mụn:**
            - Điều trị sớm, đúng cách
            - Kiên nhẫn (4-12 tuần)
            - Không nặn mụn

            **3. Sống tích cực:**
            - Mụn rất phổ biến, không phải lỗi của bạn
            - Có thể điều trị khỏi
            - Đừng để mụn ảnh hưởng đến tâm lý

            **4. Tư vấn:**
            - Khám bác sĩ da liễu nếu mụn nặng
            - Tư vấn tâm lý nếu cần
            - Tham gia nhóm hỗ trợ
            """,
            related_disease="acne",
            related_drugs=["Benzoyl Peroxide", "Tretinoin", "Adapalene", "Clindamycin", "Doxycycline", "Isotretinoin"],
            printable=True
        ),

        PatientEducationTopic(
            id="eczema_basics",
            title="Understanding Eczema",
            title_vn="Hiểu về Chàm",
            category="Disease",
            content="""
            # Hiểu về Chàm

            ## Chàm là gì?

            Chàm (Eczema) là bệnh viêm da mạn tính, đặc trưng bởi da đỏ, ngứa, khô, bong vảy. Chàm là thuật ngữ chung cho nhiều loại viêm da, phổ biến nhất là viêm da cơ địa (Atopic Dermatitis).

            **⚠️ Đặc điểm:**
            - Viêm da mạn tính
            - Da đỏ, ngứa, khô, bong vảy
            - Rất phổ biến
            - Có thể kiểm soát

            **Phân loại:**
            - **Viêm da cơ địa (Atopic Dermatitis):** Phổ biến nhất, liên quan đến dị ứng
            - **Viêm da tiếp xúc:** Do tiếp xúc chất gây dị ứng/kích thích
            - **Viêm da tiết bã:** Ở da đầu, mặt (gàu, viêm da tiết bã)
            - **Chàm đồng tiền:** Tổn thương hình tròn

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Da đỏ:** Da đỏ, viêm
            - **Ngứa:** Ngứa dữ dội, đặc biệt ban đêm
            - **Da khô:** Da khô, bong vảy
            - **Mụn nước:** Mụn nước nhỏ (có thể vỡ, chảy dịch)
            - **Da dày lên:** Da dày lên, nứt nẻ (mạn tính)

            **Vị trí:**
            - **Trẻ em:** Mặt, tay chân, thân mình
            - **Người lớn:** Nếp gấp (khuỷu tay, đầu gối, cổ)

            **Triệu chứng khác:**
            - Da nhạy cảm
            - Nhiễm trùng da thứ phát (gãi → nhiễm khuẩn)

            **⚠️ Bội nhiễm:**
            - Da đỏ, sưng, đau
            - Mủ, vảy vàng
            - Sốt (hiếm)

            ## Nguyên nhân:

            **1. Viêm da cơ địa:**
            - **Di truyền:** Có người thân bị dị ứng
            - **Cơ địa dị ứng:** Dễ dị ứng
            - **Yếu tố kích thích:**
              - Dị nguyên (bụi, lông thú, phấn hoa)
              - Thực phẩm (trứng, sữa, đậu phộng)
              - Stress
              - Thay đổi thời tiết
              - Mồ hôi

            **2. Viêm da tiếp xúc:**
            - **Chất gây dị ứng:** Nikel, cao su, mỹ phẩm
            - **Chất kích thích:** Xà phòng, chất tẩy rửa

            **3. Yếu tố nguy cơ:**
            - Di truyền
            - Cơ địa dị ứng
            - Môi trường khô
            - Stress

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám da

            **Xét nghiệm:**
            - **Test dị ứng:** Xác định dị nguyên (nếu cần)
            - **Sinh thiết da:** Hiếm dùng

            **⚠️ Phân biệt:**
            - Vẩy nến
            - Nấm da
            - Viêm da tiếp xúc

            ## Điều trị:

            **1. Dưỡng ẩm (QUAN TRỌNG NHẤT!):**
            - **Dưỡng ẩm:** Dưỡng ẩm 2-3 lần/ngày
            - **Sau tắm:** Dưỡng ẩm ngay sau tắm
            - **Loại:** Kem, mỡ (tốt hơn lotion)

            **2. Thuốc bôi:**
            - **Corticosteroid tại chỗ:**
              - Hydrocortisone (nhẹ)
              - Betamethasone (trung bình-nặng)
              - Bôi 1-2 lần/ngày
            - **Tacrolimus, Pimecrolimus:** Ức chế miễn dịch (không phải steroid)
            - **Kháng sinh:** Nếu bội nhiễm

            **3. Thuốc uống:**
            - **Antihistamine:** Cetirizine, Loratadine (giảm ngứa)
            - **Corticosteroid:** Prednisolone (ngắn hạn, nếu nặng)
            - **Cyclosporine:** Nếu nặng, không đáp ứng

            **4. Điều trị không dùng thuốc:**
            - **Tránh dị nguyên:** Tránh chất gây dị ứng
            - **Quản lý stress:** Stress có thể làm nặng
            - **Tắm đúng cách:** Tắm nước ấm, không nóng, < 10 phút

            **⚠️ Lưu ý:**
            - Dưỡng ẩm quan trọng nhất!
            - Tránh gãi (làm nặng)
            - Điều trị đủ thời gian

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm)
            - **Rau xanh:** Rau cải, rau bina (chất chống oxy hóa)
            - **Trái cây:** Dâu, cam (vitamin C)
            - **Probiotic:** Sữa chua (tăng lợi khuẩn)

            **2. Thực phẩm nên tránh (nếu dị ứng):**
            - **Trứng:** Nếu dị ứng trứng
            - **Sữa:** Nếu dị ứng sữa
            - **Đậu phộng:** Nếu dị ứng đậu phộng
            - **Hải sản:** Nếu dị ứng hải sản

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + sữa chua + trái cây
            - **Trưa:** Cơm + cá + rau xanh
            - **Chiều:** Cơm + cá + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            **4. Lưu ý:**
            - Ghi nhật ký thức ăn để tìm yếu tố kích thích
            - Tránh thức ăn gây dị ứng (nếu biết)

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - Giảm stress (có thể giảm chàm)

            **2. Lưu ý:**
            - **Tắm ngay sau tập:** Tránh mồ hôi ứ đọng
            - **Thay quần áo:** Quần áo khô, sạch
            - **Dưỡng ẩm:** Dưỡng ẩm sau tắm

            ## 💊 QUẢN LÝ THUỐC:

            **1. Dưỡng ẩm:**
            - **Bôi 2-3 lần/ngày:** Quan trọng nhất!
            - **Sau tắm:** Bôi ngay sau tắm
            - **Loại:** Kem, mỡ (tốt hơn lotion)

            **2. Corticosteroid tại chỗ:**
            - **Bôi 1-2 lần/ngày:** Theo chỉ định
            - **Giảm liều từ từ:** Khi đã cải thiện
            - **Không dùng lâu dài:** Tránh teo da

            **3. Antihistamine:**
            - **Uống tối:** Giảm ngứa ban đêm
            - **Theo chỉ định bác sĩ**

            **4. Lưu ý:**
            - Dưỡng ẩm quan trọng nhất!
            - Không tự ý dùng corticosteroid lâu dài
            - Báo bác sĩ nếu không cải thiện

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Bội nhiễm:**
            - Da đỏ, sưng, đau
            - Mủ, vảy vàng
            - Sốt

            **2. Chàm nặng:**
            - Lan rộng, không đáp ứng điều trị
            - Ảnh hưởng cuộc sống

            **3. Tác dụng phụ:**
            - Teo da (do corticosteroid lâu dài)
            - Nhiễm trùng nặng

            ## 💡 PHÒNG NGỪA:

            **1. Dưỡng ẩm:**
            - **Dưỡng ẩm thường xuyên** (quan trọng nhất!)
            - 2-3 lần/ngày
            - Sau tắm

            **2. Tránh dị nguyên:**
            - Tránh chất gây dị ứng (nếu biết)
            - Vệ sinh môi trường

            **3. Tắm đúng cách:**
            - Tắm nước ấm, không nóng
            - < 10 phút
            - Dưỡng ẩm ngay sau tắm

            **4. Tránh:**
            - Gãi (làm nặng)
            - Xà phòng mạnh
            - Quần áo thô, chật

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Dưỡng ẩm thường xuyên** (quan trọng nhất!)
            - Tránh dị nguyên
            - Tắm đúng cách

            **2. Khi bị chàm:**
            - Dưỡng ẩm ngay
            - Bôi thuốc theo chỉ định
            - Tránh gãi

            **3. Sống tích cực:**
            - Chàm có thể kiểm soát
            - Điều trị đúng → Cải thiện
            - Phòng ngừa tốt → Không tái phát
            """,
            related_disease="eczema",
            related_drugs=["Hydrocortisone", "Betamethasone", "Tacrolimus", "Cetirizine", "Loratadine"],
            printable=True
        ),

        PatientEducationTopic(
            id="onychomycosis_basics",
            title="Understanding Onychomycosis",
            title_vn="Hiểu về Nấm móng",
            category="Disease",
            content="""
            # Hiểu về Nấm móng

            ## Nấm móng là gì?

            Nấm móng (Onychomycosis) là tình trạng nhiễm nấm ở móng tay hoặc móng chân, gây móng dày, giòn, đổi màu. Bệnh phổ biến, đặc biệt ở người cao tuổi, móng chân.

            **⚠️ Đặc điểm:**
            - Nhiễm nấm ở móng
            - Móng dày, giòn, đổi màu
            - Phổ biến (10% dân số)
            - Khó điều trị, dễ tái phát

            **Phân loại:**
            - **Nấm móng chân:** Phổ biến hơn (80%)
            - **Nấm móng tay:** Ít phổ biến hơn (20%)

            **Loại nấm:**
            - **Dermatophytes:** Trichophyton (phổ biến nhất)
            - **Nấm men:** Candida
            - **Nấm mốc:** Hiếm

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Móng dày:** Móng dày, giòn
            - **Đổi màu:** Móng vàng, nâu, trắng, đen
            - **Bong móng:** Móng bong khỏi nền móng
            - **Mất bóng:** Móng mất độ bóng
            - **Vụn móng:** Móng vụn, dễ gãy

            **Vị trí:**
            - **Móng chân:** Phổ biến hơn, đặc biệt ngón cái
            - **Móng tay:** Ít phổ biến hơn

            **Triệu chứng khác:**
            - Đau (nếu nặng)
            - Khó chịu khi đi giày
            - Ảnh hưởng thẩm mỹ

            **⚠️ Biến chứng:**
            - Nhiễm trùng thứ phát
            - Mất móng
            - Lây sang móng khác

            ## Nguyên nhân:

            **1. Nấm:**
            - **Dermatophytes:** Trichophyton rubrum, T. mentagrophytes
            - **Nấm men:** Candida
            - **Nấm mốc:** Hiếm

            **2. Lây truyền:**
            - **Từ nấm da:** Nấm da lan sang móng
            - **Tiếp xúc:** Tiếp xúc với nấm
            - **Môi trường:** Hồ bơi, phòng tắm công cộng

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** > 60 tuổi (tăng nguy cơ)
            - **Nấm da:** Có nấm da
            - **Đái tháo đường:** Đái tháo đường
            - **Suy giảm miễn dịch:** HIV, thuốc ức chế miễn dịch
            - **Mang giày kín:** Giày bít, không thông thoáng
            - **Chấn thương móng:** Chấn thương móng
            - **Hút thuốc lá:** Tăng nguy cơ

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám móng

            **Xét nghiệm:**
            - **Soi tươi:** Lấy mẫu móng, soi dưới kính hiển vi
            - **Nuôi cấy:** Nuôi cấy nấm (2-4 tuần)
            - **PCR:** Phát hiện nấm nhanh

            **⚠️ Phân biệt:**
            - Vẩy nến móng
            - Chấn thương móng
            - Bệnh móng khác

            ## Điều trị:

            **1. Điều trị tại chỗ (Nấm móng nhẹ, < 50% móng):**
            - **Sơn móng:**
              - **Ciclopirox:** Sơn móng 1 lần/ngày, 6-12 tháng
              - **Amorolfine:** Sơn móng 1-2 lần/tuần, 6-12 tháng
            - **Cách dùng:** Sơn toàn bộ móng, cắt móng bị bệnh

            **2. Điều trị toàn thân (Nấm móng nặng, > 50% móng, nhiều móng):**
            - **Terbinafine:** 250mg/ngày, 6-12 tuần (móng tay), 12 tuần (móng chân)
            - **Itraconazole:** 200mg/ngày, 6-12 tuần, hoặc 400mg/ngày, 1 tuần/tháng, 3-4 tháng
            - **Fluconazole:** 150-300mg/tuần, 6-12 tháng

            **3. Cắt móng:**
            - Cắt móng bị bệnh
            - Giúp thuốc thấm tốt hơn

            **4. Điều trị kết hợp:**
            - Thuốc uống + Sơn móng
            - Tăng hiệu quả

            **⚠️ Lưu ý:**
            - Điều trị lâu dài (6-12 tháng)
            - Không ngừng thuốc sớm (tái phát)
            - Xét nghiệm chức năng gan (nếu dùng thuốc uống)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Thực phẩm chống nấm:** Tỏi, hành, gừng
            - **Probiotic:** Sữa chua (tăng lợi khuẩn)
            - **Vitamin C:** Trái cây, rau xanh (tăng miễn dịch)
            - **Kẽm:** Thịt, cá, đậu (tăng miễn dịch)

            **2. Thực phẩm nên tránh:**
            - **Đường:** Đường, bánh kẹo (nấm phát triển)
            - **Tinh bột tinh chế:** Bánh mì trắng, gạo trắng
            - **Rượu bia:** Làm suy giảm miễn dịch

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + sữa chua + trái cây
            - **Trưa:** Cơm + canh (có tỏi, gừng) + thịt/cá + rau xanh
            - **Chiều:** Cơm + canh (có tỏi, gừng) + thịt/cá + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - Tăng miễn dịch

            **2. Lưu ý:**
            - **Mang giày thông thoáng:** Khi tập thể dục
            - **Thay tất:** Tất khô, sạch
            - **Rửa chân:** Rửa chân sau khi tập

            ## 💊 QUẢN LÝ THUỐC:

            **1. Sơn móng:**
            - **Ciclopirox:** Sơn 1 lần/ngày
            - **Amorolfine:** Sơn 1-2 lần/tuần
            - **Cách dùng:** Sơn toàn bộ móng, cắt móng bị bệnh
            - **Thời gian:** 6-12 tháng

            **2. Thuốc uống:**
            - **Terbinafine:** 250mg/ngày, 6-12 tuần
            - **Itraconazole:** 200mg/ngày hoặc 400mg/ngày, 1 tuần/tháng
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Xét nghiệm gan:** Trước và trong điều trị

            **3. Lưu ý:**
            - Điều trị đủ thời gian (quan trọng!)
            - Không ngừng thuốc sớm
            - Xét nghiệm gan định kỳ
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Nấm móng nặng:**
            - Nhiều móng, > 50% móng
            - Không đáp ứng điều trị tại chỗ

            **2. Tác dụng phụ:**
            - Vàng da (tổn thương gan)
            - Phát ban, ngứa toàn thân

            **3. Biến chứng:**
            - Nhiễm trùng thứ phát
            - Mất móng

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh:**
            - **Rửa tay, chân:** Rửa tay, chân thường xuyên
            - **Lau khô:** Lau khô tay, chân, đặc biệt kẽ ngón
            - **Cắt móng:** Cắt móng ngắn, thẳng

            **2. Giày dép:**
            - **Thông thoáng:** Giày dép thông thoáng
            - **Thay tất:** Tất khô, sạch, thay thường xuyên
            - **Tránh:** Giày bít, ẩm ướt

            **3. Tránh lây lan:**
            - **Không dùng chung:** Kéo cắt móng, dũa móng
            - **Vệ sinh:** Vệ sinh dụng cụ cắt móng

            **4. Điều trị nấm da:**
            - Điều trị nấm da (nếu có)
            - Giảm nguy cơ lan sang móng

            **5. Môi trường:**
            - **Tránh:** Đi chân đất ở nơi công cộng
            - **Mang dép:** Mang dép riêng ở hồ bơi, phòng tắm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Vệ sinh sạch sẽ** (quan trọng nhất!)
            - Giày dép thông thoáng
            - Tránh lây lan

            **2. Khi bị nấm móng:**
            - Điều trị sớm, đủ thời gian
            - Kiên nhẫn (6-12 tháng)
            - Không ngừng thuốc sớm

            **3. Sống tích cực:**
            - Nấm móng có thể điều trị khỏi
            - Điều trị đúng → Khỏi
            - Phòng ngừa tốt → Không tái phát

            **4. Kiên nhẫn:**
            - Điều trị cần thời gian (6-12 tháng)
            - Không nản lòng
            - Tiếp tục điều trị sau khi móng mới mọc
            """,
            related_disease="onychomycosis",
            related_drugs=["Ciclopirox", "Amorolfine", "Terbinafine", "Itraconazole", "Fluconazole"],
            printable=True
        ),

]
