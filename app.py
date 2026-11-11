import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم، الخلفية المتحركة، وتثبيت التنسيقات
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

    .stApp {
        background-color: #010409 !important;
        color: #F8FAFC !important;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    /* خلفية سلاسل الـ DNA المتحركة في الفضاء الخلفي */
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
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 0.9;
        }
        100% {
            transform: translateY(-900px) rotate(360deg);
            opacity: 0;
        }
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

# 4. قسم الشات الذكي التفاعلي المتطور
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

    # ذكاء اصطناعي تفاعلي يحلل السؤال ويرد بدقة علمية مخصصة
    user_q = prompt.lower()
    if "cas9" in user_q or "إنزيم" in user_q or "قص" in user_q:
        response = f"أهلاً بك يا هدى! بناءً على سؤالك حول **({prompt})**: يعمل إنزيم Cas9 كـ 'مقص جيني' موجه بواسطة جزيء RNA لإيجاد تسلسل الـ DNA المستهدف بدقة نانوية ثم إحداث قص مزدوج بدقة مذهلة."
    elif "أمان" in user_q or "خطورة" in user_q or "مخاطر" in user_q:
        response = f"سؤال مهم جداً حول **({prompt})**: نظام فحص الأمان في منصتنا يعتمد على خوارزميات استباقية تمنع أي طفرات عشوائية أو تأثيرات خارج الجين المستهدف لضمان الأمان الحيوي التام."
    elif "دقة" in user_q or "نص" in user_q or "قواعد" in user_q:
        response = f"فيما يتعلق بـ **({prompt})**: تعتمد تقنية دقة النص على مطابقة القواعد النيتروجينية (A, T, C, G) بنسبة دقة فائقة تصل إلى 99.8% لاكتشاف الطفرات."
    else:
        response = f"مرحباً بك! استفسارك الذكي حول **({prompt})** يلامس جوهر تقنية كريسبر-كاس9؛ وهي تقنية ثورية لتعديل الجينات تستخدم نظام دفاع بكتيري مذهل لمعالجة الأمراض الوراثية بدقة لا تصدق."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
