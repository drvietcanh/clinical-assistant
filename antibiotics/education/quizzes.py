"""
Antibiotics Quizzes
Educational quizzes to test knowledge about antibiotics
"""

import streamlit as st
from typing import List, Dict, Optional
import random

# Quiz questions database
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "category": "Dosing",
        "question": "Bệnh nhân suy thận (CrCl = 25 mL/min) cần điều chỉnh liều cho kháng sinh nào sau đây?",
        "options": [
            "Vancomycin - cần giảm liều",
            "Ceftriaxone - không cần điều chỉnh",
            "Meropenem - cần giảm liều",
            "Tất cả đều đúng"
        ],
        "correct": 3,
        "explanation": "Vancomycin và Meropenem đều thải chủ yếu qua thận nên cần giảm liều khi CrCl < 30. Ceftriaxone thải qua gan nên không cần điều chỉnh."
    },
    {
        "id": 2,
        "category": "Spectrum",
        "question": "Kháng sinh nào sau đây có phổ tác dụng tốt nhất với MRSA?",
        "options": [
            "Ceftriaxone",
            "Vancomycin",
            "Ciprofloxacin",
            "Azithromycin"
        ],
        "correct": 1,
        "explanation": "Vancomycin là lựa chọn đầu tay cho MRSA. Ceftriaxone và Azithromycin không hiệu quả với MRSA. Ciprofloxacin có thể có kháng thuốc."
    },
    {
        "id": 3,
        "category": "PK/PD",
        "question": "Chỉ số PK/PD quan trọng nhất cho beta-lactam (như Ceftriaxone) là gì?",
        "options": [
            "AUC/MIC",
            "Time above MIC",
            "Cmax/MIC",
            "Trough level"
        ],
        "correct": 1,
        "explanation": "Beta-lactam là time-dependent antibiotics. Time above MIC > 40-50% của khoảng cách liều là quan trọng nhất."
    },
    {
        "id": 4,
        "category": "Allergy",
        "question": "Bệnh nhân dị ứng Penicillin có thể dùng Cephalosporin không?",
        "options": [
            "Không, nguy cơ phản ứng chéo cao",
            "Có, nguy cơ phản ứng chéo rất thấp (1-2%)",
            "Chỉ dùng được Cephalosporin thế hệ 3 trở lên",
            "Cần test da trước"
        ],
        "correct": 1,
        "explanation": "Nguy cơ phản ứng chéo giữa Penicillin và Cephalosporin là thấp (1-2%), nhưng vẫn nên thận trọng, đặc biệt với phản ứng nặng."
    },
    {
        "id": 5,
        "category": "Stewardship",
        "question": "Khi nào nên de-escalate kháng sinh?",
        "options": [
            "Ngay sau khi bắt đầu điều trị",
            "Sau 48-72 giờ khi có kết quả cấy và bệnh nhân cải thiện",
            "Sau 7 ngày điều trị",
            "Không bao giờ"
        ],
        "correct": 1,
        "explanation": "De-escalation nên thực hiện sau 48-72 giờ khi có kết quả cấy máu/đờm và bệnh nhân đã cải thiện lâm sàng."
    },
    {
        "id": 6,
        "category": "Resistance",
        "question": "Tỷ lệ kháng Ceftriaxone của E. coli tại Việt Nam là bao nhiêu?",
        "options": [
            "5-10%",
            "15-25%",
            "35-45%",
            ">50%"
        ],
        "correct": 2,
        "explanation": "Tỷ lệ kháng Ceftriaxone của E. coli tại Việt Nam là 35-45% do ESBL phổ biến. Cần cân nhắc kháng sinh khác hoặc test độ nhạy."
    },
    {
        "id": 7,
        "category": "Pregnancy",
        "question": "Kháng sinh nào an toàn nhất trong thai kỳ?",
        "options": [
            "Penicillin (Category B)",
            "Tetracycline (Category D)",
            "Ciprofloxacin (Category C)",
            "Vancomycin (Category C)"
        ],
        "correct": 0,
        "explanation": "Penicillin và các beta-lactam khác (Category B) là an toàn nhất trong thai kỳ. Tetracycline (D) và Ciprofloxacin (C) cần tránh."
    },
    {
        "id": 8,
        "category": "ICU",
        "question": "Bệnh nhân ICU với sốc nhiễm khuẩn cần điều chỉnh liều kháng sinh như thế nào?",
        "options": [
            "Giảm liều do suy thận",
            "Tăng liều do tăng Vd và ARC",
            "Không thay đổi",
            "Chỉ tăng tần suất"
        ],
        "correct": 1,
        "explanation": "Bệnh nhân ICU với sốc nhiễm khuẩn có tăng Vd (volume of distribution) và ARC (augmented renal clearance), nên cần tăng liều."
    },
    {
        "id": 9,
        "category": "TDM",
        "question": "Kháng sinh nào cần TDM (therapeutic drug monitoring)?",
        "options": [
            "Vancomycin và Aminoglycoside",
            "Ceftriaxone",
            "Azithromycin",
            "Tất cả kháng sinh"
        ],
        "correct": 0,
        "explanation": "Vancomycin và Aminoglycoside (Gentamicin, Amikacin, Tobramycin) cần TDM do có nguy cơ độc tính và phạm vi điều trị hẹp."
    },
    {
        "id": 10,
        "category": "Duration",
        "question": "Thời gian điều trị kháng sinh cho CAP (Community-Acquired Pneumonia) không biến chứng là bao lâu?",
        "options": [
            "3 ngày",
            "5-7 ngày",
            "10-14 ngày",
            "21 ngày"
        ],
        "correct": 1,
        "explanation": "CAP không biến chứng chỉ cần 5-7 ngày điều trị. Thời gian dài hơn không cải thiện kết quả và tăng nguy cơ kháng thuốc."
    },
]


