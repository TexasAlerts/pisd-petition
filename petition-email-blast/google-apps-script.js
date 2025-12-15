/**
 * Windsong Ranch Petition - Email Blast Script (BCC Batch Version)
 *
 * SETUP INSTRUCTIONS:
 * 1. Open your Google Sheet with petition signers
 * 2. Go to Extensions > Apps Script
 * 3. Delete any existing code and paste this entire script
 * 4. Click Save (disk icon)
 * 5. Run 'setupMenu' once to add the menu
 * 6. Refresh your Google Sheet - you'll see a new "Petition Emails" menu
 *
 * This version sends emails in batches using BCC for privacy and speed.
 * It automatically removes duplicate email addresses.
 */

// ============================================
// CONFIGURATION - EDIT THESE VALUES
// ============================================

var CONFIG = {
  // Your email (for sending test emails and as reply-to)
  SENDER_EMAIL: 'dbcharles@me.com',

  // Column letters in your sheet (case insensitive)
  EMAIL_COLUMN: 'C',        // Column containing email addresses

  // Email details
  SUBJECT: 'URGENT: Prosper ISD Votes MONDAY at 7 PM - Your Presence is Critical!',

  // Sheet name (leave as null to use first sheet)
  SHEET_NAME: null,

  // Start row (2 = skip header row)
  START_ROW: 2,

  // BCC batch size (Gmail allows up to 100 recipients per email)
  // Using 50 to be safe and avoid spam filters
  BATCH_SIZE: 50,

  // Add tracking column to mark sent emails
  TRACK_SENT: true,
  SENT_COLUMN: 'Z'
};

// ============================================
// EMAIL TEMPLATE (Generic - No personalization)
// ============================================

