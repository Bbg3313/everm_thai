# -*- coding: utf-8 -*-
"""Generate privacy.html from EVERM official policy text."""
from pathlib import Path

HEADER = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="에버엠치과의원 개인정보 처리방침" />
  <title>개인정보 처리방침 | 에버엠치과의원</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body class="legal-page lang-ko">
  <a class="skip-link" href="#main">본문으로 건너뛰기</a>
  <header class="site-header scrolled" id="top">
    <div class="header-inner header-inner--legal">
      <a href="index.html" class="logo">
        <img src="images/logo.svg" alt="EVERM Surgery Clinic" class="logo-img" width="1000" height="333" decoding="async" />
      </a>
      <nav class="legal-header-nav" aria-label="법적 고지">
        <a href="index.html" class="btn btn-ghost btn-sm">홈으로</a>
        <a href="index.html#contact" class="btn btn-primary btn-sm">상담 예약</a>
      </nav>
    </div>
  </header>
  <main id="main" class="legal-main">
    <div class="container">
      <header class="legal-hero">
        <p class="section-label">EVERM Dental Clinic Privacy</p>
        <h1>에버엠치과 개인정보 처리방침</h1>
        <p class="legal-hero__source">본 방침은 <a href="https://www.everm.net/privacy/" target="_blank" rel="noopener noreferrer">에버엠치과 공식 홈페이지</a>의 개인정보처리방침과 동일한 내용입니다.</p>
      </header>
      <article class="legal-doc">
"""

FOOTER = """
      </article>
    </div>
  </main>
  <footer class="site-footer" id="footer">
    <div class="container footer-top">
      <div class="footer-brand-block">
        <a href="index.html" class="logo logo-footer">
          <img src="images/logo-footer.svg" alt="EVERM Surgery Clinic" class="logo-img" width="1000" height="333" decoding="async" />
        </a>
        <p class="footer-tagline">안면윤곽·악안면 수술 전문</p>
      </div>
      <div class="footer-contact-block">
        <h4>클리닉 정보</h4>
        <dl class="footer-info">
          <div>
            <dt>상호</dt>
            <dd>에버엠치과의원 <span lang="en">(EverM Dental Clinic)</span></dd>
          </div>
          <div>
            <dt>주소</dt>
            <dd><address>서울특별시 강남구 학동로3길 2 EVERM빌딩</address></dd>
          </div>
          <div>
            <dt>대표·문의 전화</dt>
            <dd><a href="tel:+8225408275">+82 2-540-8275</a></dd>
          </div>
          <div>
            <dt>이메일</dt>
            <dd><a href="mailto:bbghmcollab@gmail.com">bbghmcollab@gmail.com</a></dd>
          </div>
          <div>
            <dt>진료 시간</dt>
            <dd>평일 AM 10:00 ~ PM 07:00<br>토요일 AM 10:00 ~ PM 04:00<br>일요일, 공휴일은 휴진입니다.</dd>
          </div>
        </dl>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>© 2026 에버엠치과의원. All rights reserved.</p>
        <p class="legal-footer-links"><a href="privacy.html" aria-current="page">개인정보처리방침</a><span aria-hidden="true"> · </span><a href="terms.html">이용약관</a></p>
      </div>
    </div>
  </footer>
  <script src="js/main.js"></script>
