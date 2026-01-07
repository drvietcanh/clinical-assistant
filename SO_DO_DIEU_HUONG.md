# Sơ đồ điều hướng hệ thống Clinical Assistant

## 1. Cấu trúc điều hướng tổng quan

```mermaid
graph TB
    Start[🏠 Trang chủ<br/>app.py] --> Sidebar[Sidebar Navigation]
    Start --> Homepage[Homepage Dashboard]
    
    Sidebar --> Cat1[🏠 Trang chủ & Tìm kiếm]
    Sidebar --> Cat2[💊 Thuốc & Liều dùng]
    Sidebar --> Cat3[📊 Tính toán & Thang điểm]
    Sidebar --> Cat4[🫁 Hồi sức & Phác đồ]
    Sidebar --> Cat5[🩺 Chẩn đoán & Tham khảo]
    Sidebar --> Cat6[🧭 Hỗ trợ & Công cụ]
    
    Cat1 --> MainMenu[00_🏠_Main_Menu.py]
    
    Cat2 --> DrugDB[07_💊_Drug_Database.py]
    DrugDB --> Tab1[Tab: Database]
    DrugDB --> Tab2[Tab: Antibiotics]
    DrugDB --> Tab3[Tab: Pill Identifier]
    DrugDB --> Tab4[Tab: TDM]
    
    Cat3 --> Scores[01_📊_Scores.py]
    Scores --> TabS1[Tab: Clinical Scores]
    Scores --> TabS2[Tab: Labs & Calculators]
    
    Cat4 --> CriticalCare[09_🫁_Critical_Care.py]
    CriticalCare --> TabC1[Tab: Critical Care Tools]
    CriticalCare --> TabC2[Tab: Ventilator]
    CriticalCare --> TabC3[Tab: Protocols]
    CriticalCare --> TabC4[Tab: Guidelines]
    CriticalCare --> TabC5[Tab: Medical News]
    
    Cat5 --> Diagnosis[06_🩺_Diagnosis.py]
    Diagnosis --> TabD1[Tab: Differential Diagnosis]
    Diagnosis --> TabD2[Tab: Disease Encyclopedia]
    Diagnosis --> TabD3[Tab: ICD-10 Lookup]
    Diagnosis --> TabD4[Tab: In-Depth Articles]
    Diagnosis --> TabD5[Tab: Patient Education]
    
    Cat6 --> DecisionSupport[10_🧭_Decision_Support.py]
    DecisionSupport --> TabDS1[Tab: Decision Support]
    DecisionSupport --> TabDS2[Tab: AI Assistant]
    DecisionSupport --> TabDS3[Tab: Vaccination]
    DecisionSupport --> TabDS4[Tab: Settings]
    DecisionSupport --> TabDS5[Tab: Analytics]
    
    style Start fill:#2D7DF6,color:#fff
    style Cat1 fill:#f5f5f5
    style Cat2 fill:#e8f5e9
    style Cat3 fill:#e3f2fd
    style Cat4 fill:#fff3e0
    style Cat5 fill:#ffebee
    style Cat6 fill:#e1f5fe
```

## 2. Chi tiết nhóm Thuốc & Liều dùng

```mermaid
graph LR
    DrugDB[💊 Drug Database<br/>07_💊_Drug_Database.py] --> Func1[Tra cứu thuốc]
    DrugDB --> Func2[Tính liều eGFR/CrCl]
    DrugDB --> Func3[So sánh thuốc]
    DrugDB --> Func4[Lịch trình liều]
    DrugDB --> Func5[Tương thích IV]
    DrugDB --> Func6[Tương tác thuốc]
    
    DrugDB --> Tab1[Tab 1: Database<br/>Main functions]
    DrugDB --> Tab2[Tab 2: Antibiotics<br/>02_💊_Antibiotics.py]
    DrugDB --> Tab3[Tab 3: Pill Identifier<br/>21_💊_Pill_Identifier.py]
    DrugDB --> Tab4[Tab 4: TDM<br/>08_📊_TDM.py]
    
    style DrugDB fill:#e1f5fe
    style Tab1 fill:#bbdefb
    style Tab2 fill:#c8e6c9
    style Tab3 fill:#c8e6c9
    style Tab4 fill:#ce93d8
```

## 3. Chi tiết nhóm Hồi sức & Phác đồ

```mermaid
graph TB
    CriticalCare[🫁 Critical Care<br/>09_🫁_Critical_Care.py] --> Tab1[Tab 1: Critical Care Tools]
    CriticalCare --> Tab2[Tab 2: Ventilator<br/>03_🫁_Ventilator.py]
    CriticalCare --> Tab3[Tab 3: Protocols<br/>04_📋_Protocols.py]
    CriticalCare --> Tab4[Tab 4: Guidelines<br/>15_📋_Guidelines_Tracker.py]
    CriticalCare --> Tab5[Tab 5: Medical News<br/>10_📰_Medical_News.py]
    
    Tab1 --> Tool1[Dashboard]
    Tab1 --> Tool2[Scoring Systems]
    Tab1 --> Tool3[Fluid Therapy]
    Tab1 --> Tool4[Vasopressors]
    Tab1 --> Tool5[Transfusion]
    Tab1 --> Tool6[Sedation]
    Tab1 --> Tool7[RRT Calculator]
    
    style CriticalCare fill:#fff3e0
    style Tab1 fill:#ffe0b2
    style Tab2 fill:#ffe0b2
    style Tab3 fill:#ffe0b2
    style Tab4 fill:#ffe0b2
    style Tab5 fill:#ffe0b2
```