function getEmailBody() {
  return '<!DOCTYPE html>' +
'<html>' +
'<head>' +
'    <meta charset="UTF-8">' +
'    <style>' +
'        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 600px; margin: 0 auto; }' +
'        .header { background: #dc2626; color: white; padding: 20px; text-align: center; }' +
'        .header h1 { margin: 0; font-size: 24px; }' +
'        .urgent-badge { background: #fef3c7; border: 2px solid #f59e0b; padding: 15px; margin: 20px; border-radius: 8px; text-align: center; }' +
'        .urgent-badge strong { color: #92400e; font-size: 18px; }' +
'        .content { padding: 20px; }' +
'        .meeting-box { background: #fee2e2; border: 3px solid #dc2626; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }' +
'        .meeting-box h2 { color: #991b1b; margin: 0 0 10px 0; }' +
'        .action-btn { display: inline-block; background: #dc2626; color: white; padding: 15px 30px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 10px 5px; }' +
'        .action-btn.secondary { background: #1e3a8a; }' +
'        .key-points { background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }' +
'        .key-points li { margin: 8px 0; }' +
'        .options-box { background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 15px 20px; margin: 20px 0; }' +
'        .options-box h3 { color: #1e40af; margin: 0 0 10px 0; font-size: 16px; }' +
'        .rallying-cry { background: #059669; color: white; padding: 15px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0; border-radius: 8px; }' +
'        .footer { background: #f8fafc; padding: 20px; text-align: center; font-size: 14px; color: #64748b; }' +
'    </style>' +
'</head>' +
'<body>' +
'    <div class="header">' +
'        <h1>URGENT: Prosper ISD Votes MONDAY</h1>' +
'        <p style="margin: 10px 0 0 0;">Now we really need your support!</p>' +
'    </div>' +
'' +
'    <div class="urgent-badge">' +
'        <strong>DEADLINE: Sign up to speak by NOON on Monday, December 15</strong><br>' +
'        <a href="https://www.prosper-isd.net/page/school-board-meetings" style="color: #1e3a8a;">Register to Speak Here</a>' +
'    </div>' +
'' +
'    <div class="content">' +
'        <p>Dear Neighbor,</p>' +
'' +
'        <p>Thank you for previously signing the petition in support of Prosper ISD annexation. <strong>Now we really need your support.</strong></p>' +
'' +
'        <p>Next Monday, December 15th, the PISD Board will be voting on annexation. We understand the votes may not currently be in our favor, but <strong>we think we can get there</strong>. An impressive turnout of supporters will get the folks on the fence to support our effort.</p>' +
'' +
'        <p><strong>We\'re so close to making this a reality - don\'t miss this opportunity!</strong></p>' +
'' +
'        <div class="meeting-box">' +
'            <h2>PROSPER ISD BOARD MEETING</h2>' +
'            <p style="font-size: 20px; margin: 10px 0;"><strong>Monday, December 15, 2025 at 7:00 PM</strong></p>' +
'            <p style="margin: 5px 0;">605 E 7th Street, Prosper, TX 75078<br>Central Administration Board Room</p>' +
'            <p style="color: #991b1b; font-weight: bold; margin-top: 15px;">If Prosper ISD approves, this goes to the TEA Commissioner for final decision!</p>' +
'        </div>' +
'' +
'        <p style="text-align: center;">' +
'            <a href="https://www.prosper-isd.net/page/school-board-meetings" class="action-btn">Sign Up to Speak (by NOON Monday)</a>' +
'            <a href="https://prosperisdpetition.com" class="action-btn secondary">Our Website: Data, Financials & Overview</a>' +
'        </p>' +
'' +
'        <div class="options-box">' +
'            <h3>Ways You Can Help:</h3>' +
'            <ol style="margin: 0; padding-left: 20px;">' +
'                <li><strong>Speak at the meeting</strong> - <a href="https://www.prosper-isd.net/page/school-board-meetings">Register by NOON Monday</a></li>' +
'                <li><strong>Attend in person</strong> - Even if you don\'t speak, a packed room matters!</li>' +
'                <li><strong>Submit a comment card</strong> - If you can\'t attend, submit written comments that become part of the official record</li>' +
'            </ol>' +
'        </div>' +
'' +
'        <div class="key-points">' +
'            <strong>Why Your Presence Matters:</strong>' +
'            <ul>' +
'                <li><strong>52.6% of voters signed</strong> - We have majority support (360 of 684)</li>' +
'                <li><strong>$6.5M annually</strong> - Tax revenue that should follow our 274 students</li>' +
'                <li><strong>Only $83/year difference</strong> - Less than $7/month in tax rates</li>' +
'                <li><strong>Board members need to see us</strong> - A packed room shows community support</li>' +
'            </ul>' +
'        </div>' +
'' +
'        <p><strong>What to do NOW:</strong></p>' +
'        <ol>' +
'            <li><strong>Sign up to speak</strong> at <a href="https://www.prosper-isd.net/page/school-board-meetings">prosper-isd.net</a> by NOON Monday</li>' +
'            <li><strong>Add the meeting</strong> to your calendar (attached)</li>' +
'            <li><strong>Show up Monday at 7 PM</strong> - Bring your family, bring your neighbors</li>' +
'            <li><strong>Share this</strong> with other Windsong Ranch residents</li>' +
'        </ol>' +
'' +
'        <div class="rallying-cry">' +
'            Let\'s do this... #ProsperStrong #WindsongStrong' +
'        </div>' +
'' +
'        <p><strong>See you Monday at 7 PM!</strong></p>' +
'' +
'        <p>' +
'            Doug Charles & Jeff Sterling<br>' +
'            Windsong Ranch Annexation Committee<br>' +
'            <a href="https://prosperisdpetition.com">prosperisdpetition.com</a>' +
'        </p>' +
'    </div>' +
'' +
'    <div class="footer">' +
'        <p>You\'re receiving this because you signed the Windsong Ranch annexation petition.</p>' +
'        <p>Questions? Reply to this email or visit <a href="https://prosperisdpetition.com">prosperisdpetition.com</a></p>' +
'    </div>' +
'</body>' +
'</html>';
}

// ============================================
// CALENDAR INVITE (ICS FILE)
// ============================================

