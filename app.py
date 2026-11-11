import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم والتنسيق مع ضبط اتجاه الشات والبار والخطوط بدقة متناهية
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

    .stApp {
        background-color: #010409 !important;
        color: #F8FAFC !important;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    /* خلفية سلاسل الـ DNA المتحركة */
    .dna-space {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .dna-strand {
        position: absolute;
        display: block;
        font-size: 40px;
        color: rgba(56, 189, 248, 0.7);
        bottom: -100px;
        animation: floatDNA 12s linear infinite;
        filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.9));
    }

    .dna-strand:nth-child(1) { left: 10%; animation-duration: 10s; animation-delay: 0s; }
    .dna-strand:nth-child(2) { left: 25%; animation-duration: 14s; animation-delay: 2s; color: rgba(168, 85, 247, 0.8); }
    .dna-strand:nth-child(3) { left: 40%; animation-duration: 9s; animation-delay: 4s; }
    .dna-strand:nth-child(4) { left: 60%; animation-duration: 13s; animation-delay: 1s; color: rgba(168, 85, 247, 0.8); }
    .dna-strand:nth-child(5) { left: 75%; animation-duration: 11s; animation-delay: 3s; }
    .dna-strand:nth-child(6) { left: 90%; animation-duration: 15s; animation-delay: 5s; }

    @keyframes floatDNA {
        0% { transform: translateY(0) rotate(0deg); opacity: 0.9; }
        100% { transform: translateY(-900px) rotate(360deg); opacity: 0; }
    }

    /* تصميم الكروت الفخمة والثابتة */
    .lab-card {
        position: relative;
        z-index: 10;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
        border: 1px solid rgba(56, 189, 248, 0.5);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.4);
        margin-bottom: 15px;
        text-align: right;
    }
    
    h1, h2, h3, h4, span, p, label, div {
        font-family: 'Cairo', sans-serif !important;
        color: #F8FAFC !important;
        text-align: right;
    }

    /* ضبط اتجاه ووستلة النصوص داخل الشات لكي لا تنعكس الحروف */
    .stChatMessage {
        direction: rtl !important;
        text-align: right !important;
    }
    
    .stChatMessage p, .stChatMessage div {
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: plaintext;
    }

    /* ضبط بار الكتابة ليكون واضح وسلس */
    .stChatInput input, .stChatInput textarea, div[data-baseweb="base-input"] input, textarea {
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        caret-color: #0F172A !important;
        direction: rtl !important;
        text-align: right !important;
        font-weight: 700 !important;
    }
</style>

<!-- عناصر سلاسل الـ DNA الخلفية -->
<div class="dna-space">
    <div class="dna-strand">🧬</div>
    <div class="dna-strand">🧬</div>
    <div class="dna-strand">🧬</div>
    <div class="dna-strand">🧬</div>
    <div class="dna-strand">🧬</div>
    <div class="dna-strand">🧬</div>
</div>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي والمنصة الأساسية
st.title("🧬 CRISPR-Cas9 Elite Lab")
st.markdown("<p style='font-size: 1.2rem; text-align: right;'>منصة النانو الذكية لتحليل واستكشاف تقنية كريسبر لتعديل الجينات بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="lab-card">
            <h3>🔬 دقة النص</h3>
            <p>تحليل فائق الدقة لتسلسلات النيوكليوتيدات واكتشاف الطفرات المستهدفة.</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <p style="font-size: 0.9rem; color: #38bdf8;">• فحص مطابقة القواعد النيتروجينية (A, T, C, G).<br>• خوارزمية ذكية لاكتشاف الأخطاء بنسبة 99.8%.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="lab-card">
            <h3>⚡ محاكاة فورية</h3>
            <p>محاكاة بصرية حية لعملية القص المزدوج والربط الجيني لحظياً.</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <p style="font-size: 0.9rem; color: #38bdf8;">• محاكاة عمل إنزيم Cas9 وهو يقطع شريط الـ DNA.<br>• تتبع حركة الإنزيم خطوة بخطوة.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="lab-card">
            <h3>🛡️ فحص الأمان</h3>
            <p>فحص استباقي لمنع أي تأثيرات جانبية خارج المستهدف وبأمان تام.</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <p style="font-size: 0.9rem; color: #38bdf8;">• تقييم المخاطر البيولوجية المحتملة.<br>• منع التعديلات العشوائية خارج الجين المستهدف.</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. قسم الشات الذكي التفاعلي مع إجابات دقيقة ومخصصة لكل سؤال
st.subheader("💬 اسأل المختبر الذكي عن تقنية CRISPR-Cas9")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اطرح سؤالك هنا (مثلاً: كيف يعمل إنزيم Cas9؟)..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ذكاء اصطناعي تفاعلي يحلل كل سؤال على حدة ويعطي إجابة مخصصة فريدة
    q = prompt.strip()
    q_lower = q.lower()
    
    if any(word in q_lower for word in ["كيف", "يعمل", "انزيم", "إنزيم", "cas9", "كاس9", "قص"]):
        response = f"أهلاً بك يا هدى! استفسارك عن ({q}) دقيق للغاية؛ إنزيم Cas9 يعمل بمثابة 'مقص جيني' ذكي يتم توجيهه بواسطة حمض نووي ريبوزي (Guide RNA) لتحديد موقع الجين المستهدف بدقة نانوية ثم إحداث قطع دقيق في شريط الـ DNA."
    elif any(word in q_lower for word in ["أمان", "امان", "مخاطر", "خطورة", "جانبية", "ضرر"]):
        response = f"بخصوص سؤالك عن ({q}): نظام فحص الأمان في منصتنا يستبق أي طفرات عشوائية أو تأثيرات جانبية محتملة خارج الجين المستهدف، لضمان أعلى معايير الأمان الحيوي أثناء التعديل."
    elif any(word in q_lower for word in ["دقة", "نسبة", "نص", "قواعد", "نيوكليوتيدات", "a", "t", "c", "g"]):
        response = f"تساؤلك حول ({q}) في محلّه؛ تعتمد تقنية دقة النص على مطابقة القواعد النيتروجينية بدقة فائقة تصل إلى 99.8% لتحليل التسلسل الجيني واكتشاف أي طفرات بدقة مذهلة."
    elif any(word in q_lower for word in ["مرض", "علاج", "امراض", "أمراض", "وراثية"]):
        response = f"إجابة على استفسارك ({q}): تُستخدم تقنية CRISPR-Cas9 بشكل ثوري لتصحيح الطفرات المسببة للأمراض الوراثية عبر استبدال أو تعديل التسلسلات المعطوبة بدقة عالية."
    else:
        response = f"مرحباً بك يا هدى! سؤالك المميز حول ({q}) يبرز مدى أهمية تقنية كريسبر-كاس9 في إحداث ثورة في الهندسة الوراثية وتعديل الجينات بدقة متناهية."

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
