/**
 * PISD PETITION - ENHANCED GOOGLE APPS SCRIPT BACKEND
 * 
 * This script receives form submissions from the petition website,
 * validates the data, and stores it in Google Sheets.
 * 
 * ENHANCED FEATURES:
 * - Phone number collection for SMS campaigns
 * - SMS opt-in tracking
 * - Better data validation
 * - Duplicate detection
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
 * 11. Use this URL in your website form submission
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
    
    // Check for duplicate email
    const isDuplicate = checkDuplicate(sheet, data.email);
    
    // Prepare row data with enhanced fields
    const rowData = [
      new Date(), // Timestamp
      data.name || '',
      data.email || '',
      data.phone || '', // NEW: Phone number
      data.smsOptIn === true ? 'Yes' : 'No', // NEW: SMS opt-in
      data.street || '',
      data.city || '',
      data.state || '',
      data.zip || '',
      data.voterType || '',
      data.fullAddress || '',
      data.userAgent || '',
      isDuplicate ? 'Duplicate' : 'Submitted', // Status with duplicate detection
      isDuplicate ? 'Duplicate email submission' : '' // Notes
    ];
    
    // Append to sheet
    sheet.appendRow(rowData);
    
    // Log success
    Logger.log('Submission saved: ' + data.email + (isDuplicate ? ' (DUPLICATE)' : ''));
    
    // Return success response
    return createResponse(200, {
      success: true,
      message: 'Submission recorded successfully',
      timestamp: new Date().toISOString(),
      isDuplicate: isDuplicate
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
    status: 'PISD Petition Backend (Enhanced) is running',
    message: 'Send POST requests to submit data',
    features: ['Phone collection', 'SMS opt-in', 'Duplicate detection'],
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
  
  // Validate phone number format if provided (10 digits)
  if (data.phone && data.phone.trim() !== '') {
    const phoneDigits = data.phone.replace(/\D/g, '');
    if (phoneDigits.length !== 10) {
      return {
        valid: false,
        error: 'Phone number must be 10 digits'
      };
    }
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
 * Check if email already exists in sheet
 */
function checkDuplicate(sheet, email) {
  const data = sheet.getDataRange().getValues();
  
  // Skip header row, check email column (column 3, index 2)
  for (let i = 1; i < data.length; i++) {
    if (data[i][2] && data[i][2].toLowerCase() === email.toLowerCase()) {
      return true;
    }
  }
  
  return false;
}

/**
 * Get the target spreadsheet
 */
function getSheet() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(CONFIG.SHEET_NAME);
  
  // If sheet doesn't exist or is empty, set up headers
  if (!sheet) {
    sheet = spreadsheet.insertSheet(CONFIG.SHEET_NAME);
  }
  
  // Check if headers exist (first row)
  if (sheet.getLastRow() === 0) {
    setupHeaders(sheet);
  }
  
  return sheet;
}

/**
 * Set up column headers
 */
function setupHeaders(sheet) {
  const headers = [
    'Timestamp',
    'Name',
    'Email',
    'Phone', // NEW
    'SMS Opt-In', // NEW
    'Street',
    'City',
    'State',
    'ZIP',
    'Voter Type',
    'Full Address',
    'User Agent',
    'Status',
    'Notes'
  ];
  
  sheet.appendRow(headers);
  
  // Format header row
  const headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange.setFontWeight('bold');
  headerRange.setBackground('#4A90E2');
  headerRange.setFontColor('#FFFFFF');
  
  Logger.log('Headers set up successfully');
}

/**
 * Create a JSON response with CORS headers
 */
function createResponse(statusCode, data) {
  const output = ContentService.createTextOutput(JSON.stringify(data));
  output.setMimeType(ContentService.MimeType.JSON);
  
  // Note: Apps Script web apps automatically handle CORS for deployed apps
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
 * Test function to verify setup (run this from Script Editor)
 */
function testSetup() {
  Logger.log('Testing enhanced backend setup...');
  
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
    phone: '9725551234',
    smsOptIn: true,
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
  
  Logger.log('Enhanced backend setup test complete!');
}
