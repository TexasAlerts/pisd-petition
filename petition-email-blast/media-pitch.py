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
SUBJECT = "STORY IDEA: 360 Families Fight for School District Choice - Prosper ISD Votes Monday"
DELAY_BETWEEN_EMAILS = 3

# ============================================
# PRESS PITCH EMAIL TEMPLATE
# ============================================

def get_email_body(organization_name=None):
    """Generate the HTML press pitch email."""

    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 650px; margin: 0 auto; }
        .header { background: #1e3a8a; color: white; padding: 20px; }
        .header h1 { margin: 0; font-size: 20px; }
        .header p { margin: 10px 0 0 0; font-size: 14px; opacity: 0.9; }
        .content { padding: 20px; }
        .event-box { background: #fee2e2; border: 2px solid #dc2626; border-radius: 8px; padding: 15px; margin: 20px 0; }
        .event-box h2 { color: #991b1b; margin: 0 0 10px 0; font-size: 16px; }
        .story-angles { background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }
        .story-angles h3 { margin: 0 0 10px 0; color: #374151; }
        .story-angles li { margin: 8px 0; }
        .key-facts { background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px 20px; margin: 20px 0; }
        .key-facts h3 { margin: 0 0 10px 0; color: #1e40af; }
        .contact-box { background: #ecfdf5; border: 1px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 8px; }
        .contact-box h3 { margin: 0 0 10px 0; color: #065f46; }
        .footer { font-size: 14px; color: #64748b; padding: 20px; border-top: 1px solid #e5e7eb; }
    </style>
</head>
<body>
    <div class="header">
        <h1>PRESS RELEASE / STORY IDEA</h1>
        <p>For Immediate Release - December 12, 2025</p>
    </div>

    <div class="content">
        <h2 style="color: #1e3a8a; margin-top: 0;">360 Windsong Ranch Families Challenge "Taxation Without Education" - Prosper ISD Board Votes Monday</h2>

        <p><strong>PROSPER, TX</strong> - In a rare case of community-driven school district annexation, over 360 families in the Windsong Ranch subdivision are fighting to leave Denton ISD and join Prosper ISD - even though they already send their children to Prosper schools.</p>

        <p>The twist? <strong>Denton ISD collects $6.5 million annually in property taxes from these families but educates zero of their 274 students.</strong> A quirk of district boundaries drawn over a decade ago means Windsong Ranch falls within Denton ISD, but the nearest Denton schools are 10+ miles away while Prosper ISD schools are walking distance.</p>

        <div class="event-box">
            <h2>BOARD MEETING - MONDAY, DECEMBER 15</h2>
            <p style="margin: 0;"><strong>Time:</strong> 7:00 PM</p>
            <p style="margin: 5px 0;"><strong>Location:</strong> Prosper ISD Administration Building, 605 E 7th Street, Prosper, TX 75078</p>
            <p style="margin: 5px 0;"><strong>Expected:</strong> 100+ community members to attend and speak</p>
            <p style="margin: 5px 0;"><strong>Action Item:</strong> Board vote on annexation petition</p>
        </div>

        <div class="story-angles">
            <h3>Story Angles:</h3>
            <ul>
                <li><strong>David vs. Goliath:</strong> Families take on the system to get their tax dollars to follow their kids</li>
                <li><strong>"Taxation Without Education":</strong> Residents pay $6.5M/year to a district that serves none of their children</li>
                <li><strong>Rare Annexation Process:</strong> Texas Education Code Chapter 13 allows district changes - but it's rarely used</li>
                <li><strong>Community Democracy:</strong> 52.6% of registered voters (360 of 684) signed the petition - majority support</li>
                <li><strong>Growing Pains:</strong> How rapid North Texas growth creates absurd school district boundary situations</li>
            </ul>
        </div>

        <div class="key-facts">
            <h3>Key Facts:</h3>
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>274 students</strong> from Windsong Ranch already attend Prosper ISD (via transfer)</li>
                <li><strong>$6.5 million</strong> in annual tax revenue at stake</li>
                <li><strong>360 petition signatures</strong> (52.6% of registered voters)</li>
                <li><strong>Since 2012:</strong> Denton ISD has educated zero Windsong Ranch students</li>
                <li><strong>Only $83/year</strong> difference in tax rates between districts (~$7/month)</li>
                <li><strong>Denton ISD denied</strong> the petition on December 9, 2025 (expected - they'd lose the revenue)</li>
                <li><strong>If Prosper approves:</strong> Goes to TEA Commissioner for final decision</li>
            </ul>
        </div>

        <h3>The Process:</h3>
        <p>Under Texas Education Code Chapter 13, residents can petition to change school districts. Both the "losing" and "gaining" districts vote, but the final decision rests with the Texas Education Agency Commissioner. Denton ISD denied the petition on December 9 - now all eyes are on Prosper ISD's vote Monday.</p>

        <h3>What to Expect Monday:</h3>
        <ul>
            <li>Packed boardroom - families encouraged to bring children</li>
            <li>Multiple community speakers registered to present</li>
            <li>Organized grassroots effort with website, data analysis, and community organizing</li>
            <li>Board vote on whether to approve the annexation petition</li>
        </ul>

        <div class="contact-box">
            <h3>Media Contacts:</h3>
            <p style="margin: 0;"><strong>Doug Charles</strong><br>
            Windsong Ranch Annexation Committee<br>
            Email: dbcharles@me.com<br>
            Phone: Available upon request</p>
            <p style="margin: 15px 0 0 0;"><strong>Website:</strong> <a href="https://prosperisdpetition.com">prosperisdpetition.com</a><br>
            (Includes financial analysis, FAQs, community data)</p>
        </div>

        <h3>Available for Interview:</h3>
        <ul>
            <li>Petition organizers</li>
            <li>Affected parents with children currently transferring to Prosper ISD</li>
            <li>Community members who can speak to the 13-year history of this boundary issue</li>
        </ul>

        <p>###</p>
    </div>

    <div class="footer">
        <p><em>This story has strong visual potential: packed community meeting, families with kids, maps showing the absurd boundary situation, and a clear "little guy vs. the system" narrative.</em></p>
        <p>For more information or to schedule an interview, please reply to this email.</p>
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
    msg['From'] = f"Doug Charles <{ICLOUD_EMAIL}>"
    msg['To'] = to_email
    msg['Reply-To'] = ICLOUD_EMAIL

    # Create HTML part
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    # Send via iCloud SMTP
    with smtplib.SMTP('smtp.mail.me.com', 587) as server:
        server.starttls()
        server.login(ICLOUD_EMAIL, ICLOUD_APP_PASSWORD)
        server.sendmail(ICLOUD_EMAIL, to_email, msg.as_string())

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
                html_body=html_body
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