</body>
</html>
"""

INTRO = """
        <div class="legal-intro">
          <p><strong>에버엠치과</strong> (이하 ‘본원’이라 합니다)는 인터넷 상에서의 개인정보 보호를 매우 중요하게 생각하고 있으며, 이용자가 본원을 이용함에 있어서 본원에게 제공한 개인정보가 보호받을 수 있도록 최선을 다하고 있습니다.</p>
          <p>이에 따라, 본원은 통신비밀보호법, 전기통신사업법, 정보통신망이용촉진 등에 관한 법률 등 정보통신 서비스 제공자가 준수하여야 할 관련 법규를 바탕으로 개인정보 보호정책을 만들어 이를 준수해 나가고 있습니다.</p>
          <p>본 개인정보처리방침은 정부의 법률 및 지침 변경이나 본원의 내부방침 변경 등으로 인하여 수시로 변경될 수 있으며, 본원은 변경사항이 있을 경우 즉시 관련 내용을 홈페이지 초기 화면에 게시된 개인정보처리방침에 반영하고 있습니다.</p>
          <p>본 개인정보처리방침을 통하여 이용자는 수집된 개인정보가 어떠한 용도와 방식으로 이용되고 있으며 어떻게 안전하게 보호되고 있는지 이해하실 수 있을 것입니다.</p>
          <p>마케팅 정보 수신에 동의하시는 분께 개인정보 보호법 및 정보통신망 이용촉진 및 정보보호 등에 관한 법률에 따라 수집하는 개인정보의 항목 및 수집방법, 개인정보의 수집 및 이용목적, 개인정보의 보유 및 이용기간 및 동의 거부 시 불이익을 안내 드리오니 자세히 읽은 후 동의하여 주시기 바랍니다.</p>
        </div>
        <nav class="legal-toc" aria-label="목차">
          <h2 class="legal-toc__title">목차</h2>
          <ol>
            <li><a href="#section-1">수집하는 개인정보의 항목 및 수집방법</a></li>
            <li><a href="#section-2">개인정보 및 마케팅 광고 활용의 수집 및 이용목적</a></li>
            <li><a href="#section-3">개인정보 제공 및 공유</a></li>
            <li><a href="#section-4">개인정보처리(취급) 업무의 위탁</a></li>
            <li><a href="#section-5">개인정보의 보유 및 이용기간</a></li>
            <li><a href="#section-6">개인정보의 파기절차 및 그 방법</a></li>
            <li><a href="#section-7">이용자 및 법정대리인의 권리와 그 행사방법</a></li>
            <li><a href="#section-8">동의철회 / 회원탈퇴 방법</a></li>
            <li><a href="#section-9">개인정보 자동 수집 장치의 설치/운영 및 그 거부에 관한 사항</a></li>
            <li><a href="#section-10">개인정보의 안전성 확보조치에 관한 사항</a></li>
            <li><a href="#section-11">영상정보처리기기 운영/관리에 관한 사항</a></li>
            <li><a href="#section-12">개인정보관리책임자</a></li>
            <li><a href="#section-13">정책 변경에 따른 공지의무</a></li>
          </ol>
        </nav>
