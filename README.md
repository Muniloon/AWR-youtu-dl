<div dir="rtl" align="right">

<h1 align="center">📥 AWR‑youtube‑dl</h1>
<p align="center">
  <b>دانلودر خودکار ویدیوهای یوتیوب روی گیت‌هاب اَکشنز</b><br>
  <sub>بدون نیاز به VPN یا نرم‌افزار اضافی روی سیستم شما</sub>
</p>

<hr>

<h2>💡 ایده‌ی اصلی</h2>
<p>
  این پروژه بر اساس ساختار اولیه‌ی 
  <a href="https://github.com/nikzad-avasam/downloader"><span dir="ltr">danialbehzadi / downloader</span></a> 
  (تحت لیسانس <span dir="ltr">MIT</span>) شکل گرفته و سپس برای دانلود از یوتیوب، پشتیبانی از 
  <span dir="ltr">V2Ray</span>، کوکی و بهینه‌سازی‌های مختلف توسعه داده شده است.
</p>

<h2>✨ ویژگی‌ها</h2>
<ul>
  <li>🎬 <b>فقط لینک بدهید</b> – گیت‌هاب با اینترنت پرسرعت خود ویدیو را دانلود می‌کند.</li>
  <li>🔐 <b>بدون مصرف حجم فیلترشکن</b> – پروژه از پروکسی <span dir="ltr">V2Ray</span> در سرور گیت‌هاب استفاده می‌کند.</li>
  <li>🔄 <b>فایل نهایی در ریپوزیتوری شما</b> – بعد از اتمام، ویدیو مستقیماً در پوشه‌ی <code dir="ltr">downloads/</code> ذخیره می‌شود.</li>
  <li>🧠 <b>دریافت خودکار کانفیگ‌های عمومی <span dir="ltr">V2Ray</span></b> – هیچ فایل کانفیگ خصوصی داخل پروژه نیست؛ همه چیز از منابع عمومی دریافت می‌شود.</li>
  <li>🍪 <b>پشتیبانی از کوکی اکانت گوگل</b> – برای دور زدن خطای «ربات نیستید» (<span dir="ltr">Sign in to confirm</span>).</li>
  <li>⏱️ <b>نیازی به روشن ماندن سیستم شما نیست</b> – تمام کارها روی سرور گیت‌هاب انجام می‌شود.</li>
</ul>

<h2>📋 پیش‌نیازها</h2>
<ul>
  <li>یک حساب رایگان <a href="https://github.com"><span dir="ltr">github.com</span></a></li>
  <li>حدود ۱۰ دقیقه برای راه‌اندازی اولیه</li>
</ul>

<h2>🚀 راه‌اندازی (فقط یک‌بار)</h2>
<ol>
  <li><b>پروژه را از دکمه</b> <b>Fork</b> <b>بالای صفحه فورک کنید.</b><br>
    <sub>تمامی ابزارهای ضروری (<span dir="ltr">yt‑dlp</span> و <span dir="ltr">sing‑box</span>) از قبل در پوشه‌ی <code dir="ltr">bin/</code> قرار دارند و به‌همراه پروژه فورک می‌شوند.</sub>
  </li>
  <li>
    <b>کوکی یوتیوب را اضافه کنید (اختیاری ولی توصیه اکید)</b><br>
    برای دور زدن خطای «<span dir="ltr">Sign in to confirm you’re not a bot</span>»:
    <ul>
      <li>با مرورگر (Chrome) وارد اکانت گوگل شوید و سری به یوتیوب بزنید.</li>
      <li>افزونه‌ی <b><span dir="ltr">cookies.txt</span></b> را نصب کرده و کوکی‌ها را با فرمت <span dir="ltr">Netscape</span> ذخیره کنید.</li>
      <li>فایل را با یک ویرایشگر متن باز کنید و فقط خطوطی که شامل یکی از نام‌های زیر هستند را نگه دارید (بقیه را پاک کنید):<br>
        <code dir="ltr">SID</code>, <code dir="ltr">HSID</code>, <code dir="ltr">SSID</code>, <code dir="ltr">APISID</code>, <code dir="ltr">SAPISID</code>, <code dir="ltr">__Secure‑1PSID</code>, <code dir="ltr">__Secure‑3PSID</code>, <code dir="ltr">__Secure‑1PAPISID</code>, <code dir="ltr">__Secure‑3PAPISID</code>, <code dir="ltr">LOGIN_INFO</code>, <code dir="ltr">PREF</code>, <code dir="ltr">CONSISTENCY</code>
      </li>
      <li>به <b><span dir="ltr">Settings → Secrets and variables → Actions</span></b> بروید و یک <span dir="ltr">Secret</span> به نام <code dir="ltr">YOUTUBE_COOKIES</code> بسازید، سپس محتوای فایل اصلاح شده را آن‌جا جای‌گذاری کنید.</li>
    </ul>
  </li>
