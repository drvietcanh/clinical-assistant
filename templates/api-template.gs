// Template for creating new API endpoints
// Replace MODULE_NAME and implement your logic

/**
 * List all items in this module
 * Used for displaying options or reference data
 */
function api_MODULE_NAME_list() {
  const ver = _readMetaVersion('MODULE_NAME_VERSION');
  const cacheKey = 'MODULE_NAME_list_' + ver;
  const cached = _cacheGet(cacheKey);
  
  if (cached) {
    return JSON.parse(cached);
  }
  
  // Read from Google Sheet
  const rows = _readSheetObjects('MODULE_NAME');
  
  // Transform data if needed
  const result = rows.map(row => ({
    id: row.id,
    name: row.name,
    // ... other fields
  }));
  
  // Cache for 10 minutes
  _cachePut(cacheKey, _json(result), 600);
  
  return result;
}

/**
 * Get details for a specific item
 */
function api_MODULE_NAME_detail(itemId) {
  const rows = _readSheetObjects('MODULE_NAME');
  const item = rows.find(r => String(r.id) === String(itemId));
  
  if (!item) {
    throw new Error('Item not found: ' + itemId);
  }
  
  return item;
}

/**
 * Main calculation function
 * This is called from the frontend
 */
function api_MODULE_NAME_calculate(payload) {
  /*
   * Example payload structure:
   * {
   *   input1: 123,
   *   input2: 'value',
   *   input3: true
   * }
   */
  
  // Validate inputs
  if (!payload || !payload.input1) {
    throw new Error('Missing required parameter: input1');
  }
  
  // Perform calculation
  let result = 0;
  let interpretation = '';
  
  // Example calculation logic
  try {
    result = performCalculation(payload);
    interpretation = interpretResult(result, payload);
  } catch (e) {
    // Log error
    Logger.log('Error in MODULE_NAME calculation: ' + e.message);
    throw e;
  }
  
  // Return structured result
  return {
    value: result,
    interpretation: interpretation,
    details: {
      // Additional breakdown
    },
    ref: 'Citation or guideline reference',
    timestamp: new Date().toISOString()
  };
}

/**
 * Helper: Perform actual calculation
 * @private
 */
function performCalculation(payload) {
  // Implement your calculation logic here
  const value = payload.input1 * 2; // Example
  return value;
}

/**
 * Helper: Interpret the result
 * @private
 */
function interpretResult(value, payload) {
  // Provide clinical interpretation
  if (value < 10) {
    return 'Low risk';
  } else if (value < 20) {
    return 'Moderate risk';
  } else {
    return 'High risk';
  }
}

/**
 * Optional: Batch calculation for multiple inputs
 */
function api_MODULE_NAME_batch_calculate(payloads) {
  if (!Array.isArray(payloads)) {
    throw new Error('Expected array of payloads');
  }
  
  return payloads.map(payload => {
    try {
      return {
        success: true,
        result: api_MODULE_NAME_calculate(payload)
      };
    } catch (e) {
      return {
        success: false,
        error: e.message
      };
    }
  });
}

/**
 * Optional: Export calculation history
 */
function api_MODULE_NAME_export_history() {
  const sheet = _getSheet('MODULE_NAME_History');
  const data = sheet.getDataRange().getValues();
  
  return data.map(row => ({
    timestamp: row[0],
    user: row[1],
    inputs: JSON.parse(row[2]),
    result: JSON.parse(row[3])
  }));
}

/**
 * Optional: Save calculation to history
 */
function api_MODULE_NAME_save(payload, result) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                  .getSheetByName('MODULE_NAME_History') ||
                  SpreadsheetApp.getActiveSpreadsheet().insertSheet('MODULE_NAME_History');
  
  // Add headers if new sheet
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'User', 'Inputs', 'Result']);
  }
  
  sheet.appendRow([
    new Date(),
    Session.getActiveUser().getEmail(),
    JSON.stringify(payload),
    JSON.stringify(result)
  ]);
}

/* 
USAGE INSTRUCTIONS:
1. Copy this template to server/MODULE_NAME.api.gs
2. Replace MODULE_NAME throughout the file
3. Implement calculation logic in performCalculation()
4. Implement interpretation in interpretResult()
5. Create corresponding Google Sheet named "MODULE_NAME"
6. Add version entry to Meta sheet: MODULE_NAME_VERSION, 2025-10-29, initial
7. Test function directly in Apps Script editor before deploying
*/

/* 
TESTING:
Run this in Apps Script editor to test:

function testModuleAPI() {
  const payload = {
    input1: 123,
    input2: 'test',
    input3: true
  };
  
  const result = api_MODULE_NAME_calculate(payload);
  Logger.log(result);
}
*/

