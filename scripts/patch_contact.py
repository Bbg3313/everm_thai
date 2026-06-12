from pathlib import Path
path = Path(__file__).resolve().parent.parent / "index.html"
text = path.read_text(encoding="utf-8")
start = text.index('    <section class="section contact" id="contact"')
end = text.index('  </main>', start)
d = "div"
new = f"""    <section class="section contact" id="contact" aria-labelledby="contact-title">
      <{d} class="container">
        <header class="contact-header section-head center">
          <p class="section-label" data-i18n="contact_label">ติดต่อเรา</p>
          <h2 id="contact-title" data-i18n-html="contact_title">นัดปรึกษา<br />โครงหน้าของคุณ</h2>
        </header>

        <{d} class="contact-grid">
          <aside class="contact-aside" aria-label="Clinic location and contact">
            <figure class="contact-visual">
              <img
                src="images/clinic/building-exterior.png"
                alt="อาคาร EVERM Surgery Clinic"
                data-i18n-alt="contact_img_alt"
                class="contact-building"
                width="480"
                height="640"
                loading="lazy"
              />
            </figure>
            <{d} class="contact-info-card">
              <ul class="contact-info">
                <li>
                  <strong data-i18n="contact_addr_label">ที่อยู่</strong>
                  <span data-i18n="contact_addr">EVERM Building, 2 Hakdong-ro 3-gil, Gangnam-gu, Seoul, Republic of Korea</span>
                </li>
                <li>
                  <strong data-i18n="contact_phone_label">โทรศัพท์</strong>
                  <a href="tel:+8225408275">02-540-8275</a>
                </li>
                <li>
                  <strong data-i18n="contact_email_label">อีเมล</strong>
                  <a href="mailto:hello@evermclinic.th">hello@evermclinic.th</a>
                </li>
                <li>
                  <strong data-i18n="contact_hours_label">เวลาทำการ</strong>
                  <span data-i18n="contact_hours">จันทร์ – อาทิตย์ 10:00 – 19:00</span>
                </li>
              </ul>
            </{d}>
          </aside>

          <{d} class="contact-form-wrap">
            <form class="contact-form" id="appointment-form" novalidate>
              <h3 class="contact-form-title" data-i18n="form_title_hidden">แบบฟอร์มนัดหมาย</h3>
              <{d} class="form-row">
                <label for="name" data-i18n="form_name">ชื่อ-นามสกุล *</label>
                <input type="text" id="name" name="name" data-i18n-placeholder="form_name_ph" required autocomplete="name" placeholder="ชื่อของคุณ" />
              </{d}>
              <{d} class="form-row">
                <label for="phone" data-i18n="form_phone">เบอร์โทร / Line ID *</label>
                <input type="tel" id="phone" name="phone" data-i18n-placeholder="form_phone_ph" required autocomplete="tel" placeholder="08x-xxx-xxxx" />
              </{d}>
              <{d} class="form-row">
                <label for="service" data-i18n="form_service">บริการที่สนใจ *</label>
                <select id="service" name="service" required>
                  <option value="" data-i18n="form_service_ph">เลือกบริการ</option>
                  <option data-i18n="form_opt0">ปรึกษาศัลยกรรมโครงหน้า (ทั่วไป)</option>
                  <option data-i18n="form_opt1">ผ่าตัดเลื่อนขากรรไกร</option>
                  <option data-i18n="form_opt2">ตัดกราม / ตัดโหนกแก้ม</option>
                  <option data-i18n="form_opt3">จัดฟัน + ศัลยกรรมขากรรไกร</option>
                  <option data-i18n="form_opt4">ผู้ป่วยต่างชาติ (International)</option>
                </select>
              </{d}>
              <{d} class="form-row two-col">
                <{d}>
                  <label for="date" data-i18n="form_date">วันที่สะดวก</label>
                  <input type="date" id="date" name="date" data-i18n-lang lang="th" data-i18n-title="form_date_hint" title="ปี-เดือน-วัน" />
                  <p class="form-field-hint" data-i18n="form_date_hint">ปี-เดือน-วัน</p>
                </{d}>
                <{d}>
                  <label for="time" data-i18n="form_time">เวลา</label>
                  <input type="time" id="time" name="time" data-i18n-lang lang="th" data-i18n-title="form_time_hint" title="ชั่วโมง:นาที" />
                  <p class="form-field-hint" data-i18n="form_time_hint">ชั่วโมง:นาที</p>
                </{d}>
              </{d}>
              <{d} class="form-row">
                <label for="message" data-i18n="form_message">รายละเอียดเพิ่มเติม</label>
                <textarea id="message" name="message" data-i18n-placeholder="form_message_ph" rows="3" placeholder="เล่าความกังวลหรือเคสที่เคยปรึกษามา"></textarea>
              </{d}>
              <p class="form-note" data-i18n="form_note">* เจ้าหน้าที่จะติดต่อกลับเพื่อยืนยันนัดหมาย — ข้อมูลของคุณเป็นความลับ</p>
              <button type="submit" class="btn btn-primary btn-block" data-i18n="form_submit">ส่งคำขอนัดปรึกษา</button>
              <p class="form-success" id="form-success" data-i18n="form_success" hidden role="status">ขอบคุณค่ะ/ครับ เราได้รับข้อมูลแล้ว จะติดต่อกลับโดยเร็วที่สุด</p>
            </form>
          </{d}>
        </{d}>
      </{d}>
    </section>

"""
path.write_text(text[:start] + new + text[end:], encoding="utf-8")
print("patched contact section")
