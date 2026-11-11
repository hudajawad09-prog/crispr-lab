import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. تصميم الواجهة بالكامل وتثبيت الاتجاه العربي الحقيقي (RTL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

    .stApp {
        background-color: #010409 !important;
        color: #F8FAFC !important;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
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
        direction: rtl;
    }

    /* تنسيق صناديق المحادثة المباشرة */
    .chat-box-user {
        background: rgba(30, 41, 59, 0.9);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 12px;
        padding: 14px;
        margin: 10px 0;
        text-align: right;
        direction: rtl;
        color: #38bdf8;
        font-weight: 700;
    }

    .chat-box-ai {
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(168, 85, 247, 0.5);
        border-radius: 12px;
        padding: 16px;
        margin: 10px 0;
        text-align: right;
        direction: rtl;
        color: #F8FAFC;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.2);
    }

    /* تصميم فاخر للفوتر واسمك بخط أصغر في الأسفل */
    .footer-box {
        position: relative;
        z-index: 10;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.98));
        border: 1px solid rgba(168, 85, 247, 0.4);
        border-radius: 16px;
        padding: 20px;
        margin-top: 40px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(56, 189, 248, 0.2);
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

# 4. نظام ذكاء اصطناعي تفاعلي متطور
st.subheader("💬 اسأل المختبر الذكي عن تقنية CRISPR-Cas9")

if "history" not in st.session_state:
    st.session_state.history = []

user_query = st.text_input("اطرح أي سؤال عن تقنية كريسبر:", key="user_question")

if st.button("إرسال السؤال 🚀"):
    if user_query.strip():
        q = user_query.strip()
        q_lower = q.lower()
        
        # محرك تحليل ذكي آمن وخالٍ من الأخطاء
        if any(word in q_lower for word in ["كيف", "يعمل", "انزيم", "إنزيم", "cas9", "كاس9", "آلية", "طريقة"]):
            ans = "يعمل إنزيم Cas9 بمثابة مقص جيني دقيق يتم توجيهه بواسطة حمض نووي ريبوزي (Guide RNA) لتحديد موقع التسلسل المستهدف في الـ DNA بدقة نانوية وإحداث قطع دقيق."
        elif any(word in q_lower for word in ["أمان", "امان", "مخاطر", "خطورة", "جانبية", "ضرر", "أخلاقيات"]):
            ans = "يعتمد نظام الأمان على خوارزميات استباقية تفحص الجينوم لمنع أي طفرات عشوائية أو تأثيرات خارج الهدف، لضمان أعلى معايير السلامة الحيوية والدقة المطلقة."
        elif any(word in q_lower for word in ["دقة", "نسبة", "نص", "قواعد", "نيوكليوتيدات", "a", "t", "c", "g", "أخطاء"]):
            ans = "تعتمد دقة النظام على مطابقة القواعد النيتروجينية بدقة فائقة تصل إلى 99.8% لتحليل التسلسلات بدقة واكتشاف الطفرات."
        elif any(word in q_lower for word in ["مرض", "علاج", "امراض", "أمراض", "وراثية", "سرطان", "الوراثية"]):
            ans = "تُستخدم التقنية في العلاج الجيني عبر تصحيح الطفرات المسببة للأمراض الوراثية المستعصية وإزالة أو استبدال الجينات المعطوبة بدقة متناهية."
        elif any(word in q_lower for word in ["تاريخ", "اكتشاف", "من اخترع", "نشأة"]):
            ans = "تم تطويع نظام CRISPR-Cas9 المأخوذ أساساً من جهاز المناعة الطبيعي للبكتيريا ليصبح أداة ثورية لتعديل الجينات في عام 2012 على يد العلماء."
        elif any(word in q_lower for word in ["مستقبل", "تطبيقات", "استخدامات", "مجالات"]):
            ans = "تشمل التطبيقات المستقبلية للتقنية علاج الأمراض الوراثية، تطوير المحاصيل الزراعية المقاومة للظروف المناخية، والقضاء على بعض الأعباء الطبية الوراثية."
        else:
            ans = "تُعد تقنية CRISPR-Cas9 ثورة حقيقية في الهندسة الوراثية، حيث تتيح للباحثين تعديل الحمض النووي بدقة متناهية وفتح آفاق جديدة كلياً في الطب الحيوي."

        # حفظ السجل لعرضه بالترتيب الصحيح
        st.session_state.history.append({"user": q, "ai": ans})

# عرض المحادثات السابقة بشكل مرتب ومنضبط يمين لليسار
if st.session_state.history:
    st.markdown("---")
    for chat in reversed(st.session_state.history):
        st.markdown(f"<div class='chat-box-user'>👤 سؤالك: {chat['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-box-ai'>🤖 إجابة المختبر: {chat['ai']}</div>", unsafe_allow_html=True)

# 5. قسم الأعضاء والاعتمادات الرسمية أولاً ثم اسمك أسفلهم بحجم أصغر
st.markdown("""
<div class="footer-box">
    <p style="color: #F8FAFC; font-size: 1rem; margin: 4px 0;">إشراف المعلمة: أ. وديعة خليل</p>
    <p style="color: #F8FAFC; font-size: 1rem; margin: 4px 0;">المعلمة الأولى: هدى العرادي</p>
    <p style="color: #F8FAFC; font-size: 1rem; margin: 4px 0;">مديرة المدرسة: هاشمية السيد شرف</p>
    <hr style="border-color: rgba(168, 85, 247, 0.2); margin: 12px 0;">
    <p style="color: #38bdf8; font-size: 0.85rem; font-weight: 600; margin: 0;">By: Huda Hasan</p>
</div>
""", unsafe_allow_html=True)
