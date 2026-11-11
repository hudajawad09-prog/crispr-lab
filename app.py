import streamlit as st
from openai import OpenAI

# 1. إعدادات الصفحة الفخمة
st.set_page_config(
    page_title="CRISPR-Cas9 Elite Lab",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم الواجهة الداكنة الفخمة مع حركات وتأثيرات بصرية (CSS Animations)
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 5px rgba(0, 210, 255, 0.2); }
        50% { box-shadow: 0 0 20px rgba(0, 210, 255, 0.6); }
        100% { box-shadow: 0 0 5px rgba(0, 210, 255, 0.2); }
    }
    @keyframes floatDNA {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }
    .floating-header {
        animation: floatDNA 3s ease-in-out infinite;
        text-align: center;
        font-size: 45px;
        margin-bottom: 10px;
    }
    .card-box {
        background: linear-gradient(145deg, #131b2e, #1a233a);
        border: 1px solid #1e3a8a;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
        margin-bottom: 20px;
        animation: pulseGlow 4s infinite;
        transition: 0.3s;
    }
    .card-box:hover {
        transform: translateY(-4px);
        border-color: #00d2ff;
    }
    .stTextInput input {
        background-color: #111827;
        color: #ffffff;
        border: 1px solid #3b82f6;
        border-radius: 10px;
    }
    div.stButton > button {
        background: linear-gradient(93.5deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# 3. جلب مفتاح OpenAI
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = None

client = OpenAI(api_key=api_key) if api_key else None

# 4. الشريط الجانبي الفخم
with st.sidebar:
    st.markdown("## 🧬 مركز قيادة المختبر")
    st.markdown("---")
    app_mode = st.radio(
        "اختر القسم:",
        ["🔬 المحاكي الجيني التفاعلي", "📊 خريطة تقنية CRISPR", "💡 أسئلة العرض التقديمي"]
    )
    st.markdown("---")
    st.markdown("### 🌟 حالة النظام السحابي")
    if api_key:
        st.success("الذكاء الاصطناعي: متصل وجاهز 🟢")
    else:
        st.error("مفتاح API غير متصل!")
    st.markdown("---")
    st.markdown("<p style='font-size: 11px; color: #94a3b8;'>منصة الـ CRISPR الذكية © 2026</p>", unsafe_allow_html=True)

# 5. الواجهة الرئيسية
if app_mode == "🔬 المحاكي الجيني التفاعلي":
    st.markdown('<div class="floating-header">🧬 CRISPR-Cas9 Elite Lab 🧬</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #93c5fd; margin-bottom: 30px;'>منصة تحليل واستكشاف تعديل الجينات بالذكاء الاصطناعي</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-box"><h3>🎯 دقة القص</h3><p>استهداف تسلسلات الـ DNA بدقة مطلقة تصل لمستوى النيوكليوتيد الواحد.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card-box"><h3>⚡ محاكاة فورية</h3><p>معالجة بيانات البروتينات والجينات الحيوية وتسجيل النتائج بثوانٍ.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card-box"><h3>🛡️ فحص الأمان</h3><p>خوارزميات ذكية لتقييم الطفرات الجانبية وضمان سلامة الخلايا.</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💬 اسأل مساعد المختبر الذكي:")
    
    user_prompt = st.text_input("اكتب استفسارك العلمي هنا (مثلاً: كيف يوجه الـ Guide RNA إنزيم Cas9 للهدف بدقة؟):")
    
    if st.button("🚀 بدء التحليل الجيني المتقدم"):
        if not client:
            st.error("الرجاء ضبط مفتاح OpenAI API في إعدادات المنصة (Secrets).")
        elif not user_prompt:
            st.warning("الرجاء كتابة سؤال أو استفسار علمي أولاً.")
        else:
            with st.spinner("🔄 جاري فك الرموز الجينية وصياغة الإجابة الاحترافية..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "أنت عالم خبير في الوراثة وتقنية كريسبر. أجب بأسلوب علمي، دقيق، ومبهر باللغة العربية."},
                            {"role": "user", "content": user_prompt}
                        ]
                    )
                    answer = response.choices[0].message.content
                    st.markdown("### 🔬 تقرير التحليل العلمي:")
                    st.markdown(f'<div class="card-box">{answer}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال: {e}")

elif app_mode == "📊 خريطة تقنية CRISPR":
    st.markdown("# 📊 الهيكل البنيوي والتطبيقات الحيوية")
    st.markdown("تعرف على المكونات الثورية التي جعلت هذه التقنية تتصدر أبحاث العصر.")
    
    tab1, tab2, tab3 = st.tabs(["مقص Cas9 الجزيئي", "دليل الـ RNA", "آفاق المستقبل العلاجي"])
    
    with tab1:
        st.markdown("### إنزيم Cas9 (The Molecular Scalpel)")
        st.write("بروتين يعمل بمثابة مقص جزيئي دقيق يمتلك القدرة على شطر شريطي الحمض النووي (DNA) في مواقع مخصصة بدقة فائقة.")
    with tab2:
        st.markdown("### جزيء RNA الدليل (Guide RNA)")
        st.write("سلسلة مبرمجة هندسياً لتقود إنزيم Cas9 مباشرة إلى التسلسل الجيني المستهدف بدقة تطابق تامة.")
    with tab3:
        st.markdown("### ثورة التطبيقات الطبية")
        st.write("- تصحيح الطفرات الوراثية المسببة للأمراض المستعصية.\n- تطوير علاجات جينية متطورة للسرطان.\n- الهندسة الحيوية للمحاصيل المقاومة للظروف المناخية القاسية.")

else:
    st.markdown("# 💡 أسئلة المناقشة والعرض التقديمي")
    st.markdown("أبرز الركائز العلمية وجاهزة تماماً لعرضها غداً بكل ثقة:")
    
    st.markdown("""
    * **1. أصل الفكرة:** مستوحاة بالأساس من نظام المناعة الطبيعي لدى البكتيريا للدفاع عن نفسها ضد الفيروسات.
    * **2. لماذا أحدثت ضجة عالمية؟** بسبب رخص تكلفتها العالية وسرعتها الفائقة وسهولة برمج مقارنة بالتقنيات الكلاسيكية القديمة.
    * **3. الببعاد الأخلاقية:** الحدود التنظيمية والأخلاقية حول تعديل الجينات البشرية والأجنة.
    """)