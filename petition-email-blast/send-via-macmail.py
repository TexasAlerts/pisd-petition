#!/usr/bin/env python3
"""
Send remaining 7 media emails via Mac Mail app.
Run this from Terminal: python3 send-via-macmail.py
"""

import subprocess
import time

SUBJECT = "TONIGHT: Prosper ISD Votes on $375M Annexation — Presentation Available"

# The 7 contacts that failed via SMTP
CONTACTS = [
    ("Fort Worth Star-Telegram", "newsroom@star-telegram.com"),
    ("Denton Record-Chronicle", "drc@dentonrc.com"),
    ("Texas Tribune", "community@texastribune.org"),
    ("Spectrum News", "DFWNewsDesk@Charter.com"),
    ("CW33 Dallas", "news@cw33.com"),
    ("Univision 23", "23@univision.net"),
    ("Telemundo Dallas", "noticierodallas@telemundo.com"),
]

BODY = """TONIGHT: Prosper ISD Votes on $375M Annexation

PROSPER, TX — Tonight at 7:00 PM, the Prosper ISD Board of Trustees will vote on a historic annexation petition that would bring 360 Windsong Ranch families — and an estimated $375 million in property value — into the district.

TONIGHT'S MEETING
Monday, December 15 at 7:00 PM
Prosper ISD Administration Building
605 E 7th Street, Prosper, TX 75078
Expected: 100+ community members to attend

VIEW OUR FULL BOARD PRESENTATION:
https://prosperisdpetition.com/board-presentation

KEY NUMBERS:
- $6.5 million annually — Tax revenue that would follow our students to PISD
- 274 students — Already attend Prosper ISD schools (via transfer)
- 52.6% of voters signed — Majority community support (360 of 684 registered voters)
- $375 million — Estimated property value in petition area
- 13 years — How long Denton ISD has collected taxes while educating zero Windsong students

THE STORY:
Windsong Ranch families pay $6.5 million per year in school taxes to Denton ISD — but their nearest Denton school is 10+ miles away. Meanwhile, Prosper ISD schools are walking distance. For 13 years, families have been transferring their kids to Prosper while their tax dollars go elsewhere.

Tonight's vote is the next step in a rare Texas Education Code Chapter 13 annexation process. Denton ISD denied the petition on December 9 (as expected — they'd lose the revenue). If Prosper ISD approves tonight, the petition goes to the TEA Commissioner for final decision.

WHAT TO EXPECT TONIGHT:
- Packed boardroom with families and children
- Formal presentation to the board
- Community speakers in support
- Board vote on the annexation petition

MEDIA CONTACT:
Doug Charles
Windsong Ranch Annexation Committee
Email: dbcharles@me.com
Website: https://prosperisdpetition.com

Strong visual opportunity: packed community meeting, families with kids, maps showing the boundary situation, and a clear "taxation without education" narrative.

###"""


def send_email_via_mail_app(to_email, subject, body):
    """Send email using Mac Mail app via AppleScript."""

    # Write body to temp file to avoid escaping issues
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(body)
        temp_file = f.name

    applescript = f'''
    set bodyText to read POSIX file "{temp_file}" as «class utf8»
    tell application "Mail"
        set newMessage to make new outgoing message with properties {{subject:"{subject}", content:bodyText, visible:false}}
        tell newMessage
            make new to recipient at end of to recipients with properties {{address:"{to_email}"}}
            send
        end tell
    end tell
    '''

    result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)

    # Clean up temp file
    import os
    os.unlink(temp_file)

    return result.returncode == 0, result.stderr


def main():
    print("=" * 60)
    print("Sending 7 Media Emails via Mac Mail App")
    print("=" * 60)
    print()

    sent = 0
    failed = 0

    for i, (org, email) in enumerate(CONTACTS, 1):
        print(f"[{i}/7] Sending to {org} ({email})...", end=" ", flush=True)

        success, error = send_email_via_mail_app(email, SUBJECT, BODY)

        if success:
            print("SENT")
            sent += 1
        else:
            print(f"FAILED: {error}")
            failed += 1

        time.sleep(2)

    print()
    print("=" * 60)
    print(f"COMPLETE: {sent} sent, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
