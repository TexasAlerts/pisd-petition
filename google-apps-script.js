/**
 * PISD PETITION - GOOGLE APPS SCRIPT BACKEND
 * 
 * This script receives form submissions from the petition website,
 * validates the data, and stores it in Google Sheets.
 * 
 * SETUP INSTRUCTIONS:
 * 1. Open your Google Sheet
 * 2. Go to Extensions > Apps Script
 * 3. Delete any default code
 * 4. Paste this entire file
 * 5. Click "Deploy" > "New deployment"
 * 6. Choose "Web app" as deployment type
 * 7. Set "Execute as" to "Me"
 * 8. Set "Who has access" to "Anyone"
 * 9. Click "Deploy"
 * 10. Copy the Web app URL
 * 11. Paste it into index.html where it says "PASTE_YOUR_APPS_SCRIPT_URL_HERE"
 */

// Configuration
const CONFIG = {
  SHEET_NAME: 'Sheet1', // The sheet tab name where data will be stored
  ALLOWED_ORIGINS: ['*'], // Allow all origins - can restrict later
  REQUIRED_FIELDS: ['name', 'email', 'street', 'city', 'state', 'zip', 'voterType']
};

/**
 * Handle OPTIONS requests (CORS preflight)
 * This is REQUIRED for browsers to send POST requests from web pages
 */
function doOptions(e) {
  return createCORSResponse();
}

/**
 * Handle POST requests from the petition form
 */
function doPost(e) {
  try {
    // Parse incoming JSON data
    const data = JSON.parse(e.postData.contents);
    
    // Validate required fields
    const validation = validateData(data);
    if (!validation.valid) {
      return createResponse(400, {
        success: false,
        error: validation.error
      });
    }
    
    // Check honeypot (spam prevention)
    if (data.website && data.website.trim() !== '') {
      Logger.log('Honeypot triggered - possible spam submission');
      return createResponse(200, {
        success: true,
        message: 'Submission received' // Don't reveal honeypot to spammers
      });
    }
    
    // Get the spreadsheet
    const sheet = getSheet();
    
    // Prepare row data - matches sheet columns:
    // A: Timestamp, B: Name, C: Email, D: Phone, E: SMS Opt-In, F: Street, G: City, H: State, I: ZIP,
    // J: Voter Type, K: Full Address, L: User Agent, M: Status, N: (Duplicate formula), O: Letter Type
    const rowData = [
      new Date(), // A: Timestamp
      data.name || '', // B: Name
      data.email || '', // C: Email
      data.phone || '', // D: Phone
      data.smsConsent ? 'Yes' : 'No', // E: SMS Opt-In
      data.street || '', // F: Street
      data.city || '', // G: City
      data.state || '', // H: State
      data.zip || '', // I: ZIP
      data.voterType || '', // J: Voter Type
      data.fullAddress || '', // K: Full Address
      data.userAgent || '', // L: User Agent
      'Submitted', // M: Status
      '', // N: Leave blank for Duplicate formula
      data.letterType || 'BOARD_LETTER' // O: Letter Type (TEA_COMMISSIONER or BOARD_LETTER)
    ];
    
    // Append to sheet
    sheet.appendRow(rowData);
    
    // Log success
    Logger.log('Submission saved: ' + data.email);
    
    // Return success response
    return createResponse(200, {
      success: true,
      message: 'Submission recorded successfully',
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    Logger.log('Error processing submission: ' + error.message);
    return createResponse(500, {
      success: false,
      error: 'Server error processing submission'
    });
  }
}

/**
 * Handle GET requests (for testing)
 */
function doGet(e) {
  return createResponse(200, {
    status: 'PISD Petition Backend is running',
    message: 'Send POST requests to submit data',
    timestamp: new Date().toISOString()
  });
}

/**
 * Validate incoming data
 */
function validateData(data) {
  // Check all required fields are present
  for (const field of CONFIG.REQUIRED_FIELDS) {
    if (!data[field] || data[field].trim() === '') {
      return {
        valid: false,
        error: `Missing required field: ${field}`
      };
    }
  }
  
  // Validate email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(data.email)) {
    return {
      valid: false,
      error: 'Invalid email format'
    };
  }
  
  // Validate ZIP code format (5 digits)
  const zipRegex = /^\d{5}$/;
  if (!zipRegex.test(data.zip)) {
    return {
      valid: false,
      error: 'Invalid ZIP code format'
    };
  }
  
  // Validate state (2 letters)
  if (data.state.length !== 2) {
    return {
      valid: false,
      error: 'Invalid state code'
    };
  }
  
  return { valid: true };
}

/**
 * Get the target spreadsheet
 */
function getSheet() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  return spreadsheet.getSheetByName(CONFIG.SHEET_NAME);
}

