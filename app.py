import streamlit as st
import openai

# 1. إعدادات الصفحة
st.set_page_config(page_title="CRISPR-Cas9 Elite Lab", page_icon="🧬", layout="wide")

# 2. كود التصميم والخلفية المتحركة (DNA Animation & Glowing UI)
st.markdown("""
<style>
    /* خلفية داكنة فخمة للمختبر */
    .stApp {
        background-color: #030712;
        color: #E2E8F0;
    }
    
    /* تصميم الكروت بتأثير النيون الزاهي */
    .lab-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.2);
        transition: all 0.3s ease-in-out;
    }
    .lab-card:hover {
        transform: translateY(-5px);
        border-color: rgba(56, 189, 248, 0.8);
        box-shadow: 0 20px 40px -15px rgba(56, 189, 248, 0.4);
    }
    
    /* تنسيق العناوين والنصوص بوضوح تام */
    h1, h2, h3 {
        color: #F8FAFC !important;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    p, span, label, div {
        color: #CBD5E1 !important;
    }
</style>

<!-- عنصر حركي بصري لجزيئات الـ DNA المتحركة في الخلفية -->
<div id="dna-animation-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; opacity: 0.15;">
    <canvas id="dnaCanvas"></canvas>
</div>

<script>
    // رسم وتدوير خيوط وجزيئات الـ DNA بشكل حيوي ومستمر لتأكيد الانبهار البصري
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
            particles.type = Math.random() > 0.5 ? 'dna' : 'node';
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

                // ربط الجزيئات بخطوط رفيعة كأنها روابط هيدروجينية متحركة للـ DNA
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

# عرض الأقسام بتصميم الكروت الفخمة والمضيئة
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="lab-card">
            <h3>🔬 دقة النص</h3>
            <p>تحليل فائق الدقة لتسلسلات النيوكليوتيدات واكتشاف الطفرات المستهدفة بالتعاون مع خوارزميات Cas9.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="lab-card">
            <h3>⚡ محاكاة فورية</h3>
            <p>محاكاة بصرية حية لعملية القص المزدوج والربط الجيني للحمض النووي لحظياً وبكفاءة مذهلة.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="lab-card">
            <h3>🛡️ فحص الأمان</h3>
            <p>فحص استباقي لمنع أي تأثيرات جانبية خارج المستهدف وضمان أعلى معايير السلامة البيولوجية.</p>
        </div>
    """, unsafe_allow_html=True)