def get_quiz_questions(category: Optional[str] = None, num_questions: int = 10) -> List[Dict]:
    """Get quiz questions, optionally filtered by category"""
    questions = QUIZ_QUESTIONS.copy()
    
    if category:
        questions = [q for q in questions if q["category"].lower() == category.lower()]
    
    # Randomize and limit
    random.shuffle(questions)
    return questions[:num_questions]


def render_quizzes():
    """Render Quizzes UI"""
    
    st.markdown("### 📝 Câu Hỏi Trắc Nghiệm về Kháng Sinh")
    st.caption("Kiểm tra kiến thức về kháng sinh: liều dùng, phổ tác dụng, PK/PD, stewardship")
    
    # Category selection
    categories = sorted(list(set([q["category"] for q in QUIZ_QUESTIONS])))
    selected_category = st.selectbox(
        "Chọn chủ đề:",
        options=["Tất cả"] + categories,
        key="quiz_category"
    )
    
    # Number of questions
    num_questions = st.slider(
        "Số câu hỏi:",
        min_value=5,
        max_value=len(QUIZ_QUESTIONS),
        value=10,
        step=5,
        key="quiz_num_questions"
    )
    
    # Initialize session state
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'quiz_current_index' not in st.session_state:
        st.session_state.quiz_current_index = 0
    if 'quiz_finished' not in st.session_state:
        st.session_state.quiz_finished = False
    
    # Start quiz button
    if not st.session_state.quiz_started:
        if st.button("🚀 Bắt Đầu Quiz", type="primary", use_container_width=True):
            category = None if selected_category == "Tất cả" else selected_category
            questions = get_quiz_questions(category, num_questions)
            st.session_state.quiz_questions = questions
            st.session_state.quiz_answers = {}
            st.session_state.quiz_current_index = 0
            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False
            st.rerun()
    
    # Quiz in progress
    if st.session_state.quiz_started and not st.session_state.quiz_finished:
        questions = st.session_state.quiz_questions
        current_index = st.session_state.quiz_current_index
        
        if current_index < len(questions):
            question = questions[current_index]
            
            st.markdown("---")
            st.markdown(f"#### Câu {current_index + 1}/{len(questions)}")
            st.markdown(f"**Chủ đề:** {question['category']}")
            st.markdown(f"**{question['question']}**")
            
            # Answer options
            selected_answer = st.radio(
                "Chọn đáp án:",
                options=question["options"],
                key=f"quiz_answer_{question['id']}",
                label_visibility="collapsed"
            )
            
            # Navigation buttons
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if current_index > 0:
                    if st.button("⬅️ Câu trước", use_container_width=True):
                        # Save current answer
                        answer_index = question["options"].index(selected_answer)
                        st.session_state.quiz_answers[question['id']] = answer_index
                        st.session_state.quiz_current_index -= 1
                        st.rerun()
            
            with col2:
                if st.button("💾 Lưu đáp án", use_container_width=True):
                    answer_index = question["options"].index(selected_answer)
                    st.session_state.quiz_answers[question['id']] = answer_index
                    st.success("Đã lưu!")
            
            with col3:
                if current_index < len(questions) - 1:
                    if st.button("Câu sau ➡️", use_container_width=True):
                        # Save current answer
                        answer_index = question["options"].index(selected_answer)
                        st.session_state.quiz_answers[question['id']] = answer_index
                        st.session_state.quiz_current_index += 1
                        st.rerun()
                else:
                    if st.button("✅ Nộp bài", type="primary", use_container_width=True):
                        # Save current answer
                        answer_index = question["options"].index(selected_answer)
                        st.session_state.quiz_answers[question['id']] = answer_index
                        st.session_state.quiz_finished = True
                        st.rerun()
            
            # Progress bar
            progress = (current_index + 1) / len(questions)
            st.progress(progress)
            st.caption(f"Tiến độ: {current_index + 1}/{len(questions)} câu")
    
    # Quiz finished - show results
    if st.session_state.quiz_finished:
        questions = st.session_state.quiz_questions
        answers = st.session_state.quiz_answers
        
        st.markdown("---")
        st.markdown("### 📊 Kết Quả Quiz")
        
        # Calculate score
        correct = 0
        total = len(questions)
        
        results = []
        for question in questions:
            q_id = question['id']
            user_answer = answers.get(q_id, -1)
            correct_answer = question['correct']
            is_correct = user_answer == correct_answer
            
            if is_correct:
                correct += 1
            
            results.append({
                "question": question['question'],
                "user_answer": question['options'][user_answer] if user_answer >= 0 else "Chưa trả lời",
                "correct_answer": question['options'][correct_answer],
                "is_correct": is_correct,
                "explanation": question['explanation']
            })
        
        score_percent = (correct / total) * 100
        
        # Display score
        if score_percent >= 80:
            color = "#4caf50"
            emoji = "🎉"
            message = "Xuất sắc!"
        elif score_percent >= 60:
            color = "#8bc34a"
            emoji = "👍"
            message = "Tốt!"
        elif score_percent >= 40:
            color = "#ffc107"
            emoji = "📚"
            message = "Cần cải thiện"
        else:
            color = "#f44336"
            emoji = "💪"
            message = "Tiếp tục học tập!"
        
        st.markdown(f"""
        <div style='
            background: {color};
            color: white;
            padding: 30px;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 20px;
        '>
            <h1 style='margin: 0; color: white; font-size: 3em;'>{emoji}</h1>
            <h2 style='margin: 10px 0; color: white;'>{message}</h2>
            <p style='margin: 0; font-size: 2em; font-weight: bold;'>{correct}/{total}</p>
            <p style='margin: 5px 0 0 0; font-size: 1.5em;'>{score_percent:.0f}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed results
        st.markdown("---")
        st.markdown("#### 📋 Chi Tiết Từng Câu")
        
        for idx, result in enumerate(results, 1):
            with st.expander(f"Câu {idx}: {'✅' if result['is_correct'] else '❌'}", expanded=False):
                st.markdown(f"**Câu hỏi:** {result['question']}")
                st.markdown(f"**Đáp án của bạn:** {result['user_answer']}")
                st.markdown(f"**Đáp án đúng:** {result['correct_answer']}")
                st.info(f"**Giải thích:** {result['explanation']}")
        
        # Restart button
        st.markdown("---")
        if st.button("🔄 Làm lại Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False
            st.session_state.quiz_questions = []
            st.session_state.quiz_answers = {}
            st.session_state.quiz_current_index = 0
            st.rerun()
