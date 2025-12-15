# Windsong Ranch Petition - Email Blast System

This folder contains everything you need to send emails to petition signers.

## Quick Setup (5 minutes)

### Step 1: Open Google Apps Script

1. Open your Google Sheet with petition signers
2. Click **Extensions** > **Apps Script**
3. Delete any existing code in the editor

### Step 2: Copy the Script

1. Open `google-apps-script.js` in this folder
2. Copy ALL the code
3. Paste it into the Apps Script editor
4. Click the **Save** icon (disk)

### Step 3: Configure Your Columns

Edit the CONFIG section at the top of the script:

```javascript
const CONFIG = {
  SENDER_EMAIL: 'dbcharles@me.com',  // Your email
  EMAIL_COLUMN: 'E',                  // Column with email addresses
  FIRST_NAME_COLUMN: 'B',             // Column with first names
  // ... other settings
};
```

### Step 4: Run Setup

1. In Apps Script, select `setupMenu` from the dropdown
2. Click **Run**
3. Authorize the script when prompted (click through the warnings)
4. Go back to your Google Sheet and refresh the page

### Step 5: Send Emails

You'll now see a **"Petition Emails"** menu in your Google Sheet:

1. **Send Test Email** - Sends one email to yourself first (ALWAYS DO THIS FIRST!)
2. **Preview Email Count** - Shows how many emails will be sent
3. **Send to ALL Recipients** - Sends to everyone (asks for confirmation)

## Files Included

| File | Purpose |
|------|---------|
| `google-apps-script.js` | The main script to paste into Apps Script |
| `email-template.html` | HTML preview of the email (for reference) |
| `prosper-isd-meeting.ics` | Calendar file that gets attached |
| `README.md` | This file |

## Email Content

The email includes:
- Urgent header about Monday's vote
- Sign-up deadline reminder (NOON today)
- Meeting details (7 PM, 605 E 7th Street)
- Key talking points ($6.5M, 274 students, 52.6% support)
- Call to action buttons
- Calendar invite attachment (.ics file)

## Daily Sending Limits

Google has daily email limits:
- **Gmail (free)**: 100-500 emails/day
- **Google Workspace**: 1,500-2,000 emails/day

The script shows your remaining quota before sending.

## Troubleshooting

### "Authorization required" error
- Click through the authorization prompts
- On "This app isn't verified" screen, click "Advanced" > "Go to [project name]"

### Menu doesn't appear
- Run `setupMenu` from Apps Script first
- Refresh the Google Sheet page

### Emails going to spam
- Have recipients add your email to contacts
- Keep the email short and avoid spam trigger words

### Not enough quota
- Wait until tomorrow (quota resets daily)
- Or use a Google Workspace account

## Testing Checklist

Before sending to everyone:

- [ ] Sent test email to yourself
- [ ] Verified email looks correct
- [ ] Calendar attachment works
- [ ] Links work (sign-up form, website)
- [ ] Checked remaining quota
- [ ] Previewed email count

## Support

Questions? Contact Doug Charles at dbcharles@me.com
