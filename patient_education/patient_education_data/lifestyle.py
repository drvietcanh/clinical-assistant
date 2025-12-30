"""
Patient Education Topics - Lifestyle
"""

from patient_education.models import PatientEducationTopic


LIFESTYLE_TOPICS = [
    PatientEducationTopic(
            id="diabetes_diet",
            title="Diet for Diabetes",
            title_vn="Chế độ ăn cho người Đái tháo đường",
            category="Lifestyle",
            content="""
        # Chế độ ăn cho người Đái tháo đường

        ## Nguyên tắc cơ bản:

        **1. Ăn đúng giờ, đều đặn:**
        - **Bữa sáng:** 6-8 giờ sáng (quan trọng nhất!)
        - **Bữa trưa:** 11-12 giờ trưa
        - **Bữa tối:** 6-7 giờ tối (trước 8 giờ tối)
        - **Bữa phụ:** 9-10 giờ sáng, 3-4 giờ chiều, 9 giờ tối (nếu cần)
        - Không bỏ bữa, đặc biệt bữa sáng
        - Cách nhau 3-4 giờ giữa các bữa

        **2. Kiểm soát khẩu phần (Portion Control):**
        - **Phương pháp đĩa:** 1/2 đĩa rau, 1/4 đĩa protein, 1/4 đĩa tinh bột
        - **Phương pháp bàn tay:**
          - Tinh bột: 1 nắm tay (gạo, bánh mì)
          - Protein: 1 lòng bàn tay (thịt, cá)
          - Rau xanh: 2 bàn tay
          - Chất béo: 1 ngón tay cái (dầu ăn)
        - **Tổng calo/ngày:** 1500-2000 kcal (tùy cân nặng, hoạt động)

        **3. Chọn thực phẩm có chỉ số đường huyết thấp (GI < 55):**
        - Giúp đường huyết tăng từ từ, ổn định
        - Tránh đường huyết tăng đột ngột

        ## 📋 THỰC PHẨM NÊN ĂN (Chi tiết):

        **1. Rau xanh (Ăn tự do, không giới hạn):**
        - Rau cải, rau muống, rau ngót, rau dền
        - Bông cải xanh, bông cải trắng
        - Cà rốt, cà chua, dưa chuột
        - Rau diếp, xà lách, rau thơm
        - Măng tây, đậu bắp
        - **Cách chế biến:** Luộc, hấp, xào ít dầu, salad

        **2. Trái cây (Chọn loại ít ngọt, ăn có giới hạn):**
        - **Nên ăn:** Táo, lê, cam, quýt, bưởi, ổi, thanh long
        - **Lượng:** 1-2 phần/ngày (1 phần = 1 quả táo nhỏ, 1/2 quả cam)
        - **Thời gian:** Ăn sau bữa chính 1-2 giờ, hoặc bữa phụ
        - **Tránh:** Nước ép trái cây (mất chất xơ, đường hấp thu nhanh)

        **3. Tinh bột (Chọn loại nguyên hạt, GI thấp):**
        - **Gạo lứt:** Thay thế gạo trắng (GI thấp hơn)
        - **Yến mạch:** Bữa sáng (GI thấp, giàu chất xơ)
        - **Khoai lang:** Luộc, hấp (không chiên)
        - **Bánh mì đen, bánh mì nguyên cám**
        - **Lượng:** 1-2 chén cơm/bữa (tùy mức độ hoạt động)

        **4. Protein nạc:**
        - **Cá:** Cá hồi, cá thu, cá trích (giàu omega-3)
        - **Thịt:** Thịt gà (bỏ da), thịt bò nạc, thịt heo nạc
        - **Đậu:** Đậu phụ, đậu nành, đậu đen, đậu xanh
        - **Trứng:** 3-4 quả/tuần
        - **Lượng:** 100-150g/bữa

        **5. Chất béo tốt:**
        - **Dầu:** Dầu ô liu, dầu hạt cải, dầu đậu nành
        - **Quả bơ:** 1/4-1/2 quả/ngày
        - **Các loại hạt:** Hạnh nhân, óc chó, hạt điều (1 nắm nhỏ/ngày)
        - **Lượng:** 2-3 thìa cà phê dầu/ngày

        **6. Sữa và sản phẩm sữa:**
        - Sữa tách béo, sữa không đường
        - Sữa chua không đường
        - Phô mai ít béo
        - **Lượng:** 1-2 ly/ngày

        ## ⚠️ THỰC PHẨM CẦN TRÁNH/HẠN CHẾ:

        **1. Đường và đồ ngọt (TRÁNH HOÀN TOÀN):**
        - Đường trắng, đường nâu, mật ong, siro
        - Bánh kẹo, kẹo, chocolate
        - Mứt, mứt dừa
        - Kem, chè ngọt

        **2. Nước ngọt và đồ uống có đường:**
        - Nước ngọt có ga, nước tăng lực
        - Nước ép trái cây đóng chai
        - Trà sữa, cà phê có đường
        - Rượu bia (hạn chế tối đa)

        **3. Tinh bột tinh chế (HẠN CHẾ):**
        - Gạo trắng (ăn ít, thay bằng gạo lứt)
        - Bánh mì trắng
        - Bún, phở, miến (ăn ít)
        - Khoai tây chiên

        **4. Thực phẩm chế biến sẵn:**
        - Đồ hộp, thức ăn nhanh
        - Xúc xích, thịt nguội
        - Đồ chiên rán nhiều dầu mỡ
        - Mì gói, snack

        **5. Trái cây quá ngọt (HẠN CHẾ):**
        - Sầu riêng, mít, nhãn, vải
        - Xoài chín, chuối chín quá
        - Nho, dưa hấu (ăn ít)

        **6. Đồ uống có cồn:**
        - Rượu bia làm tăng đường huyết, tăng nguy cơ hạ đường huyết
        - Nếu uống: Tối đa 1-2 ly rượu vang/ngày, với thức ăn

        ## 🍽️ THỰC ĐƠN MẪU (1 ngày):

        **Bữa sáng (7h):**
        - 1 bát cháo yến mạch + 1 quả trứng luộc
        - Hoặc: 1 lát bánh mì đen + 1 quả trứng + rau xanh
        - 1 ly sữa không đường

        **Bữa phụ (10h):**
        - 1 quả táo nhỏ hoặc 1/2 quả cam

        **Bữa trưa (12h):**
        - 1 chén cơm gạo lứt
        - 100g cá kho hoặc thịt gà luộc
        - Rau xanh luộc/xào (nhiều)
        - Canh rau

        **Bữa phụ (15h):**
        - 1 hộp sữa chua không đường
        - Hoặc: 1 quả ổi

        **Bữa tối (18h):**
        - 1 chén cơm gạo lứt (ít hơn bữa trưa)
        - 100g đậu phụ hoặc cá
        - Rau xanh
        - Canh

        **Bữa phụ (21h - nếu cần):**
        - 1 ly sữa không đường ấm

        ## 💡 LỜI KHUYÊN THỰC TẾ:

        **1. Khi đi ăn ngoài:**
        - Chọn món luộc, hấp, nướng
        - Tránh món chiên, xào nhiều dầu
        - Yêu cầu không thêm đường, nước mắm ngọt
        - Ăn nhiều rau xanh
        - Chia nhỏ phần ăn

        **2. Khi nấu ăn tại nhà:**
        - Dùng ít dầu mỡ (2-3 thìa cà phê/bữa)
        - Nêm nhạt, ít muối
        - Không thêm đường vào món ăn
        - Chế biến đơn giản: luộc, hấp, nướng

        **3. Đọc nhãn thực phẩm:**
        - Kiểm tra lượng đường (sugar) - nên < 5g/100g
        - Kiểm tra lượng carb - tính vào tổng carb/ngày
        - Tránh thực phẩm có nhiều đường ẩn

        **4. Theo dõi đường huyết:**
        - Đo trước bữa ăn: 80-130 mg/dL
        - Đo sau bữa ăn 2 giờ: < 180 mg/dL
        - Ghi nhật ký ăn uống và đường huyết
        - Điều chỉnh khẩu phần nếu đường huyết cao

        **5. Dấu hiệu cần điều chỉnh:**
        - Đường huyết tăng cao sau ăn → Giảm tinh bột, tăng rau
        - Đường huyết hạ → Ăn thêm bữa phụ
        - Tăng cân → Giảm khẩu phần, tăng vận động

        **6. Khi có triệu chứng hạ đường huyết:**
        - Run, đổ mồ hôi, đói, chóng mặt
        - Ăn/uống ngay: 15g đường (3 viên kẹo, 1/2 ly nước ngọt)
        - Đo lại sau 15 phút
        - Ăn bữa phụ sau đó

        ## ⚠️ LƯU Ý QUAN TRỌNG:

        - **Không bỏ bữa:** Dễ gây hạ đường huyết hoặc ăn quá nhiều bữa sau
        - **Ăn chậm, nhai kỹ:** Giúp no lâu, kiểm soát đường huyết tốt hơn
        - **Uống đủ nước:** 1.5-2 lít/ngày (nước lọc, trà không đường)
        - **Kết hợp với tập thể dục:** Giúp kiểm soát đường huyết tốt hơn
        - **Tham khảo bác sĩ dinh dưỡng:** Để có thực đơn phù hợp với từng người
        - **Không tự ý thay đổi chế độ ăn đột ngột:** Thay đổi từ từ, theo dõi đường huyết
            """,
            related_disease="diabetes_type2",
            printable=True
    ),
    
    # === EXERCISE ===
    PatientEducationTopic(
        id="exercise_benefits",
        title="Benefits of Regular Exercise",
        title_vn="Lợi ích của Tập thể dục đều đặn",
        category="Lifestyle",
        content="""
# Lợi ích của Tập thể dục đều đặn

## Tại sao tập thể dục quan trọng?

Tập thể dục đều đặn giúp cải thiện sức khỏe toàn diện và phòng ngừa bệnh tật.

## Lợi ích:

**1. Tim mạch:**
- Tăng sức khỏe tim
- Giảm huyết áp
- Giảm cholesterol
- Giảm nguy cơ đột quỵ, nhồi máu cơ tim

**2. Kiểm soát cân nặng:**
- Đốt cháy calo
- Giảm cân, duy trì cân nặng
- Tăng cơ, giảm mỡ

**3. Xương khớp:**
- Tăng sức mạnh cơ
- Tăng độ linh hoạt
- Giảm đau khớp
- Phòng loãng xương

**4. Tinh thần:**
- Giảm stress, lo âu
- Cải thiện tâm trạng
- Tăng năng lượng
- Cải thiện giấc ngủ

**5. Bệnh mạn tính:**
- Giảm nguy cơ đái tháo đường type 2
- Kiểm soát đái tháo đường
- Giảm nguy cơ một số ung thư

## Loại bài tập:

**1. Aerobic (Tim mạch):**
- Đi bộ, chạy bộ
- Bơi lội
- Đạp xe
- Nhảy dây
- **Mục tiêu:** 150 phút/tuần (cường độ vừa)

**2. Sức mạnh:**
- Nâng tạ
- Tập với dây kháng lực
- **Mục tiêu:** 2 lần/tuần

**3. Kéo giãn:**
- Yoga
- Pilates
- Kéo giãn cơ
- **Mục tiêu:** Hàng ngày

## Bắt đầu như thế nào?

**1. Bắt đầu từ từ:**
- 10-15 phút/ngày
- Tăng dần thời gian
- Không vội vàng

**2. Chọn hoạt động yêu thích:**
- Dễ duy trì hơn
- Vui vẻ hơn

**3. Tìm bạn tập:**
- Động lực hơn
- An toàn hơn

**4. Lắng nghe cơ thể:**
- Nghỉ khi mệt
- Dừng nếu đau
- Uống đủ nước

## Lưu ý:
- Khởi động trước khi tập
- Giãn cơ sau khi tập
- Uống đủ nước
- Mặc quần áo phù hợp
- Không tập khi ốm

## Khi nào cần hỏi bác sĩ:
- Bệnh mạn tính
- Đau ngực khi tập
- Chóng mặt, ngất
- Khó thở nặng
- Trên 40 tuổi, ít vận động

## Lời khuyên:
- Tập đều đặn (quan trọng hơn cường độ)
- Bắt đầu từ từ
- Chọn hoạt động yêu thích
- Đặt mục tiêu thực tế
- Theo dõi tiến độ
- Vui vẻ!
        """,
        printable=True
    ),
    
    # === NUTRITION ===
    PatientEducationTopic(
        id="healthy_nutrition",
        title="Healthy Eating Guidelines",
        title_vn="Hướng dẫn Ăn uống lành mạnh",
        category="Lifestyle",
        content="""
# Hướng dẫn Ăn uống lành mạnh

## Nguyên tắc cơ bản:

**1. Ăn đa dạng:**
- Nhiều loại thực phẩm
- Đủ chất dinh dưỡng
- Cân bằng

**2. Ăn đúng giờ:**
- 3 bữa chính
- 1-2 bữa phụ (nếu cần)
- Không bỏ bữa

**3. Kiểm soát khẩu phần:**
- Ăn vừa đủ
- Không quá no
- Đọc nhãn thực phẩm

## Thực phẩm nên ăn:

**1. Rau xanh và trái cây:**
- Nhiều vitamin, chất xơ
- Ít calo
- **Mục tiêu:** 5 phần/ngày

**2. Ngũ cốc nguyên hạt:**
- Gạo lứt, bánh mì đen
- Yến mạch, quinoa
- Nhiều chất xơ

**3. Protein nạc:**
- Thịt gà (bỏ da)
- Cá (đặc biệt cá béo)
- Đậu, đậu phụ
- Trứng

**4. Sữa ít béo:**
- Sữa tách béo
- Sữa chua
- Phô mai ít béo

**5. Chất béo tốt:**
- Dầu ô liu
- Quả bơ
- Các loại hạt
- Cá béo

## Thực phẩm nên hạn chế:

**1. Đường:**
- Bánh kẹo
- Nước ngọt
- Đồ ngọt
- **Mục tiêu:** < 50g/ngày

**2. Muối:**
- Đồ mặn
- Đồ hộp
- Thức ăn nhanh
- **Mục tiêu:** < 5g/ngày

**3. Chất béo xấu:**
- Đồ chiên rán
- Thịt mỡ
- Bơ, mỡ động vật

**4. Thực phẩm chế biến:**
- Đồ hộp
- Thức ăn nhanh
- Đồ đóng gói

## Uống đủ nước:

- **Nước:** Tốt nhất
- **Mục tiêu:** 1.5-2 lít/ngày
- Tránh nước ngọt
- Hạn chế cà phê, trà

## Lời khuyên:

**1. Lập kế hoạch:**
- Lên thực đơn
- Mua sắm thông minh
- Chuẩn bị trước

**2. Nấu ăn tại nhà:**
- Kiểm soát được nguyên liệu
- Ít muối, đường, dầu mỡ

**3. Ăn chậm:**
- Nhai kỹ
- Thưởng thức
- Cảm nhận no

**4. Đọc nhãn:**
- Kiểm tra calo
- Kiểm tra muối, đường
- Kiểm tra chất béo

**5. Không bỏ bữa:**
- Ăn đều đặn
- Tránh ăn quá nhiều sau đó

## Khi nào cần tư vấn dinh dưỡng:

- Bệnh mạn tính (đái tháo đường, tăng huyết áp)
- Cần giảm/tăng cân
- Dị ứng thực phẩm
- Mang thai, cho con bú
- Trẻ em, người già

## Lời khuyên:

- Ăn đa dạng, cân bằng
- Kiểm soát khẩu phần
- Uống đủ nước
- Hạn chế đường, muối
- Ăn nhiều rau xanh, trái cây
- Nấu ăn tại nhà
- Thưởng thức bữa ăn
        """,
        printable=True
    ),
    
    # === SMOKING CESSATION ===
    PatientEducationTopic(
        id="smoking_cessation",
        title="Quitting Smoking",
        title_vn="Bỏ Thuốc lá",
        category="Lifestyle",
        content="""
# Bỏ Thuốc lá

## Tại sao nên bỏ thuốc lá?

Bỏ thuốc lá là điều tốt nhất bạn có thể làm cho sức khỏe của mình!

## Lợi ích ngay lập tức:

**Sau 20 phút:**
- Nhịp tim, huyết áp giảm

**Sau 12 giờ:**
- Nồng độ CO trong máu về bình thường

**Sau 2 tuần - 3 tháng:**
- Tuần hoàn cải thiện
- Chức năng phổi tăng
- Giảm nguy cơ đau tim

**Sau 1 năm:**
- Nguy cơ bệnh mạch vành giảm 50%

**Sau 5 năm:**
- Nguy cơ đột quỵ giảm về mức người không hút

**Sau 10 năm:**
- Nguy cơ ung thư phổi giảm 50%
- Nguy cơ ung thư miệng, họng, thực quản giảm

## Cách bỏ thuốc:

**1. Chuẩn bị:**
- Chọn ngày bỏ thuốc
- Bỏ hết thuốc, gạt tàn
- Nói với người thân
- Tìm lý do bỏ

**2. Thay đổi thói quen:**
- Tránh tình huống thường hút
- Tìm hoạt động thay thế
- Uống nước, nhai kẹo cao su
- Tập thể dục

**3. Quản lý cơn thèm:**
- Cơn thèm chỉ kéo dài 3-5 phút
- Hít thở sâu
- Uống nước
- Đi bộ
- Gọi điện cho người thân

**4. Hỗ trợ:**
- **Thuốc:** Nicotine thay thế, Bupropion, Varenicline
- **Tư vấn:** Nói chuyện với bác sĩ
- **Nhóm hỗ trợ:** Tham gia nhóm bỏ thuốc
- **Ứng dụng:** App hỗ trợ bỏ thuốc

## Triệu chứng cai nghiện:

- Thèm thuốc
- Cáu gắt
- Lo âu
- Khó tập trung
- Mệt mỏi
- Mất ngủ
- Tăng cân (tạm thời)

**Lưu ý:** Triệu chứng sẽ giảm sau vài tuần

## Phòng ngừa tái nghiện:

- Tránh tình huống cũ
- Tránh rượu bia (thường đi kèm hút thuốc)
- Tập thể dục
- Quản lý stress
- Nhắc nhở bản thân lý do bỏ

## Nếu tái nghiện:

- **Đừng bỏ cuộc!**
- Hầu hết người bỏ thuốc thử nhiều lần
- Học từ lần trước
- Thử lại với cách khác
- Tìm hỗ trợ

## Lời khuyên:

- Quyết tâm bỏ
- Tìm hỗ trợ (bác sĩ, người thân)
- Dùng thuốc hỗ trợ nếu cần
- Thay đổi thói quen
- Tập thể dục
- Quản lý stress
- Đừng bỏ cuộc nếu tái nghiện
- Nhớ lợi ích sức khỏe

## ⚠️ QUAN TRỌNG:

Bỏ thuốc lá là quyết định quan trọng nhất cho sức khỏe của bạn. Hãy bắt đầu ngay hôm nay!
        """,
        printable=True
    ),
    
    # === STRESS MANAGEMENT ===
    PatientEducationTopic(
        id="stress_management",
        title="Managing Stress",
        title_vn="Quản lý Stress",
        category="Lifestyle",
        content="""
# Quản lý Stress

## Stress là gì?

Stress là phản ứng của cơ thể với áp lực, thay đổi, hoặc thách thức.

## Tác động của stress:

**Stress ngắn hạn (tốt):**
- Giúp tập trung
- Tăng hiệu suất
- Phản ứng nhanh

**Stress dài hạn (xấu):**
- Lo âu, trầm cảm
- Mất ngủ
- Đau đầu
- Tăng huyết áp
- Suy giảm miễn dịch
- Bệnh tim mạch

## Dấu hiệu stress:

**Thể chất:**
- Mệt mỏi
- Đau đầu
- Đau cơ
- Rối loạn tiêu hóa
- Mất ngủ
- Thay đổi ăn uống

**Tinh thần:**
- Lo âu
- Cáu gắt
- Khó tập trung
- Quên
- Thiếu động lực

## Cách quản lý stress:

**1. Tập thể dục:**
- Giảm stress hiệu quả
- Tăng endorphin (hormone hạnh phúc)
- 30 phút/ngày

**2. Thư giãn:**
- Hít thở sâu
- Thiền
- Yoga
- Nghe nhạc
- Đọc sách

**3. Ngủ đủ:**
- 7-9 giờ/đêm
- Giờ ngủ đều đặn
- Phòng ngủ yên tĩnh, tối

**4. Ăn uống lành mạnh:**
- Ăn đều đặn
- Hạn chế cà phê, rượu
- Uống đủ nước

**5. Quản lý thời gian:**
- Lập kế hoạch
- Ưu tiên công việc
- Nói "không" khi cần
- Nghỉ giải lao

**6. Hỗ trợ xã hội:**
- Nói chuyện với người thân
- Tham gia nhóm
- Tìm bạn bè

**7. Sở thích:**
- Làm điều mình thích
- Giải trí
- Sáng tạo

## Kỹ thuật thư giãn:

**1. Hít thở sâu:**
- Hít vào 4 giây
- Giữ 4 giây
- Thở ra 4 giây
- Lặp lại 5-10 lần

**2. Thư giãn cơ:**
- Căng và thả từng nhóm cơ
- Bắt đầu từ chân
- Lên đến đầu

**3. Thiền:**
- Ngồi yên
- Tập trung hơi thở
- 10-20 phút/ngày

## Khi nào cần giúp đỡ:

- Stress ảnh hưởng cuộc sống hàng ngày
- Lo âu, trầm cảm
- Mất ngủ kéo dài
- Tự làm hại bản thân
- Ý nghĩ tự tử

## Lời khuyên:

- Nhận biết dấu hiệu stress
- Tập thể dục đều đặn
- Ngủ đủ giấc
- Thư giãn mỗi ngày
- Nói chuyện với người thân
- Quản lý thời gian
- Tìm sở thích
- Tìm giúp đỡ khi cần
- Chăm sóc bản thân
        """,
        printable=True
    ),

]
