# 🚀 DEPLOYMENT CHECKLIST - Make It Live!

## ✅ PRE-DEPLOYMENT VERIFICATION

Open the file locally first:
```bash
open /Users/dougcharles/Projects/pisd-petition/index.html
```

### **Check These Features:**

1. **🚨 Countdown Timer**
   - [ ] Red banner visible at top
   - [ ] Siren icon (🚨) has white background
   - [ ] Countdown updates every second
   - [ ] Shows Days, Hours, Minutes, Seconds

2. **📍 Location Section**
   - [ ] Pin drop icon (📍) has white background
   - [ ] Address clearly visible
   - [ ] Google Maps link works
   - [ ] "Get Directions" link works

3. **🎯 Action Buttons**
   - [ ] "📧 Email Boards Now" scrolls to form
   - [ ] "📱 Share This Page" opens share modal
   - [ ] "📅 Add to Calendar" opens Google Calendar

4. **✅ Quick Signup Form**
   - [ ] Form visible in red banner
   - [ ] Email field works
   - [ ] Phone auto-formats: (972) 555-1234
   - [ ] SMS checkbox checked by default
   - [ ] "Sign Me Up!" button works
   - [ ] Success message shows after submit
   - [ ] Data goes to Google Sheets

5. **📧 Full Form Section**
   - [ ] All fields present
   - [ ] Phone auto-formats
   - [ ] SMS checkbox checked by default
   - [ ] Form validation works
   - [ ] Submit opens email client
   - [ ] Data goes to Google Sheets

6. **📱 Share Modal**
   - [ ] Click "Share" opens modal
   - [ ] "💬 Text Your Friends" works
   - [ ] "📧 Email Your Network" works
   - [ ] "🔗 Copy Link" works
   - [ ] Can close modal with X or Cancel

7. **🔗 All Links Work**
   - [ ] Google Drive documents open
   - [ ] Resource links work
   - [ ] Social share buttons work

---

## 🚀 DEPLOYMENT METHODS

### **Method 1: FTP Upload (Most Common)**

**Tools You Can Use:**
- FileZilla (free)
- Cyberduck (free)
- Transmit (paid)

**Steps:**
1. Open your FTP client
2. Connect to your web host:
   - Host: ftp.prosperisdpetition.com (or similar)
   - Username: [your FTP username]
   - Password: [your FTP password]
3. Navigate to web root (usually `public_html` or `www`)
4. Find existing `index.html`
5. **Backup first:** Download current `index.html`
6. Upload new file from:
   `/Users/dougcharles/Projects/pisd-petition/index.html`
7. Overwrite the old file
8. Done!

---

### **Method 2: cPanel File Manager**

**Steps:**
1. Log into your hosting cPanel
   - Usually: https://prosperisdpetition.com:2083
   - Or through your hosting provider's website
2. Click "File Manager"
3. Navigate to `public_html` (or wherever your site lives)
4. Find `index.html`
5. **Backup first:** 
   - Right-click current `index.html`
   - Click "Download"
6. Click "Upload" button
7. Select: `/Users/dougcharles/Projects/pisd-petition/index.html`
8. Confirm overwrite
9. Done!

---

### **Method 3: flow.page**

**Steps:**
1. Go to flow.page
2. Log into your account
3. Find "pisdannexation" page
4. Click "Edit"
5. Look for HTML/Code section
6. Open your local file:
   `/Users/dougcharles/Projects/pisd-petition/index.html`
7. Copy ALL the code (Cmd+A, Cmd+C)
8. Paste into flow.page HTML editor
9. Click "Save" or "Publish"
10. Done!

---

### **Method 4: Direct Server Access (SSH)**

If you have SSH access:
```bash
# On your Mac Terminal
scp /Users/dougcharles/Projects/pisd-petition/index.html \
  username@prosperisdpetition.com:/path/to/public_html/
```

---

## 📋 POST-DEPLOYMENT CHECKLIST

After uploading, verify on the LIVE site:

1. **Visit the Live Site:**
   ```
   https://prosperisdpetition.com
   ```

2. **Hard Refresh (Clear Cache):**
   - Mac: Cmd+Shift+R
   - Windows: Ctrl+Shift+R
   - Mobile: Settings → Clear Browser Data

