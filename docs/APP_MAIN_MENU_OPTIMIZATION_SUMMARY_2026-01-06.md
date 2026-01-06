## Tóm tắt tối ưu App & Main Menu (2026-01-06)

### 1. Mục tiêu
- **Tối ưu hiệu năng** khởi động app và tải trang Main Menu.
- **Cải thiện UX**: tìm kiếm mượt hơn, giảm re-render, bố cục dễ bảo trì.

### 2. Thay đổi chính ở Main Menu (`pages/00_🏠_Main_Menu.py`)
- **Tách CSS ra component riêng**
  - Tạo `components/main_menu_styles.py` với hàm `inject_main_menu_styles()`.
  - Thay thế toàn bộ CSS inline bằng một lệnh gọi `inject_main_menu_styles()`.

- **Caching & snapshot thống kê**
  - Thêm `utils/cache_helpers.py` với:
    - `compute_usage_stats_snapshot()` (TTL 60s) tạo snapshot thống kê từ `session_state.usage_stats`.
    - `get_popular_calculators()` (TTL 600s) trả danh sách calculators phổ biến dựa trên danh sách mặc định.
  - Khu vực thống kê sử dụng dùng snapshot đã cache để tránh tính lại và giảm logic trong trang.

- **Tối ưu search**
  - Trong `components/global_search.py`, thêm:
    - `@st.cache_data(ttl=300, max_entries=200)` cho `search_calculators()`.
  - Ở Main Menu:
    - Chỉ gọi lại search khi query **thay đổi** và có **≥ 2 ký tự**.
    - Lưu kết quả vào `st.session_state.main_menu_search_results` để tái sử dụng khi gõ tiếp.

- **Favorites / Recently used dạng lazy**
  - Thay layout 2 cột cố định bằng một `st.radio`:
    - `"⭐ Yêu thích"` → chỉ render favorites.
    - `"🕐 Gần đây"` → chỉ render recently used.
  - Giảm số component render đồng thời, thân thiện hơn trên màn hình nhỏ.

- **Quick access – popular calculators**
  - Danh sách popular calculators được lấy từ `get_popular_calculators(default_ids)` (đã cache).
  - Giữ layout 4 cột, nhưng dùng dữ liệu đã qua cache thay vì list cứng tính tại chỗ.

### 3. Thay đổi chính ở App chính (`app.py`)
- **Cache danh sách modules**
  - Import: `from utils.cache_helpers import get_module_list_for_navigation_cached`.
  - Tab 1 (“Tất cả modules”) sử dụng:
    - `modules = get_module_list_for_navigation_cached()`
  - Giảm chi phí gọi `get_module_list_for_navigation()` mỗi lần rerun.

- **Lazy load mobile navigation**
  - Tạo hàm `_init_mobile_features()`:
    - Import cục bộ `components.mobile_navigation` và `components.mobile_inputs`.
    - Gọi `_init_mobile_features()` sau khi config trang.
  - Nếu thiếu module mobile → bỏ qua (không gây lỗi).

- **Lazy load analytics & stats (Tab 3)**
  - Di chuyển import `components.analytics` và `components.stats` vào bên trong `with tab3:`.
  - Nếu `components.analytics` không có:
    - Thử import riêng `components.stats`.
    - Nếu vẫn không có → hiển thị thông báo nhẹ `"Stats module tạm thời không khả dụng."`.

- **Tối ưu render module cards**
  - Trong tab 1:
    - Mỗi card module được bọc trong `st.container()` riêng cho nút “Mở module”.
    - Giúp cô lập re-render của từng nút, tránh ảnh hưởng cả lưới card khi một card thay đổi.

- **Tabs 2 (Favorites)**
  - Nội dung favorites + recently used bọc trong một `st.container()` bên trong `with tab2:` để giới hạn phạm vi re-render.

### 4. Ảnh hưởng & kỳ vọng hiệu năng
- **Khởi động app nhanh hơn** nhờ:
  - Cache danh sách modules.
  - Import một số component (analytics, stats, mobile) theo nhu cầu.
- **Main Menu phản hồi tốt hơn**:
  - Search không gọi lại liên tục từng phím, có caching.
  - Stats, popular calculators dùng snapshot/cached helpers.
- **Dễ bảo trì UI hơn**:
  - CSS Main Menu tập trung trong `components/main_menu_styles.py`.
  - Logic caching & thống kê tách ra `utils/cache_helpers.py`.

### 5. Files liên quan
- `pages/00_🏠_Main_Menu.py` – logic hiển thị Main Menu (search, stats, favorites, quick access).
- `components/main_menu_styles.py` – CSS cho Main Menu.
- `components/global_search.py` – global search, thêm caching.
- `utils/cache_helpers.py` – helper cho caching (stats snapshot, popular calculators, module list).
- `app.py` – tối ưu app chính: cache module list, lazy load mobile features, analytics & stats, tối ưu render modules.