</ol>

<h2>🎬 استفاده (دانلود یک ویدیو)</h2>
<ol>
  <li>به تب <b><span dir="ltr">Actions</span></b> بروید.</li>
  <li>از ستون سمت چپ، <b><span dir="ltr">🎖️Downloader</span></b> را انتخاب کنید.</li>
  <li>روی <b><span dir="ltr">Run workflow</span></b> کلیک کنید.</li>
  <li>در کادر بازشده:
    <ul>
      <li><b><span dir="ltr">video_url</span></b>: لینک کامل ویدیوی یوتیوب</li>
      <li><b><span dir="ltr">quality</span></b>: کیفیت دلخواه (مثلاً <code dir="ltr">720</code>، <code dir="ltr">1080</code>، <code dir="ltr">best</code>) – پیش‌فرض <code dir="ltr">best</code></li>
    </ul>
  </li>
  <li>دکمه‌ی سبز <b><span dir="ltr">Run workflow</span></b> را بزنید.</li>
  <li>بعد از اتمام (✅ سبز)، به پوشه‌ی <code dir="ltr">downloads/</code> در ریشه‌ی پروژه بروید و فایل خود را (احتمالاً به صورت چند بخش) دانلود کنید.</li>
</ol>

<h2>🧹 پاک‌سازی</h2>
<ul>
  <li>برای خالی کردن پوشه‌ی <code dir="ltr">downloads/</code>، Workflow <b><span dir="ltr">Clean Up Downloads</span></b> را اجرا کنید.</li>
</ul>

<h2>🧱 ساختار پروژه</h2>
<table>
  <tr><th>فایل / پوشه</th><th>توضیح</th></tr>
  <tr><td><code dir="ltr">.github/workflows/download.yml</code></td><td>Workflow اصلی دانلود با سه استراتژی + commit خودکار</td></tr>
  <tr><td><code dir="ltr">.github/workflows/cleanup-downloads.yml</code></td><td>پاک‌سازی پوشه‌ی دانلودها</td></tr>
  <tr><td><code dir="ltr">.github/workflows/setup-tools.yml</code></td><td>فقط برای دریافت اولیه‌ی ابزارها (در Fork نیازی نیست)</td></tr>
  <tr><td><code dir="ltr">bin/</code></td><td>فایل‌های اجرایی <code dir="ltr">yt‑dlp</code> و <code dir="ltr">sing‑box</code></td></tr>
  <tr><td><code dir="ltr">scripts/fetch_configs.py</code></td><td>دریافت و ادغام کانفیگ‌های عمومی V2Ray</td></tr>
  <tr><td><code dir="ltr">scripts/add_socks_inbound.py</code></td><td>افزودن inbound socks و راه‌اندازی انتخاب خودکار بهترین سرور</td></tr>
</table>

<h2>❓ پرسش‌های پرتکرار</h2>
<dl>
  <dt><b>۱. آیا حجم فیلترشکن من مصرف می‌شود؟</b></dt>
  <dd>خیر. دانلود و عبور از فیلتر توسط سرور گیت‌هاب انجام می‌شود و شما فقط فایل نهایی را دریافت می‌کنید.</dd>
  <dt><b>۲. چرا باید کوکی اضافه کنم؟</b></dt>
  <dd>یوتیوب گاهی IP گیت‌هاب را ربات تشخیص می‌دهد. کوکی اکانت گوگل این خطا را برطرف می‌کند.</dd>
  <dt><b>۳. محدودیت حجم چیست؟</b></dt>
  <dd>تا حدود ۲ گیگابایت مشکلی نیست. فایل‌های بزرگ‌تر به‌طور خودکار قطعه‌قطعه می‌شوند.</dd>
  <dt><b>۴. آیا باید <code dir="ltr">Setup Tools</code> را اجرا کنم؟</b></dt>
  <dd>اگر از Fork استفاده می‌کنید، نه. ابزارها از قبل در <code dir="ltr">bin/</code> هستند.</dd>
</dl>

<h2>📄 مجوز</h2>
<p>
  این پروژه تحت لیسانس <b><span dir="ltr">MIT</span></b> منتشر شده است.
</p>

</div>
