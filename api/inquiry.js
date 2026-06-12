/**
 * POST /api/inquiry — sends consultation form to company inbox via Resend.
 *
 * Vercel env:
 *   RESEND_API_KEY      — https://resend.com API key
 *   INQUIRY_TO_EMAIL    — recipient (default: info@bluebridge-global.com)
 *   INQUIRY_FROM_EMAIL  — sender, e.g. "EVERM <onboarding@resend.dev>"
 */

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

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
  const service = String(payload.service || "").trim();
  const date = String(payload.date || "").trim();
  const time = String(payload.time || "").trim();
  const message = String(payload.message || "").trim();
  const lang = String(payload.lang || "").trim();

  if (!name || !phone || !lineId || !service) {
    return res.status(400).json({ ok: false, error: "missing_fields" });
  }

  const subject = `[EVERM 상담 문의] ${name} — ${service}`;
  const html = `
    <h2>에버엠치과 웹사이트 상담 문의</h2>
    <table cellpadding="8" cellspacing="0" style="border-collapse:collapse;font-family:sans-serif;font-size:14px;">
      <tr><td><strong>이름</strong></td><td>${escapeHtml(name)}</td></tr>
      <tr><td><strong>전화번호</strong></td><td>${escapeHtml(phone)}</td></tr>
      <tr><td><strong>LINE ID</strong></td><td>${escapeHtml(lineId)}</td></tr>
      <tr><td><strong>관심 진료</strong></td><td>${escapeHtml(service)}</td></tr>
      <tr><td><strong>희망 날짜</strong></td><td>${escapeHtml(date || "—")}</td></tr>
      <tr><td><strong>희망 시간</strong></td><td>${escapeHtml(time || "—")}</td></tr>
      <tr><td><strong>언어</strong></td><td>${escapeHtml(lang || "—")}</td></tr>
    </table>
    <h3>추가 메모</h3>
    <p style="white-space:pre-wrap;">${escapeHtml(message || "—")}</p>
    <hr />
    <p style="color:#666;font-size:12px;">전송 시각: ${new Date().toISOString()}</p>
  `;

  const text = [
    "에버엠치과 웹사이트 상담 문의",
    "",
    `이름: ${name}`,
    `전화번호: ${phone}`,
    `LINE ID: ${lineId}`,
    `관심 진료: ${service}`,
    `희망 날짜: ${date || "—"}`,
    `희망 시간: ${time || "—"}`,
    `언어: ${lang || "—"}`,
    "",
    "추가 메모:",
    message || "—",
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
    console.error("Inquiry API error:", err);
    return res.status(500).json({ ok: false, error: "server_error" });
  }
}
