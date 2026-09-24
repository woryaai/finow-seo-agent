# Finow — Astro + Tailwind

نسخه بازنویسی‌شده وب‌سایت Finow بر پایه **Astro 7** و **Tailwind CSS 4**.

## اجرا

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

خروجی production در `dist/` ساخته می‌شود. `build.format = "file"` عمداً فعال است تا URLهای فعلی مانند `/pages/about.html` بدون تغییر باقی بمانند.

## ساختار

- `src/pages/` — Routeهای Astro
- `src/layouts/BaseLayout.astro` — Layout اصلی
- `src/components/` — Header، Footer، Mobile nav و Loader
- `src/styles/global.css` — Tailwind + design layer فاینو
- `public/assets/` — تصاویر، ویدیو و JS تعاملی
- `scripts/` — ابزارهای build/QA محیط پروژه

## مهاجرت

- Bootstrap CSS/JS حذف شده است.
- Tailwind v4 از Vite plugin رسمی استفاده می‌کند.
- Header/Footer/Mobile navigation به کامپوننت‌های Astro منتقل شده‌اند.
- ۳۵ route فعلی و URLهای `.html` حفظ شده‌اند.
- رفتار modal/offcanvas/collapse/carousel با یک runtime سبک بدون Bootstrap حفظ شده است.

## GitHub connector note

فایل‌های متنی سورس در `source-payload/` به‌صورت gzip+base64 نگهداری شده‌اند تا محدودیت انتقال فایل باینری connector دور زده شود. برای بازسازی فایل‌های متنی پروژه در همین پوشه اجرا کنید:

```bash
node restore-source.mjs
```

دارایی‌های باینری (WEBP/AVIF/MP4) در ZIP کامل سورس تحویلی داخل ChatGPT قرار دارند.
