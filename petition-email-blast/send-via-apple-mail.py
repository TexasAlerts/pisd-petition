#!/usr/bin/env python3
"""
Windsong Ranch Petition - Apple Mail Email Sender

This script sends emails through Apple Mail on macOS.
No Gmail quota limits!

SETUP:
1. Export your Google Sheet as CSV to: ~/Desktop/petition-contacts.csv
   - Column A: Name (or First Name)
   - Column B: Email address

2. Run this script:
   python3 send-via-apple-mail.py

3. The script will send emails via Apple Mail with a delay between each.
"""

import subprocess
import csv
import os
import time
import sys

# ============================================
# CONFIGURATION
# ============================================

# Path to your CSV file (exported from Google Sheets)
CSV_FILE = os.path.expanduser("~/Desktop/petition-contacts.csv")

# Email subject
SUBJECT = "URGENT: Prosper ISD Votes MONDAY at 7 PM - Your Presence is Critical!"

# Delay between emails (seconds) - helps avoid spam filters
DELAY_BETWEEN_EMAILS = 2

# Path to calendar attachment (optional)
CALENDAR_FILE = os.path.join(os.path.dirname(__file__), "prosper-isd-meeting.ics")

# ============================================
# EMAIL TEMPLATE
# ============================================

def get_email_body(first_name):
    """Generate the HTML email body with personalized name."""
    name = first_name if first_name else "Neighbor"

    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 600px; margin: 0 auto; }}
        .header {{ background: #dc2626; color: white; padding: 20px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .urgent-badge {{ background: #fef3c7; border: 2px solid #f59e0b; padding: 15px; margin: 20px; border-radius: 8px; text-align: center; }}
        .urgent-badge strong {{ color: #92400e; font-size: 18px; }}
        .content {{ padding: 20px; }}
        .meeting-box {{ background: #fee2e2; border: 3px solid #dc2626; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }}
        .meeting-box h2 {{ color: #991b1b; margin: 0 0 10px 0; }}
        .action-btn {{ display: inline-block; background: #dc2626; color: white; padding: 15px 30px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 10px 5px; }}
        .action-btn.secondary {{ background: #1e3a8a; }}
        .key-points {{ background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }}
        .key-points li {{ margin: 8px 0; }}
        .options-box {{ background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 15px 20px; margin: 20px 0; }}
        .options-box h3 {{ color: #1e40af; margin: 0 0 10px 0; font-size: 16px; }}
        .rallying-cry {{ background: #059669; color: white; padding: 15px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0; border-radius: 8px; }}
        .footer {{ background: #f8fafc; padding: 20px; text-align: center; font-size: 14px; color: #64748b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>URGENT: Prosper ISD Votes MONDAY</h1>
        <p style="margin: 10px 0 0 0;">Now we really need your support!</p>
    </div>

    <div class="urgent-badge">
        <strong>DEADLINE: Sign up to speak by NOON TODAY (Friday, December 12)</strong><br>
        <a href="https://www.prosper-isd.net/page/school-board-meetings" style="color: #1e3a8a;">Register to Speak Here</a>
    </div>

    <div class="content">
        <p>Dear {name},</p>

        <p>Thank you for previously signing the petition in support of Prosper ISD annexation. <strong>Now we really need your support.</strong></p>

        <p>Next Monday, December 15th, the PISD Board will be voting on annexation. We understand the votes may not currently be in our favor, but <strong>we think we can get there</strong>. An impressive turnout of supporters will get the folks on the fence to support our effort.</p>

        <p><strong>We're so close to making this a reality - don't miss this opportunity!</strong></p>

        <div class="meeting-box">
            <h2>PROSPER ISD BOARD MEETING</h2>
            <p style="font-size: 20px; margin: 10px 0;"><strong>Monday, December 15, 2025 at 7:00 PM</strong></p>
            <p style="margin: 5px 0;">605 E 7th Street, Prosper, TX 75078<br>Central Administration Board Room</p>
            <p style="color: #991b1b; font-weight: bold; margin-top: 15px;">If Prosper ISD approves, this goes to the TEA Commissioner for final decision!</p>
        </div>

        <p style="text-align: center;">
            <a href="https://www.prosper-isd.net/page/school-board-meetings" class="action-btn">Sign Up to Speak (by NOON Today)</a>
            <a href="https://prosperisdpetition.com" class="action-btn secondary">Our Website: Data, Financials & Overview</a>
        </p>

        <div class="options-box">
            <h3>Ways You Can Help:</h3>
            <ol style="margin: 0; padding-left: 20px;">
                <li><strong>Speak at the meeting</strong> - <a href="https://www.prosper-isd.net/page/school-board-meetings">Register by NOON Friday</a></li>
                <li><strong>Attend in person</strong> - Even if you don't speak, a packed room matters!</li>
                <li><strong>Submit a comment card</strong> - If you can't attend, submit written comments that become part of the official record</li>
            </ol>
        </div>

        <div class="key-points">
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
            <li><strong>Sign up to speak</strong> at <a href="https://www.prosper-isd.net/page/school-board-meetings">prosper-isd.net</a> by NOON today</li>
            <li><strong>Add the meeting</strong> to your calendar (attached)</li>
            <li><strong>Show up Monday at 7 PM</strong> - Bring your family, bring your neighbors</li>
            <li><strong>Share this</strong> with other Windsong Ranch residents</li>
        </ol>

        <div class="rallying-cry">
            Let's do this... #ProsperStrong #WindsongStrong
        </div>

        <p><strong>See you Monday at 7 PM!</strong></p>

        <p>
            Doug Charles & Jeff Sterling<br>
            Windsong Ranch Annexation Committee<br>
            <a href="https://prosperisdpetition.com">prosperisdpetition.com</a>
        </p>
    </div>

    <div class="footer">
        <p>You're receiving this because you signed the Windsong Ranch annexation petition.</p>
        <p>Questions? Reply to this email or visit <a href="https://prosperisdpetition.com">prosperisdpetition.com</a></p>
    </div>
</body>
</html>'''


# iCloud SMTP Configuration
ICLOUD_EMAIL = "dbcharles@me.com"
ICLOUD_APP_PASSWORD = "ooxy-ovgf-ahfn-srjr"


def send_email_via_icloud_smtp(to_email, to_name, subject, html_body):
    """Send HTML email via iCloud SMTP."""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Windsong Ranch Annexation Committee <{ICLOUD_EMAIL}>"
    msg['To'] = f"{to_name} <{to_email}>"
    msg['Reply-To'] = ICLOUD_EMAIL

    # Create HTML part
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    # Send via iCloud SMTP (port 587 with STARTTLS)
    with smtplib.SMTP('smtp.mail.me.com', 587) as server:
        server.starttls()
        server.login(ICLOUD_EMAIL, ICLOUD_APP_PASSWORD)
        server.sendmail(ICLOUD_EMAIL, to_email, msg.as_string())

    return True


def send_email_via_apple_mail(to_email, to_name, subject, html_body, attachment_path=None):
    """Send an email using Apple Mail via AppleScript with proper HTML rendering."""

    # Write HTML to a temp file
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_body)
        html_file_path = f.name

    try:
        # Escape quotes in subject for AppleScript
        escaped_subject = subject.replace('"', '\\"')

        # AppleScript that creates message, then uses System Events to paste HTML
        # This approach works around the html content property issues
        applescript = f'''
        set theFile to POSIX file "{html_file_path}"
        set theHTML to read theFile as «class utf8»

        tell application "Mail"
            activate
            set newMessage to make new outgoing message with properties {{subject:"{escaped_subject}", visible:true}}
            tell newMessage
                make new to recipient at end of to recipients with properties {{address:"{to_email}", name:"{to_name}"}}
                -- Set content directly - Mail will interpret as HTML if it starts with DOCTYPE
                set content to theHTML
            end tell
            delay 0.3
            send newMessage
        end tell
        '''

        # Run AppleScript
        result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(f"AppleScript error: {result.stderr}")

        return True
    finally:
        # Clean up temp file
        os.unlink(html_file_path)


def main():
    """Main function to read CSV and send emails."""

    # Check for command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Send emails via Apple Mail')
    parser.add_argument('--test', type=str, help='Send test email to this address')
    parser.add_argument('--send-all', action='store_true', help='Send to all contacts (no confirmation)')
    args = parser.parse_args()

    print("=" * 60)
    print("Windsong Ranch Petition - Apple Mail Email Sender")
    print("=" * 60)
    print()

    # Check if CSV file exists
    if not os.path.exists(CSV_FILE):
        print(f"ERROR: CSV file not found at: {CSV_FILE}")
        print()
        print("Please export your Google Sheet to CSV:")
        print("1. Open your Google Sheet")
        print("2. File > Download > Comma Separated Values (.csv)")
        print("3. Save to your Desktop as 'petition-contacts.csv'")
        print()
        print("Expected format:")
        print("  Column A: Name")
        print("  Column B: Email")
        sys.exit(1)

    # Read CSV file
    # Your CSV format: Timestamp, Name, Email, Phone, ...
    # So Name is column 1 (index 1), Email is column 2 (index 2)
    contacts = []
    seen_emails = set()
    duplicates = 0

    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header row

        for row in reader:
            if len(row) >= 3:
                name = row[1].strip()  # Column B = Name
                email = row[2].strip().lower()  # Column C = Email (lowercase for dedup)
                if '@' in email:
                    # Check for duplicates
                    if email in seen_emails:
                        duplicates += 1
                        continue
                    seen_emails.add(email)

                    # Extract first name
                    first_name = name.split()[0] if name else ""
                    contacts.append({
                        'name': name,
                        'first_name': first_name,
                        'email': email
                    })

    print(f"Found {len(contacts)} unique email addresses")
    if duplicates > 0:
        print(f"Removed {duplicates} duplicate email(s)")
    print()

    # Handle command line arguments
    if args.test:
        test_email = args.test
        print(f"Sending TEST email to {test_email} via iCloud SMTP...")

        try:
            html_body = get_email_body("Doug")  # Use your name for test

            send_email_via_icloud_smtp(
                to_email=test_email,
                to_name="Test User",
                subject="[TEST] " + SUBJECT,
                html_body=html_body
            )
            print("TEST email sent! Check your inbox.")
        except Exception as e:
            print(f"FAILED: {e}")

        sys.exit(0)

    elif args.send_all:
        # Skip confirmation, go straight to sending
        pass

    else:
        # Interactive mode
        print("Options:")
        print("  1. Send TEST email (to yourself only)")
        print("  2. Send to ALL contacts")
        print("  3. Cancel")
        print()

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            # Test mode - send to yourself
            test_email = input("Enter YOUR email address for test: ").strip()
            if not test_email or '@' not in test_email:
                print("Invalid email. Cancelled.")
                sys.exit(1)

            print()
            print(f"Sending TEST email to {test_email}...")

            try:
                html_body = get_email_body("Doug")
                attachment = CALENDAR_FILE if os.path.exists(CALENDAR_FILE) else None

                send_email_via_apple_mail(
                    to_email=test_email,
                    to_name="Test User",
                    subject="[TEST] " + SUBJECT,
                    html_body=html_body,
                    attachment_path=attachment
                )
                print("TEST email sent! Check your inbox.")
            except Exception as e:
                print(f"FAILED: {e}")

            sys.exit(0)

        elif choice == '3' or choice.lower() == 'cancel':
            print("Cancelled.")
            sys.exit(0)

        elif choice != '2':
            print("Invalid choice. Cancelled.")
            sys.exit(0)

        # Confirm before sending to all
        print()
        response = input(f"Send to ALL {len(contacts)} unique contacts? Type 'yes' to confirm: ")
        if response.lower() != 'yes':
            print("Cancelled.")
            sys.exit(0)

    print()
    print("Starting to send emails...")
    print()

    sent_count = 0
    error_count = 0
    errors = []

    for i, contact in enumerate(contacts, 1):
        try:
            print(f"[{i}/{len(contacts)}] Sending to {contact['email']}...", end=" ")

            html_body = get_email_body(contact['first_name'])

            send_email_via_icloud_smtp(
                to_email=contact['email'],
                to_name=contact['name'],
                subject=SUBJECT,
                html_body=html_body
            )

            print("SENT")
            sent_count += 1

            # Delay between emails
            if i < len(contacts):
                time.sleep(DELAY_BETWEEN_EMAILS)

        except Exception as e:
            print(f"FAILED: {e}")
            error_count += 1
            errors.append(f"{contact['email']}: {e}")

    print()
    print("=" * 60)
    print("COMPLETE!")
    print(f"  Sent: {sent_count}")
    print(f"  Failed: {error_count}")
    print("=" * 60)

    if errors:
        print()
        print("Errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")


if __name__ == "__main__":
    main()