"""

SECTIONS = [
  ("section-1", "1. 수집하는 개인정보의 항목 및 수집방법", """
        <p>본원은 회원가입 시 서비스 이용을 위해 필요한 최소한의 개인정보만을 수집합니다. 본원의 개인정보 수집항목은 아래와 같습니다. 필수항목과 선택항목이 있는데, 선택항목은 입력하지 않더라도 서비스 이용에는 제한이 없습니다.</p>
        <h3>가. 진료 시 수집항목</h3>
        <ul>
          <li><strong>필수항목</strong> 이름, 주민등록번호, 주소, 전화번호, 휴대폰번호, 이메일. 외국인등록번호(외국인에 한함)</li>
          <li><strong>건강정보</strong> 병력, 가족력 등 진료서비스 제공을 위하여 의료진이 필요하다고 판단되는 개인정보</li>
        </ul>
        <p class="legal-note">※ 의료법에 의해 고유식별정보 및 진료정보를 의무적으로 보유하여야 합니다. (진료정보 수집에 대하여는 별도의 동의를 받지 않습니다.)</p>
        <h3>나. 홈페이지 회원가입 시 수집항목</h3>
        <ul>
          <li><strong>필수항목</strong> 아이디, 비밀번호, 이름, 휴대폰번호, 이메일</li>
          <li><strong>선택항목</strong> SMS 수신여부, 이메일 수신여부</li>
          <li><strong>민감정보사항</strong> 과거병력, 수술이력, 관심수술분야</li>
          <li>서비스 이용 과정이나 서비스 제공 업무 처리 과정에서 다음과 같은 정보들이 자동으로 생성되어 수집될 수 있습니다: 서비스 이용기록, 접속 로그, 쿠키, 접속 IP 정보</li>
        </ul>
        <h3>다. 진료비 수납 시 수집항목</h3>
        <p>신용카드 결제 시 카드사명, 카드번호 등 결제 승인정보</p>
        <h3>라. 개인정보 수집방법</h3>
        <p>다음과 같은 방법으로 개인정보를 수집합니다.<br>홈페이지(회원가입, 수술비용상담, 카카오톡 상담, 실시간 상담, 온라인 예약, 온라인 상담, 리얼후기, 빠른상담 등), 서면양식, 팩스, 전화, 이메일</p>
  """),
  ("section-2", "2. 개인정보 및 마케팅 광고 활용의 수집 및 이용목적", """
        <p>본원은 수집한 개인정보를 다음의 목적을 위해 활용합니다. 이용자가 제공한 모든 정보는 하기 목적에 필요한 용도 이외로는 사용되지 않으며 이용 목적이 변경될 시에는 사전 동의를 구할 것입니다.</p>
        <ul>
          <li>진단 및 치료를 위한 진료서비스 제공</li>
          <li>진료비 청구, 수납, 환급 등 진료지원을 위한 자료</li>
          <li>제증명서 발송, 검진 관련 물품 발송</li>
          <li>교육, 연구, 진료서비스에 필요한 최소한의 분석 자료</li>
          <li>온라인수탁검사 및 임상시험심사를 위한 기초 자료</li>
          <li>건강 컨텐츠 및 임상연구정보 제공</li>
          <li>진료예약, 예약조회, 등 홈페이지 회원제 서비스 제공</li>
          <li>서비스 이용에 대한 통계</li>
          <li>고지사항 전달, 불만처리 등을 위한 의사소통 경로로 이용</li>
          <li>온라인 상담 답변 처리를 위한 자료</li>
          <li>새로운 서비스 및 행사정보 안내 제공</li>
          <li>신규 서비스 개발과 개인 맞춤 서비스 제공을 위한 자료</li>
          <li>소비자 기본법 제 54조에 의거한 소비자 위해 정보 수집</li>
          <li>설문조사, 행사 등의 서비스 제공</li>
        </ul>
        <p><strong>마케팅 및 광고에 활용:</strong> 새로운 서비스, 이벤트 정보 등 최신 정보의 안내, 인구통계학적 특성에 따른 서비스 제공 및 광고 게재, 접속 빈도 파악, 서비스 이용 분석 및 통계, 서비스품질 향상을 위한 각종 설문조사, 회원 유형 및 관심분야 등에 따른 맞춤서비스 제공, 이벤트 운영</p>
  """),
  ("section-3", "3. 개인정보 제공 및 공유", """
        <p>본원은 귀하의 동의가 있거나 관련법령의 규정에 의한 경우를 제외하고는 어떠한 경우에도 『개인정보의 수집 및 이용목적』에서 고지한 범위를 넘어 귀하의 개인정보를 이용하거나 타인 또는 타기업·기관에 제공하지 않습니다. 다만, 아래의 경우에는 예외로 합니다.</p>
        <ul>
          <li>이용자들이 사전에 공개에 동의한 경우</li>
          <li>법령의 규정에 의거하거나, 수사 목적으로 법령에 정해진 절차와 방법에 따라 수사기관의 요구가 있는 경우</li>
          <li>통계작성·학술연구 또는 시장조사를 위하여 필요한 경우로서 특정 개인을 알아볼 수 없는 형태로 가공하여 제공하는 경우</li>
        </ul>
  """),
  ("section-4", "4. 개인정보처리(취급) 업무의 위탁", """
        <p>본원은 보다 나은 서비스 제공, 고객편의 제공 등 원활한 업무 수행을 위하여 다음과 같이 개인정보 처리(취급) 업무를 외부 전문업체에 위탁하여 운영하고 있습니다.</p>
        <div class="legal-table-wrap">
          <table class="legal-table">
            <thead>
              <tr>
                <th scope="col">수탁사</th>
                <th scope="col">위탁 업무의 내용</th>
                <th scope="col">위탁개인정보</th>
                <th scope="col">개인정보 보유기간</th>
                <th scope="col">연락처</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>크로스디자인</td>
                <td>홈페이지 개발 및 운영</td>
                <td>성명, 이메일, 전화번호</td>
                <td>위탁계약 종료시까지</td>
                <td>070-8676-0090</td>
              </tr>
              <tr>
                <td>i-PRO</td>
                <td>전자차트 개발 및 운영</td>
                <td>성명, 주민번호, 주소, 연락처, 이메일</td>
                <td>위탁계약 종료시까지</td>
                <td>02-575-2882</td>
              </tr>
              <tr>
                <td>한국필의료재단</td>
                <td>혈액검사</td>
                <td>성명, 생년월일, 성별</td>
                <td>위탁계약 종료시까지</td>
                <td>02-517-1728</td>
              </tr>
            </tbody>
          </table>
        </div>
  """),
  ("section-5", "5. 개인정보의 보유 및 이용기간", """
        <p>본원은 개인정보의 수집목적 또는 제공받은 목적이 달성된 때에는 귀하의 개인정보를 지체 없이 파기합니다.</p>
        <ul>
          <li><strong>회원가입정보의 경우:</strong> 회원가입을 탈퇴하거나 회원에서 제명된 때, 최종 로그인 날짜로부터 1년을 경과한 경우(정보통신망 이용촉진 및 정보보호 등에 관한 법률 제29조 및 동법 시행령 제 16조)</li>
          <li><strong>설문조사, 행사 등의 목적을 위하여 수집한 경우:</strong> 당해 설문조사, 행사 등이 종료한 때</li>
          <li><strong>진료목적을 위하여 수집한 경우:</strong> 『의료법』시행규칙 제15조 “진료에 관한 기록의 보존”에 명시된 기간에 준하여 보존 (환자 명부: 5년, 진료기록부: 10년), (보존 항목: 성명, 주소, 진료정보)</li>
          <li><strong>소비자의 불만 또는 분쟁처리에 관한 기록:</strong> 3년 (전자상거래 등에서의 소비자보호에 관한 법률)</li>
          <li><strong>신용정보의 수집/처리 및 이용 등에 관한 정보의 경우:</strong> 신용정보의 이용 및 보호에 관한 법률에 따라 3년간 보존 (보존 항목: 카드사명, 카드번호 등 카드결제 승인 정보)</li>
          <li><strong>본인 확인에 관한 기록:</strong> 6개월 (정보통신망 이용촉진 및 정보보호 등에 관한 법률)</li>
          <li><strong>방문에 관한 기록:</strong> 3개월 (통신비밀보호법)</li>
          <li><strong>마케팅 및 광고에 활용:</strong> 회원 탈퇴 시, 보유기간 만료 시(개인정보 수집 및 마케팅,광고 활용 동의 시 정한 바에 따름) 또는 맞춤형 광고 제공을 위해 자동으로 생성된 정보의 경우 쿠키 수집시부터 최대 2년간 보관 후 파기). 단, 기타 회원 자격 및 이벤트 제한 사유 발생 시 회원 탈퇴 시 또는 보유기간 도과 시부터 6개월 간 보관 후 파기.</li>
        </ul>
        <p>다만, 수집목적 또는 제공받은 목적이 달성된 경우에도 상법 등 법령의 규정에 의하여 보존할 필요성이 있는 경우에는 귀하의 개인정보를 보유할 수 있습니다.</p>
  """),
  ("section-6", "6. 개인정보의 파기절차 및 그 방법", """
        <ul>
          <li><strong>파기절차</strong> 이용자가 회원가입 등을 위해 입력한 정보는 목적이 달성된 후 이하 파기방법에 의하여 즉시 파기합니다.</li>
          <li><strong>파기기한</strong> 이용자의 개인정보는 개인정보의 보유기간이 경과된 경우에는 보유기간의 종료일로부터 5일 이내에, 개인정보의 처리 목적 달성, 해당 서비스의 폐지, 사업의 종료 등 그 개인정보가 불필요하게 되었을 때에는 개인정보의 처리가 불필요한 것으로 인정되는 날로부터 5일 이내에 그 개인정보를 파기합니다.</li>
          <li><strong>파기방법</strong> 전자적 파일형태로 저장된 개인정보는 기록을 재생할 수 없는 기술적 방법을 사용하여 삭제합니다. 종이에 출력된 개인정보는 분쇄기로 분쇄하거나 소각하여 파기합니다.</li>
        </ul>
  """),
  ("section-7", "7. 이용자 및 법정대리인의 권리와 그 행사방법", """
        <p>본원은 고객이 개인정보에 대한 열람, 정정 및 삭제를 요구하는 경우에는 고객의 요구에 성실하게 응대하고, 지체 없이 처리합니다. 개인정보를 보호하기 위하여 고객의 방문 이외의 전화, 우편, FAX 등 기타 신청방법에 의한 고객의 개인정보의 열람, 정정 및 삭제 절차는 제공하지 않습니다.</p>
        <h3>가. 개인정보의 열람</h3>
        <p>고객은 본원을 방문하여 개인정보의 열람을 요구할 수 있으며, 신속하게 이에 대하여 응대합니다.</p>
        <h3>나. 개인정보의 정정/삭제</h3>
        <ul>
          <li>본원은 고객이 개인정보에 대한 정정/삭제를 요구하는 경우, 개인정보에 오류가 있다고 판명되는 등 정정·삭제를 할 필요가 있다고 인정되는 경우에는 지체 없이 정정/삭제를 합니다.</li>
          <li>고객이 본인의 개인정보에 대한 열람, 정정 및 삭제를 요구하는 경우, 고객의 신분을 나타내는 주민등록증, 여권, 운전면허증 등의 신분증명서를 제시 받아 본인 여부를 확인합니다.</li>
          <li>고객의 대리인이 방문하여 열람, 정정 및 삭제를 요구하는 경우에는 고객의 위임장 및 동의서와 대리인의 신분증명서 등을 확인하여 정당한 대리인인지 여부를 확인합니다.</li>
        </ul>
        <p class="legal-note">※ 법에 의해 보관이 의무화된 개인정보는 요청이 있더라도 보관기간 내에 수정/삭제할 수 없습니다.</p>
  """),
  ("section-8", "8. 동의철회 / 회원탈퇴 방법", """
        <p>귀하는 회원가입 시 개인정보의 수집·이용 및 제공에 대해 동의하신 내용을 언제든지 철회하실 수 있습니다. 동의철회(회원탈퇴)는 홈페이지 내의 『회원탈퇴』을 클릭하여 본인 확인 절차를 거치신 후 직접 동의철회(회원탈퇴)를 하시거나, 개인정보담당자에게 연락하시면 지체 없이 귀하의 개인정보를 파기하는 등 필요한 조치를 하겠습니다.</p>
  """),
  ("section-9", "9. 개인정보 자동 수집 장치의 설치/운영 및 그 거부에 관한 사항", """
        <p>본원은 이용자들에게 특화된 맞춤서비스를 제공하기 위해서 이용자들의 정보를 저장하고 수시로 불러오는 ‘쿠키(cookie)’를 사용합니다. 쿠키는 웹사이트가 이용자의 컴퓨터 웹 브라우저로 전송하는 소량의 정보로 PC 하드디스크에 저장되기도 합니다.</p>
        <h3>가. 쿠키의 사용 목적</h3>
        <ul>
          <li>쿠키는 이용자의 컴퓨터를 식별하지만 이용자 개개인을 개별적으로 식별하지는 않습니다.</li>
          <li>이용자들은 웹 브라우저의 옵션을 조정하여 쿠키에 대한 사용 여부를 선택하실 수 있습니다.</li>
          <li>다만, 이용자들은 본원에 접속한 후 로그인(LOG-IN)하여 서비스를 이용하기 위해서는 쿠키를 허용하여야 합니다.</li>
        </ul>
        <h3>나. 쿠키의 설치/운영 및 거부</h3>
        <ul>
          <li>Internet Explorer: 도구 메뉴 &gt; 인터넷 옵션 &gt; 개인정보 &gt; 설정</li>
          <li>Chrome: 설정 메뉴 &gt; 고급 설정 &gt; 개인정보의 콘텐츠 설정 &gt; 쿠키</li>
        </ul>
      """),
  ("section-10", "10. 개인정보의 안전성 확보조치에 관한 사항", """
        <ul>
          <li><strong>개인정보 취급 직원의 최소화 및 교육</strong> — 개인정보취급자의 지정을 최소화하고 정기적인 교육을 시행하고 있습니다.</li>
          <li><strong>정기적인 자체 점검 실시</strong> — 연 1회 이상 정기적으로 자체점검을 실시하고 있습니다.</li>
          <li><strong>내부관리계획의 수립 및 시행</strong></li>
          <li><strong>개인정보의 암호화</strong></li>
          <li><strong>해킹 등에 대비한 기술적 대책</strong></li>
          <li><strong>개인정보에 대한 접근 제한</strong></li>
          <li><strong>비인가자에 대한 출입 통제</strong></li>
        </ul>
  """),
  ("section-11", "11. 영상정보처리기기 운영/관리에 관한 사항", """
        <ul>
          <li><strong>설치 근거 및 설치 목적:</strong> 환자 및 시설안전, 화재 및 범죄 예방</li>
          <li><strong>설치 대수, 설치 위치 및 촬영범위:</strong> 총 24대 — 로비, 복도, 상담실, 진료실 등</li>
          <li><strong>관리책임자:</strong> 김종안 대리 / 02-540-8275 / evermdental@naver.com</li>
          <li><strong>영상정보의 촬영시간, 처리방법:</strong> 24시간 촬영, 보관기간 만료 시 영구 삭제</li>
        </ul>
  """),
  ("section-12", "12. 개인정보관리책임자", """
        <p>귀하의 개인정보를 보호하고 개인정보와 관련한 불만을 처리하기 위하여 본원은 아래와 같이 개인정보관리책임자를 두고 있습니다.</p>
        <ul>
          <li>개인분쟁조정위원회 (<a href="http://www.1336.or.kr" target="_blank" rel="noopener noreferrer">www.1336.or.kr</a> / 1336)</li>
          <li>대검찰청 사이버범죄수사단 (<a href="http://www.spo.go.kr" target="_blank" rel="noopener noreferrer">www.spo.go.kr</a> / 02-3480-3573)</li>
          <li>경찰청 사이버테러대응센터 (<a href="http://www.ctrc.go.kr" target="_blank" rel="noopener noreferrer">www.ctrc.go.kr</a> / 02-392-0330)</li>
        </ul>
        <h3>가. 개인정보 관리책임자</h3>
        <p>관리책임자: 김종안 · 소속: 에버엠치과 · 직위: 대리</p>
        <h3>나. 개인정보 취급담당자</h3>
        <p>취급담당자: 최지유 · 소속: 에버엠치과 · 직위: 실장</p>
  """),
  ("section-13", "13. 정책 변경에 따른 공지의무", """
        <p>이 개인정보처리방침은 2014년 11월 17일에 제정되었으며 법령·정책 또는 보안기술의 변경에 따라 내용의 추가·삭제 및 수정이 있을 시에는 변경되는 개인정보처리방침을 시행하기 최소 7일전에 본원 홈페이지를 통해 변경이유 및 내용 등을 공지하도록 하겠습니다.</p>
        <p class="legal-dates"><strong>공고일자:</strong> 2014년 11월 17일<br><strong>시행일자:</strong> 2014년 11월 19일</p>
  """),
]

def main():
    parts = [HEADER, INTRO]
    for sid, title, body in SECTIONS:
        parts.append(f'        <section class="legal-section" id="{sid}">\n')
        parts.append(f'          <h2>{title}</h2>\n')
        parts.append(body)
        parts.append('        </section>\n')
    parts.append(FOOTER)
    out = Path(__file__).resolve().parent.parent / "privacy.html"
    out.write_text("".join(parts), encoding="utf-8")
    print("Wrote", out)

if __name__ == "__main__":
    main()
