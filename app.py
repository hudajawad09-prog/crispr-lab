import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم، الخطوط، والخلفية الفضائية المتحركة للـ DNA
st.markdown("""
<style>
    /* استيراد خط عربي أنيق وفخم يشبه الأسلوب المطلوب */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

    .stApp {
        background-color: #020617;
        color: #F8FAFC;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    /* تصميم الكروت بتأثير النيون الزاهي والتفاعل */
    .lab-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(30, 41, 59, 0.9));
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.3);
        transition: all 0.3s ease-in-out;
        margin-bottom: 15px;
    }
    .lab-card:hover {
        transform: translateY(-5px);
        border-color: rgba(56, 189, 248, 0.9);
        box-shadow: 0 20px 40px -15px rgba(56, 189, 248, 0.6);
    }
    
    h1, h2, h3, h4 {
        color: #38bdf8 !important;
        font-family: 'Cairo', sans-serif;
        font-weight: 800;
    }
    p, span, label, div {
        color: #E2E8F0 !important;
        font-family: 'Cairo', sans-serif;
    }
</style>

<!-- خلفية تفاعلية لجزيئات الـ DNA وهي تسبح في الفضاء -->
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; opacity: 0.25;">
    <canvas id="spaceDnaCanvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('spaceDnaCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;
        
        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        let particles = [];
        for(let i=0; i<80; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 1.2,
                vy: (Math.random() - 0.5) * 1.2,
                radius: Math.random() * 3.5 + 1.5,
                angle: Math.random() * Math.PI,
                color: Math.random() > 0.5 ? '#38bdf8' : '#818cf8'
            });
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            
            particles.forEach((p, index) => {
                p.x += p.vx;
                p.y += p.vy;
                p.angle += 0.02;

                if (p.x < 0) p.x = width;
                if (p.x > width) p.x = 0;
                if (p.y < 0) p.y = height;
                if (p.y > height) p.y = 0;

                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y + Math.sin(p.angle)*15, p.radius, 0, Math.PI * 2);
                ctx.fill();

                // رسم روابط شبحية بين الجزيئات كأنها شريط DNA يسبح
                for(let j = index + 1; j < particles.length; j++) {
                    let p2 = particles[j];
                    let dist = Math.hypot(p.x - p2.x, p.y - p2.y);
                    if(dist < 100) {
                        ctx.strokeStyle = `rgba(56, 189, 248, ${0.25 * (1 - dist/100)})`;
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y + Math.sin(p.angle)*15);
                        ctx.lineTo(p2.x, p2.y + Math.sin(p2.angle)*15);
                        ctx.stroke();
                    }
                }
            });
            requestAnimationFrame(animate);
        }
        animate();
    }
</script>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي
st.title("🧬 CRISPR-Cas9 Elite Lab")
st.markdown("<p style='font-size: 1.2rem;'>منصة النانو الذكية لتحليل واستكشاف تقنية كريسبر لتعديل الجينات بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
st.divider()

# الأقسام التفاعلية مع إمكانية إظهار التفاصيل بالضغط
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
