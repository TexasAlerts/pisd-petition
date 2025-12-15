-- Windsong Ranch Petition - Apple Mail Email Sender
--
-- HOW TO USE:
-- 1. First, export your contacts from Google Sheets as CSV
-- 2. Open Script Editor (Applications > Utilities > Script Editor)
-- 3. Paste this entire script
-- 4. Click the "Run" button (or press Cmd+R)
-- 5. The script will create draft emails (not send automatically for safety)
-- 6. Review a few drafts, then run the "Send All Drafts" script section
--
-- NOTE: Apple Mail has no hard daily limit like Gmail, but sending too fast
-- may trigger spam filters. This script adds delays between emails.

-- ============================================
-- CONFIGURATION
-- ============================================

-- Path to your CSV file (exported from Google Sheets)
-- Format: Name in column 1, Email in column 2
set csvFilePath to (path to desktop as text) & "petition-contacts.csv"

-- Your email subject
set emailSubject to "URGENT: Prosper ISD Votes MONDAY at 7 PM - Your Presence is Critical!"

-- Delay between emails (seconds) - helps avoid spam filters
set delayBetweenEmails to 2

-- ============================================
-- EMAIL TEMPLATE (HTML)
-- ============================================

on getEmailBody(firstName)
    if firstName is "" or firstName is missing value then
        set firstName to "Neighbor"
    end if

    return "<!DOCTYPE html>