function getCalendarInvite() {
  return 'BEGIN:VCALENDAR\n' +
'VERSION:2.0\n' +
'PRODID:-//Windsong Ranch Petition//EN\n' +
'CALSCALE:GREGORIAN\n' +
'METHOD:PUBLISH\n' +
'BEGIN:VEVENT\n' +
'UID:prosper-meeting-20251215@prosperisdpetition.com\n' +
'DTSTAMP:20251212T120000Z\n' +
'DTSTART:20251215T190000\n' +
'DTEND:20251215T210000\n' +
'SUMMARY:CRITICAL: Prosper ISD Board Vote - Windsong Ranch Annexation\n' +
'DESCRIPTION:CRITICAL: Prosper ISD votes on Windsong Ranch annexation petition.\\n\\nDenton ISD denied on Dec 9 - now PISD approval sends this to TEA Commissioner for final decision.\\n\\nYour attendance is crucial!\\n\\nSign up to speak by NOON on December 15:\\nhttps://www.prosper-isd.net/page/school-board-meetings\\n\\nMore info: https://prosperisdpetition.com\n' +
'LOCATION:Prosper ISD Administration Building, 605 E 7th Street, Prosper, TX 75078\n' +
'STATUS:CONFIRMED\n' +
'SEQUENCE:0\n' +
'BEGIN:VALARM\n' +
'TRIGGER:-PT24H\n' +
'ACTION:DISPLAY\n' +
'DESCRIPTION:CRITICAL: Prosper ISD Vote Tomorrow at 7:00 PM - Pack the Room!\n' +
'END:VALARM\n' +
'BEGIN:VALARM\n' +
'TRIGGER:-PT2H\n' +
'ACTION:DISPLAY\n' +
'DESCRIPTION:Prosper ISD Vote in 2 hours at 7:00 PM!\n' +
'END:VALARM\n' +
'END:VEVENT\n' +
'END:VCALENDAR';
}

// ============================================
// MAIN FUNCTIONS
// ============================================

function onOpen() {
  setupMenu();
}

function setupMenu() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Petition Emails')
    .addItem('Send Test Email (to yourself)', 'sendTestEmail')
    .addSeparator()
    .addItem('Check Email Quota', 'checkQuota')
    .addItem('Preview Email Count (with dedup)', 'previewEmailCount')
    .addItem('Send BCC Batch to ALL', 'sendBatchBCC')
    .addSeparator()
    .addItem('View Configuration', 'showConfig')
    .addItem('Reset Sent Status (clear column Z)', 'resetSentStatus')
    .addToUi();
}

function checkQuota() {
  var ui = SpreadsheetApp.getUi();
  var quota = MailApp.getRemainingDailyQuota();
  ui.alert('Email Quota Check',
    'Your remaining daily email quota: ' + quota + '\n\nWith BCC batching (' + CONFIG.BATCH_SIZE + ' per batch), you can reach ' + (quota * CONFIG.BATCH_SIZE) + ' recipients today.',
    ui.ButtonSet.OK);
}

function getSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  return CONFIG.SHEET_NAME ? ss.getSheetByName(CONFIG.SHEET_NAME) : ss.getActiveSheet();
}

function columnToIndex(col) {
  if (!col) return null;
  col = col.toUpperCase();
  var index = 0;
  for (var i = 0; i < col.length; i++) {
    index = index * 26 + col.charCodeAt(i) - 64;
  }
  return index;
}

// Get unique emails that haven't been sent to yet
function getUniqueUnsentEmails() {
  var sheet = getSheet();
  var data = sheet.getDataRange().getValues();

  var emailColIndex = columnToIndex(CONFIG.EMAIL_COLUMN) - 1;
  var sentColIndex = CONFIG.TRACK_SENT ? columnToIndex(CONFIG.SENT_COLUMN) - 1 : null;

  var seenEmails = {};
  var emailsToSend = [];
  var rowMap = {}; // Map email to row numbers for marking sent
  var duplicates = 0;
  var alreadySent = 0;

  for (var i = CONFIG.START_ROW - 1; i < data.length; i++) {
    var rawEmail = data[i][emailColIndex];
    if (!rawEmail || rawEmail.toString().indexOf('@') === -1) {
      continue;
    }

    var email = rawEmail.toString().trim().toLowerCase();

    // Skip duplicates
    if (seenEmails[email]) {
      duplicates++;
      continue;
    }
    seenEmails[email] = true;

    // Skip if already sent
    if (sentColIndex !== null && data[i][sentColIndex] === 'Sent') {
      alreadySent++;
      continue;
    }

    emailsToSend.push(email);
    if (!rowMap[email]) {
      rowMap[email] = [];
    }
    rowMap[email].push(i + 1); // 1-indexed row
  }

  return {
    emails: emailsToSend,
    rowMap: rowMap,
    duplicates: duplicates,
    alreadySent: alreadySent,
    total: Object.keys(seenEmails).length
  };
}