## 4. Chi tiết nhóm Chẩn đoán & Tham khảo

```mermaid
graph TB
    Diagnosis[🩺 Diagnosis<br/>06_🩺_Diagnosis.py] --> Tab1[Tab 1: Differential Diagnosis<br/>Main DDx Generator]
    Diagnosis --> Tab2[Tab 2: Disease Encyclopedia<br/>16_📖_Disease_Encyclopedia.py]
    Diagnosis --> Tab3[Tab 3: ICD-10 Lookup<br/>13_🏷️_ICD10_Lookup.py]
    Diagnosis --> Tab4[Tab 4: In-Depth Articles<br/>12_📚_In_Depth_Articles.py]
    Diagnosis --> Tab5[Tab 5: Patient Education<br/>19_👥_Patient_Education.py]
    
    Tab2 --> DiseaseFunc1[Search Diseases]
    Tab2 --> DiseaseFunc2[By Category]
    Tab2 --> DiseaseFunc3[By Symptom]
    
    Tab3 --> ICDFunc1[Search by Name]
    Tab3 --> ICDFunc2[Search by Code]
    Tab3 --> ICDFunc3[By Specialty]
    
    style Diagnosis fill:#ffebee
    style Tab1 fill:#ffcdd2
    style Tab2 fill:#ffcdd2
    style Tab3 fill:#ffcdd2
    style Tab4 fill:#ffcdd2
    style Tab5 fill:#ffcdd2
```

## 5. Chi tiết nhóm Hỗ trợ & Công cụ

```mermaid
graph TB
    DecisionSupport[🧭 Decision Support<br/>10_🧭_Decision_Support.py] --> Tab1[Tab 1: Decision Support<br/>Flowcharts, Pregnancy, Pediatric]
    DecisionSupport --> Tab2[Tab 2: AI Assistant<br/>09_🤖_AI_Assistant.py]
    DecisionSupport --> Tab3[Tab 3: Vaccination<br/>11_💉_Vaccination.py]
    DecisionSupport --> Tab4[Tab 4: Settings<br/>23_⚙️_Settings.py]
    DecisionSupport --> Tab5[Tab 5: Analytics<br/>24_📈_Analytics.py]
    
    Tab1 --> Flow1[Flowcharts]
    Tab1 --> Flow2[Pregnancy/Lactation]
    Tab1 --> Flow3[Pediatric Dosing]
    
    Flow1 --> FlowAlgo1[Wells PE]
    Flow1 --> FlowAlgo2[CHA2DS2-VASc]
    Flow1 --> FlowAlgo3[Sepsis-3]
    Flow1 --> FlowAlgo4[CURB-65]
    Flow1 --> FlowAlgo5[+ 15 more]
    
    style DecisionSupport fill:#e1f5fe
    style Tab1 fill:#b3e5fc
    style Tab2 fill:#b3e5fc
    style Tab3 fill:#b3e5fc
    style Tab4 fill:#b3e5fc
    style Tab5 fill:#b3e5fc
```

## 6. Luồng điều hướng từ Trang chủ

```mermaid
sequenceDiagram
    participant User
    participant Homepage
    participant Sidebar
    participant MainPage
    participant Tabs
    participant SubModule
    
    User->>Homepage: Truy cập app.py
    Homepage->>Homepage: Hiển thị Dashboard
    Homepage->>Sidebar: Render Navigation
    User->>Sidebar: Click Category
    Sidebar->>MainPage: Switch to Main Page
    MainPage->>Tabs: Render Tabs
    User->>Tabs: Click Tab
    Tabs->>SubModule: Render/Redirect to Sub-module
    SubModule->>User: Hiển thị nội dung
```

## 7. Cấu trúc dữ liệu Navigation

```mermaid
classDiagram
    class NavigationCategory {
        +str id
        +str title
        +str icon
        +str description
        +List[str] module_ids
        +str color
        +str border
        +bool default_expanded
    }
    
    class NavigationItem {
        +str id
        +str title
        +str icon
        +str page_path
        +bool is_sub_item
        +str parent_id
    }
    
    class ModuleInfo {
        +str id
        +str title
        +str icon
        +str page_path
        +str description
        +str color
        +str border
    }
    
    NavigationCategory "1" --> "*" NavigationItem : contains
    NavigationItem "1" --> "0..1" NavigationItem : parent
    NavigationItem "1" --> "1" ModuleInfo : references
```

## 8. Tổng hợp số liệu

### Trang chính: 6 trang
- 🏠 Trang chủ
- 📊 Calculators & Thang điểm
- 💊 Cơ sở dữ liệu thuốc
- 🫁 Hồi sức
- 🩺 Chẩn đoán phân biệt
- 🧭 Hỗ trợ quyết định

### Sub-modules: 18 trang
- Tích hợp qua tabs trong các trang chính

### Navigation Categories: 6 nhóm
- Mỗi nhóm có 1-5 sub-modules

### Tabs Integration:
- Drug Database: 4 tabs ✅
- Critical Care: 5 tabs ✅
- Diagnosis: 5 tabs ⚠️ (chưa tích hợp hoàn toàn)
- Decision Support: 5 tabs ✅
- Scores: 2 tabs ✅

---

**Ghi chú:** 
- ✅ = Đã tích hợp hoàn toàn
- ⚠️ = Chưa tích hợp hoàn toàn (chỉ có redirect buttons)