/**
 * Create a JSON response with CORS headers
 */
function createResponse(statusCode, data) {
  const output = ContentService.createTextOutput(JSON.stringify(data));
  output.setMimeType(ContentService.MimeType.JSON);
  
  // Note: Apps Script web apps automatically handle CORS for deployed apps
  // Additional headers are set via createCORSResponse for OPTIONS requests
  return output;
}

/**
 * Create CORS preflight response
 */
function createCORSResponse() {
  const output = ContentService.createTextOutput('');
  output.setMimeType(ContentService.MimeType.JSON);
  
  // Return empty response for OPTIONS - Apps Script handles CORS automatically
  return output;
}

/**
 * COLUMN HEADERS - Run this function once to set up column headers
 * Go to Apps Script Editor > Run > setupColumnHeaders
 */
function setupColumnHeaders() {
  const sheet = getSheet();
  if (!sheet) {
    Logger.log('ERROR: Cannot access sheet. Check SHEET_NAME in CONFIG.');
    return;
  }

  // Column headers A through O
  const headers = [
    'Timestamp',      // A
    'Name',           // B
    'Email',          // C
    'Phone',          // D
    'SMS Opt-In',     // E
    'Street',         // F
    'City',           // G
    'State',          // H
    'ZIP',            // I
    'Voter Type',     // J
    'Full Address',   // K
    'User Agent',     // L
    'Status',         // M
    'Duplicate',      // N
    'Letter Type'     // O
  ];

  // Set headers in row 1
  const headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange.setValues([headers]);

  // Format header row
  headerRange.setFontWeight('bold');
  headerRange.setBackground('#1e3a8a');
  headerRange.setFontColor('#ffffff');

  // Freeze header row
  sheet.setFrozenRows(1);

  // Auto-resize columns
  for (let i = 1; i <= headers.length; i++) {
    sheet.autoResizeColumn(i);
  }

  Logger.log('✅ Column headers set up successfully!');
  Logger.log('Headers: ' + headers.join(', '));
}

/**
 * Set up the Duplicate formula for existing rows
 * Run this after setupColumnHeaders to add the duplicate detection formula
 */
function setupDuplicateFormulas() {
  const sheet = getSheet();
  if (!sheet) {
    Logger.log('ERROR: Cannot access sheet.');
    return;
  }

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) {
    Logger.log('No data rows found. Add some submissions first.');
    return;
  }

  // For each row starting from row 2, set the duplicate formula in column N
  // Formula checks: same Letter Type (O) + same Email (C) + same Name (B)
  for (let row = 2; row <= lastRow; row++) {
    const formula = `=IF(COUNTIFS($O$2:O${row}, O${row}, $C$2:C${row}, C${row}, $B$2:B${row}, B${row}) > 1, "DUPLICATE", "Unique")`;
    sheet.getRange(row, 14).setFormula(formula); // Column N = 14
  }

  Logger.log(`✅ Duplicate formulas set for rows 2-${lastRow}`);
}

/**
 * Test function to verify setup (run this from Script Editor)
 */
function testSetup() {
  Logger.log('Testing backend setup...');

  // Test sheet access
  const sheet = getSheet();
  if (!sheet) {
    Logger.log('ERROR: Cannot access sheet. Check SHEET_NAME in CONFIG.');
    return;
  }

  Logger.log('✅ Sheet access successful: ' + sheet.getName());

  // Test data validation
  const testData = {
    name: 'Test User',
    email: 'test@example.com',
    street: '123 Test St',
    city: 'Prosper',
    state: 'TX',
    zip: '75078',
    voterType: 'Prosper ISD Voter (NOT in Windsong Ranch)',
    fullAddress: '123 Test St, Prosper, TX 75078'
  };

  const validation = validateData(testData);
  if (validation.valid) {
    Logger.log('✅ Data validation working');
  } else {
    Logger.log('ERROR: Data validation failed - ' + validation.error);
  }

  Logger.log('Backend setup test complete!');
  Logger.log('');
  Logger.log('NEXT STEPS:');
  Logger.log('1. Run setupColumnHeaders() to set up column headers A-O');
  Logger.log('2. Run setupDuplicateFormulas() to add duplicate detection');
  Logger.log('3. Deploy as web app');
}
