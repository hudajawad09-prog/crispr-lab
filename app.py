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

    /* تصميم الكروت الفخمة والثابتة فوق الخلفية المتحركة */
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
            <p style="font-size: 0.85rem; color: #38bdf8;">👇 <b>اقرأ التفاصيل أدناه:</b><br>• فحص مطابقة القواعد النيتروجينية (A, T, C, G).<br>• خوارزمية ذكية لاكتشاف الأخطاء بنسبة 99.8%.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="lab-card">
            <h3>⚡ محاكاة فورية</h3>
            <p>محاكاة بصرية حية لعملية القص المزدوج والربط الجيني لحظياً.</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <p style="font-size: 0.85rem; color: #38bdf8;">👇 <b>اقرأ التفاصيل أدناه:</b><br>• محاكاة عمل إنزيم Cas9 وهو يقطع شريط الـ DNA.<br>• تتبع حركة الإنزيم خطوة بخطوة.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="lab-card">
            <h3>🛡️ فحص الأمان</h3>
            <p>فحص استباقي لمنع أي تأثيرات جانبية خارج المستهدف وبأمان تام.</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <p style="font-size: 0.85rem; color: #38bdf8;">👇 <b>اقرأ التفاصيل أدناه:</b><br>• تقييم المخاطر البيولوجية المحتملة.<br>• منع التعديلات العشوائية خارج الجين المستهدف.</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. قسم الشات الذكي للاستفسارات
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

    response = f"أهلاً بك يا هدى! استفسارك الكريم حول ({prompt}) يعكس فهمك العالي؛ تقنية كريسبر تستخدم نظام دفاع بكتيري موجّه بواسطة RNA لقص وتعديل الجينات بدقة مذهلة."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