function previewEmailCount() {
  var ui = SpreadsheetApp.getUi();
  var result = getUniqueUnsentEmails();
  var remainingQuota = MailApp.getRemainingDailyQuota();
  var batchesNeeded = Math.ceil(result.emails.length / CONFIG.BATCH_SIZE);

  var warningMsg = batchesNeeded > remainingQuota ?
    'WARNING: Need ' + batchesNeeded + ' quota but only have ' + remainingQuota + '!\nWill send ' + (remainingQuota * CONFIG.BATCH_SIZE) + ' emails today.' :
    'You have enough quota to send all emails.';

  ui.alert('Email Preview (Deduplicated)',
    'Total unique emails: ' + result.total + '\n' +
    'Duplicates removed: ' + result.duplicates + '\n' +
    'Already sent: ' + result.alreadySent + '\n' +
    'To be sent: ' + result.emails.length + '\n\n' +
    'Batches needed: ' + batchesNeeded + ' (' + CONFIG.BATCH_SIZE + ' per batch)\n' +
    'Your remaining quota: ' + remainingQuota + ' emails\n\n' +
    warningMsg,
    ui.ButtonSet.OK);
}

function sendTestEmail() {
  var ui = SpreadsheetApp.getUi();

  var quota = MailApp.getRemainingDailyQuota();
  if (quota < 1) {
    ui.alert('No Quota', 'You have no remaining email quota today. Try again tomorrow.', ui.ButtonSet.OK);
    return;
  }

  try {
    var htmlBody = getEmailBody();
    var calendarBlob = Utilities.newBlob(getCalendarInvite(), 'text/calendar', 'prosper-isd-meeting.ics');

    MailApp.sendEmail({
      to: CONFIG.SENDER_EMAIL,
      subject: '[TEST] ' + CONFIG.SUBJECT,
      htmlBody: htmlBody,
      attachments: [calendarBlob],
      name: 'Windsong Ranch Annexation Committee'
    });

    ui.alert('Test Email Sent!',
      'A test email has been sent to ' + CONFIG.SENDER_EMAIL + '\n\nRemaining quota: ' + (quota - 1) + ' emails\n\nPlease check your inbox (AND SPAM FOLDER) and verify it looks correct before sending to all recipients.',
      ui.ButtonSet.OK);
  } catch (e) {
    ui.alert('Error', 'Failed to send test email: ' + e.message, ui.ButtonSet.OK);
  }
}

