# Maxillofacial M Surgery Clinic — เว็บไซต์ประเทศไทย

เว็บไซต์สำหรับคลินิกทันตกรรมเฉพาะทาง **ศัลยกรรมโครงหน้าและขากรรไกร** (อ้างอิงแนวคิดจาก [Vertex Dental Thailand](https://www.vertexdentalthailand.com/) โดยไม่คัดลอกดีไซน์หรือเนื้อหา)

## เปิดดูเว็บ

1. เปิดไฟล์ `index.html` ในเบราว์เซอร์ (ดับเบิลคลิก)
2. หรือใช้ Live Server / extension ใน VS Code / Cursor

## โครงสร้าง

```
에버엠_태국/
├── index.html      # หน้าเดียว (one-page)
├── css/styles.css
├── js/main.js
└── README.md
```

## ส่วนประกอบหลัก

- Hero + จุดเด่นคลินิก
- เกี่ยวกับเรา (Integrated facial approach)
- บริการศัลยกรรมโครงหน้า 6 รายการ
- เทคโนโลยี 3D / CBCT
- ขั้นตอนการรักษา 5 ขั้น
- ทีมแพทย์ (ตัวอย่าง)
- เคสตัวอย่าง / รีวิว / FAQ
- แบบฟอร์มนัดปรึกษา

## ปรับแต่งก่อนใช้งานจริง

- เปลี่ยนชื่อคลินิก โลโก้ ที่อยู่ เบอร์โทร อีเมล Line
- แทนที่รูปแพทย์และ Before/After จริง
- 상담 폼 이메일: Vercel 환경변수 `RESEND_API_KEY` 설정 (아래 참고)
- เพิ่มภาษาไทย–อังกฤษสลับ (ถ้าต้องการผู้ป่วยต่างชาติ)

## เทคโนโลยี

HTML5, CSS3 (responsive), Vanilla JavaScript — ไม่ต้องติดตั้ง dependencies

## 상담 폼 → 회사 이메일

폼 제출 시 Supabase 없이 **Resend** API로 지정 메일함에 전달됩니다.

1. [Resend](https://resend.com) 가입 후 API Key 발급
2. Vercel 프로젝트 → **Settings → Environment Variables** 에 추가:
   - `RESEND_API_KEY` — Resend API 키
   - `INQUIRY_TO_EMAIL` — 수신 주소 (기본: `info@bluebridge-global.com`)
   - `INQUIRY_FROM_EMAIL` — 발신 주소 (Resend에서 허용한 주소)
3. 재배포 후 폼 테스트

로컬에서 API 테스트: `vercel dev` (Vercel CLI 필요)

`.env.example` 참고
