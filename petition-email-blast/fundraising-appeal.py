#!/usr/bin/env python3
"""
Windsong Ranch Petition - Fundraising Appeal Email

Send to supporters who emailed the Prosper ISD board to help fund the TEA appeal.

Usage:
    python3 fundraising-appeal.py --test your@email.com   # Test first
    python3 fundraising-appeal.py --send-all              # Send to all contacts
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
SUBJECT = "We Need Your Help to Finish the Annexation - $5,000 by Jan 6th"
DELAY_BETWEEN_EMAILS = 10
BCC_EMAILS = ["rattinfamily@gmail.com", "dbcharles@me.com"]
GOFUNDME_LINK = "https://gofund.me/5acc47be"

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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; background-color: #f8fafc;">
    <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
        <!-- Header -->
        <tr>
            <td style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 30px 25px; text-align: center;">
                <h1 style="margin: 0; font-size: 28px; font-weight: 700;">We're in the Final Stretch!</h1>
                <p style="margin: 12px 0 0 0; font-size: 16px; opacity: 0.95;">Help Us Complete the TEA Appeal Filing</p>
            </td>
        </tr>

        <!-- Urgent Badge -->
        <tr>
            <td style="background: #dc2626; color: white; padding: 18px; text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">DEADLINE: Raise $5,000 by Monday, January 6, 2026</span>
            </td>
        </tr>

        <!-- Main Content -->
        <tr>
            <td style="padding: 30px 25px;">
                <p style="font-size: 16px; margin: 0 0 20px 0;">Attention {name},</p>

                <p style="font-size: 16px; margin: 0 0 20px 0;">We're in the final stretch of making the annexation of our small section of Windsong Ranch to Prosper ISD official. After all the work we've done to get this far—<strong>360 signatures, two board meetings, countless hours of preparation</strong>—this last step requires a licensed attorney to file everything correctly and ensure there are no mistakes that could delay or jeopardize the process.</p>

                <p style="font-size: 16px; margin: 0 0 20px 0;"><strong style="color: #dc2626;">We need to act fast!</strong> The paperwork must be filed within 45 days of Denton ISD's December 9th denial, and the lawyers need at least 3 weeks to prepare the filing.</p>

                <!-- Goal Box -->
                <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 3px solid #3b82f6; border-radius: 12px; margin: 25px 0;">
                    <tr>
                        <td style="padding: 25px; text-align: center;">
                            <p style="margin: 0 0 8px 0; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #1e40af; font-weight: 600;">Fundraising Goal</p>
                            <p style="margin: 0; font-size: 48px; font-weight: 800; color: #1e3a8a;">$5,000</p>
                            <p style="margin: 15px 0 0 0; font-size: 15px; color: #1e40af;">To retain <a href="https://www.plg-law.com" style="color: #1e40af; font-weight: 600;">Powell Law Group</a> and file our TEA appeal</p>
                            <p style="margin: 8px 0 0 0; font-size: 14px; color: #64748b;">Lead Attorney: <a href="https://www.plg-law.com/our-people/keaton-l-haney/" style="color: #3b82f6;">Keaton Haney</a></p>
                        </td>
                    </tr>
                </table>

                <!-- Call to Action (moved up after Goal Box) -->
                <table width="100%" cellpadding="0" cellspacing="0" style="margin: 25px 0;">
                    <tr>
                        <td style="text-align: center;">
                            <p style="margin: 0 0 20px 0; font-size: 18px; font-weight: 600; color: #1a1a1a;">If you can give $100—or anything—we can move forward.</p>
                            <a href="{GOFUNDME_LINK}" style="display: inline-block; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 18px 50px; text-decoration: none; border-radius: 10px; font-weight: 700; font-size: 20px; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);">DONATE NOW</a>
                            <p style="margin: 15px 0 0 0; font-size: 14px; color: #64748b;">Every dollar brings us closer to aligning our tax dollars with the schools that actually educate our children.</p>
                        </td>
                    </tr>
                </table>

                <!-- Deadline Warning -->
                <table width="100%" cellpadding="0" cellspacing="0" style="background: #fef3c7; border: 2px solid #f59e0b; border-radius: 12px; margin: 25px 0;">
                    <tr>
                        <td style="padding: 20px; text-align: center;">
                            <p style="margin: 0 0 8px 0; font-size: 18px; font-weight: 700; color: #92400e;">We must raise this by Monday, January 6, 2026</p>
                            <p style="margin: 0; font-size: 14px; color: #92400e;">A few neighbors have already covered the $3,000 in legal and administrative expenses incurred to date. Now we're counting on everyone to help us cross the finish line.</p>
                        </td>
                    </tr>
                </table>

                <!-- Proven Track Record Box -->
                <table width="100%" cellpadding="0" cellspacing="0" style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; margin: 25px 0;">
                    <tr>
                        <td style="padding: 20px;">
                            <p style="margin: 0 0 12px 0; font-size: 16px; font-weight: 700; color: #166534;">Proven Track Record of Success</p>
                            <p style="margin: 0 0 12px 0; font-size: 14px; color: #166534;">Powell Law Group has successfully represented families in cases just like ours. In <em>Brown v. Chilton ISD</em>, the firm secured a Commissioner's decision granting detachment and annexation. The Commissioner ruled:</p>
                            <p style="margin: 0; padding: 12px 15px; background: white; border-left: 4px solid #22c55e; font-style: italic; font-size: 14px; color: #374151;">"As the social and economic factors favor granting the proposed detachment and annexation and the educational factors are neutral, the proposed detachment and annexation should be granted."</p>
                            <p style="margin: 12px 0 0 0; font-size: 14px; color: #166534; font-weight: 600;">Our case is even stronger—our 274 children already attend Prosper ISD and have never attended a single day in Denton ISD schools!</p>
                        </td>
                    </tr>
                </table>

                <p style="font-size: 15px; margin: 0 0 20px 0;">We'll continue sharing updates on progress and attorney fees. Please pass this along to your neighbors impacted and <strong>contribute TODAY!</strong></p>

                <!-- Status Box -->
                <table width="100%" cellpadding="0" cellspacing="0" style="background: #f8fafc; border-radius: 12px; margin: 25px 0;">
                    <tr>
                        <td style="padding: 20px;">
                            <p style="margin: 0 0 12px 0; font-size: 15px; font-weight: 700; color: #1e3a8a;">Where We Stand:</p>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td style="padding: 8px 0; font-size: 14px; border-bottom: 1px solid #e2e8f0;">
                                        <span style="color: #22c55e; font-weight: bold;">&#10004;</span> <strong>Prosper ISD APPROVED</strong> our petition on December 15, 2025
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-size: 14px; border-bottom: 1px solid #e2e8f0;">
                                        <span style="color: #6b7280;">&#10004;</span> <strong>Denton ISD denied</strong> on December 9 (as expected)
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-size: 14px; border-bottom: 1px solid #e2e8f0;">
                                        <span style="color: #f59e0b; font-weight: bold;">&#9888;</span> <strong>TEA Filing Deadline:</strong> January 23, 2026
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-size: 14px;">
                                        <span style="color: #3b82f6; font-weight: bold;">&#9733;</span> <strong>Legal counsel retained:</strong> <a href="https://www.plg-law.com" style="color: #3b82f6;">Powell Law Group</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>

                <!-- Closing Message -->
                <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border-radius: 12px; margin: 25px 0;">
                    <tr>
                        <td style="padding: 25px; text-align: center;">
                            <p style="margin: 0; font-size: 24px; font-weight: 800; color: #059669;">We've come too far to stop now.</p>
                            <p style="margin: 10px 0 0 0; font-size: 18px; color: #047857;">Our kids deserve this. Our community deserves this.</p>
                            <p style="margin: 15px 0 0 0; font-size: 22px; font-weight: 700; color: #065f46;">We're so close — let's finish it!</p>
                        </td>
                    </tr>
                </table>

                <p style="font-size: 15px; margin: 25px 0 0 0;">
                    Thank you for standing with Windsong Ranch!<br><br>
                    <strong>Doug Charles & Jeff Sterling</strong><br>
                    Windsong Ranch Annexation Committee<br>
                    <a href="https://prosperisdpetition.com" style="color: #3b82f6;">prosperisdpetition.com</a>
                </p>
            </td>
        </tr>

        <!-- Footer -->
        <tr>
            <td style="background: #1e293b; padding: 25px; text-align: center;">
                <p style="margin: 0 0 10px 0; font-size: 13px; color: #94a3b8;">You're receiving this because you supported the Windsong Ranch annexation petition.</p>
                <p style="margin: 0; font-size: 13px; color: #94a3b8;">Questions? Reply to this email or visit <a href="https://prosperisdpetition.com" style="color: #60a5fa;">prosperisdpetition.com</a></p>
            </td>
        </tr>
    </table>
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
    msg['From'] = f"PISD Petition Update <{ICLOUD_EMAIL}>"
    msg['To'] = f"{to_name} <{to_email}>"
    msg['Reply-To'] = ICLOUD_EMAIL
    msg['Bcc'] = ", ".join(BCC_EMAILS)

    # Create HTML part
    html_part = MIMEText(html_body, 'html')
    msg.attach(html_part)

    # All recipients (To + BCC)
    all_recipients = [to_email] + BCC_EMAILS

    # Send via iCloud SMTP (port 587 with STARTTLS)
    with smtplib.SMTP('smtp.mail.me.com', 587) as server:
        server.starttls()
        server.login(ICLOUD_EMAIL, ICLOUD_APP_PASSWORD)
        server.sendmail(ICLOUD_EMAIL, all_recipients, msg.as_string())

    return True


def main():
    """Main function to read CSV and send emails."""

    import argparse
    parser = argparse.ArgumentParser(description='Send fundraising appeal emails')
    parser.add_argument('--test', type=str, help='Send test email to this address')
    parser.add_argument('--send-all', action='store_true', help='Send to all contacts (no confirmation)')
    args = parser.parse_args()

    print("=" * 60)
    print("Windsong Ranch - FUNDRAISING APPEAL")
    print("Subject: " + SUBJECT)
    print("=" * 60)
    print()

    # Test mode
    if args.test:
        print(f"Sending TEST email to: {args.test}")
        try:
            html_body = get_email_body("Test")
            send_email_via_icloud_smtp(args.test, "Test User", SUBJECT, html_body)
            print("Test email sent successfully!")
        except Exception as e:
            print(f"Error sending test email: {e}")
        return

    # Check if CSV exists
    if not os.path.exists(CSV_FILE):
        print(f"ERROR: CSV file not found: {CSV_FILE}")
        print("Please export your contacts to this location.")
        return

    # Read contacts and deduplicate by email
    contacts = []
    seen_emails = set()
    duplicates_skipped = 0

    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Try different possible column names
            email = row.get('Email') or row.get('email') or row.get('EMAIL')

            # Parse name from "Name" column (format: "First Last")
            name = row.get('Name') or ''
            name_parts = name.split() if name else []
            first_name = name_parts[0] if name_parts else ''
            last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

            if email:
                email_lower = email.strip().lower()
                if email_lower in seen_emails:
                    duplicates_skipped += 1
                    continue
                seen_emails.add(email_lower)
                contacts.append({
                    'email': email.strip(),
                    'first_name': first_name.strip() if first_name else '',
                    'last_name': last_name.strip() if last_name else ''
                })

    print(f"Found {len(contacts)} unique contacts ({duplicates_skipped} duplicates skipped)")
    print()

    if not args.send_all:
        print("To send to all contacts, run with --send-all flag")
        print("To test first, run with --test your@email.com")
        return

    # Send to all
    print("Starting to send emails...")
    print()

    success_count = 0
    error_count = 0

    for i, contact in enumerate(contacts, 1):
        email = contact['email']
        first_name = contact['first_name']
        full_name = f"{first_name} {contact['last_name']}".strip() or email

        try:
            html_body = get_email_body(first_name)
            send_email_via_icloud_smtp(email, full_name, SUBJECT, html_body)
            print(f"[{i}/{len(contacts)}] Sent to: {email}")
            success_count += 1
        except Exception as e:
            print(f"[{i}/{len(contacts)}] ERROR sending to {email}: {e}")
            error_count += 1

        # Delay between emails
        if i < len(contacts):
            time.sleep(DELAY_BETWEEN_EMAILS)

    print()
    print("=" * 60)
    print(f"COMPLETE: {success_count} sent, {error_count} errors")
    print("=" * 60)


if __name__ == "__main__":
    main()