function sendBatchBCC() {
  var ui = SpreadsheetApp.getUi();
  var result = getUniqueUnsentEmails();

  if (result.emails.length === 0) {
    ui.alert('No Emails to Send', 'All emails have already been sent or there are no valid email addresses.', ui.ButtonSet.OK);
    return;
  }

  var remainingQuota = MailApp.getRemainingDailyQuota();
  var batchesNeeded = Math.ceil(result.emails.length / CONFIG.BATCH_SIZE);
  var batchesToSend = Math.min(batchesNeeded, remainingQuota);
  var emailsToSend = result.emails.slice(0, batchesToSend * CONFIG.BATCH_SIZE);

  // Confirm
  var response = ui.alert(
    'Confirm BCC Batch Send',
    'Ready to send ' + emailsToSend.length + ' emails in ' + batchesToSend + ' batch(es).\n\n' +
    'Duplicates removed: ' + result.duplicates + '\n' +
    'Already sent (skipped): ' + result.alreadySent + '\n\n' +
    'Each batch sends to up to ' + CONFIG.BATCH_SIZE + ' recipients via BCC.\n\n' +
    'Click OK to proceed.',
    ui.ButtonSet.OK_CANCEL
  );

  if (response !== ui.Button.OK) {
    return;
  }

  var sheet = getSheet();
  var sentColIndex = columnToIndex(CONFIG.SENT_COLUMN);
  var htmlBody = getEmailBody();
  var calendarBlob = Utilities.newBlob(getCalendarInvite(), 'text/calendar', 'prosper-isd-meeting.ics');

  var batchesSent = 0;
  var totalEmailsSent = 0;
  var errors = [];

  // Process in batches
  for (var i = 0; i < emailsToSend.length; i += CONFIG.BATCH_SIZE) {
    var batch = emailsToSend.slice(i, i + CONFIG.BATCH_SIZE);

    try {
      // Send email with BCC
      MailApp.sendEmail({
        to: CONFIG.SENDER_EMAIL,  // Send TO yourself
        bcc: batch.join(','),      // BCC all recipients
        subject: CONFIG.SUBJECT,
        htmlBody: htmlBody,
        attachments: [calendarBlob],
        name: 'Windsong Ranch Annexation Committee',
        replyTo: CONFIG.SENDER_EMAIL
      });

      // Mark all emails in this batch as sent
      if (CONFIG.TRACK_SENT) {
        for (var j = 0; j < batch.length; j++) {
          var email = batch[j];
          var rows = result.rowMap[email];
          if (rows) {
            for (var k = 0; k < rows.length; k++) {
              sheet.getRange(rows[k], sentColIndex).setValue('Sent');
              sheet.getRange(rows[k], sentColIndex + 1).setValue(new Date());
            }
          }
        }
      }

      batchesSent++;
      totalEmailsSent += batch.length;

      // Small delay between batches
      if (i + CONFIG.BATCH_SIZE < emailsToSend.length) {
        Utilities.sleep(1000);
      }

    } catch (e) {
      errors.push('Batch ' + (batchesSent + 1) + ': ' + e.message);
      break; // Stop on error (likely quota exceeded)
    }
  }

  var message = 'Batches sent: ' + batchesSent + '\n' +
    'Total recipients: ' + totalEmailsSent + '\n' +
    'Remaining to send: ' + (result.emails.length - totalEmailsSent);

  if (errors.length > 0) {
    message += '\n\nErrors:\n' + errors.join('\n');
  }

  if (result.emails.length > totalEmailsSent) {
    message += '\n\nRun this again tomorrow to send the remaining ' + (result.emails.length - totalEmailsSent) + ' emails.';
  }

  ui.alert('Send Complete', message, ui.ButtonSet.OK);
}

function resetSentStatus() {
  var ui = SpreadsheetApp.getUi();

  var response = ui.alert(
    'Reset Sent Status',
    'This will clear all "Sent" markers in column Z, allowing you to resend emails.\n\nAre you sure?',
    ui.ButtonSet.YES_NO
  );

  if (response !== ui.Button.YES) {
    return;
  }

  var sheet = getSheet();
  var sentColIndex = columnToIndex(CONFIG.SENT_COLUMN);
  var lastRow = sheet.getLastRow();

  if (lastRow > 1) {
    sheet.getRange(2, sentColIndex, lastRow - 1, 2).clearContent();
  }

  ui.alert('Reset Complete', 'Sent status has been cleared. You can now resend emails.', ui.ButtonSet.OK);
}

function showConfig() {
  var ui = SpreadsheetApp.getUi();
  ui.alert('Current Configuration',
    'Email Column: ' + CONFIG.EMAIL_COLUMN + '\n' +
    'Start Row: ' + CONFIG.START_ROW + '\n' +
    'Subject: ' + CONFIG.SUBJECT + '\n' +
    'Sender Email: ' + CONFIG.SENDER_EMAIL + '\n' +
    'Batch Size: ' + CONFIG.BATCH_SIZE + '\n' +
    'Track Sent: ' + CONFIG.TRACK_SENT + '\n' +
    'Sent Column: ' + CONFIG.SENT_COLUMN,
    ui.ButtonSet.OK);
}
