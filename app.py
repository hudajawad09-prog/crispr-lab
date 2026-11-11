import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم والخلفية المتحركة بالـ CSS الحية والواضحة
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

    .stApp {
        background-color: #010409;
        color: #F8FAFC;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    /* تأثيرات جزيئات الـ DNA المتحركة في الخلفية */
    .floating-dna {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .dna-particle {
        position: absolute;
        display: block;
        list-style: none;
        width: 25px;
        height: 25px;
        background: rgba(56, 189, 248, 0.15);
        border: 2px solid rgba(56, 189, 248, 0.5);
        border-radius: 50%;
        bottom: -150px;
        animation: animateParticle 12s linear infinite;
    }

    .dna-particle:nth-child(1) { left: 10%; width: 30px; height: 30px; animation-duration: 8s; background: rgba(56, 189, 248, 0.2); }
    .dna-particle:nth-child(2) { left: 25%; width: 20px; height: 20px; animation-duration: 12s; animation-delay: 2s; border-color: rgba(168, 85, 247, 0.6); }
    .dna-particle:nth-child(3) { left: 40%; width: 40px; height: 40px; animation-duration: 10s; animation-delay: 4s; }
    .dna-particle:nth-child(4) { left: 55%; width: 25px; height: 25px; animation-duration: 14s; animation-delay: 1s; border-color: rgba(168, 85, 247, 0.6); }
    .dna-particle:nth-child(5) { left: 70%; width: 35px; height: 35px; animation-duration: 9s; animation-delay: 3s; }
    .dna-particle:nth-child(6) { left: 85%; width: 20px; height: 20px; animation-duration: 11s; animation-delay: 5s; }

    @keyframes animateParticle {
        0% {
            transform: translateY(0) rotate(0deg) scale(1);
            opacity: 0.8;
        }
        100% {
            transform: translateY(-900px) rotate(720deg) scale(1.3);
            opacity: 0;
        }
    }

    /* تصميم الكروت الفخمة */
    .lab-card {
        position: relative;
        z-index: 1;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.95));
        border: 1px solid rgba(56, 189, 248, 0.5);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.4);
        transition: all 0.3s ease-in-out;
        margin-bottom: 15px;
    }
    .lab-card:hover {
        transform: translateY(-5px);
        border-color: rgba(56, 189, 248, 1);
        box-shadow: 0 20px 40px -15px rgba(56, 189, 248, 0.7);
    }
    
    h1, h2, h3, h4 {
        color: #38bdf8 !important;
        font-family: 'Cairo', sans-serif;
        font-weight: 800;
        position: relative;
        z-index: 1;
    }
    p, span, label, div {
        color: #E2E8F0 !important;
        font-family: 'Cairo', sans-serif;
        position: relative;
        z-index: 1;
    }
</style>

<!-- عناصر الخلفية المتحركة -->
<div class="floating-dna">
    <div class="dna-particle"></div>
    <div class="dna-particle"></div>
    <div class="dna-particle"></div>
    <div class="dna-particle"></div>
    <div class="dna-particle"></div>
    <div class="dna-particle"></div>
</div>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي
st.title("🧬 CRISPR-Cas9 Elite Lab")
st.markdown("<p style='font-size: 1.2rem; position: relative; z-index: 1;'>منصة النانو الذكية لتحليل واستكشاف تقنية كريسبر لتعديل الجينات بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="lab-card">
            <h3>🔬 دقة النص</h3>
            <p>تحليل فائق الدقة لتسلسلات النيوكليوتيدات واكتشاف الطفرات المستهدفة.</p>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("عرض تفاصيل دقة النص"):
        st.write("• فحص مطابقة قواعد القواعد النيتروجينية (A, T, C, G).")
        st.write("• خوارزمية ذكية لاكتشاف الأخطاء بنسبة دقة تصل إلى 99.8%.")

with col2:
    st.markdown("""
        <div class="lab-card">
            <h3>⚡ محاكاة فورية</h3>
            <p>محاكاة بصرية حية لعملية القص المزدوج والربط الجيني لحظياً.</p>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("عرض تفاصيل المحاكاة"):
        st.write("• محاكاة عمل إنزيم Cas9 وهو يقطع شريط الـ DNA بدقة.")
        st.write("• تتبع حركة الإنزيم خطوة بخطوة على الشاشة.")

with col3:
    st.markdown("""
        <div class="lab-card">
            <h3>🛡️ فحص الأمان</h3>
            <p>فحص استباقي لمنع أي تأثيرات جانبية خارج المستهدف وبأمان تام.</p>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("عرض تفاصيل الأمان"):
        st.write("• تقييم المخاطر البيولوجية المحتملة.")
        st.write("• منع التعديلات العشوائية خارج الجين المستهدف.")

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
