/**
 * POST /api/meta-consult — Meta ads pre-screening form (Resend email).
 *
 * Vercel env: RESEND_API_KEY, INQUIRY_TO_EMAIL, INQUIRY_FROM_EMAIL
 */

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

const MALOCCLUSION_LABELS = {
  yes: { th: "มี / เคยจัดฟัน", en: "Yes / orthodontic history" },
  no: { th: "ไม่มี", en: "No" },
  unsure: { th: "ไม่แน่ใจ", en: "Not sure" },
};

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ ok: false, error: "method_not_allowed" });
  }

  const apiKey = process.env.RESEND_API_KEY;
  const toEmail = process.env.INQUIRY_TO_EMAIL || "info@bluebridge-global.com";
  const fromEmail = process.env.INQUIRY_FROM_EMAIL || "EVERM Website <onboarding@resend.dev>";

  if (!apiKey) {
    return res.status(503).json({ ok: false, error: "not_configured" });
  }

  let payload = req.body;
  if (typeof payload === "string") {
    try {
      payload = JSON.parse(payload);
    } catch {
      return res.status(400).json({ ok: false, error: "invalid_json" });
    }
  }

  if (!payload || typeof payload !== "object") {
    return res.status(400).json({ ok: false, error: "invalid_body" });
  }

  if (payload.website) {
    return res.status(200).json({ ok: true });
  }

  const name = String(payload.name || "").trim();
  const phone = String(payload.phone || "").trim();
  const lineId = String(payload.line_id || "").trim();
  const concern = String(payload.concern || "").trim();
  const surgeryHistory = String(payload.surgery_history || "").trim();
  const surgeryDate = String(payload.surgery_date || "").trim();
  const malocclusion = String(payload.malocclusion || "").trim();
  const malocclusionDetails = String(payload.malocclusion_details || "").trim();
  const lang = String(payload.lang || "th").trim();
  const utmSource = String(payload.utm_source || "").trim();
  const utmCampaign = String(payload.utm_campaign || "").trim();
  const utmMedium = String(payload.utm_medium || "").trim();
  const fbclid = String(payload.fbclid || "").trim();

  if (!name || !phone || !lineId) {
    return res.status(400).json({ ok: false, error: "missing_contact" });
  }

  if (!concern || !surgeryHistory || !surgeryDate || !malocclusion) {
    return res.status(400).json({ ok: false, error: "missing_fields" });
  }

  if (!["yes", "no", "unsure"].includes(malocclusion)) {
    return res.status(400).json({ ok: false, error: "invalid_malocclusion" });
  }

  const maloLabel =
    (MALOCCLUSION_LABELS[malocclusion] && MALOCCLUSION_LABELS[malocclusion][lang === "en" ? "en" : "th"]) ||
    malocclusion;

  const subject = `[EVERM Meta 상담] ${name} — ${surgeryDate}`;
  const html = `
    <h2>EVERM Meta Ads Pre-Screening</h2>
    <p style="color:#666;font-size:13px;">Source: /consult landing page</p>
    <table cellpadding="8" cellspacing="0" style="border-collapse:collapse;font-family:sans-serif;font-size:14px;">
      <tr><td><strong>이름</strong></td><td>${escapeHtml(name)}</td></tr>
      <tr><td><strong>전화번호</strong></td><td>${escapeHtml(phone)}</td></tr>
      <tr><td><strong>LINE ID</strong></td><td>${escapeHtml(lineId)}</td></tr>
      <tr><td><strong>언어</strong></td><td>${escapeHtml(lang)}</td></tr>
      <tr><td colspan="2" style="padding-top:16px;"><strong>── 사전 문진 ──</strong></td></tr>
      <tr><td><strong>1. 가장 고민인 부분</strong></td><td style="white-space:pre-wrap;">${escapeHtml(concern)}</td></tr>
      <tr><td><strong>2. 수술·상담 이력</strong></td><td style="white-space:pre-wrap;">${escapeHtml(surgeryHistory)}</td></tr>
      <tr><td><strong>3. 수술 예정일</strong></td><td>${escapeHtml(surgeryDate)}</td></tr>
      <tr><td><strong>4. 부정교합·교정 이력</strong></td><td>${escapeHtml(maloLabel)}${malocclusionDetails ? `<br/><span style="color:#555;">${escapeHtml(malocclusionDetails)}</span>` : ""}</td></tr>
      <tr><td colspan="2" style="padding-top:16px;"><strong>── 광고 추적 ──</strong></td></tr>
      <tr><td><strong>utm_source</strong></td><td>${escapeHtml(utmSource || "—")}</td></tr>
      <tr><td><strong>utm_campaign</strong></td><td>${escapeHtml(utmCampaign || "—")}</td></tr>
      <tr><td><strong>utm_medium</strong></td><td>${escapeHtml(utmMedium || "—")}</td></tr>
      <tr><td><strong>fbclid</strong></td><td>${escapeHtml(fbclid || "—")}</td></tr>
    </table>
    <hr />
    <p style="color:#666;font-size:12px;">Submitted: ${new Date().toISOString()}</p>
  `;

  const text = [
    "EVERM Meta Ads Pre-Screening",
    "",
    `이름: ${name}`,
    `전화번호: ${phone}`,
    `LINE ID: ${lineId}`,
    `언어: ${lang}`,
    "",
    "1. 가장 고민인 부분:",
    concern,
    "",
    "2. 수술·상담 이력:",
    surgeryHistory,
    "",
    `3. 수술 예정일: ${surgeryDate}`,
    "",
    `4. 부정교합·교정 이력: ${maloLabel}`,
    malocclusionDetails || "",
    "",
    `utm_source: ${utmSource || "—"}`,
    `utm_campaign: ${utmCampaign || "—"}`,
    `utm_medium: ${utmMedium || "—"}`,
    `fbclid: ${fbclid || "—"}`,
  ].join("\n");

  try {
    const sendRes = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        subject,
        html,
        text,
      }),
    });

    if (!sendRes.ok) {
      console.error("Resend error:", sendRes.status, await sendRes.text());
      return res.status(502).json({ ok: false, error: "send_failed" });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error("Meta consult API error:", err);
    return res.status(500).json({ ok: false, error: "server_error" });
  }
}
