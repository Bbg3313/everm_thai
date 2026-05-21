from pathlib import Path
INDEX = Path(r"c:\Users\MSI\Desktop\에버엠_태국\index.html")
MARKER = "    <section class=\"section services\" id=\"services\""
tag = "di" + "v"
open_tag = "<" + tag
close_tag = "</" + tag + ">"
section = f"""    <section class=\"section videos\" id=\"videos\" aria-labelledby=\"videos-title\">
      {open_tag} class=\"container\">
        {open_tag} class=\"section-head center\">
          <p class=\"section-label\" data-i18n=\"videos_label\">วิดีโอ</p>
          <h2 id=\"videos-title\" data-i18n=\"videos_title\">ทำความรู้จัก EVERM</h2>
          <p class=\"section-desc\" data-i18n=\"videos_desc\">ภาพรวมความร่วมมือระดับนานาชาติและบรรยากาศของคลินิก</p>
        {close_tag}
        {open_tag} class=\"video-grid\">
          <article class=\"video-card\">
            {open_tag} class=\"video-player\">
              <video
                controls
                playsinline
                preload=\"metadata\"
                data-i18n-aria=\"video1_aria\"
                aria-label=\"K-Orthognathic EVERM Thailand Korea cooperation\"
              >
                <source src=\"videos/everm-thailand-cooperation.mp4\" type=\"video/mp4\" />
              </video>
            {close_tag}
            <h3 data-i18n=\"video1_title\">K-양악 세계가 찾는 에버엠 — ไทย·เกาหลี</h3>
            <p data-i18n=\"video1_desc\">ความร่วมมือระดับโลกเพื่อศัลยกรรมขากรรไกรและโครงหน้า</p>
          </article>
          <article class=\"video-card\">
            {open_tag} class=\"video-player\">
              <video
                controls
                playsinline
                preload=\"metadata\"
                data-i18n-aria=\"video2_aria\"
                aria-label=\"EVERM clinic introduction\"
              >
                <source src=\"videos/everm-ivory.mp4\" type=\"video/mp4\" />
              </video>
            {close_tag}
            <h3 data-i18n=\"video2_title\">EVERM Surgery Clinic</h3>
            <p data-i18n=\"video2_desc\">วิดีโอแนะนำคลินิกและมาตรฐานการดูแล</p>
          </article>
        {close_tag}
      {close_tag}
    </section>

"""
text = INDEX.read_text(encoding="utf-8")
if "id=\"videos\"" in text:
    print("already")
elif MARKER not in text:
    raise SystemExit("marker missing")
else:
    INDEX.write_text(text.replace(MARKER, section + "\n\n" + MARKER, 1), encoding="utf-8")
    print("inserted")
