# rewording

تحوّل طلبك الخام إلى برومت جاهز للسطح المناسب في Claude، مع الموديل والجهد والإعدادات المقترحة. تكتب البرومت فقط ولا تنفذ المهمة، ولا تعمل إلا عندما تستدعيها.

## التثبيت في claude.ai أو تطبيق Claude

Customize ثم Plugins ثم Add ثم Add marketplace ثم Add from a repository، واكتب `HMUSEY/rewording`، ثم ثبّت **rewording** فقط.

بديل بلا GitHub: Customize ثم Plugins ثم Add ثم Upload plugin واختر `rewording-plugin.zip`.

## التثبيت في Claude Code

```
/plugin marketplace add HMUSEY/rewording
/plugin install rewording@hmusey
/plugin install rewording-guard@hmusey
```

الثاني اختياري، ويضيف فحصا محليا للحجم والأسرار قبل كل استدعاء. يحتاج Python 3.

## الاستخدام

اكتب `/` واختر rewording ثم اكتب طلبك. في Claude Code: `/rewording:rewording طلبك`.

## محتوى المستودع

- `plugins/rewording/` الأداة نفسها، ملفات Markdown فقط.
- `plugins/rewording-guard/` إضافة Claude Code للفحص المحلي.
- `tools/` أدوات صيانة تشغّلها يدويا: مقارنة صفحات التوثيق الرسمية، الاختبارات، أمر API بمفتاحك، وبناء ملفات ZIP.
- `docs/instructions.md` متطلبات النظام.
