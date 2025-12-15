#!/usr/bin/env python3
"""
Windsong Ranch Petition - TONIGHT Meeting Email (Day-Of)

Send this Monday December 15 to remind everyone about TONIGHT's meeting.
Focus: TONIGHT at 7 PM! Arrive by 6:45! Bring everyone!

Usage:
    python3 tonight-meeting.py --test your@email.com   # Test first
    python3 tonight-meeting.py --send-all              # Send to all contacts
"""

import subprocess
import csv
import os
import time
import sys

# ============================================
# CONFIGURATION
# ============================================

CSV_FILE = os.path.expanduser("~/Desktop/petition-contacts.csv")
SUBJECT = "TONIGHT at 7 PM: Prosper ISD Board Meeting - Be There!"
DELAY_BETWEEN_EMAILS = 2

# ============================================
# EMAIL TEMPLATE - TONIGHT / DAY-OF
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
        .header {{ background: #991b1b; color: white; padding: 25px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 28px; }}
        .tonight-badge {{ background: #dc2626; color: white; padding: 20px; margin: 0; text-align: center; }}
        .tonight-badge strong {{ font-size: 24px; }}
        .content {{ padding: 20px; }}
        .meeting-box {{ background: #fee2e2; border: 3px solid #dc2626; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }}
        .meeting-box h2 {{ color: #991b1b; margin: 0 0 10px 0; font-size: 22px; }}
        .action-btn {{ display: inline-block; background: #dc2626; color: white; padding: 15px 30px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 10px 5px; }}
        .key-points {{ background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }}
        .key-points li {{ margin: 8px 0; }}
        .checklist {{ background: #ecfdf5; border: 2px solid #10b981; border-radius: 8px; padding: 20px; margin: 20px 0; }}
        .checklist h3 {{ color: #065f46; margin: 0 0 15px 0; }}
        .checklist li {{ margin: 10px 0; font-size: 1.05rem; }}
        .rallying-cry {{ background: #059669; color: white; padding: 20px; text-align: center; font-size: 22px; font-weight: bold; margin: 20px 0; border-radius: 8px; }}
        .footer {{ background: #f8fafc; padding: 20px; text-align: center; font-size: 14px; color: #64748b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>TONIGHT IS THE NIGHT</h1>
        <p style="margin: 10px 0 0 0; font-size: 18px;">Prosper ISD Board Meeting - 7 PM</p>
    </div>

    <div class="tonight-badge">
        <strong>Monday, December 15, 2025 at 7:00 PM</strong><br>
        <span style="font-size: 16px;">605 E 7th Street, Prosper, TX 75078</span>
    </div>

    <div class="content">
        <p>Dear {name},</p>

        <p><strong>TONIGHT is the night.</strong> The Prosper ISD Board votes on our annexation petition at 7:00 PM. If they approve, this goes to the TEA Commissioner for final decision.</p>

        <div class="meeting-box">
            <h2>PROSPER ISD BOARD MEETING</h2>
            <p style="font-size: 22px; margin: 10px 0;"><strong>TONIGHT - Monday, December 15</strong></p>
            <p style="font-size: 20px; margin: 10px 0;"><strong>7:00 PM</strong></p>
            <p style="margin: 5px 0;">605 E 7th Street, Prosper, TX 75078<br>Central Administration Board Room</p>
        </div>

        <div class="checklist">
            <h3>Arrive by 6:45 PM - Here's What to Do:</h3>
            <ul style="margin: 0; padding-left: 20px; list-style: none;">
                <li>&#10004; <strong>Bring everyone</strong> - your spouse, your kids (all ages!), your neighbors</li>
                <li>&#10004; <strong>Get there early</strong> - arrive by 6:45 PM to get a seat</li>
                <li>&#10004; <strong>Wear Prosper ISD gear</strong> if you have it</li>
                <li>&#10004; <strong>Stay until our item</strong> is discussed</li>
            </ul>
            <p style="margin: 15px 0 0 0; color: #065f46; font-weight: bold;">Every person in that room matters. The board needs to SEE our community support!</p>
        </div>

        <div class="key-points">
            <strong>Remember Why We're Here:</strong>
            <ul>
                <li><strong>274 students</strong> already attend Prosper ISD schools</li>
                <li><strong>$6.5 million annually</strong> in tax revenue should follow our kids</li>
                <li><strong>52.6% of voters signed</strong> - we have majority support</li>
                <li><strong>Only $83/year difference</strong> in tax rates ($6.92/month)</li>
            </ul>
        </div>

        <p style="text-align: center;">
            <a href="https://prosperisdpetition.com" class="action-btn">Our Website - Share With Neighbors</a>
        </p>

        <div class="rallying-cry">
            See you TONIGHT at 7 PM!<br>
            <span style="font-size: 18px;">#ProsperStrong #WindsongStrong</span>
        </div>

        <p>Thank you for standing with us. Tonight we show the board that Windsong Ranch families are united.</p>

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


def main():
    """Main function to read CSV and send emails."""

    import argparse
    parser = argparse.ArgumentParser(description='Send TONIGHT meeting reminder emails')
    parser.add_argument('--test', type=str, help='Send test email to this address')
    parser.add_argument('--send-all', action='store_true', help='Send to all contacts (no confirmation)')
    args = parser.parse_args()

    print("=" * 60)
    print("Windsong Ranch - TONIGHT MEETING REMINDER")
    print("Subject: " + SUBJECT)
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
        sys.exit(1)

    # Read CSV file
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
                    if email in seen_emails:
                        duplicates += 1
                        continue
                    seen_emails.add(email)

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
            html_body = get_email_body("Doug")

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
        pass  # Skip confirmation

    else:
        # Interactive mode
        print("Options:")
        print("  1. Send TEST email (to yourself only)")
        print("  2. Send to ALL contacts")
        print("  3. Cancel")
        print()

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            test_email = input("Enter YOUR email address for test: ").strip()
            if not test_email or '@' not in test_email:
                print("Invalid email. Cancelled.")
                sys.exit(1)

            print()
            print(f"Sending TEST email to {test_email}...")

            try:
                html_body = get_email_body("Doug")
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

        elif choice == '3' or choice.lower() == 'cancel':
            print("Cancelled.")
            sys.exit(0)

        elif choice != '2':
            print("Invalid choice. Cancelled.")
            sys.exit(0)

        # Confirm before sending to all
        print()
        response = input(f"Send TONIGHT MEETING REMINDER to ALL {len(contacts)} contacts? Type 'yes' to confirm: ")
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
