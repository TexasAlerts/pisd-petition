#!/usr/bin/env python3
"""
Windsong Ranch Petition - Media Outreach Email

Send press pitch to Dallas-Fort Worth news media about Monday's PISD board meeting.

Usage:
    python3 media-pitch.py --test your@email.com   # Test first
    python3 media-pitch.py --send-all              # Send to all media contacts
"""

import csv
import os
import time
import sys

# ============================================
# CONFIGURATION
# ============================================

MEDIA_CSV = os.path.join(os.path.dirname(__file__), "media-contacts.csv")
SUBJECT = "TONIGHT: Prosper ISD Votes on $375M Annexation — Presentation Available"
DELAY_BETWEEN_EMAILS = 3

# ============================================
# PRESS PITCH EMAIL TEMPLATE
# ============================================

def get_email_body(organization_name=None):
    """Generate the HTML press pitch email for TONIGHT's meeting."""

    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 650px; margin: 0 auto; }
        .header { background: #991b1b; color: white; padding: 20px; text-align: center; }
        .header h1 { margin: 0; font-size: 24px; }
        .header p { margin: 10px 0 0 0; font-size: 16px; }
        .content { padding: 20px; }
        .event-box { background: #fee2e2; border: 3px solid #dc2626; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }
        .event-box h2 { color: #991b1b; margin: 0 0 10px 0; font-size: 20px; }
        .presentation-box { background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: center; }
        .presentation-box a { color: #1e40af; font-size: 18px; font-weight: bold; }
        .key-facts { background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }
        .key-facts h3 { margin: 0 0 10px 0; color: #374151; }
        .key-facts li { margin: 8px 0; }
        .story-angles { background: #ecfdf5; border-left: 4px solid #10b981; padding: 15px 20px; margin: 20px 0; }
        .story-angles h3 { margin: 0 0 10px 0; color: #065f46; }
        .contact-box { background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; margin: 20px 0; border-radius: 8px; }
        .contact-box h3 { margin: 0 0 10px 0; color: #334155; }
        .footer { font-size: 14px; color: #64748b; padding: 20px; border-top: 1px solid #e5e7eb; }
    </style>
</head>
<body>
    <div class="header">
        <h1>TONIGHT: Prosper ISD Votes on $375M Annexation</h1>
        <p>Monday, December 15, 2025 at 7:00 PM</p>
    </div>

    <div class="content">
        <p><strong>PROSPER, TX</strong> — Tonight at 7:00 PM, the Prosper ISD Board of Trustees will vote on a historic annexation petition that would bring 360 Windsong Ranch families — and an estimated <strong>$375 million in property value</strong> — into the district.</p>

        <div class="event-box">
            <h2>TONIGHT'S MEETING</h2>
            <p style="font-size: 20px; margin: 10px 0;"><strong>Monday, December 15 at 7:00 PM</strong></p>
            <p style="margin: 5px 0;">Prosper ISD Administration Building<br>605 E 7th Street, Prosper, TX 75078</p>
            <p style="margin: 15px 0 0 0;"><strong>Expected: 100+ community members to attend</strong></p>
        </div>

        <div class="presentation-box">
            <h3 style="margin: 0 0 10px 0; color: #1e3a8a;">📊 View Our Full Board Presentation</h3>
            <a href="https://prosperisdpetition.com/board-presentation">prosperisdpetition.com/board-presentation</a>
            <p style="margin: 10px 0 0 0; font-size: 14px; color: #64748b;">Complete financial analysis, student data, and community impact</p>
        </div>

        <div class="key-facts">
            <h3>Key Numbers:</h3>
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>$6.5 million annually</strong> — Tax revenue that would follow our students to PISD</li>
                <li><strong>274 students</strong> — Already attend Prosper ISD schools (via transfer)</li>
                <li><strong>52.6% of voters signed</strong> — Majority community support (360 of 684 registered voters)</li>
                <li><strong>$375 million</strong> — Estimated property value in petition area</li>
                <li><strong>13 years</strong> — How long Denton ISD has collected taxes while educating zero Windsong students</li>
            </ul>
        </div>

        <div class="story-angles">
            <h3>The Story:</h3>
            <p style="margin: 0;">Windsong Ranch families pay <strong>$6.5 million per year in school taxes to Denton ISD</strong> — but their nearest Denton school is 10+ miles away. Meanwhile, Prosper ISD schools are walking distance. For 13 years, families have been transferring their kids to Prosper while their tax dollars go elsewhere.</p>
            <p style="margin: 15px 0 0 0;">Tonight's vote is the next step in a rare Texas Education Code Chapter 13 annexation process. Denton ISD denied the petition on December 9 (as expected — they'd lose the revenue). If Prosper ISD approves tonight, the petition goes to the TEA Commissioner for final decision.</p>
        </div>

        <h3>What to Expect Tonight:</h3>
        <ul>
            <li>Packed boardroom with families and children</li>
            <li>Formal presentation to the board</li>
            <li>Community speakers in support</li>
            <li>Board vote on the annexation petition</li>
        </ul>

        <div class="contact-box">
            <h3>Media Contact:</h3>
            <p style="margin: 0;"><strong>Doug Charles</strong><br>
            Windsong Ranch Annexation Committee<br>
            Email: dbcharles@me.com<br>
            Phone: Available for interview</p>
            <p style="margin: 15px 0 0 0;"><strong>Website:</strong> <a href="https://prosperisdpetition.com">prosperisdpetition.com</a></p>
        </div>

        <p style="font-style: italic; color: #64748b;">Strong visual opportunity: packed community meeting, families with kids, maps showing the boundary situation, and a clear "taxation without education" narrative.</p>

        <p>###</p>
    </div>

    <div class="footer">
        <p>For more information or to schedule an interview, please reply to this email.</p>
    </div>
</body>
</html>'''


# iCloud SMTP Configuration
ICLOUD_EMAIL = "dbcharles@me.com"
ICLOUD_APP_PASSWORD = "ooxy-ovgf-ahfn-srjr"


CC_EMAIL = "dbcharles@me.com"  # CC Doug on all media emails


def send_email_via_icloud_smtp(to_email, to_name, subject, html_body, cc_email=None):
    """Send HTML email via iCloud SMTP with optional CC."""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Doug Charles <{ICLOUD_EMAIL}>"
    msg['To'] = to_email
    msg['Reply-To'] = ICLOUD_EMAIL

    if cc_email:
        msg['Cc'] = cc_email

    # Create HTML part
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    # Build recipient list (To + CC)
    recipients = [to_email]
    if cc_email:
        recipients.append(cc_email)

    # Send via iCloud SMTP
    with smtplib.SMTP('smtp.mail.me.com', 587) as server:
        server.starttls()
        server.login(ICLOUD_EMAIL, ICLOUD_APP_PASSWORD)
        server.sendmail(ICLOUD_EMAIL, recipients, msg.as_string())

    return True


def main():
    """Main function to read media CSV and send emails."""

    import argparse
    parser = argparse.ArgumentParser(description='Send media pitch emails')
    parser.add_argument('--test', type=str, help='Send test email to this address')
    parser.add_argument('--send-all', action='store_true', help='Send to all media contacts')
    parser.add_argument('--list', action='store_true', help='List all media contacts')
    args = parser.parse_args()

    print("=" * 60)
    print("Windsong Ranch - MEDIA OUTREACH")
    print("Subject: " + SUBJECT)
    print("=" * 60)
    print()

    # Check if media CSV exists
    if not os.path.exists(MEDIA_CSV):
        print(f"ERROR: Media contacts file not found at: {MEDIA_CSV}")
        sys.exit(1)

    # Read media contacts
    contacts = []
    with open(MEDIA_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append(row)

    print(f"Found {len(contacts)} media contacts")
    print()

    # List contacts
    if args.list:
        print("Media Contacts:")
        print("-" * 60)
        for c in contacts:
            print(f"  {c['Organization']}: {c['Email']}")
        print()
        sys.exit(0)

    # Test mode
    if args.test:
        test_email = args.test
        print(f"Sending TEST email to {test_email}...")

        try:
            html_body = get_email_body()
            send_email_via_icloud_smtp(
                to_email=test_email,
                to_name="Test",
                subject="[TEST] " + SUBJECT,
                html_body=html_body
            )
            print("TEST email sent! Check your inbox.")
        except Exception as e:
            print(f"FAILED: {e}")

        sys.exit(0)

    # Send to all
    elif args.send_all:
        pass

    else:
        # Interactive mode
        print("Media Contacts to receive pitch:")
        print("-" * 60)
        for c in contacts:
            print(f"  {c['Organization']}: {c['Email']}")
        print()
        print("Options:")
        print("  1. Send TEST email (to yourself)")
        print("  2. Send to ALL media contacts")
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
                html_body = get_email_body()
                send_email_via_icloud_smtp(
                    to_email=test_email,
                    to_name="Test",
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

        # Confirm
        print()
        response = input(f"Send PRESS PITCH to ALL {len(contacts)} media contacts? Type 'yes' to confirm: ")
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
            email = contact['Email']
            org = contact['Organization']
            print(f"[{i}/{len(contacts)}] Sending to {org} ({email})...", end=" ")

            html_body = get_email_body(org)

            send_email_via_icloud_smtp(
                to_email=email,
                to_name=org,
                subject=SUBJECT,
                html_body=html_body,
                cc_email=CC_EMAIL
            )

            print("SENT")
            sent_count += 1

            if i < len(contacts):
                time.sleep(DELAY_BETWEEN_EMAILS)

        except Exception as e:
            print(f"FAILED: {e}")
            error_count += 1
            errors.append(f"{contact['Email']}: {e}")

    print()
    print("=" * 60)
    print("COMPLETE!")
    print(f"  Sent: {sent_count}")
    print(f"  Failed: {error_count}")
    print("=" * 60)

    if errors:
        print()
        print("Errors:")
        for err in errors:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
