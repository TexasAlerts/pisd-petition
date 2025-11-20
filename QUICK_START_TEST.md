# 🚀 QUICK START: Test Your Enhanced Petition Form

## 1️⃣ Open the Form (10 seconds)
```bash
open /Users/dougcharles/Projects/pisd-petition/index.html
```
OR: Double-click `index.html` in Finder

---

## 2️⃣ Fill Out Test Data (1 minute)

**Name:** Doug Charles Test  
**Email:** test@example.com  
**Phone:** 9725551234  
☑️ **SMS Opt-In:** [CHECK THE BOX]  
**Street:** 123 Test Lane  
**City:** Prosper  
**State:** TX  
**ZIP:** 75078  
**Voter Type:** Prosper ISD Voter (NOT in Windsong Ranch)

---

## 3️⃣ Submit and Watch (30 seconds)

1. Click "✉️ Email Both Boards Now"
2. Watch your browser status message
3. Your email client should open
4. **Check your Google Sheet** for the new row

---

## 4️⃣ Verify Google Sheet Has New Data

**Open your sheet:**
https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE

**Check for these NEW columns:**
- Column D: **Phone** = "9725551234"
- Column E: **SMS Opt-In** = "Yes"

If you see those columns with data → ✅ **SUCCESS!**

---

## 5️⃣ Deploy to Production (5 minutes)

### If using flow.page:
1. Log into flow.page
2. Edit your pisdannexation page
3. Replace the form HTML with your updated version
4. Save and publish

### If using a custom domain:
1. Upload `index.html` to your web host
2. Replace the old file at prosperisdpetition.com
3. Clear your browser cache (Cmd+Shift+R)
4. Test the live site

---

## 🎯 WHAT YOU'LL SEE

### Phone Number Auto-Formats:
- Type: `9725551234`
- See: `(972) 555-1234`

### SMS Checkbox:
- Blue background box
- "📲 Yes, send me SMS updates about the petition"
- Helper text about message rates

### After Submit:
- ✅ Success message
- Email client opens
- Data in Google Sheet with phone/SMS

---

## 🐛 TROUBLESHOOTING

**Email client doesn't open?**
→ Use the "Copy & Paste" option below the form

**No data in Google Sheet?**
→ Check that you deployed the Apps Script correctly
→ Verify the URL in `index.html` matches your deployment URL

**Phone validation error?**
→ Phone must be exactly 10 digits
→ Remove all formatting, just type numbers: 9725551234

**SMS checkbox not showing?**
→ Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

---

## 📞 SMS CAMPAIGN PREVIEW

Once you have 50+ phone opt-ins:

```
Hi! Doug from PISD petition. 🎯 URGENT: Board meets Dec 15 at 7 PM. 
We need YOU there! Reply YES to confirm. Reply STOP to unsubscribe.
```

---

**Need Help?** Check `PHONE_SMS_ENHANCEMENT.md` for full documentation