<html>
<head>
    <meta charset=\"UTF-8\">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 600px; margin: 0 auto; }
        .header { background: #dc2626; color: white; padding: 20px; text-align: center; }
        .header h1 { margin: 0; font-size: 24px; }
        .urgent-badge { background: #fef3c7; border: 2px solid #f59e0b; padding: 15px; margin: 20px; border-radius: 8px; text-align: center; }
        .urgent-badge strong { color: #92400e; font-size: 18px; }
        .content { padding: 20px; }
        .meeting-box { background: #fee2e2; border: 3px solid #dc2626; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }
        .meeting-box h2 { color: #991b1b; margin: 0 0 10px 0; }
        .action-btn { display: inline-block; background: #dc2626; color: white; padding: 15px 30px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 10px 5px; }
        .action-btn.secondary { background: #1e3a8a; }
        .key-points { background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }
        .key-points li { margin: 8px 0; }
        .options-box { background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 15px 20px; margin: 20px 0; }
        .options-box h3 { color: #1e40af; margin: 0 0 10px 0; font-size: 16px; }
        .rallying-cry { background: #059669; color: white; padding: 15px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0; border-radius: 8px; }
        .footer { background: #f8fafc; padding: 20px; text-align: center; font-size: 14px; color: #64748b; }
    </style>
</head>
<body>
    <div class=\"header\">
        <h1>URGENT: Prosper ISD Votes MONDAY</h1>
        <p style=\"margin: 10px 0 0 0;\">Now we really need your support!</p>
    </div>

    <div class=\"urgent-badge\">
        <strong>DEADLINE: Sign up to speak by NOON TODAY (Friday, December 12)</strong><br>
        <a href=\"https://www.prosper-isd.net/page/school-board-meetings\" style=\"color: #1e3a8a;\">Register to Speak Here</a>
    </div>

    <div class=\"content\">
        <p>Dear " & firstName & ",</p>

        <p>Thank you for previously signing the petition in support of Prosper ISD annexation. <strong>Now we really need your support.</strong></p>

        <p>Next Monday, December 15th, the PISD Board will be voting on annexation. We understand the votes may not currently be in our favor, but <strong>we think we can get there</strong>. An impressive turnout of supporters will get the folks on the fence to support our effort.</p>

        <p><strong>We're so close to making this a reality - don't miss this opportunity!</strong></p>

        <div class=\"meeting-box\">
            <h2>PROSPER ISD BOARD MEETING</h2>
            <p style=\"font-size: 20px; margin: 10px 0;\"><strong>Monday, December 15, 2025 at 7:00 PM</strong></p>
            <p style=\"margin: 5px 0;\">605 E 7th Street, Prosper, TX 75078<br>Central Administration Board Room</p>
            <p style=\"color: #991b1b; font-weight: bold; margin-top: 15px;\">If Prosper ISD approves, this goes to the TEA Commissioner for final decision!</p>
        </div>

        <p style=\"text-align: center;\">
            <a href=\"https://www.prosper-isd.net/page/school-board-meetings\" class=\"action-btn\">Sign Up to Speak (by NOON Today)</a>
            <a href=\"https://prosperisdpetition.com\" class=\"action-btn secondary\">Our Website: Data, Financials & Overview</a>
        </p>

        <div class=\"options-box\">
            <h3>Ways You Can Help:</h3>
            <ol style=\"margin: 0; padding-left: 20px;\">
                <li><strong>Speak at the meeting</strong> - <a href=\"https://www.prosper-isd.net/page/school-board-meetings\">Register by NOON Friday</a></li>
                <li><strong>Attend in person</strong> - Even if you don't speak, a packed room matters!</li>
                <li><strong>Submit a comment card</strong> - If you can't attend, submit written comments that become part of the official record</li>
            </ol>
        </div>

        <div class=\"key-points\">
            <strong>Why Your Presence Matters:</strong>
            <ul>
                <li><strong>52.6% of voters signed</strong> - We have majority support (360 of 684)</li>
                <li><strong>$6.5M annually</strong> - Tax revenue that should follow our 274 students</li>
                <li><strong>Only $83/year difference</strong> - Less than $7/month in tax rates</li>
                <li><strong>Board members need to see us</strong> - A packed room shows community support</li>
            </ul>
        </div>

        <p><strong>What to do NOW:</strong></p>
        <ol>
            <li><strong>Sign up to speak</strong> at <a href=\"https://www.prosper-isd.net/page/school-board-meetings\">prosper-isd.net</a> by NOON today</li>
            <li><strong>Add the meeting</strong> to your calendar (attached)</li>
            <li><strong>Show up Monday at 7 PM</strong> - Bring your family, bring your neighbors</li>
            <li><strong>Share this</strong> with other Windsong Ranch residents</li>
        </ol>

        <div class=\"rallying-cry\">
            Let's do this... #ProsperStrong #WindsongStrong
        </div>

        <p><strong>See you Monday at 7 PM!</strong></p>

        <p>
            Doug Charles & Jeff Sterling<br>
            Windsong Ranch Annexation Committee<br>
            <a href=\"https://prosperisdpetition.com\">prosperisdpetition.com</a>
        </p>
    </div>

    <div class=\"footer\">
        <p>You're receiving this because you signed the Windsong Ranch annexation petition.</p>
        <p>Questions? Reply to this email or visit <a href=\"https://prosperisdpetition.com\">prosperisdpetition.com</a></p>
    </div>
</body>
</html>"
end getEmailBody

-- ============================================
-- MAIN SCRIPT - READ CSV AND CREATE EMAILS
-- ============================================

on run
    display dialog "This script will read contacts from:" & return & return & csvFilePath & return & return & "Make sure you have exported your Google Sheet contacts to this location." & return & return & "Format: Column A = Name, Column B = Email" buttons {"Cancel", "Continue"} default button "Continue"

    try
        -- Read the CSV file
        set csvFile to read file csvFilePath
        set csvLines to paragraphs of csvFile

        set emailCount to 0
        set skippedCount to 0

        tell application "Mail"
            activate

            repeat with i from 2 to count of csvLines -- Skip header row
                set currentLine to item i of csvLines

                if currentLine is not "" then
                    -- Parse CSV line (simple split by comma)
                    set AppleScript's text item delimiters to ","
                    set lineItems to text items of currentLine
                    set AppleScript's text item delimiters to ""

                    if (count of lineItems) ≥ 2 then
                        set recipientName to item 1 of lineItems
                        set recipientEmail to item 2 of lineItems

                        -- Clean up the email (remove quotes if present)
                        if recipientEmail starts with "\"" then
                            set recipientEmail to text 2 thru -2 of recipientEmail
                        end if

                        -- Clean up the name
                        if recipientName starts with "\"" then
                            set recipientName to text 2 thru -2 of recipientName
                        end if

                        -- Extract first name
                        set AppleScript's text item delimiters to " "
                        set nameParts to text items of recipientName
                        set AppleScript's text item delimiters to ""
                        set firstName to item 1 of nameParts

                        -- Validate email
                        if recipientEmail contains "@" then
                            -- Create the email
                            set emailBody to my getEmailBody(firstName)

                            set newMessage to make new outgoing message with properties {subject:emailSubject, content:emailBody, visible:true}

                            tell newMessage
                                make new to recipient at end of to recipients with properties {address:recipientEmail, name:recipientName}
                            end tell

                            -- Send the email
                            send newMessage

                            set emailCount to emailCount + 1

                            -- Delay to avoid spam filters
                            delay delayBetweenEmails
                        else
                            set skippedCount to skippedCount + 1
                        end if
                    end if
                end if
            end repeat
        end tell

        display dialog "Email sending complete!" & return & return & "Sent: " & emailCount & " emails" & return & "Skipped: " & skippedCount & " (invalid)" buttons {"OK"} default button "OK"

    on error errMsg
        display dialog "Error: " & errMsg buttons {"OK"} default button "OK"
    end try
end run