3. **Test All Features:**
   - [ ] Countdown timer updates
   - [ ] Quick signup form works
   - [ ] Full form works
   - [ ] Share modal opens
   - [ ] SMS sharing works (mobile)
   - [ ] Email boards button works
   - [ ] All links work

4. **Test on Multiple Devices:**
   - [ ] iPhone (Safari)
   - [ ] Android (Chrome)
   - [ ] Desktop (Chrome/Safari/Firefox)
   - [ ] Tablet (if available)

5. **Check Google Sheet:**
   - [ ] Test submission appears
   - [ ] All columns filled correctly
   - [ ] Phone formatted properly
   - [ ] SMS opt-in recorded

6. **Delete Test Submissions:**
   - [ ] Remove test rows from Google Sheet
   - [ ] Keep only real submissions

---

## 🚨 IF SOMETHING BREAKS

**Problem: Old version still showing**
- Solution: Hard refresh (Cmd+Shift+R)
- Or: Clear browser cache completely

**Problem: Features not working**
- Check browser console (Cmd+Option+I)
- Look for red error messages
- Send me screenshot

**Problem: Form not submitting**
- Verify Google Apps Script URL is correct
- Check Google Sheet permissions
- Test with different browser

**Problem: Share button not working**
- Check browser console for errors
- Try on different device
- Verify modal appears

---

## 🎯 FINAL VERIFICATION SCRIPT

Run these tests on LIVE site:

1. **Quick Signup Test:**
   - Enter: quicktest@example.com
   - Enter: 9725551234
   - Keep SMS checked
   - Submit
   - Should see success message
   - Check Google Sheet

2. **Share Test:**
   - Click "📱 Share This Page"
   - Modal should appear
   - Try "Copy Link"
   - Should show "✅ Link Copied!"
   - Try "Text Your Friends"
   - Should open Messages/SMS

3. **Full Form Test:**
   - Fill out all fields
   - Include phone
   - Submit
   - Email should open
   - Check Google Sheet

4. **Mobile Test:**
   - Open on phone
   - Countdown should be visible
   - Forms should be easy to use
   - Share should open native menu

---

## 📊 SUCCESS METRICS

After going live, monitor:

**First 24 Hours:**
- [ ] 10+ quick signups
- [ ] 5+ full form submissions
- [ ] 3+ shares (check console logs)
- [ ] No error messages in console

**First Week:**
- [ ] 50+ total signups
- [ ] 30+ SMS opt-ins
- [ ] Growing daily rate
- [ ] No technical issues reported

---

## 🆘 ROLLBACK PLAN

If something goes wrong:

1. You backed up the old `index.html`, right?
2. Upload the old version back
3. Site returns to previous state
4. Contact me with error details
5. We fix and redeploy

---

## 🎉 LAUNCH ANNOUNCEMENT

Once live, announce it:

**Email Blast:**
```
Subject: 🚨 NEW: Quick Sign-Up + Share Features!

We've made it even easier to support the PISD petition!

✅ Quick signup (10 seconds)
📱 One-tap sharing to friends
⏰ Live countdown to Dec 15 meeting

Check it out: prosperisdpetition.com

Every signature and share helps!
```

**Social Media:**
```
🚨 MAJOR UPDATE! Our petition site now has:
✅ 10-second quick signup
📱 Easy text-to-friends sharing
⏰ Live countdown to Dec 15

Sign + Share: prosperisdpetition.com
#ProsperISD #WindsongRanch
```

**Text to Existing List:**
```
NEW FEATURES! Our petition site is even better:
• Quick signup (10 sec)
• Easy sharing
• Dec 15 countdown
Sign + Share: prosperisdpetition.com
```

---

## 📞 DEPLOYMENT SUPPORT

**Tell me your hosting setup and I can give exact instructions:**
1. flow.page?
2. GoDaddy/Bluehost/HostGator?
3. Custom hosting?
4. Something else?

**Or just tell me:**
- Where do you normally update your website?
- Do you have FTP access?
- Do you have cPanel?

---

**Created:** November 20, 2025  
**File Location:** `/Users/dougcharles/Projects/pisd-petition/index.html`  
**File Size:** 60KB  
**Status:** ✅ READY TO DEPLOY
