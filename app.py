import streamlit as st
import openai

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم والخلفية المتحركة (DNA Animation & Glowing UI)
st.markdown("""
<style>
    .stApp {
        background-color: #030712;
        color: #E2E8F0;
    }
    
    .lab-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.2);
    }
    
    h1, h2, h3 {
        color: #F8FAFC !important;
        font-weight: 800;
    }
    p, span, label, div {
        color: #CBD5E1 !important;
    }
</style>

<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; opacity: 0.15;">
    <canvas id="dnaCanvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('dnaCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;
        
        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        let particles = [];
        for(let i=0; i<60; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 1.5,
                vy: (Math.random() - 0.5) * 1.5,
                radius: Math.random() * 3 + 2,
                angle: Math.random() * Math.PI
            });
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            ctx.fillStyle = '#38bdf8';
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.2)';

            particles.forEach((p, index) => {
                p.x += p.vx;
                p.y += p.vy;
                p.angle += 0.03;

                if (p.x < 0) p.x = width;
                if (p.x > width) p.x = 0;
                if (p.y < 0) p.y = height;
                if (p.y > height) p.y = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y + Math.sin(p.angle)*10, p.radius, 0, Math.PI * 2);
                ctx.fill();

                for(let j = index + 1; j < particles.length; j++) {
                    let p2 = particles[j];
                    let dist = Math.hypot(p.x - p2.x, p.y - p2.y);
                    if(dist < 120) {
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y + Math.sin(p.angle)*10);
                        ctx.lineTo(p2.x, p2.y + Math.sin(p2.angle)*10);
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
st.markdown("<p style='font-size: 1.1rem;'>منصة النانو الذكية لتحليل واستكشاف تقنية كريسبر لتعديل الجينات بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="lab-card">
            <h3>🔬 دقة النص</h3>
            <p>تحليل فائق الدقة لتسلسلات النيوكليوتيدات واكتشاف الطفرات.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="lab-card">
            <h3>⚡ محاكاة فورية</h3>
            <p>محاكاة بصرية حية لعملية القص المزدوج والربط الجيني.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="lab-card">
            <h3>🛡️ فحص الأمان</h3>
            <p>فحص استباقي لمنع أي تأثيرات جانبية خارج المستهدف.</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. قسم الشات التفاعلي الذكي (مربع إدخال الأسئلة)
st.subheader("💬 اسأل المختبر الذكي عن تقنية CRISPR-Cas9")

# تخزين المحادثة في الذاكرة المؤقتة للصفحة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# مربع الشات السفلي اللي يكتبون فيه المستخدمين
if prompt := st.chat_input("اطرح سؤالك هنا (مثلاً: كيف يعمل إنزيم Cas9؟)..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد تجريبي ذكي ومباشر عن كريسبر (أو ربطه بـ OpenAI إذا المفتاح جاهز)
    response = f"أهلاً بك يا هدى! استفسارك الكريم حول ({prompt}) يوضح أهمية تقنية CRISPR-Cas9 في إحداث قص دقيق في الحمض النووي المستهدف بدقة نانوية عالية."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
